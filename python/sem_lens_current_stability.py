#!/usr/bin/env python3
"""Lens-current stability requirements for a three-lens SEM column.

Column: CL1 -> CL2 -> objective, where "the 3rd lens" is the probe-forming
objective.  Every number quoted in sem-lens-current-stability.md is produced
here, so the note and the script cannot drift apart.

Model
-----
A magnetic lens has 1/f ~ I^2, hence a fractional current change eps = dI/I
shifts the focal length by

    df/f = -2*eps

The binding criterion is focus: a defocus dz blurs the probe to 2*alpha*dz,
and we let that blur eat `budget` of the depth of focus DOF = d/alpha:

    dz_max = budget * d / alpha

    objective : dz = 2*Cc*eps                    -> eps = dz_max/(2*Cc)
    CL2       : dz = Mo^2 * 2*(1+m)^2*f_c*eps    -> eps = dz_max/(2*Mo^2*(1+m)^2*f_c)
    CL1       : min( crossover shift through CL2 and the objective,
                     probe-current drift 4*eps <= tol )

The objective sets the requirement for the whole column; the condensers come
free with the same supply.

Usage
-----
    python sem_lens_current_stability.py                    # report, `default` working point
    python sem_lens_current_stability.py --preset highmag   # 30 kV, 200 000x: 1 nm probe, short WD
    python sem_lens_current_stability.py --compare          # both working points, side by side
    python sem_lens_current_stability.py --markdown         # table rows for the note
    python sem_lens_current_stability.py --set d=5e-9 alpha=5e-3
"""

from __future__ import annotations

import argparse
import math
import sys

# name: (SI value, display divisor, display unit, description)
DEFAULTS: dict[str, tuple[float, float, str, str]] = {
    "V0":     (15e3,  1e3,  "kV",   "accelerating voltage"),
    "WD":     (10e-3, 1e-3, "mm",   "working distance"),
    "d":      (10e-9, 1e-9, "nm",   "probe diameter at the specimen"),
    "alpha":  (10e-3, 1e-3, "mrad", "convergence semi-angle at the specimen"),
    "Cc":     (10e-3, 1e-3, "mm",   "objective chromatic aberration coefficient"),
    "f_obj":  (8e-3,  1e-3, "mm",   "objective focal length"),
    "u_obj":  (50e-3, 1e-3, "mm",   "objective object distance (crossover)"),
    "f_cond": (20e-3, 1e-3, "mm",   "condenser focal length (CL1 and CL2)"),
    "m_cond": (0.3,   1.0,  "",     "condenser demagnification (CL1 and CL2)"),
    "budget": (0.5,   1.0,  "",     "focus budget, as a fraction of the depth of focus"),
    "tol_ip": (0.01,  1.0,  "",     "allowed probe-current drift (CL1 criterion only)"),
    "margin": (10.0,  1.0,  "",     "design margin before quoting a 1-2-5 spec"),
}

# Named working points. `default` is the modest 15 kV imaging condition;
# `highmag` is a 30 kV field-emission column pushed to 200 000x, where the probe
# is ~1 nm and the short working distance shrinks Cc and the focal length too.
PRESETS: dict[str, dict[str, float]] = {
    "default": {},
    "highmag": {
        "V0": 30e3,     # higher voltage: shorter lambda, same lens geometry
        "WD": 4e-3,     # short working distance is what buys the small Cc
        "d": 1e-9,      # probe, not pixel: a 0.5 nm pixel is already oversampled
        "alpha": 6e-3,  # optimum for Cs ~ 2 mm: balances diffraction against Cs
        "Cc": 2.5e-3,   # immersion objective, Cc ~ 0.6 * (1+M) * WD
        "f_obj": 3.5e-3,
        "u_obj": 26.7e-3,   # thin lens: 1/f = 1/u + 1/v with v = WD
    },
}


def ppm(x: float) -> float:
    """Parts per million, i.e. a relative quantity scaled by 1e6."""
    return x / 1e-6


def ladder_down(x: float) -> float:
    """Round down to the nearest 1-2-5 value, so the design margin survives."""
    e = math.floor(math.log10(x))
    for m in (5, 2, 1):
        if m * 10 ** e <= x:
            return m * 10 ** e
    return 10 ** e  # pragma: no cover - float-noise fallback


