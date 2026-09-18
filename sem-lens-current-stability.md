---
title: "SEM lens current stability"
subtitle: "How stable do the lens supplies actually have to be?"
author: "Samo F."
date: "2025"
---

# TLDR

- One number decides everything: the **focus budget**, i.e. how much of the depth of focus
  you let a defocus eat.
- For a 15 kV / 10 nm probe / $\alpha = 10$ mrad working point, the **objective lens**
  (the third and last lens in the column) needs
  $\Delta I/I \lesssim 2.5\times10^{-5}$ — **25 ppm**. Quote **1–2 ppm**.
- Each lens further up the column is about an order of magnitude looser:
  CL2 $\approx 2\times10^{-2}\,\%$, CL1 $\approx 2\times10^{-1}\,\%$.
- All of it presumes a **current** source. On a voltage-driven coil copper alone drifts
  ~4000 ppm/K, which is 160x over the objective budget.
- **Magnification is not in the formula.** Pushing to 30 kV / 200 000x leaves the objective
  requirement about where it is (25 → 17 ppm), because the short working distance that buys
  the 1 nm probe shrinks $C_c$ by almost the same factor. The condensers do get ~3.4x
  tighter, so they stop being an afterthought.

# The column

"Three-lens SEM" means three lenses below the gun:

| Lens | Job | What its instability spoils |
|---|---|---|
| CL1 | first demagnification of the gun crossover | probe **current** (illumination) |
| CL2 | sets the crossover that the objective images | crossover **position** → focus |
| objective (3rd) | images that crossover onto the specimen — the probe-forming lens | **focus**, probe size |

The objective is last, so its own error is not demagnified by anything: it dominates the
column, and the two condenser lenses only matter through the crossover they hand down.

# Model

A magnetic lens with $N$ ampere-turns produces an axial field $B_z \propto NI$; well below
pole-piece saturation the lens power integral obeys

$$\frac{1}{f} \;\propto\; \int B_z^2\,dz \;\propto\; I^2
\qquad\Longrightarrow\qquad \frac{\Delta f}{f} = -\,2\,\frac{\Delta I}{I}.$$

Call $\varepsilon \equiv \Delta I/I$. The factor 2 is the whole story: a 1 ppm current error
is a 2 ppm focal-length error.

# Criterion: spend the depth of focus

A defocus $\Delta z$ spreads a cone of semi-angle $\alpha$ into a blur disc of diameter
$2\alpha\,\Delta z$, so the usable depth of focus for a probe of diameter $d$ is

$$\mathrm{DOF} = \frac{d}{\alpha}, \qquad
  \Delta z_{\max} = \texttt{budget}\cdot\frac{d}{\alpha}
  \quad(\texttt{budget} = 0.5 \text{ by default}).$$

Equivalently, in the chromatic-aberration language the same error is
$\Delta z = 2C_c\,\varepsilon$ — which is where the $4\alpha C_c$ in the master formula below
comes from.

## Objective (the 3rd lens)

$$\varepsilon_{\mathrm{obj}} = \frac{\Delta z_{\max}}{2C_c}
  = \frac{\texttt{budget}\cdot d}{4\,\alpha\,C_c}$$

Cross-check by the focal-length route, $\Delta z = 2(1+M_o)^2 f\,\varepsilon$: with the
defaults it lands at $0.87\times$ the value above, so the two routes agree to 13 %.

## CL2

Its crossover moves by $\Delta v = 2(1+m)^2 f_c\,\varepsilon$, and that displacement reaches
the specimen demagnified by $M_o^2$:

$$\varepsilon_{\mathrm{CL2}} = \frac{\Delta z_{\max}}{2\,M_o^2\,(1+m)^2 f_c}$$

The identical shift from CL1 travels through CL2 *and* the objective, so it picks up
$M_o^2 m^2$ instead — which is why CL1 is looser again.

## CL1

Two criteria, take the tighter:

- **crossover shift** (as above, propagated through CL2 and the objective), and
- **probe-current constancy**: $\Delta I_p/I_p = 4\varepsilon$ for $m \ll 1$, so a 1 % current
  budget means $\varepsilon \le 2500$ ppm.

# Defaults

Chosen to be boring rather than clever; every one is editable in the script.

