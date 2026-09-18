#!/usr/bin/env python3
"""Drift budget for a 2 A SEM lens current supply.

Companion to sem-lens-current-supply.md.  Computes the 1 h drift budget, the
sense-resistor trade, the setpoint resolution, the rail-ripple tolerance and the
refocus interval, so the note's tables are generated rather than asserted.

Topology assumed (the note draws it): V_ref -> DAC -> error amp -> N-MOSFET ->
lens coil -> 4-terminal sense resistor -> ground, with the sense voltage servoed
1:1 to the DAC output.  The loop rejects everything it does not measure (rail
sag, MOSFET drift, the coil's resistance rise when hot); everything inside the
measuring chain lands straight in the output current.

    dI/I = dV_ref/V_ref + dV_os/V_sense - dR_sense/R_sense

Usage
-----
    python sem_lens_supply_budget.py             # report
    python sem_lens_supply_budget.py --markdown  # the note's tables
    python sem_lens_supply_budget.py --set r_sense=0.2 i_max=1.5
"""

from __future__ import annotations

import argparse
import math
import sys

# name: (SI value, display divisor, display unit, description)
DEFAULTS: dict[str, tuple[float, float, str, str]] = {
    # load and compliance
    "i_max":       (2.0,   1.0,  "A",   "maximum lens current"),
    "i_op":        (2.0,   1.0,  "A",   "operating current for the budget"),
    "r_coil":      (16.0,  1.0,  "Ω",   "lens coil resistance, cold (old SEM: 8 or 16)"),
    "l_coil":      (40e-3, 1e-3, "mH",  "lens coil inductance"),
    "v_rail":      (30.0,  1.0,  "V",   "pass-element rail"),
    "r_sense":     (0.1,   1.0,  "Ω",   "sense resistor"),
    # 1 h drift budget: assume a settled box in a ±0.5 K/h room
    "target":      (1.0,   1.0,  "ppm", "1 h drift budget"),
    "dT_ambient":  (0.5,   1.0,  "K",   "ambient change over the hour"),
    "tc_ref":      (0.5,   1e-6, "ppm/K", "voltage reference tempco"),
    "tc_dac":      (0.2,   1e-6, "ppm/K", "DAC gain tempco (ratiometric)"),
    "tc_shunt":    (0.2,   1e-6, "ppm/K", "sense resistor tempco (foil)"),
    "dT_settle":   (0.2,   1.0,  "K",   "residual self-heating settling, 30 min..1 h"),
    "vos_K":       (0.02,  1e-6, "µV/K", "error-amp offset drift (chopper)"),
    "dT_amp":      (0.7,   1.0,  "K",   "amp local temperature change over the hour"),
    "emf_K":       (0.1,   1e-6, "µV/K", "differential thermal EMF of the sense loop"),
    "noise_1h":    (0.05,  1e-6, "µV",  "0.1-10 Hz noise over the hour, as ±"),
    # thermal tricks: a heated sibling resistor, and a real oven (see the note)
    "oven_gain":   (20.0,  1.0,  "x",   "temperature-servo loop gain of the oven"),
    "dT_island_oven": (2e-3, 1e-3, "mK", "island stability a temperature servo holds"),
    "draft_frac":  (0.05,  1.0,  "",    "airflow-induced change in the shunt's rise"),
    # The reference's own noise, which the 7-term budget above leaves out. It enters the
    # current 1:1 (the reference *is* the setpoint scale), so parts_report() charges it.
    "noise_ref":   (1.0,   1.0,  "ppm", "reference 0.1-10 Hz noise, peak-to-peak"),
    # broadband noise, carried only to show that it averages away (see sums_report)
    "e_n":         (20e-9, 1e-9, "nV/rootHz", "error-amp input voltage noise density"),
    "loop_bw":     (1e3,   1e3,  "kHz",  "loop bandwidth that admits that noise"),
    # verification floor: the planned LEM fluxgate + DMM6500 setup
    "fg_nominal":  (60.0,  1.0,  "A",    "fluxgate nominal primary current, one turn"),
    "fg_ratio":    (600.0, 1.0,  "",     "fluxgate primary-to-secondary turns ratio"),
    "fg_turns":    (30.0,  1.0,  "",     "primary turns threaded through the aperture"),
    "fg_off_tc":   (20.0,  1.0,  "ppm/K", "fluxgate offset drift, of nominal"),
    "fg_dT":       (0.01,  1e-3, "mK",   "fluxgate temperature change over the hour"),
    "r_load_tc":   (0.2,   1.0,  "ppm/K", "secondary load resistor tempco"),
    "dmm_ratio":   (0.3,   1.0,  "ppm",  "DMM6500 ratiometric path floor over one hour"),
    # rail rejection
    "g_ds":        (0.1,   1.0,  "%/V", "pass-element dI/I per V of rail change"),
    "loop_100Hz":  (10.0,  1.0,  "x",   "loop gain at 100 Hz"),
    "ripple_ok":   (0.2,   1.0,  "ppm", "allowed contribution from rail ripple"),
}