def solve(p: dict[str, float]) -> dict[str, float]:
    """Derive every intermediate and per-lens requirement from the parameters."""
    lam = 1.226e-9 / math.sqrt(p["V0"])        # electron wavelength [m]
    M = p["WD"] / p["u_obj"]                   # objective magnification (demagnified)
    dof = p["d"] / p["alpha"]                  # depth of focus [m]
    dz = p["budget"] * dof                     # focus budget [m]

    r: dict[str, float] = {"lambda": lam, "M": M, "dof": dof, "dz": dz}
    r["objective"] = dz / (2 * p["Cc"])
    r["objective_focal"] = dz / (2 * (1 + M) ** 2 * p["f_obj"])   # cross-check
    r["CL2"] = dz / (2 * M**2 * (1 + p["m_cond"]) ** 2 * p["f_cond"])
    r["CL1_focus"] = dz / (2 * M**2 * p["m_cond"] ** 2 * (1 + p["m_cond"]) ** 2 * p["f_cond"])
    r["CL1_current"] = p["tol_ip"] / 4         # dIp/Ip = 4*eps for m << 1
    r["CL1"] = min(r["CL1_focus"], r["CL1_current"])
    r["CL1_binds"] = "crossover shift" if r["CL1_focus"] < r["CL1_current"] else "probe current"

    # The same chromatic defocus comes from an HT change, without the factor 2:
    #   dz = Cc * (dV/V + 2*dI/I)
    # so the relative voltage requirement is twice as loose as the current one.
    r["voltage"] = dz / p["Cc"]

    # Gaussian cross-check on Cc itself: a pure focal-length change gives
    # dz = 2*(1+M)^2*f*eps, i.e. Cc_equivalent = (1+M)^2*f. Quote both routes
    # when they disagree, because that is the dominant uncertainty here.
    r["Cc_gauss"] = (1 + M) ** 2 * p["f_obj"]
    return r


def report(p: dict[str, float], r: dict[str, float], markdown: bool) -> None:
    if markdown:
        ol = r["objective"]
        ol_spec = ladder_down(ol / p["margin"])
        print("| Lens | Requirement | Governing criterion | Spec to quote |")
        print("|---|---|---|---|")
        print(f"| **Objective (3rd lens)** | {ppm(ol):.0f} ppm | "
              f"focus shift $\\Delta z = 2C_c\\,\\Delta I/I$ | "
              f"{ppm(ol_spec):.0f} ppm ({ol / ol_spec:.0f}x margin) |")
        print(f"| CL2 | {ppm(r['CL2']):.0f} ppm | crossover shift, demagnified by $M_o^2$ | "
              f"{ppm(ladder_down(r['CL2'] / p['margin'])):.0f} ppm |")
        print(f"| CL1 | {ppm(r['CL1']):.0f} ppm | {r['CL1_binds']} | "
              f"{ppm(ladder_down(r['CL1'] / p['margin'])):.0f} ppm |")
        return

    print("\ndefaults")
    for name, (_, div, unit, desc) in DEFAULTS.items():
        print(f"  {name:<8} {p[name] / div:>8.3f} {unit:<5} {desc}")

    print("\nderived")
    print(f"  lambda   {r['lambda'] / 1e-12:>8.1f} pm")
    print(f"  M_obj    {r['M']:>8.2f}      (WD / crossover distance)")
    print(f"  DOF      {r['dof'] / 1e-9:>8.0f} nm      d / alpha")
    print(f"  budget   {r['dz'] / 1e-9:>8.0f} nm      dz_max = budget * DOF")

    print("\nrequired current stability (dI/I)")
    print(f"  {'lens':<20}{'required':>12}{'quote':>12}")
    for label, key in (("objective (3rd)", "objective"), ("CL2", "CL2"), ("CL1", "CL1")):
        eps = r[key]
        spec = ladder_down(eps / p["margin"])
        print(f"  {label:<20}{ppm(eps):>9.1f} ppm{ppm(spec):>9.1f} ppm   "
              f"({eps / spec:.0f}x margin, 1-2-5)")

    print("\ncross-checks")
    for label, value in (
        ("objective via focal-length route",
         f"{ppm(r['objective_focal']):>8.1f} ppm  "
         f"({r['objective_focal'] / r['objective']:.2f}x the Cc route)"),
        ("equivalent Cc = (1+M)^2*f_obj",
         f"{r['Cc_gauss'] / 1e-3:>8.2f} mm  "
         f"(vs quoted Cc {p['Cc'] / 1e-3:.2f} mm, ratio {r['Cc_gauss'] / p['Cc']:.2f})"),
        ("HT stability (dV/V)",
         f"{ppm(r['voltage']):>8.1f} ppm  "
         f"({r['voltage'] * p['V0'] * 1e3:.2f} mV at {p['V0'] / 1e3:.0f} kV)"),
        ("CL1 via crossover shift", f"{ppm(r['CL1_focus']):>8.1f} ppm"),
        (f"CL1 via probe current ({p['tol_ip']:.0%})", f"{ppm(r['CL1_current']):>8.1f} ppm"),
        ("CL1 value set by", r["CL1_binds"]),
    ):
        print(f"  {label:<35}: {value}")

    ds = (2e-9, 5e-9, 10e-9, 20e-9)
    alphas = (5e-3, 10e-3, 20e-3)
    corner = "d \\ alpha"  # kept out of the f-string: 3.11 f-strings reject backslashes
    print("\nobjective requirement [ppm]: rows = probe d, columns = alpha")
    print(f"  {corner:>10}" + "".join(f"{a * 1e3:>12.0f} mrad" for a in alphas))
    for d in ds:
        cells = "".join(f"{ppm(p['budget'] * d / a / (2 * p['Cc'])):>12.1f}" for a in alphas)
        print(f"  {d / 1e-9:>7.1f} nm{cells}")
    print("\n  scaling: eps = budget*d / (2*alpha*Cc) ~ d / (alpha*Cc)")


