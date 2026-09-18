---
title: "SEM lens current supply"
subtitle: "A 2 A, 1 ppm/hour linear current source: architecture and drift budget"
author: "Samo F."
date: "2025"
---

# TLDR

- The loop rejects everything it does not measure. So the entire budget lives in the
  measuring chain: reference, DAC gain, error-amp offset, thermal EMF, sense resistor.
- One hour is the drift interval because it is longer than every internal time constant,
  much shorter than aging, and longer than a session: 1 ppm/h buys **16.6 hours** before the
  focus walk alone would exhaust the objective's depth of focus.
- The five blocks (reference, DAC, op-amp, MOSFET, sense resistor) are enough — but only with
  a **1:1 servo** (no gain divider at all), a **quiet rail** (an LDO is mandatory, not an
  upgrade) and a **thermal layout** that treats the reference as a thermometer.
- The two biggest single terms in the 1 h budget are the reference's tempco and the thermal
  EMF of the Kelvin pair. Neither is a parts-quality problem; both are temperature problems.

# What the lens needs

The stability note [`sem-lens-current-stability.md`](sem-lens-current-stability.md) ends with a
specification: hold the objective lens current to about **2 ppm**, of which **1 ppm per hour
of drift** and **1 ppm rms of ripple** (the two together are 1.4 ppm by RSS, inside the 2 ppm
spec with 30 % to spare). This note is the supply that has to hit it.

| Load and compliance | Measured on the old column | Why it matters |
|---|---|---|
| Coil resistance | 8 or 16 $\Omega$ (16 $\Omega$ used below) | sets the whole compliance budget |
| Coil inductance | 40 mH (measure it) | sets the loop dynamics, not the drift |
| Current | 1.5 A into 16 $\Omega$ | 24.0 V cold, 28.8 V hot |
| Rail | 30 V | leaves ~1.2 V: about 1 V for the pass element, 0.2 V for the sense drop |
| $V_{\mathrm{sense}}$ | 0.15 V at 1.5 A, 0.20 V at 2 A (into 0.1 $\Omega$) | the budget tables use the 200 mV figure; see the trade table, because this rail has no room for a large one |
| Dissipation | 36-43 W in the coil, ~1.5 W in the pass element, 0.4 W in the shunt | the coil is water-cooled, the electronics are not |

The whole design follows from one sentence: **the loop rejects everything it does not
measure.** Rail sag, MOSFET drift, the coil's resistance rising 20 % when it warms up, cable
resistance: all inside the loop, all suppressed by the loop gain. What is left is the
measuring chain, and that chain *is* the drift budget:

$$\frac{\Delta I}{I} \;=\; \frac{\Delta V_{\mathrm{ref}}}{V_{\mathrm{ref}}}
  \;+\; \frac{\Delta V_{\mathrm{os}}}{V_{\mathrm{sense}}}
  \;-\; \frac{\Delta R_{\mathrm{sense}}}{R_{\mathrm{sense}}}$$

# Reality check: what the old SEM actually did

An old column is worth reading as a specification, and the first thing it settles is the
compliance. 30 V is not odd — it is *matched*:

| Load | cold | hot (+20 %) | + sense | fits 30 V? |
|---|---|---|---|---|
| 16 $\Omega$ at 1.5 A | 24.0 V | 28.8 V | 29.0 V | yes, ~1 V left |
| 16 $\Omega$ at 2 A | 32.0 V | 38.4 V | 38.6 V | no — needs ~40 V |
| 8 $\Omega$ at 2 A | 16.0 V | 19.2 V | 19.4 V | yes, but 10.6 V spare = 21 W in the pass element |

That last column is the whole art of a linear current source: leave the pass element just enough
voltage to stay in saturation — about a volt — and not a volt more. So the 30 V is a design
sized for a 16 $\Omega$ coil at roughly 1.5 A, with ~1 V for the MOSFET and ~0.2 V for the sense
drop. Which also means:

> **The compliance bounds the sense voltage.** With only ~1.2 V of margin, $V_{\mathrm{sense}}$
> has to stay small (0.1-0.25 $\Omega$ at 1.5 A). The cheap 5x improvement in offset sensitivity
> that a large $V_{\mathrm{sense}}$ would buy is simply not affordable on 30 V, so the old
> design's TO-3 foils are more likely a ~0.1 $\Omega$ sense resistor and the gain network than a
> 1 V sense resistor. If the coil current is well below 1.5 A there is room, and the schematic's
> sense-resistor value and servo divider will say which.

**Take these from the old design.**

- **The architecture.** LM399 plus bulk-metal-foil TO-3 parts is the measuring chain derived
  here, arrived at independently — and the TO-3 class (0.05-2 ppm/K, 5-30 W) is exactly what the
  budget asks for.
- **Compliance sized for the hot coil.** The rail includes the +20 % resistance rise. That is
  what the load table above is for, and it is the step easiest to forget.
- **A pass element idling at a watt or two.** Because the rail is matched, the MOSFET is not a
  heater, which also keeps its thermal gradients away from the measuring chain.

**Do not copy these.**

- **The reference — or rather the requirement it was chosen for.** An LM399 has 1 ppm pp of
  0.1-10 Hz noise, the largest single term in the budget here. The old instrument got away with
  it because its *requirement* was looser: a column aimed at micrometre work, whose focus budget,
  working distance and magnification were nothing like a 200 000x, 1 nm probe. The schematic is
  not evidence that a ppm was ever demonstrated end-to-end.
- **Its rail, unexamined.** With 30 V the pass element's output conductance leaks more in
  absolute terms, so rail clean-up matters *more* here than at 12 V. Find what made the rail
  quiet — the pre-regulator, the LC, the transformer taps. The taps are probably how the
  8 $\Omega$ lens avoids burning 21 W in the MOSFET.

# Why one hour

Drift is not a number without an interval: the same supply is 0.1 ppm over a minute and
10 ppm over a month. The interval has to be stated, and one hour is the honest choice:

- **Shorter than aging.** Resistor and solder-joint aging is quoted per 1000 h; over one hour
  it is far below the thermal terms. A 1 h spec therefore measures the *thermal* design, and
  aging gets its own line and its own calibration.
- **Longer than every internal time constant.** The shunt's thermal time constant is tens of
  seconds, the coil's is minutes, the closed box's is tens of minutes. One hour sees a settled
  system, so what it measures is drift rather than settling.
- **Longer than a session, which is the point.** At the 30 kV / 200 000x working point the
  objective's focus sensitivity is $2C_c = 5$ mm per unit $\varepsilon$ and the focus budget
  is 83 nm, so $\varepsilon = 17$ ppm exhausts the depth of focus. At 1 ppm/h that is
  **16.6 hours of continuous operation** before drift alone would force a refocus. A session
  is one to two hours. So 1 ppm/h means the operator never chases focus, with an order of
  magnitude to spare — and it is a target you can actually verify by logging for an hour.