# Component sets for the cheap-parts comparison: the foil + ovenized-reference original,
# and a 0.25 ohm / 2 ppm/K part (Vishay Y0850 class) with a quiet low-noise reference.
PARTSETS: dict[str, dict[str, float]] = {
    "original": {"r_sense": 0.1, "tc_shunt": 0.2, "tc_ref": 0.5, "noise_ref": 1.0},
    "y0850":    {"r_sense": 0.25, "tc_shunt": 2.0, "tc_ref": 2.0, "noise_ref": 0.25},
}

PARTSET_LABELS: dict[str, str] = {
    "original": "original: 0.1 Ω foil, 0.2 ppm/K + LM399",
    "y0850": "Y0850: 0.25 Ω, 2 ppm/K + quiet 2 ppm/K reference",
}


def ppm(x: float) -> float:
    """Parts per million, i.e. a relative quantity scaled by 1e6."""
    return x / 1e-6


def budget(p: dict[str, float]) -> list[tuple[str, str, float]]:
    """The 1 h drift terms, as (item, mechanism, ppm)."""
    v_sense = p["i_op"] * p["r_sense"]
    return [
        ("voltage reference", "tempco × ambient",
         p["tc_ref"] * p["dT_ambient"]),
        ("DAC gain", "ratiometric ladder, tempco × ambient",
         p["tc_dac"] * p["dT_ambient"]),
        ("sense resistor", "tempco × ambient",
         p["tc_shunt"] * p["dT_ambient"]),
        ("sense resistor", "residual self-heating settling",
         p["tc_shunt"] * p["dT_settle"]),
        ("error amp", f"offset drift × temp / V_sense",
         p["vos_K"] * p["dT_amp"] / v_sense),
        ("sense loop", "thermal EMF drift / V_sense",
         p["emf_K"] * p["dT_ambient"] / v_sense),
        ("error amp", "0.1-10 Hz noise over 1 h / V_sense",
         p["noise_1h"] / v_sense),
        ("reference", "0.1-10 Hz noise, 1:1 into the setpoint",
         p["noise_ref"] / 2),
    ]


def rss(terms: list[tuple[str, str, float]]) -> float:
    return math.sqrt(sum(t[2] ** 2 for t in terms))