def _comparison_rows() -> list[tuple[str, str]]:
    """Label plus one format callable per preset, so both renderers share the data."""
    return [
        ("$V_0$", lambda p, r: f"{p['V0'] / 1e3:.0f} kV"),
        ("working distance", lambda p, r: f"{p['WD'] / 1e-3:.0f} mm"),
        ("probe $d$", lambda p, r: f"{p['d'] / 1e-9:.1f} nm"),
        (r"$\alpha$", lambda p, r: f"{p['alpha'] / 1e-3:.0f} mrad"),
        ("$C_c$", lambda p, r: f"{p['Cc'] / 1e-3:.1f} mm"),
        (r"$(1+M)^2 f$", lambda p, r: f"{r['Cc_gauss'] / 1e-3:.2f} mm"),
        ("depth of focus", lambda p, r: f"{r['dof'] / 1e-9:.0f} nm"),
        ("focus budget", lambda p, r: f"{r['dz'] / 1e-9:.0f} nm"),
        ("objective, $C_c$ route", lambda p, r: f"{ppm(r['objective']):.0f} ppm"),
        ("objective, focal-length route", lambda p, r: f"{ppm(r['objective_focal']):.0f} ppm"),
        ("CL2", lambda p, r: f"{ppm(r['CL2']):.0f} ppm"),
        ("CL1", lambda p, r: f"{ppm(r['CL1']):.0f} ppm"),
        (r"high tension ($\Delta V/V$)",
         lambda p, r: f"{ppm(r['voltage']):.0f} ppm = "
                      f"{r['voltage'] * p['V0'] * 1e3:.0f} mV"),
        ("spec: objective", lambda p, r: f"{ppm(ladder_down(r['objective'] / p['margin'])):.0f} ppm"),
        ("spec: CL2", lambda p, r: f"{ppm(ladder_down(r['CL2'] / p['margin'])):.0f} ppm"),
        ("spec: CL1", lambda p, r: f"{ppm(ladder_down(r['CL1'] / p['margin'])):.0f} ppm"),
    ]


def comparison(names: list[str], markdown: bool) -> None:
    """Compare working points side by side, since the requirement is inherited, not scaled."""
    runs: list[tuple[str, dict[str, float], dict[str, float]]] = []
    for name in names:
        if name not in PRESETS:
            raise SystemExit(f"unknown preset {name!r}; known: {', '.join(PRESETS)}")
        p = {k: v[0] for k, v in DEFAULTS.items()}
        p.update(PRESETS[name])
        runs.append((name, p, solve(p)))

    cells = [(label, [f(p, r) for _, p, r in runs]) for label, f in _comparison_rows()]

    if markdown:
        print("| Quantity | " + " | ".join(name for name, _, _ in runs) + " |")
        print("|" + "---|" * (len(runs) + 1))
        for label, values in cells:
            print(f"| {label} | " + " | ".join(values) + " |")
        return

    w_label = max(len(label) for label, _ in cells)
    w_col = max(len(v) for _, values in cells for v in values)
    print("\n" + " " * (w_label + 2) + "".join(f"{n:>{w_col + 2}}" for n, _, _ in runs))
    for label, values in cells:
        print(f"  {label:<{w_label}}" + "".join(f"{v:>{w_col + 2}}" for v in values))


def main(argv: list[str] | None = None) -> int:
    # keep the report pipe-safe: Windows falls back to a legacy codec for pipes,
    # which cannot encode the µ/Ω in the default descriptions
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--markdown", action="store_true",
                       help="emit the markdown table rows for the note instead of a report")
    parser.add_argument("--set", nargs="*", default=[], metavar="NAME=VALUE",
                       help="override any default, e.g. --set d=5e-9 margin=3")
    parser.add_argument("--preset", choices=sorted(PRESETS), default="default",
                       help="named working point; --set wins over the preset")
    parser.add_argument("--compare", nargs="*", metavar="PRESET",
                       help="compare presets side by side (default: all of them)")
    args = parser.parse_args(argv)

    p = {name: v[0] for name, v in DEFAULTS.items()}
    p.update(PRESETS[args.preset])
    for override in args.set:
        if "=" not in override:
            parser.error(f"--set expects NAME=VALUE, got {override!r}")
        name, _, raw = override.partition("=")
        if name not in p:
            parser.error(f"unknown parameter {name!r}; try one of {', '.join(p)}")
        if name == "margin" and float(raw) < 1:
            parser.error("margin must be >= 1")
        p[name] = float(raw)

    if args.compare is not None:
        comparison(args.compare or list(PRESETS), args.markdown)
        return 0

    if not args.markdown:
        print(f"\npreset: {args.preset}")
    report(p, solve(p), args.markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