- **Also the period of the dominant disturbance.** A building's HVAC cycle and a lab's daily
  swing both live at this scale, so "ambient moves less than 0.5 K per hour" is the
  disturbance a 1 h spec is designed against.

That fixes the wording of the spec: **the change in current between consecutive 1 h windows,
after a 30 min warm-up, at a fixed setpoint, with the ambient moving less than 0.5 K.**
Everything that settles during the warm-up (shunt self-heating, thermal gradients, the coil
reaching temperature) is a *bias*, not drift — the operator re-sets the current anyway. The
1 ppm is only about what still moves after the box has settled.

# Architecture

```
  V_ref --> DAC --> RC --> V_set ------+
                                       v
  V_sense ----------------------> [error amp] --> gate of M1
                                       ^
  +30 V --> LDO --> coil --> M1 drain --- M1 source --> R_sense --> GND
                                                        (4-terminal)
                                                              |
                                                              +--> V_sense (Kelvin pair)
```

Three consequences of this topology:

1. **The servo is 1:1, so there is no gain network.** $V_{\mathrm{sense}}$ is compared
   directly with the DAC output; nothing divides, so no resistor-ratio term enters the budget.
   This is why the five blocks are enough — no separate precision sense amplifier and no
   matched divider are needed.
2. **Everything upstream is rejected.** The coil's resistance rising 20 % (200 000 ppm) is a
   load change, and a current source's output follows it by $1/(1+T)$: with a DC loop gain of
   about $5\times10^5$, that is 0.4 ppm.
3. **Everything in the measuring chain is not.** The reference, the DAC's gain, the amp's
   offset, the thermal EMFs of the Kelvin pair and the sense resistor *are* the output current.

| Block | What it has to buy | Why it is in the budget |
|---|---|---|
| $V_{\mathrm{ref}}$ | 0.5 ppm/K or better, quiet, and kept away from heat | it defines the current |
| DAC | 16-18 bit, ratiometric to $V_{\mathrm{ref}}$, gain TC $\le 0.5$ ppm/K | its gain error is the current's scale factor |
| Error amp | zero-drift (chopper), offset drift $\le 0.05$ µV/K | offset adds directly to $V_{\mathrm{sense}}$: 0.1 µV on 200 mV is 0.5 ppm |
| Pass element | linear-mode rated, low output conductance | inside the loop, but its output conductance leaks rail ripple |
| Sense resistor | 4-terminal foil, $\le 0.2$ ppm/K, rated 10x its actual power | it is the current-to-voltage converter |
| Layout | isothermal island for reference, amp and Kelvin pair; heat goes elsewhere | thermal EMF and gradients are the biggest single terms |

# Do three lenses need three references?

No. The three supplies share an architecture, not a requirement:

| Lens | Required $\Delta I/I$ | What that means for its reference |
|---|---|---|
| objective | 17-25 ppm | the only one where the reference's tempco *and* noise matter |
| CL2 | 55-185 ppm | a 10 ppm/K bandgap, or 100 ppm/K plus a still box |
| CL1 | 610-2055 ppm | anything; a reference an order of magnitude worse would still pass |

So the architecture is one quiet, ovenized reference for the objective and something cheap for
the condensers. Whether that is *one reference or three* is then a packaging question rather
than an accuracy one:

- **One chassis, three channels**: share a single reference, and even a single multichannel DAC
  (AD5686R class). Give each DAC's reference pin its own RC — 1 k$\Omega$ with 1-10 µF — which
  is legitimate because every code is set-and-hold, and which both decouples the channels and
  low-passes the shared noise. One reference, three channels, and the channel *gains* then drift
  together, so the column rescales instead of losing alignment.
- **Three separate boxes**: either ship the reference out as a buffered, twisted-pair voltage
  with a local RC at each far end, or give the condensers their own €1-2 references and keep
  the quiet one (with its oven) in the objective's box. Do not run an unfiltered reference
  around a chassis next to three switching supplies.
- **One caution about sharing**: it makes the three lens currents *correlated* — they scale
  together. For the objective that changes nothing, and for the column it is arguably kinder
  (the beam stays on axis) than three independent drifts, each moving the axis its own way.

# The 1 h drift budget

Assumptions: $I = 2$ A, $V_{\mathrm{sense}} = 200$ mV in 0.1 $\Omega$; ambient moves 0.5 K over
the hour; box closed and settled (30 min warm-up); same-metal Kelvin pair laid out
isothermally.

| Item | Mechanism over the hour | 1 h drift |
|---|---|---|
| voltage reference | tempco x ambient | 0.25 ppm |
| DAC gain | ratiometric ladder, tempco x ambient | 0.10 ppm |
| sense resistor | tempco x ambient | 0.10 ppm |
| sense resistor | residual self-heating settling | 0.04 ppm |
| error amp | offset drift x temp / $V_{\mathrm{sense}}$ | 0.07 ppm |
| sense loop | thermal EMF drift / $V_{\mathrm{sense}}$ | 0.25 ppm |
| error amp | 0.1-10 Hz noise over 1 h / $V_{\mathrm{sense}}$ | 0.25 ppm |
| **reference** | **0.1-10 Hz noise, 1:1 into the setpoint** | **0.50 ppm** |
| **RSS** | | **0.68 ppm** |
| worst case (linear sum) | | 1.56 ppm |
| same, without the reference's noise (for continuity) | | 1.06 ppm |

- The RSS lands at 0.68 of the 1 ppm budget, the linear sum at 1.56 — so the margin depends
  entirely on how the terms are added. Those are not two answers but two bounds; the
  defensible middle is worked out in *How the budget is summed* below.
- **The reference's own noise is the largest single term**, and it is the one thing a stiller
  island cannot fix. That is why the LM399 is the wrong part here even though its tempco looks
  impressive; see the reference table in *Four combinations* below.
- The biggest *temperature-driven* terms are the reference's tempco and the Kelvin pair's EMF,
  which is thermal design rather than electronics sophistication: both yield to low-tempco parts
  and to holding the whole measuring chain at one temperature.
- The noise figures are not drift in the strict sense (random, not monotone), but over a
  one-hour window the 0.1-10 Hz band *is* what a slow observation sees, and unlike white noise
  it does not average down. Peak-to-peak figures are taken as plus/minus half — i.e. as bounds,
  not as $1\sigma$ values — which is exactly the inconsistency the summation section deals with.

# How the budget is summed

## Correlated terms add linearly, independent terms in quadrature