def report(p: dict[str, float], markdown: bool) -> int:
    v_sense = p["i_op"] * p["r_sense"]
    v_coil_cold = p["i_op"] * p["r_coil"]
    v_coil_hot = v_coil_cold * 1.2          # copper, +0.4 %/K over a ~50 K rise
    headroom = p["v_rail"] - v_coil_hot - v_sense
    p_fet = headroom * p["i_op"]
    terms = budget(p)
    total_rss = rss(terms)
    total_wc = sum(t[2] for t in terms)

    if markdown:
        print("| Item | Mechanism over the hour | 1 h drift |")
        print("|---|---|---|")
        for item, mech, value in terms:
            print(f"| {item} | {mech} | {value:.2f} ppm |")
        print(f"| **RSS** | | **{total_rss:.2f} ppm** |")
        print(f"| worst case (linear sum) | | {total_wc:.2f} ppm |")
        return 0

    print(f"\nload: I_max {p['i_max']:.1f} A, R_coil {p['r_coil']:.1f} Ω, "
          f"L {p['l_coil'] * 1e3:.0f} mH")
    print(f"  V_coil  {v_coil_cold:.1f} V cold, {v_coil_hot:.1f} V hot "
          f"(+20 % for a 50 K rise)")
    print(f"  V_sense {v_sense * 1e3:.0f} mV in {p['r_sense']:.2f} Ω, "
          f"{p['r_sense'] * p['i_op'] ** 2:.2f} W")
    if headroom >= 0:
        print(f"  rail {p['v_rail']:.0f} V -> {headroom:.1f} V of headroom, "
              f"{p_fet:.1f} W in the pass element, {v_coil_hot * p['i_op']:.1f} W in the coil")
    else:
        print(f"  at {p['i_op']:.1f} A the rail is {-headroom:.1f} V SHORT of the "
              f"{v_coil_hot + v_sense:.1f} V the hot coil plus sense drop needs")
    need = p["i_max"] * p["r_coil"] * 1.2 + v_sense + 1.0
    if need > p["v_rail"]:
        print(f"  !! at I_max {p['i_max']:.1f} A the hot coil plus sense plus 1 V of "
              f"saturation needs {need:.1f} V: lower the current, raise the rail, or add a "
              f"{(need - p['v_rail']) / p['i_max']:.2f} Ω series ballast outside the pass element")
    else:
        print(f"  compliance at I_max: {need:.1f} V of the {p['v_rail']:.0f} V rail used")

    print(f"\n1 h drift budget (target {p['target']:.1f} ppm, V_sense "
          f"{v_sense * 1e3:.0f} mV)")
    for item, mech, value in terms:
        print(f"  {item:<20}{mech:<44}{value:>6.2f} ppm")
    print(f"  {'RSS':<20}{'':<44}{total_rss:>6.2f} ppm")
    print(f"  {'worst case':<20}{'linear sum':<44}{total_wc:>6.2f} ppm")

    print("\nsense resistor trade")
    print(f"  {'R_sense':>8}{'V_sense':>11}{'P':>8}{'dT':>7}{'offset':>9}{'TCR':>8}{'RSS':>8}")
    for r in (0.05, 0.1, 0.2, 0.5):
        vs = p["i_op"] * r
        power = p["i_op"] ** 2 * r
        dT = 10.0 * power
        offset = (p["vos_K"] * p["dT_amp"] + p["emf_K"] * p["dT_ambient"]
                  + p["noise_1h"]) / vs
        tcr = p["tc_shunt"] * (p["dT_ambient"] + p["dT_settle"])
        # airflow/draft sensitivity grows with the temperature rise above ambient
        draft = p["tc_shunt"] * p["draft_frac"] * dT
        combo = math.sqrt(offset**2 + tcr**2 + draft**2)
        print(f"  {r:>7.2f}Ω{vs * 1e3:>9.0f}mV{power:>7.2f}W{dT:>6.1f}K"
              f"{offset:>9.2f}{tcr:>8.2f}{combo:>8.2f}")
    print("  (offset column: offset + EMF + noise drift, all divided by V_sense)")
    print("  (draft column folded into RSS: 5 % of the rise, as airflow varies)")

    print("\nsetpoint resolution: one LSB, in ppm of full scale")
    for bits in (12, 16, 18, 20, 24):
        lsb = 1 / 2**bits
        print(f"  {bits:>3} bit   {ppm(lsb):>8.2f} ppm"
              f"{'   = set and hold' if ppm(lsb) > p['target'] else ''}")

    print("\nrail ripple tolerance")
    leak = ppm(p["g_ds"] / 100)                 # ppm per volt of rail change
    allowed_v = p["ripple_ok"] * (1 + p["loop_100Hz"]) / leak
    print(f"  pass element leaks {ppm(p['g_ds'] / 100):.0f} ppm per volt of V_ds change")
    print(f"  loop rejects 100 Hz by {1 + p['loop_100Hz']:.0f}x")
    print(f"  -> rail ripple must stay under {allowed_v * 1e6:.0f} µV at 100 Hz "
          f"for {p['ripple_ok']:.1f} ppm")
    print(f"  a raw rectifier (2 V ripple) gives "
          f"{leak * 2 / (1 + p['loop_100Hz']):.0f} ppm: an LDO stage is mandatory")

    print("\nrefocus interval at the 30 kV / 200 000x working point")
    for label, cc, dz in (("objective", 2.5e-3, 83e-9), ("default 15 kV", 10e-3, 500e-9)):
        eps_max = dz / (2 * cc)
        hours = eps_max / 1e-6                  # at 1 ppm/h
        print(f"  {label:<14} 2Cc={2 * cc * 1e3:>4.1f} mm  focus budget "
              f"{dz * 1e9:>4.0f} nm -> {ppm(eps_max):>5.0f} ppm, i.e. {hours:>5.1f} h at 1 ppm/h")
    return 0