| Parameter | Value | Note |
|---|---|---|
| $V_0$ | 15 kV | typical imaging condition |
| $\lambda$ | 10.0 pm | $1.226/\sqrt{V_0}$ nm |
| Working distance | 10 mm | standard |
| Probe $d$ | 10 nm | this is the resolution knob that matters |
| $\alpha$ | 10 mrad | ~30 µm final aperture at WD 10 mm |
| $C_c$ | 10 mm | $\approx 1.2 f$, $f_{\mathrm{obj}} = 8$ mm |
| Crossover distance $u_o$ | 50 mm | $M_o = \mathrm{WD}/u_o = 0.2$ |
| Condenser $f_c$, $m$ | 20 mm, 0.3 | CL1 and CL2 |
| Focus budget | 0.5 | half the DOF, $\Delta z_{\max} = 500$ nm |
| Design margin | 10x | applied before quoting a spec |

# Results

| Lens | Requirement | Governing criterion | Spec to quote |
|---|---|---|---|
| **Objective (3rd lens)** | 25 ppm | focus shift $\Delta z = 2C_c\,\Delta I/I$ | 2 ppm (12x margin) |
| CL2 | 185 ppm | crossover shift, demagnified by $M_o^2$ | 10 ppm |
| CL1 | 2055 ppm | crossover shift | 200 ppm |

Both condensers sit far inside a supply that is good enough for the objective, so in
practice you buy one quality class of lens supply and the objective is what pays for it.
A 1 ppm/h objective supply — the customary figure for a thermostatted column — clears the
25 ppm requirement with room to spare.

The ladder also tells you which criterion to argue about: for CL2 and CL1 the crossover
shift binds (the probe-current criterion would have allowed 2500 ppm at CL1), so if you
want looser condensers, shorten the column below CL1 rather than buying better electronics.

# Where the numbers move

$\varepsilon_{\mathrm{obj}} \propto d/(\alpha C_c)$ — required stability in ppm:

| probe $d$ / $\alpha$ | 5 mrad | 10 mrad | 20 mrad |
|---|---|---|---|
| 2 nm | 10 | 5 | 2.5 |
| 5 nm | 25 | 12.5 | 6.2 |
| 10 nm | 50 | 25 | 12.5 |
| 20 nm | 100 | 50 | 25 |

Pushing to a smaller probe tightens $\alpha$ and $d$ together — but only as long as the
working distance stays put, and it does not: a short WD drags $C_c$ down with it. So the
design band stays at 10–25 ppm from 10 nm down to 1 nm, which is why "objective lens current
stable to ~1 ppm" is the number every electron-optics text ends up quoting.

# Pushing the magnification: 30 kV, 200 000x

**Magnification is not in the formula.** $\varepsilon_{\mathrm{obj}} =
\texttt{budget}\cdot d/(4\alpha C_c)$ contains no $M$ at all. Raising the magnification only
decides which working point is forced on you, and three levers move:

- **Probe.** 200 000x against the usual 100 mm reference width rasters a 0.5 µm field; on a
  1024 x 1024 frame the pixel is 0.49 nm, so a 1 nm probe is already oversampled. The budget
  follows the **probe** (1 nm), not the pixel — the requirement is set by what the column can
  focus, not by the number on the magnification dial.
- **Angle.** At 30 kV ($\lambda = 7.1$ pm) with $C_s \approx 2$ mm the optimum is
  $\alpha = 6.2$ mrad, which balances $C_s$ against diffraction at $d \approx 0.94$ nm. Hence
  6 mrad rather than 10.
- **The chromatic lever — the one that rescues you.** The short working distance is what buys
  the 1 nm probe, and it drags *both* $C_c$ and $f$ down with it: 2.5 mm at WD 4 mm instead
  of 10 mm at 10 mm.

| Quantity | default | 30 kV, 200 000x |
|---|---|---|
| $V_0$ | 15 kV | 30 kV |
| working distance | 10 mm | 4 mm |
| probe $d$ | 10.0 nm | 1.0 nm |
| $\alpha$ | 10 mrad | 6 mrad |
| $C_c$ | 10.0 mm | 2.5 mm |
| $(1+M)^2 f$ | 11.52 mm | 4.63 mm |
| depth of focus | 1000 nm | 167 nm |
| focus budget | 500 nm | 83 nm |
| **objective, $C_c$ route** | **25 ppm** | **17 ppm** |
| objective, focal-length route | 22 ppm | 9 ppm |
| CL2 | 185 ppm | 55 ppm |
| CL1 | 2055 ppm | 610 ppm |
| high tension ($\Delta V/V$) | 50 ppm = 750 mV | 33 ppm = 1000 mV |
| spec: objective / CL2 / CL1 | 2 / 10 / 200 ppm | 1 / 5 / 50 ppm |