"Is this an RSS budget?" — not blindly. The table above mixes two kinds of quantity, and they
do not sum the same way.

- The **temperature-driven** terms (reference tempco, DAC gain, shunt tempco, its settling, the
  amplifier's offset drift, the Kelvin pair's EMF) are all driven by *one* shared quantity, the
  island's temperature. Their sensitivities act on a common driver, so a guaranteed worst case
  adds them **linearly**: 0.81 ppm, i.e. a chain sensitivity of 1.5 ppm/K. If the tempcos'
  signs are unknown and random — which is the normal case — the same group adds in
  **quadrature** to 0.39 ppm.
- The **independent** terms (the two 1/f noise figures) add in quadrature exactly, because the
  variances of independent processes add: 0.56 ppm.
- The two groups are independent of each other, so they combine in quadrature under either
  convention.

| Convention | 1 h budget |
|---|---|
| all terms, linear (guaranteed bound) | 1.56 ppm |
| all terms, RSS (random signs, incoherent) | 0.68 ppm |
| temperature group, linear | 0.81 ppm |
| temperature group, RSS | 0.39 ppm |
| independent group, RSS | 0.56 ppm |
| hierarchical, tempcos worst case | 0.98 ppm |
| hierarchical, tempcos random | 0.68 ppm |

So: **group by cause first, sum linearly within a group where a common driver or a common sign
is possible, and RSS across groups.** That gives 0.98 ppm as the defensible worst case for a
particular unit and 0.68 ppm as the statistical estimate — while 1.56 ppm is what you would
have to quote if you guaranteed it without knowing any sign.

The spread is also an opportunity. The reference's and the shunt's tempcos can be chosen with
*opposing* signs, in which case the group's linear sum becomes a difference rather than a sum:
in a budget whose temperature group is 0.81 ppm linear but 0.39 ppm in quadrature, deliberately
matching two tempcos is worth more than another round of parts selection.

## How noise is summed

Noise is where plain RSS is actually right — but only after two subtleties.

- **Independent sources add as powers** (amplitudes in quadrature). That is exact for
  incoherent noise, and it is why the two 1/f figures combine cleanly into 0.56 ppm.
- **1/f noise does not average down; white noise does.** Over a window $T$ the white part of a
  source contributes as $e_n/\sqrt{T}$, while the 1/f part is *flat* in $T$: flicker noise is
  indistinguishable from drift over any interval. So the budget charges the 0.1-10 Hz (1/f)
  figures in full and ignores the broadband part. Quantitatively, at 20 nV/√Hz and a 1 kHz loop
  bandwidth:
  - in band, that white noise is **3.16 ppm rms** — alarming;
  - averaged over the hour it is **0.002 ppm** — the interval kills it.
  A 1/f term cannot be treated that way, which is exactly why a noise figure is meaningless
  without its band.

One caveat about mixing: a datasheet peak-to-peak noise is a *bound* (roughly $3\sigma$) and a
tempco times a plausible ΔT is also a bound, so an RSS of bounds is not a $\sigma$ of anything
— it is an optimistic estimate of a quantity whose honest bounds are the linear column. Quote
the convention along with the number.

# The noise budget

Drift terms and noise terms are the same money, but noise has a parameter that drift does not:
a **band**. Every source has to be quoted with one, because that decides how the interval
treats it.

| Noise source | Value and band | After 1 h |
|---|---|---|
| reference 1/f | 0.50 ppm, 0.1-10 Hz | 0.50 ppm |
| error amp 1/f | 0.25 ppm, 0.1-10 Hz | 0.25 ppm |
| error amp white | 3.16 ppm, DC-1 kHz | 0.002 ppm |
| shunt Johnson | 0.006 ppm in band | 1.1e-07 ppm |
| DAC, unfiltered | keep under 40 nVpp on a 200 mV setpoint | 0.2 ppm if met |

Three things follow.

- **Only the 1/f column survives the hour.** The amplifier's broadband noise looks alarming in
  band (3.16 ppm) and is worth nothing at the end of the interval, because white noise averages
  as $1/\sqrt{T}$. The shunt's Johnson noise is negligible either way — 41 pV/√Hz across
  0.1 $\Omega$ — so no particular resistor technology is needed for it.
- **The DAC is the sleeper term.** A precision DAC's own 0.1-10 Hz output noise is a fixed
  voltage (hundreds of nV to a few µV, depending on the part), and unlike the reference's it is
  *not* scaled by the code. On a 200 mV setpoint that can be several ppm — larger than
  everything else in the table. A smaller setpoint is therefore not automatically quieter:
  either pick a DAC whose full scale is close to the sense voltage, or filter it.
- **Filtering the setpoint path is free; filtering the feedback path is fatal.** The setpoint is
  feedforward, so the DAC output and each reference pin can carry an RC as heavy as you like —
  1 k$\Omega$ with 1000 µF is a 0.16 Hz corner, 20-40 dB down across the 1-10 Hz band — without
  touching the loop's phase margin. The only price is that a spot change now takes a second or
  two to slew. The sense chain, by contrast, *is* the feedback path: any added pole there eats
  phase margin, so it stays fast.

This also reconciles the two halves of the 2 ppm specification: the 1 ppm rms figure is the
*broadband* part of this budget (what makes the image jitter, visible while scanning), and the
1 ppm/h figure is the 1/f part. They are not two budgets for two phenomena but two bands of one
budget, and a single source can be charged in both.

# Choosing the sense resistor

This is the only real design choice in the measuring chain, because two groups of terms pull
in opposite directions: offset, EMF and noise are divided by
$V_{\mathrm{sense}} = I R_{\mathrm{sense}}$, so they want a *big* resistor, while the
resistor's own temperature rise grows with $I^2 R_{\mathrm{sense}}$, so drafts, thermal
settling and the heat dumped next to the reference want a *small* one.

| $R_{\mathrm{sense}}$ | $V_{\mathrm{sense}}$ | $P$ | rise | offset+EMF+noise | tempco | RSS |
|---|---|---|---|---|---|---|
| 0.05 $\Omega$ | 100 mV | 0.20 W | 2 K | 1.14 ppm | 0.14 ppm | 1.15 ppm |
| 0.10 $\Omega$ | 200 mV | 0.40 W | 4 K | 0.57 ppm | 0.14 ppm | 0.59 ppm |
| 0.20 $\Omega$ | 400 mV | 0.80 W | 8 K | 0.28 ppm | 0.14 ppm | 0.33 ppm |
| 0.50 $\Omega$ | 1000 mV | 2.00 W | 20 K | 0.11 ppm | 0.14 ppm | 0.27 ppm |