# Classification of budget()'s rows, in the same order:
#   "temp"     = driven by a temperature change, so an oven attenuates it
#   "vsense"   = scales as 1/V_sense, so a bigger shunt attenuates it
#   "selfheat" = the shunt's own settling, which a constant-power pair removes
TAGS: tuple[frozenset[str], ...] = (
    frozenset({"temp"}),                # voltage reference, tempco x ambient
    frozenset({"temp"}),                # DAC gain, ratiometric ladder
    frozenset({"temp"}),                # sense resistor, tempco x ambient
    frozenset({"temp", "selfheat"}),    # sense resistor, self-heating settling
    frozenset({"temp", "vsense"}),      # error amp, offset drift
    frozenset({"temp", "vsense"}),      # sense loop, thermal EMF
    frozenset({"vsense"}),              # error amp, 0.1-10 Hz noise
    frozenset(),                        # reference noise: no temperature, no V_sense
)

# what budget() calls each row: a reordering must fail loudly, not mis-tag silently
ROW_KEYS: tuple[str, ...] = ("voltage reference", "DAC gain", "sense resistor",
                             "sense resistor", "error amp", "sense loop", "error amp",
                             "reference")


def tagged_terms(p: dict[str, float]) -> list[tuple[str, str, float, frozenset[str]]]:
    """budget() rows with their tags, refusing to run if the two lists have diverged."""
    terms = budget(p)
    if len(terms) != len(TAGS) or tuple(t[0] for t in terms) != ROW_KEYS:
        raise SystemExit("TAGS/ROW_KEYS no longer match budget(): update them together.")
    return [t + (tag,) for t, tag in zip(terms, TAGS)]


def scaled_rss(terms, *, oven: float = 1.0, vsense: float = 1.0,
               drop_selfheat: bool = False) -> float:
    """RSS after attenuating temperature terms by `oven` and V_sense terms by `vsense`."""
    total = 0.0
    for _, _, value, tags in terms:
        if drop_selfheat and "selfheat" in tags:
            continue
        if "temp" in tags:
            value /= oven
        if "vsense" in tags:
            value *= vsense
        total += value ** 2
    return math.sqrt(total)


def thermal_report(p: dict[str, float], markdown: bool) -> int:
    """Does a heated sibling resistor hold the shunt still?  Mostly not -- see the note."""
    terms = tagged_terms(p)
    base = rss(terms)
    pair = scaled_rss(terms, drop_selfheat=True)
    oven = scaled_rss(terms, oven=p["oven_gain"])
    r_hi = 0.2
    oven_hi = scaled_rss(terms, oven=p["oven_gain"], vsense=p["r_sense"] / r_hi)

    # the heater reaches the signal only through temperature, so it can be crude:
    # a relative heater error e gives dT = 2*e*P_h*theta and shunt drift TCR*dT.
    # NB budget()'s terms are already plain ppm, so per_unit is ppm per unit error.
    theta, p_h = 10.0, p["i_op"] ** 2 * p["r_sense"]
    per_unit = 2 * p["tc_shunt"] * theta * p_h
    eps_h = 0.01 / per_unit               # relative heater error for a 0.01 ppm share

    # constant-sum law: power error is quadratic in the departure from the balanced split
    p_bal = 2 * p["r_sense"] * p["i_max"] ** 2
    dT_bal = theta * p_bal
    imbalance = [(x, x ** 2, dT_bal * x ** 2, p["tc_shunt"] * dT_bal * x ** 2)
                 for x in (0.0, 0.1, 0.25, 0.5, 1.0)]

    if markdown:
        print("| Variant | What it removes | 1 h drift RSS |")
        print("|---|---|---|")
        print(f"| baseline, single shunt | - | {base:.2f} ppm |")
        print(f"| heated pair, constant power | the shunt's residual settling | {pair:.2f} ppm |")
        print(f"| oven, temperature servo, gain {p['oven_gain']:.0f} | "
              f"every temperature-driven term | {oven:.2f} ppm |")
        print(f"| oven + {r_hi:.1f} $\\Omega$ shunt | the above, plus half of the "
              f"V_sense terms | {oven_hi:.2f} ppm |")
        print()
        print("| Imbalance $x$ | $\\Delta P/P = x^2$ | $\\Delta T$ | shunt drift |")
        print("|---|---|---|---|")
        for x, dp, dT, drift in imbalance:
            print(f"| {x:.2f} | {100 * dp:.0f} % | {dT:.2f} K | {drift:.3f} ppm |")
        return 0

    print("\nheated pair / oven analysis")
    print(f"  baseline single shunt              {base:>6.2f} ppm")
    print(f"  heated pair, constant power        {pair:>6.2f} ppm   removes only the "
          f"{p['tc_shunt'] * p['dT_settle']:.2f} ppm settling term")
    print(f"  oven, temperature servo G={p['oven_gain']:.0f}        {oven:>6.2f} ppm   "
          f"attenuates every temperature term")
    print(f"  oven + {r_hi:.1f} Ω shunt                {oven_hi:>6.2f} ppm   drafts stop "
          f"mattering, so a bigger V_sense is affordable")

    print(f"\n  heater accuracy: {per_unit:.1f} ppm of shunt drift per unit "
          f"heater-current error")
    print(f"  -> a heater error of {ppm(eps_h):.0f} ppm ({100 * eps_h:.1f} %) still "
          f"contributes only 0.01 ppm")
    print(f"  -> the heater path may be ~{eps_h / (p['target'] * 1e-6):.0f}x sloppier than "
          f"the {p['target']:.0f} ppm signal target")

    print(f"\n  constant-sum law (I + I_h = S, balanced at I_max): pair dissipates "
          f"{p_bal:.2f} W, rise {dT_bal:.1f} K")
    print(f"  {'imbalance x':>12}{'dP/P':>9}{'dT':>8}{'drift':>10}")
    for x, dp, dT, drift in imbalance:
        print(f"  {x:>12.2f}{100 * dp:>8.0f}%{dT:>7.2f}K{drift:>9.3f}ppm")
    return 0