What the table says:

- The focus budget falls 6x (500 → 83 nm), but the objective's sensitivity to current falls
  4x with it ($2C_c$: 20 → 5 mm), so the **objective requirement barely moves**. High
  resolution is not bought with a better lens supply; it is bought with a shorter lens.
- The condensers get no such compensation. The demagnification that protects them is a
  property of the column length, not of the working distance, so CL2 and CL1 tighten by
  about 3.4x. At 200 000x the condenser supplies stop being an afterthought.
- The two models disagree by 46 % here (17 vs 9 ppm) instead of 13 %, because $C_c$ is no
  longer close to $(1+M)^2 f$ (ratio 1.85). Design to the conservative end and the practical
  answer is unchanged: **a 1 ppm objective supply**, the same class as at 15 kV.

To make the lever explicit, keep the old column ($C_c = 10$ mm) and ask for the same 1 nm
probe: the objective requirement collapses to **4.2 ppm**, six times tighter than at 10 nm.
The requirement is a statement about how *short* the objective is, not about how large $M$ is:

$$\varepsilon_{\mathrm{obj}} \propto \frac{d}{\alpha C_c}, \qquad
  C_c \approx (1+M)\,\mathrm{WD} \ \ (\text{thin lens})
  \qquad\Longrightarrow\qquad
  \varepsilon_{\mathrm{obj}} \propto \frac{d}{\alpha\,(1+M)\,\mathrm{WD}}.$$

Two side notes at this working point:

- **The high tension is the looser half.** Since
  $\Delta z = C_c\,(\Delta V/V + 2\,\Delta I/I)$, the relative voltage requirement is twice
  the current requirement: 33 ppm at 30 kV is 1.0 V. A 1 V-class HT supply is the easy part;
  the lens current is the hard part.
- **Ignore the "image breathes" worry.** The scan coils sit above the objective, so the lens
  does scale the scanned field — but a 17 ppm current change moves features by
  $2\times10^{-6}\times 0.5\ \text{µm} \approx 1$ pm at the field edge, invisible next to a
  1 nm probe.

# What it means for the supply

- **Current source, not voltage source.** Copper has $\alpha_R \approx 3930$ ppm/K, so a
  constant-voltage drive drifts ~4000 ppm/K — two decades past the objective budget. The
  regulation loop is not a refinement here, it is the mechanism.
- **The sense element is the weak link.** Holding the objective means holding the current
  reference to well under 10 ppm, so the shunt has to be ~1 ppm/K (bulk-metal-foil, kept off
  the hot end of the column), otherwise the reference drifts more than the physics allows.
- **Split drift from ripple**, and add them in quadrature: a 2 ppm spec could be
  1 ppm/h of drift plus 1 ppm of scan-locked ripple. Drift sets the refocus interval
  (25 ppm of a 10 mm focal length is ~0.5 µm of focus walk, i.e. half the DOF), ripple is
  what you see as jitter in the image.
- **The lens is in the loop too.** Pole-piece gap expansion and permeability drift with
  temperature change the effective lens strength without any current change, so the real
  budget is a lens-*strength* budget; thermostatting and water cooling are part of the
  stability, not just good manners.

# Recomputing

The numbers above are produced, not pasted from memory:

```bash
just sem-numbers                 # full report, `default` working point
just sem-compare                 # both working points, side by side
just sem-markdown                # the table rows for this note
just sem                         # build this note to PDF
```

or directly, with no dependencies beyond the standard library:

```bash
python python/sem_lens_current_stability.py --preset highmag
python python/sem_lens_current_stability.py --compare --markdown
python python/sem_lens_current_stability.py --set d=5e-9 alpha=5e-3
```

# Further reading

- L. Reimer, *Scanning Electron Microscopy* — probe size, depth of focus, and the
  stability requirements of the column.
- J. Goldstein et al., *Scanning Electron Microscopy and X-Ray Microanalysis* — the same
  budget in terms of working distance and aperture choice.
- P. W. Hawkes and E. Kasper, *Principles of Electron Optics*, vol. 1 — the
  $1/f \propto I^2$ scaling and lens-current stability treated properly.