(Thermal resistance 10 K/W, tempco 0.2 ppm/K, draft sensitivity folded in as 5 % of the rise.)

The table prefers a large resistor, and it is right — up to the point where it is not:

- 0.5 $\Omega$ at 2 A is **2 W of heater inside the box**, and its 20 K rise is precisely the
  thermal gradient that drifts the reference and the Kelvin pair. It also costs a volt of
  rail and a 1 V DAC range.
- 0.1 $\Omega$ / 200 mV is the compromise: buy the offset sensitivity down with a chopper amp
  instead of with more sense voltage.
- If the shunt can live in its own compartment, away from the reference, 0.2 $\Omega$ is the
  better choice and the model agrees (0.33 vs 0.59 ppm).
- The *part* matters more than the value: **4-terminal (Kelvin) bulk-metal foil**, $\le 0.2$ ppm/K
  over the box temperature range, rated at least 5 W for 0.4 W actual, with the sense
  terminals connected as a matched, isothermal copper pair. Copper is 3900 ppm/K; the Kelvin
  pair is what keeps copper's tempco out of the measurement, but only if it is truly a pair.

# A heated pair: can a sibling resistor hold the shunt still?

The proposal: put a second resistor next to the sense resistor, drive it so that the pair's
**total dissipation never changes**, and freeze the pair's temperature rise. It is a good
instinct and the arithmetic is tractable, but as stated it fixes the wrong term.

## The control law is a sum of squares, not a sum

The pair's temperature is set by power, not by current:

$$T_{\mathrm{pair}} = T_{\mathrm{amb}} + \theta\,(I^2 R_a + I_h^2 R_b)$$

so what must be held constant is $I^2 R_a + I_h^2 R_b$. For equal resistors that is the
**root-sum-square** of the two currents, $I_h = \sqrt{S^2 - I^2}$, not their sum.

The naive version — hold the sum $I + I_h = S$ — is rescued by a coincidence: the power error
is exactly *quadratic* in the departure from the balanced split,

$$\frac{\Delta P}{P} = x^2, \qquad x = \frac{I - S/2}{S/2}$$

with the pair balanced at $I_{\max}$ ($S = 4$ A, 0.80 W, an 8 K rise):

| Imbalance $x$ | $\Delta P/P = x^2$ | $\Delta T$ | shunt drift |
|---|---|---|---|
| 0.00 | 0 % | 0.00 K | 0.000 ppm |
| 0.10 | 1 % | 0.08 K | 0.016 ppm |
| 0.25 | 6 % | 0.50 K | 0.100 ppm |
| 0.50 | 25 % | 2.00 K | 0.400 ppm |
| 1.00 | 100 % | 8.00 K | 1.600 ppm |

So the cheap law is excellent near the design point and useless at the extremes — $x = 1$ is
the heater switched off, i.e. back to a plain single shunt. The standing cost is real: making
the balance point 2 A means the pair idles at 0.80 W instead of 0.40 W, and the heater source
has to deliver 2 A at 0.2 V.

## What it buys: 0.04 ppm out of 1 ppm

| Variant | What it removes | 1 h drift RSS |
|---|---|---|
| baseline, single shunt | - | 0.68 ppm |
| heated pair, constant power | the shunt's residual settling | 0.68 ppm |
| oven, temperature servo, gain 20 | every temperature-driven term | 0.56 ppm |
| oven + 0.2 $\Omega$ shunt | the above, plus half of the $V_{\mathrm{sense}}$ terms | 0.52 ppm |

The pair buys nothing for the reason the interval is defined the way it is: **within the hour
the load current is already constant**, so the shunt's dissipation is already constant. Its
power-dependent drift was counted as a *bias* — settling during the 30 min warm-up — and what
remains in the budget is the ambient-driven term,

$$\varepsilon_R = \mathrm{TCR}\,\Delta T_{\mathrm{amb}} = 0.2\ \mathrm{ppm/K} \times 0.5\ \mathrm{K} = 0.10\ \mathrm{ppm}$$

A constant-power servo cannot touch that, because the pair still sits at
$T_{\mathrm{amb}} + \theta P$ and the ambient still moves. **Constant power freezes the rise,
not the temperature.** It does not fix drafts either: a draft changes $\theta$, and the servo
faithfully holds $P$ while $T$ wanders.

The operator, however, does change the current between settings. That is a *step* rather than
drift — but it is exactly what decides whether a cheap, high-tempco shunt is usable at all,
which is the subject of *Trading parts for thermal stability* below.

## The right version of the idea is an oven

Keep the second resistor as the heater, but change what its feedback measures: servo
**temperature** (a thermistor on the pair, heater drive from an op-amp), not power. Now loop
gain fights the ambient instead of ignoring it:

- every temperature-driven term in the budget divides by the oven's gain — including the two
  largest contributors, the reference's tempco (0.25 ppm) and the thermal EMF of the Kelvin
  pair (0.25 ppm);
- drafts are *compensated* rather than merely un-helped, so the draft penalty disappears;
- the real prize is that the **reference can live in the same oven**, which drops its 0.5 ppm/K
  requirement by the loop gain and lets a cheaper part do the job.

RSS 0.68 → 0.56 ppm, an 18 % cut — and the residual is now the *reference's own noise* (0.50
ppm) rather than anything thermal. Which is the point: once the temperature terms are buried,
thermometry stops being the lever and a quiet reference becomes it. Note the last row: a bigger
shunt buys almost nothing (0.56 → 0.52) because the reference's noise does not scale with
$V_{\mathrm{sense}}$, so the earlier "the oven unlocks a 0.2 $\Omega$ shunt" argument only
holds if the reference is quiet too.

The constraint is thermodynamic: a heater can only add heat, so the oven setpoint must sit
above the pair's self-heated temperature at maximum current, and the pair's own dissipation
becomes a disturbance the servo absorbs. That is precisely the "waste heat to freeze the
total" idea — spent on a servo that fixes something.

## The heater's own accuracy is nearly free

Because the heater reaches the signal only through temperature, its accuracy requirement is
absurdly loose. A relative heater-current error $\varepsilon_h$ moves the pair by
$\Delta T = 2\varepsilon_h \theta P_h$ and the shunt by $\mathrm{TCR}$ times that:

$$\varepsilon_{\mathrm{signal}} = 2\,\varepsilon_h\,\theta\,P_h\,\mathrm{TCR}
  = 1.6\ \mathrm{ppm} \text{ per unit } \varepsilon_h$$

so the heater may be **0.6 % wrong** and still contribute only 0.01 ppm: it can be roughly
**6000x sloppier than the 1 ppm signal target** and hang off the crudest rail in the box. That
part of the intuition is exactly right, and it is why the second resistor costs almost nothing
in parts.