def trade_report(p: dict[str, float], markdown: bool) -> int:
    """Can we buy cheap parts and pay for them with thermal control instead?

    Every temperature coefficient in the chain reaches the current only as
    eps = TC * dT_island, so "how bad a part can I use?" is the same question as
    "how still can I hold the island?".  The shunt is the awkward case: the operator
    changes the current with magnification, so its own dissipation steps too, and it
    needs the servo's authority -- not just immunity to the ambient.
    """
    share = 0.1e-6                      # what one term may contribute, relative
    theta = 10.0                        # shunt thermal resistance [K/W]
    i_hi, i_lo = p["i_max"], p["i_max"] / 5
    dT_self = theta * p["r_sense"] * (i_hi**2 - i_lo**2)
    cc2 = 5e-3                          # 2*Cc of the 30 kV / 200 000x objective [m]
    focus_budget_nm = 83.0

    ladder = (
        (0.2, "foil, what we buy today", "nothing special, a closed box"),
        (1.0, "metal strip, good chip", "closed box plus thermal mass"),
        (5.0, "thin film", "insulated island with mass"),
        (50.0, "thick film", "temperature servo required"),
        (100.0, "cheap chip, bandgap ref", "temperature servo, careful sensor"),
    )

    def num(x: float, digits: int = 3) -> str:
        """Round to `digits` significant figures, plain notation (never 1.9e+02)."""
        if x == 0:
            return "0"
        dec = max(0, digits - 1 - math.floor(math.log10(abs(x))))
        return f"{x:.{dec}f}"

    def hold(tc: float) -> str:
        dt = share / (tc * 1e-6)
        return f"{dt:.2f} K" if dt >= 0.1 else f"{dt * 1e3:.0f} mK"

    if markdown:
        print("| Part tempco | Island must hold, for a 0.1 ppm share | "
              "What delivers it | Part class |")
        print("|---|---|---|---|")
        for tc, label, how in ladder:
            print(f"| {tc:.1f} ppm/K | {hold(tc)} | {how} | {label} |")
        print()
        print(f"| Shunt tempco | $\\Delta R/R$ for {i_hi:.1f} A to {i_lo:.1f} A | "
              f"focus shift | vs the {focus_budget_nm:.0f} nm budget |")
        print("|---|---|---|---|")
        for tc, _, _ in ladder:
            eps = tc * 1e-6 * dT_self
            print(f"| {tc:.1f} ppm/K | {num(ppm(eps))} ppm | {num(cc2 * eps * 1e9)} nm | "
                  f"{cc2 * eps * 1e9 / focus_budget_nm:.2f}x |")
        return 0

    print("\nwhat thermal stability buys you in parts")
    print(f"  {'part tempco':>12}{'island must hold':>17}   what delivers it")
    for tc, label, how in ladder:
        print(f"  {tc:>8.1f} ppm/K{hold(tc):>17}   {how:<32} ({label})")

    print(f"\n  the shunt also sees its own dissipation step: {i_hi:.1f} A to {i_lo:.1f} A "
          f"is {dT_self:.1f} K of self-heating")
    print(f"  {'shunt tempco':>12}{'dR/R':>11}{'focus shift':>13}{'of budget':>11}")
    for tc, _, _ in ladder:
        eps = tc * 1e-6 * dT_self
        print(f"  {tc:>8.1f} ppm/K{num(ppm(eps)):>7} ppm{num(cc2 * eps * 1e9):>7} nm"
              f"{cc2 * eps * 1e9 / focus_budget_nm:>10.2f}x")

    print("\n  what the island cannot buy: noise, aging, hysteresis. The amplifier's")
    print("  1/f noise and the reference's own noise are untouched by temperature")
    print("  control, and they are already the residual of the budget -- keep those")
    print("  parts good; everything whose error is a temperature coefficient can go cheap.")
    return 0


def parts_report(p: dict[str, float], markdown: bool) -> int:
    """Four combinations: two component sets, each with and without a temperature servo.

    Note what the 0.25 ohm part really changes: at 2 A it gives 0.5 V of sense voltage -- 2.5x
    the original -- so every term that divides by V_sense gets better, while every term that
    scales with the shunt's tempco gets worse.  The oven is what converts one into the other.
    """
    theta = 10.0
    i_hi, i_lo = p["i_max"], p["i_max"] / 5
    oven_gain_dT = p["dT_ambient"] / p["dT_island_oven"]

    def num(x: float, digits: int = 3) -> str:
        if x == 0:
            return "0"
        dec = max(0, digits - 1 - math.floor(math.log10(abs(x))))
        return f"{x:.{dec}f}"

    rows = []
    for name, over in PARTSETS.items():
        ps = dict(p, **over)
        terms = tagged_terms(ps)
        v_sense = ps["i_op"] * ps["r_sense"]
        plain = rss(terms)                    # budget() carries the reference's noise
        oven = scaled_rss(terms, oven=oven_gain_dT)
        dT_step = theta * ps["r_sense"] * (i_hi**2 - i_lo**2)
        step = ps["tc_shunt"] * dT_step                       # ppm, plain topology only
        rows.append((name, ps, terms, v_sense, plain, oven, dT_step, step))

    if markdown:
        print("| Component set | Plain, no thermal control | With a temperature servo |")
        print("|---|---|---|")
        for name, _, _, _, plain, oven, _, step in rows:
            note = f" (plus a {num(step)} ppm step per magnification change)" if step >= 0.1 else ""
            label = PARTSET_LABELS[name].replace("Ω", "$\\Omega$")
            print(f"| {label} | {num(plain)} ppm{note} | {num(oven)} ppm |")
        print()
        print("| Term | original, plain | Y0850, plain | original, servo | Y0850, servo |")
        print("|---|---|---|---|---|")
        for i, (item, mech, _, tags) in enumerate(rows[0][2]):
            cells = []
            for row in rows:
                value = row[2][i][2]
                cells.append(value / oven_gain_dT if "temp" in tags else value)
            print(f"| {item}: {mech} | {num(cells[0])} | {num(cells[1])} | "
                  f"{num(cells[0]) if 'temp' not in tags else '<0.01'} | "
                  f"{num(cells[1]) if 'temp' not in tags else '<0.01'} |")
        return 0

    print("\nparts vs thermal control (1 h drift, ppm)")
    for name, ps, terms, v_sense, plain, oven, dT_step, step in rows:
        print(f"\n  {PARTSET_LABELS[name]}")
        print(f"    V_sense {v_sense * 1e3:.0f} mV, shunt {ps['r_sense'] * ps['i_op'] ** 2:.2f} W, "
              f"step {dT_step:.1f} K")
        print(f"    plain {plain:.2f} ppm   servo {oven:.2f} ppm   "
              f"step {step:.1f} ppm (plain only)")
        for label, scale in (("plain", 1.0), ("servo", oven_gain_dT)):
            items = [(i, v / scale if "temp" in tags else v)
                     for i, _, v, tags in terms]
            top = sorted(items, key=lambda t: -t[1])[:3]
            print(f"    biggest in {label:<5}: "
                  + ", ".join(f"{t[0]} {t[1]:.2f}" for t in top))

    print("\n  the reference's noise enters 1:1 -- at 2.5 V a 1 µVpp part is 0.4 ppm pp, so")
    print("  with the temperature servo in place, choose the reference on noise, not tempco.")
    return 0