## Implementing the squaring law

The constant-power law needs a squaring operation: with equal resistors the pair dissipates
$P = R(I^2 + I_h^2)$, so holding it constant means holding the *hypotenuse*
$\sqrt{I^2 + I_h^2}$ constant, i.e. driving

$$I_h = \sqrt{S^2 - I^2}, \qquad S^2 = 2\,I_{\max}^2, \quad S = 2.83\ \mathrm{A}$$

Four ways to get there, in increasing order of effort and decreasing order of sense:

| Route | How | Accuracy | Verdict |
|---|---|---|---|
| **software** | the MCU already knows $I$ — it wrote the DAC that makes it. Compute $I_h$ in one line, write it to the heater's DAC | exact | **do this** |
| **linear approximation** | $I_h = S' - I$: a subtractor, or the same one-liner | power error $x^2$: 1 % at a 10 % imbalance, i.e. 0.016 ppm | good enough, and what an analog build would do |
| true-RMS chip | LTC1968 or AD737 square and root internally | 0.1-0.5 % | only if there is no digital control at all |
| analog multiplier | AD633 or AD734, four-quadrant | 0.1-1 % | pointless here |

Why that accuracy column is so forgiving: the heater reaches the signal only through the
temperature, at 1.6 ppm of shunt drift per *unit* of heater error, so 0.6 % of heater error is
0.01 ppm. The squaring function's own offset, tempco and noise are all irrelevant — whatever
crude part is already in the box will do. What matters is only that the *sum* is right on a
slow timescale, which is an arithmetic problem, not an analog one.

The heater drive is then the same topology as the main loop — DAC, error amp, MOSFET, its own
sense resistor — with none of the ppm care: any 12-bit DAC, any op-amp, the cheapest rail. Its
resolution only has to resolve 0.6 % of 2 A = 12 mA, which 12 bits beats by 25x.

**The physical pairing is the real implementation.** Put the second resistor in the *same
package* as the sense resistor — a dual-element foil network on one substrate — and the thermal
coupling between the elements is 0.01-0.1 K/W instead of the ~10 K/W of two discrete parts.
That shrinks the heater power needed by two orders of magnitude and gives the pair a tracking
tempco as a bonus. That, rather than any multiplier, is what makes the scheme practical.