def noise_rows(p: dict[str, float]) -> tuple[tuple[str, str, str], ...]:
    """Every noise mechanism, with its band, and what an hour of observation does to it.

    The two prices of a noise figure are its *band* and whether it is white or 1/f: white parts
    fall as 1/sqrt(T), 1/f parts do not fall at all.
    """
    kb, tk = 1.380649e-23, 300.0                  # Boltzmann, room temperature
    v_sense = p["i_op"] * p["r_sense"]
    amp_white = p["e_n"] * math.sqrt(p["loop_bw"])
    johnson = math.sqrt(4 * kb * tk * p["r_sense"])   # V/sqrt(Hz) at the sense node
    dac_limit = 0.2e-6 * v_sense                  # 0.2 ppm of the setpoint
    t_h = 3600.0
    return (
        ("reference 1/f", f"{p['noise_ref'] / 2:.2f} ppm, 0.1-10 Hz",
         f"{p['noise_ref'] / 2:.2f} ppm"),
        ("error amp 1/f", f"{p['noise_1h'] / v_sense:.2f} ppm, 0.1-10 Hz",
         f"{p['noise_1h'] / v_sense:.2f} ppm"),
        ("error amp white",
         f"{amp_white / v_sense / 1e-6:.2f} ppm, DC-{p['loop_bw'] / 1e3:.0f} kHz",
         f"{amp_white / math.sqrt(p['loop_bw'] * t_h) / v_sense / 1e-6:.3f} ppm"),
        ("shunt Johnson",
         f"{johnson * math.sqrt(p['loop_bw']) / v_sense / 1e-6:.3f} ppm in band",
         f"{johnson / math.sqrt(p['loop_bw'] * t_h) / v_sense / 1e-6:.1e} ppm"),
        ("DAC, unfiltered",
         f"keep under {dac_limit * 1e9:.0f} nVpp on a {v_sense * 1e3:.0f} mV setpoint",
         "0.2 ppm if met"),
    )


def sums_report(p: dict[str, float], markdown: bool) -> int:
    """How the budget is summed: correlated terms, independent terms, and noise.

    Rules:
      - terms driven by one shared quantity (here the island's temperature) act on a common
        driver, so their sensitivities add linearly for a guaranteed bound, and in quadrature
        when the signs are random and unknown;
      - genuinely independent terms add in quadrature (variances add) -- exact for incoherent
        noise;
      - 1/f noise does not average down over the hour, which is why the 0.1-10 Hz figures are
        charged in full; white noise does average, as 1/sqrt(T), and is negligible here.
    """
    terms = tagged_terms(p)
    temp = [t for t in terms if "temp" in t[3]]
    indep = [t for t in terms if "temp" not in t[3]]
    temp_lin = sum(t[2] for t in temp)
    temp_rss = math.sqrt(sum(t[2] ** 2 for t in temp))
    indep_rss = math.sqrt(sum(t[2] ** 2 for t in indep))
    linear_all = sum(t[2] for t in terms)
    hier_worst = math.sqrt(temp_lin**2 + indep_rss**2)
    hier_stat = math.sqrt(temp_rss**2 + indep_rss**2)

    band_rms = p["e_n"] * math.sqrt(p["loop_bw"])
    v_sense = p["i_op"] * p["r_sense"]
    white_band = band_rms / v_sense
    white_1h = band_rms / math.sqrt(p["loop_bw"] * 3600.0) / v_sense

    conventions = (
        ("all terms, linear (guaranteed bound)", linear_all),
        ("all terms, RSS (random signs, incoherent)", rss(terms)),
        ("temperature group, linear", temp_lin),
        ("temperature group, RSS", temp_rss),
        ("independent group, RSS", indep_rss),
        ("hierarchical, tempcos worst case", hier_worst),
        ("hierarchical, tempcos random", hier_stat),
    )

    if markdown:
        print("| Convention | 1 h budget |")
        print("|---|---|")
        for label, value in conventions:
            print(f"| {label} | {value:.2f} ppm |")
        print(f"| white noise in {p['loop_bw'] / 1e3:.0f} kHz of band, averaged over the hour | "
              f"{ppm(white_band):.2f} ppm -> {ppm(white_1h):.3f} ppm |")
        print()
        print("| Noise source | Value and band | After 1 h |")
        print("|---|---|---|")
        for source, value, after in noise_rows(p):
            print(f"| {source} | {value} | {after} |")
        return 0

    print("\nhow the budget is summed (1 h, ppm)")
    for label, value in conventions:
        print(f"  {label:<44}{value:>7.2f}")
    print(f"\n  white noise in {p['loop_bw'] / 1e3:.0f} kHz of band: {ppm(white_band):.2f} ppm rms")
    print(f"  the same, averaged over the hour:        {ppm(white_1h):.3f} ppm  "
          f"(1/sqrt(T): it does not survive the interval)")
    print(f"  the 1/f terms are charged in full: they do not average down at all")
    print(f"\n  noise sources, and what the hour does to each")
    print(f"  {'source':<18}{'value and band':<46}{'after 1 h':>12}")
    for source, value, after in noise_rows(p):
        print(f"  {source:<18}{value:<46}{after:>12}")
    return 0


def verify_report(p: dict[str, float], markdown: bool) -> int:
    """What the planned fluxgate + DMM6500 setup can actually prove.

    The fluxgate's additive errors -- offset, its drift, its noise -- are fixed ampere-turn
    quantities, so N primary turns divide all of them by N when referred to the primary
    current. Its multiplicative errors (linearity, gain) are ratios of ampere-turns and do not
    care. Operating at the head's nominal therefore costs nothing but wire.
    """
    i_lim = p["i_max"]
    nominal_eff = p["fg_nominal"] / p["fg_turns"]           # A, referred to the primary
    occ = i_lim / nominal_eff                                # fraction of effective nominal
    off_rel = p["fg_off_tc"] * p["fg_nominal"] / p["fg_turns"] / i_lim   # ppm/K of signal
    fg_ppm_h = off_rel * p["fg_dT"]
    i_sec = i_lim * p["fg_turns"] / p["fg_ratio"]

    parts = (
        (f"fluxgate, {p['fg_turns']:.0f} turns ({occ:.0%} of effective nominal)", fg_ppm_h),
        ("secondary load resistor, inside the enclosure", p["r_load_tc"] * p["fg_dT"]),
        ("DMM6500 ratiometric path", p["dmm_ratio"]),
    )
    floor = math.sqrt(sum(v ** 2 for _, v in parts))

    if markdown:
        print(f"| Source | 1 h |")
        print("|---|---|")
        for label, value in parts:
            print(f"| {label} | {value:.3f} ppm |")
        print(f"| **verification floor** | **{floor:.2f} ppm** |")
        return 0

    print("\nverification floor of the fluxgate + DMM6500 setup")
    print(f"  head: {p['fg_nominal']:.0f} A nominal at one turn -> {nominal_eff:.1f} A with "
          f"{p['fg_turns']:.0f} turns")
    print(f"  offset drift, referred to the {i_lim:.1f} A signal: {off_rel:.1f} ppm/K "
          f"(was {p['fg_off_tc'] * p['fg_nominal'] / i_lim:.0f} ppm/K at one turn)")
    print(f"  secondary current {i_sec * 1e3:.0f} mA, load resistor "
          f"{i_sec ** 2 * 50:.2f} W into 50 Ω")
    for label, value in parts:
        print(f"  {label:<48}{value:>7.3f} ppm")
    print(f"  {'verification floor (RSS)':<48}{floor:>7.2f} ppm")
    print(f"  the 1 ppm/h target is verifiable with {p['target'] / floor:.1f}x margin")
    return 0


def main(argv: list[str] | None = None) -> int:
    # keep the report pipe-safe: Windows falls back to a legacy codec for pipes,
    # which cannot encode the µ/Ω in the descriptions
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--markdown", action="store_true",
                       help="emit the budget table for the note instead of a report")
    parser.add_argument("--set", nargs="*", default=[], metavar="NAME=VALUE",
                       help="override any default, e.g. --set r_sense=0.2")
    parser.add_argument("--thermal", action="store_true",
                       help="also analyse the heated-pair and oven variants")
    parser.add_argument("--trade", action="store_true",
                       help="also analyse cheap parts vs island stability")
    parser.add_argument("--parts", action="store_true",
                       help="also compare the two component sets, plain and servo'd")
    parser.add_argument("--sums", action="store_true",
                       help="also show how the terms are summed (correlated vs noise)")
    parser.add_argument("--verify", action="store_true",
                       help="also analyse the fluxgate + DMM6500 verification floor")
    args = parser.parse_args(argv)

    p = {name: v[0] for name, v in DEFAULTS.items()}
    for override in args.set:
        if "=" not in override:
            parser.error(f"--set expects NAME=VALUE, got {override!r}")
        name, _, raw = override.partition("=")
        if name not in p:
            parser.error(f"unknown parameter {name!r}; try one of {', '.join(p)}")
        p[name] = float(raw)

    report(p, args.markdown)
    if args.thermal:
        thermal_report(p, args.markdown)
    if args.trade:
        trade_report(p, args.markdown)
    if args.parts:
        parts_report(p, args.markdown)
    if args.sums:
        sums_report(p, args.markdown)
    if args.verify:
        verify_report(p, args.markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