(If "multiplier" meant the *setpoint* multiplier instead: that is a voltage-mode multiplying
DAC, whose output is $V_{\mathrm{ref}} \times D$. Nothing to design, and its relative noise
and gain drift pass through 1:1 exactly as the reference's do.)

## So when is the second resistor worth it?

- **Not for the drift budget.** 0.04 ppm of a 1 ppm target (RSS 0.68 → 0.68 ppm), paid for
  with 0.40 W of standing extra heat in a box whose reference is a thermometer.
- **Yes if the operator changes the spot size.** The shunt's dissipation then steps by
  $(I_{\max}^2 - I_{\min}^2)R$ — 0.8 ppm of bias plus a tens-of-seconds thermal transient that
  also pushes the reference and the Kelvin pair around, i.e. a re-focus after every setting
  change. A pair, or a dummy load that keeps the supply's *total* current constant, turns that
  step into a non-event.
- **Yes, upgraded to an oven, if you want margin.** 0.68 → 0.56 ppm — a smaller gain than the
temperature terms alone would suggest, precisely because the reference's noise does not care
about temperature (see *What thermal control cannot buy*).

# Trading parts for thermal stability

The practical question: the operator changes the current with magnification anyway, so why pay
for a 0.2 ppm/K foil shunt and a 0.5 ppm/K reference? Can thermal control buy the right to use
cheap parts instead? Mostly yes — and the exchange rate is *kelvin of island stability per
ppm/K of part quality*.

## The exchange rate is ppm/K against kelvin

Every temperature coefficient in the chain reaches the current only through the temperature of
the island the part sits on:

$$\varepsilon = \mathrm{TC} \times \Delta T_{\mathrm{island}}$$

so "how bad a part can I use?" is the same question as "how still can I hold the island?".
Asking each term for a 0.1 ppm share:

| Part tempco | Island must hold, for a 0.1 ppm share | What delivers it | Part class |
|---|---|---|---|
| 0.2 ppm/K | 0.50 K | nothing special, a closed box | foil, what we buy today |
| 1.0 ppm/K | 0.10 K | closed box plus thermal mass | metal strip, good chip |
| 5.0 ppm/K | 20 mK | insulated island with mass | thin film |
| 50.0 ppm/K | 2 mK | temperature servo required | thick film |
| 100.0 ppm/K | 1 mK | temperature servo, careful sensor | cheap chip, bandgap ref |

Read it right to left and it is a recipe: pick the parts you are willing to pay for, and the
required island stability falls straight out. A 1 € thick-film shunt and a 1 € bandgap
reference need 1-2 mK, at which point the money has moved out of parts and into thermal
engineering — a copper block, a thermistor, a heater FET and insulation.

The reference is not an exception to this: the LM399 sits in the 0.5 ppm/K row only because it
*is* an oven — a heater and a temperature-servoed die on one chip. Buying it is buying the
servo, one chip at a time.

## The shunt is the awkward one, because the operator moves the current

The reference sees the ambient and nothing else. The shunt also sees its own dissipation — and
with magnification the operator *steps* the current, so the dissipation steps with it:

$$\Delta R/R = \mathrm{TCR}\,\theta\,R\,(I_{\mathrm{hi}}^2 - I_{\mathrm{lo}}^2)$$

Going from 2 A to 0.4 A is a 3.8 K step, which a foil shunt converts into 0.77 ppm and a
thick-film shunt into 192 ppm:

| Shunt tempco | $\Delta R/R$ for 2.0 A to 0.4 A | focus shift | vs the 83 nm budget |
|---|---|---|---|
| 0.2 ppm/K | 0.768 ppm | 3.84 nm | 0.05x |
| 1.0 ppm/K | 3.84 ppm | 19.2 nm | 0.23x |
| 5.0 ppm/K | 19.2 ppm | 96.0 nm | 1.16x |
| 50.0 ppm/K | 192 ppm | 960 nm | 11.57x |
| 100.0 ppm/K | 384 ppm | 1920 nm | 23.13x |

The operator absorbs most of this by re-focusing — the objective current *is* the focus knob —
but it takes tens of seconds to settle, the first frames after every magnification change are
soft, and the current itself is wrong by 192 ppm meanwhile; through a condenser lens that
becomes ~0.08 % of probe current, the same order as a quantitative analysis budget. With a
foil shunt all of it is ~200x smaller, at 0.05x of the depth of focus: invisible.

This is also the limit of the constant-power pair from the previous section. It removes the
*setpoint* part of the step, but the shunt still tracks the ambient, and a 50 ppm/K shunt
seeing a 0.5 K ambient swing is 25 ppm — 250x the budget. Thermal control that licenses a
cheap shunt has to hold the temperature against *both* disturbances, which means a servo with
authority over the step: an oven, not a power trick.

## What thermal control cannot buy

**Noise, aging and hysteresis.** None of them is a temperature coefficient, so a stiller
island does not touch them:

- the reference's own noise, not the amplifier's, is what is left after the oven — 0.50 against
  0.25 ppm. It is the largest single term in the budget, no oven fixes it, and (being 1/f) it
  does not average down, so a quiet reference is the only cure;
- the error amplifier's 1/f noise is next at 0.25 ppm: a cheap amplifier would be several times
  worse, and the same argument applies — keep it low-noise;
- aging sets the *calibration* interval rather than the drift, and since the operator
  re-establishes the setpoint every session it barely matters for a microscope.

So the rule is: **cheapen everything whose error is a temperature coefficient, and nothing
whose error is noise.** Here that means a cheap shunt and a cheap reference on a 1 mK island,
plus the one low-noise chopper amplifier and a low-noise reference — and the parts saved pay
for the oven several times over.

# Four combinations: the original parts against a 0.25 Ω, 2 ppm/K part

## What a 0.25 Ω shunt actually changes

At 2 A, a 0.25 Ω part is not just "a worse shunt":

| | 0.1 $\Omega$ foil | 0.25 $\Omega$ (Y0850 class) |
|---|---|---|
| $V_{\mathrm{sense}}$ at 2 A | 200 mV | 500 mV |
| dissipation at 2 A | 0.40 W | 1.00 W |
| self-heating step, 2 A to 0.4 A | 3.8 K | 9.6 K |
| tempco | 0.2 ppm/K | 2 ppm/K |

The higher resistance buys a 2.5x larger measurement signal, and *every* term that divides by
$V_{\mathrm{sense}}$ gets 2.5x better with it. What gets worse is everything that multiplies
the shunt's tempco — 10x worse — and the self-heating steps, 2.5x bigger. Which of the two
effects wins is decided entirely by the thermal design.

## The four combinations

| Component set | Plain, no thermal control | With a temperature servo |
|---|---|---|
| original: 0.1 $\Omega$ foil, 0.2 ppm/K + LM399 | 0.68 ppm (plus a 0.77 ppm step per magnification change) | 0.56 ppm |
| Y0850: 0.25 $\Omega$, 2 ppm/K + quiet 2 ppm/K reference | 1.49 ppm (plus a 19.2 ppm step per magnification change) | 0.16 ppm |

And the same four, term by term (all ppm over one hour):

| Term | original, plain | Y0850, plain | original, servo | Y0850, servo |
|---|---|---|---|---|
| voltage reference (tempco x ambient) | 0.25 | 1.00 | <0.01 | <0.01 |
| DAC gain | 0.10 | 0.10 | <0.01 | <0.01 |
| sense resistor (tempco x ambient) | 0.10 | 1.00 | <0.01 | <0.01 |
| sense resistor (self-heating settling) | 0.04 | 0.40 | <0.01 | <0.01 |
| error amp offset drift | 0.07 | 0.028 | <0.01 | <0.01 |
| sense loop thermal EMF | 0.25 | 0.10 | <0.01 | <0.01 |
| error amp 1/f noise | 0.25 | 0.10 | 0.25 | 0.10 |
| **reference noise** | **0.50** | **0.125** | 0.50 | 0.125 |

Reading the table:

- **The 2 ppm/K part without an oven is the worst of the four** — 1.49 ppm of drift, plus a
  19 ppm step every time the operator changes magnification. It is not a cheap substitute for
  the foil shunt; it is a part that *requires* thermal control to be usable at all.
- **With a servo it becomes the best, by 3.5x** (0.16 against 0.56 ppm) *and the cheapest*.
  Once the temperature terms are divided by 250, what is left is noise, and the 0.25 $\Omega$
  part divides every noise term by its 2.5x larger $V_{\mathrm{sense}}$.
- **The original set is limited by its reference, not by its resistor.** With the oven in, the
  LM399's own noise (1 ppm pp in 0.1-10 Hz, i.e. 0.5 ppm here) is the largest single term in
  the table, and the 0.5 ppm/K tempco it is famous for is exactly what the oven makes
  redundant. Even the 0.25 ppm floor from the amplifier's own noise does not need the
  expensive shunt.
- **Evaluate this at the lowest current you care about, not at 2 A.** The 2.5x advantage holds
  at any given current, but the absolute numbers in the table are the 2 A ones; at 0.5 A every
  $V_{\mathrm{sense}}$-divided term is four times larger.

## The matching reference for the cheap version

With a 2 mK island a reference's *tempco* stops mattering (2 ppm/K x 2 mK = 0.004 ppm) while
its *noise* does not, because the reference is the setpoint's scale factor and its noise enters
the current 1:1. So the cheap version should be bought on noise:

| Reference | 0.1-10 Hz noise | relative (2.5 V) | tempco | verdict |
|---|---|---|---|---|
| LTC6655-2.5 | 0.625 µVpp | 0.25 ppm | 2 ppm/K | **the match**: LTZ1000-class noise at a fraction of the price |
| ADR4525 | 1.25 µVpp | 0.5 ppm | 2 ppm/K | fine second choice |
| MAX6070A, REF5025 | 3-4 µVpp | 1.2-1.6 ppm | 3-6 ppm/K | only with the filter below |
| LM399 | 7 µVpp | 1.0 ppm | 0.5 ppm/K | the tempco you pay for is the one the oven replaces |
| LTZ1000 | 1.2 µVpp | 0.17 ppm | 0.05 ppm/K | strictly better, needlessly expensive here |

(Datasheet-typical figures — verify before ordering.)

If you want the cheap reference anyway, filter it: because the code is **set and hold**, the
DAC's reference pin can carry a heavy RC — 1 k$\Omega$ with 1000 µF is a 0.16 Hz corner,
20-40 dB down in the 1-10 Hz band of interest — with no code-dependent error to worry about.
That makes a 4 µVpp part behave like a 0.5 µVpp one where the drift budget lives.

One caution on the 0.25 $\Omega$ part at 2 A: 1.00 W is a lot for a chip resistor. Check the
power rating and derating, mount it on copper — the 9.6 K step above assumes 10 K/W, and a
part run near its rating in still air can be 30-60 K/W, which triples the step — and remember
that inside the oven that watt is heat the servo must absorb, so the setpoint has to sit above
its hot-case temperature.

# What the five-block sketch hides

## The rail has to be quiet

The pass element is inside the loop, but not perfectly: a change in $V_{ds}$ still moves the
current through the device's output conductance, and at 100 Hz the loop has only about 20 dB
of gain left when the crossover is at 1 kHz.

- A linear-mode MOSFET leaks on the order of **0.1 %/V of $V_{ds}$** (1000 ppm/V). Check the
  datasheet's output curves — and check them *after* warm-up, because the DC part of that
  dependence is thermal and the loop does reject that.
- 2 V of ripple from a raw rectifier, with 11x of loop rejection, is **182 ppm**.
- So the rail must hold its 100 Hz ripple below ~2200 µV to contribute 0.2 ppm. A raw
  rectifier is not enough: an **LDO is mandatory**, and an LDO plus 10 µH/1000 µF gives
  another 48 dB at 100 Hz, which is comfortable.

If the measured leakage turns out worse than 0.1 %/V, the fix is a cascode: a second MOSFET
holding the pass element's $V_{ds}$ constant, so rail ripple never reaches the current.

## Thermal layout is a first-class part of the budget

The box holds a 1.5 W pass element and a 0.4 W shunt, while the instrument holds a 36-43 W coil
(water-cooled, and usually in the same room). The reference is a thermometer.
Concretely: reference, amp and Kelvin pair on one isothermal island; the pass element's
heatsink dumping heat *outside* the box; the shunt out of the reference's warm air plume; and
**no fans or drafts inside**, because a draft makes the shunt's temperature wander at exactly
the time scale of the measurement (that is the 5 %-of-rise term in the trade table).

## Resolution is not stability

| DAC | one LSB | verdict |
|---|---|---|
| 12 bit | 244 ppm | plenty to set a spot size |
| 16 bit | 15.3 ppm | fine, but one LSB step is 15x the drift budget: **set and hold** |
| 18 bit | 3.8 ppm | fine |
| 20 bit | 0.95 ppm | fine to trim during a session |
| 24 bit | 0.06 ppm | more resolution than the reference can hold anyway |

The operator focuses the image, so the *absolute* accuracy of the current does not matter at
all — only its stability does. But if software writes to the DAC mid-session it steps the
current by one LSB, 15 ppm at 16 bit, which is worse than the entire drift budget. Either hold
the code constant while imaging, or use 20 bit or better.

## The load is inductive

40 mH does not affect the drift, but it dictates dynamics and protection: a freewheel diode
across the coil is mandatory, disabling must *ramp the setpoint down* rather than gate the FET
off, and the slew rate is set by the headroom — 3.4 V across 40 mH is 85 A/s, so a full-scale
2 A step takes about 24 ms.

## Grounding

One star point at the sense resistor. The only current-carrying ground is the shunt's return;
the Kelvin pair, the amp and the DAC's reference all connect at the shunt terminals and carry
no load current, so copper's 3900 ppm/K never appears in the measurement.

# The loop

- **Plant:** a current source into an inductive load, a single pole at $R_c/L_c$ = 64 Hz with
the measured 16 $\Omega$ coil (14 Hz if it really were 3.5 $\Omega$).
- **Compensator:** type II — an integrator with a zero at the plant pole, which keeps a -1
  slope through the 1 kHz crossover and leaves roughly 90 degrees of phase margin.
- **DC loop gain:** the amp's open-loop gain times transconductance times
  $R_{\mathrm{sense}}$, about $5\times10^5$ (114 dB). That is what turns the coil's 20 %
  resistance rise (200 000 ppm) into 0.4 ppm of current error, and it is the same number the
  rail-step test measures.
- **Settling:** milliseconds small-signal, about 24 ms for a full-scale step (the inductor).

# How we would know we got there

One ppm of a 200 mV sense voltage is 200 nV, and that is the entire measurement problem: a
6.5-digit bench DMM cannot do it (its own 1 h drift is 5-20 ppm, its tempco 5 ppm/K), so at
best it serves as a null detector against something better.

- **Log $V_{\mathrm{sense}}$ for an hour** with a nanovoltmeter (1 nV resolution) connected
  differentially across the Kelvin pair, box closed, after the warm-up. This is the direct
  test of the drift spec.
- **Or use a 24 bit sigma-delta ADC referenced to the same $V_{\mathrm{ref}}$**, so the ADC's
  own reference drift cancels in the ratio $V_{\mathrm{sense}}/V_{\mathrm{ref}}$. This is the
  right way to instrument a supply like this one.
- **Rail-step test.** Step the rail by 1 V and watch the current. That measures the real loop
  gain and the real leakage per volt, i.e. it checks the one assumption behind the ripple
  calculation.
- **Current-reversal test.** On the bench with a dummy load, reverse the current and average:
  the thermal EMF keeps its sign while the current flips, so half the difference is the EMF
  and the mean is the true current. It quantifies the term that dominates the budget, and it
  is the only way to see it — you cannot reverse the lens field itself.

## The floor of this setup: LEM fluxgate + DMM6500

Whatever the instruments cannot see is the smallest specification this project can honestly
claim, so it is worth fixing that floor before building anything.

**The spec is about *stability*, and that is the key that unlocks the instrumentation.** 1 ppm
per hour is a relative *change*, not an absolute current, so the instruments only need
stability — not accuracy. A perfectly ordinary shunt plus a ratiometric voltmeter can resolve a
1 ppm/hour change while being 1000 ppm wrong in absolute terms.

| Path | What limits it | Class of the limit |
|---|---|---|
| DMM6500 as an absolute voltmeter on 200 mV | its own front-end thermal EMF (~1 µV is 5 ppm), its tempco (a few ppm of reading per K), 1-year accuracy (tens of ppm) | 5-30 ppm — cannot certify 1 ppm |
| DMM6500 used *rationally*: $V_{\mathrm{sense}}$ and $V_{\mathrm{ref}}$ on one instrument | the ratio cancels the instrument's reference, gain drift and most of its tempco | ~0.1-0.5 ppm (noise and differential nonlinearity) |
| an external shunt + DMM | the shunt's TCR and self-heating — and if it is the DUT's own sense resistor, the measurement cannot separate the shunt's drift from the supply's | ~0.2-1 ppm, but blind to the shunt |
| the LEM fluxgate at *one turn*: 2 A on a 60 A-nominal head | its additive errors are fixed ampere-turn quantities, so at 3 % of nominal they are 30x worse referred to your current | 600 ppm/K — fixable with turns, and only with turns |
| the fluxgate *zeroed*, temperature-stabilized, used as a null comparator | its residual offset drift (already divided by the turns), the secondary load resistor's TCR, the null detector's noise | ~0.2 ppm — and it is the only sensor that sees the real current *including* the DUT's shunt |

### Adding turns: the fix that makes the fluxgate usable

The fluxgate's error terms split cleanly, and that split is what saves it:

| Error term | Scales as | Why |
|---|---|---|
| offset, zeroed before the run | $1/N$ | a fixed ampere-turn or flux imbalance |
| offset *drift* with temperature | $1/N$ | the same quantity, different cause |
| noise, referred to the primary | $1/N$ | again a fixed ampere-turn quantity |
| linearity, gain, scale factor | unchanged | fractional errors *of* the ampere-turns |
| bandwidth, insertion impedance | unchanged | set by the secondary circuit, not by $N$ |

So **thread the 2 A through the aperture about 30 times**. The head then sits at its nominal
operating point instead of at 3 % of it, and everything additive improves 30x:

- **60.0 A nominal at one turn becomes 2.0 A** with 30 turns — exactly the operating current;
- the **offset drift referred to the signal goes from 600 ppm/K to 20 ppm/K**;
- the **secondary current lands at 100 mA**, the head's own nominal, so the load resistor runs at
  a rated 0.5 W into 50 $\Omega$ — and since that resistor's TCR scales the output 1:1 it
  belongs in the same enclosure as the head (inside, its share is 0.002 ppm/hour; left out in a
  room moving 0.5 K, it is 0.1 ppm/hour);
- the head adds **almost no insertion impedance**, because zero-flux operation cancels the
  primary magnetizing inductance — which is the entire reason to prefer it over a shunt.

What turns do *not* fix is the head's own temperature. They stop you operating at 3 % of
nominal; the residual offset drift is still 20 ppm/K, so a 10 mK/hour enclosure turns it into
0.2 ppm/hour, and that is what makes the fluxgate a credible sub-ppm *stability* witness. Two
practical limits: the aperture has to fit 30 turns of 2 A conductor (roughly a 25 mm hole for
~2 mm wire), and the linearity spec — tens of ppm — remains a *scale* error. That one is stable,
so it costs absolute accuracy, not the one-hour stability being measured.

So the shape of the plan is: **use the fluxgate as a coarse but genuinely independent sensor**
(it checks the absolute scale to tens of ppm and would catch a gross error, using magnetic
rather than resistive physics), and **get the ppm resolution from the ratiometric DMM
measurement of the supply's own sense chain** — accepting that this route is blind to the
shunt's own drift, which is exactly why the fluxgate has to be in the setup at all. Their
*difference* is the most informative number either instrument can produce on its own.

Then verify the budget in pieces, because each piece wants a different instrument:

1. **the measuring chain** (reference, DAC, amplifier, shunt) in ppm — DMM6500, ratiometric,
   one-hour log;
2. **the loop's rejection** of rail and load changes — a step test, needing no absolute
   instrument at all;
3. **the thermal EMF** — current reversal on a dummy load, half the difference of the two means;
4. **the absolute scale** — the fluxgate, at tens of ppm, plus agreement with (1).

**The honest conclusion, revised by the turns.** With the head at 30 turns and its enclosure held
to 10 mK over the hour, the setup's floor is **0.36 ppm/hour** — the fluxgate at 0.20, the
DMM's ratiometric path at 0.30, the load resistor at 0.002 — so the 1 ppm/hour target is
verifiable with about 2.8x margin. That makes the instrumentation the *co-equal* of the design
rather than its ceiling: the budget claims 0.68 ppm RSS, the setup can see 0.36 ppm, and both
live or die on the same thing, temperature. Anything better than ~0.3 ppm/hour is not claimable
with this setup, which is the sensible stopping point for the design.

# If the budget does not close

| Symptom | Fix |
|---|---|
| the ambient is what moves it | ovenize the reference (LTZ1000 class, 0.05 ppm/K), or insulate the whole measuring island |
| the rail leaks | cascode the pass element, raise the loop gain, or filter harder |
| the shunt is the limit | raise $V_{\mathrm{sense}}$ (see the trade table), or add a current-comparator or fluxgate sensor |
| offset and EMF are the limit | add a **slow digital servo**: a 24 bit ADC at the Kelvin points, ratiometric to $V_{\mathrm{ref}}$, trimming the DAC. It sees what the analog loop cannot, so the amp's offset and the thermal EMF leave the drift budget |
| three supplies to build | build one good one and reuse it: CL2 needs only 55 ppm and CL1 610 ppm, so the same design covers all three lenses |

# Parts (examples, not endorsements)

| Block | Spec that matters | Class |
|---|---|---|
| reference | $\le 0.5$ ppm/K | LM399 (ovenized; its ~250 mW heater must not sit next to the shunt), LTZ1000 for 0.05 ppm/K |
| DAC | 16-20 bit, external reference, gain TC $\le 0.5$ ppm/K | AD5689R, AD5541A |
| error amp | zero-drift, offset drift $\le 0.05$ µV/K | OPA189, ADA4522, ADA4528 |
| pass element | linear-mode rated, TO-247 with heatsink | IRFP150N / IRFP240, which idles at ~1.5 W on a matched 30 V rail — but 21 W if an 8 $\Omega$ lens is driven at 2 A off it, hence a tap or ballast |
| sense resistor | 4-terminal foil, $\le 0.2$ ppm/K, 5 W | Vishay Z-foil / Y-series current sense, 4-terminal |
| pre-regulator | low noise, high PSRR at 100 Hz | LT3045 class plus a bulk LC |
| ADC (optional servo) | 24 bit, ratiometric | ADS1262, LTC2508 |

# Recomputing

```bash
just supply-numbers              # the whole report
just supply-thermal              # the heated-pair / oven analysis
just supply-trade                # cheap parts vs island stability
just supply-parts                # the four component combinations
just supply-sums                 # correlated terms, noise, and how they are summed
just supply-verify               # the fluxgate + DMM6500 verification floor
just supply-markdown             # the budget table for this note
just sem-supply                  # build this note to PDF
```

or directly, with no dependencies beyond the standard library:

```bash
python python/sem_lens_supply_budget.py --thermal --markdown
python python/sem_lens_supply_budget.py --trade --markdown
python python/sem_lens_supply_budget.py --parts --markdown
python python/sem_lens_supply_budget.py --set r_sense=0.2 oven_gain=50
```

# Further reading

- [`sem-lens-current-stability.md`](sem-lens-current-stability.md) — where the 1 ppm comes from.
- Keithley, *Low Level Measurements Handbook* — nanovolt measurement, thermal EMF, reversal
  and ratio techniques.
- Vishay foil-resistor application notes — TCR, self-heating, and the Kelvin layout.
- Horowitz and Hill, *The Art of Electronics* — the current-source loop and its compensation.
