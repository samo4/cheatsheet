---
title: "Magnetics"
author: "Samo F."
date: "2025"
header-includes:
  - |
    \usepackage{tikz}
    \usepackage{mathtools}
    \usepackage{pgfplots}
    \usepgfplotslibrary{fillbetween}
    \pgfplotsset{compat=1.18}
    \usetikzlibrary{arrows.meta,calc,positioning}
    \tikzset{
      center-style/.style={
        rectangle,
        draw=black, very thick,
        text width=4cm,
        inner sep=10pt,
        minimum height=2em,
        text centered},
      bignode/.style={
        rectangle,
        rounded corners,
        draw=black, very thick,
        text width=5cm,
        inner sep=10pt,
        minimum height=2em,
        text centered},
      pil/.style={
        <->,
        thick,
        shorten <=2pt,
        shorten >=2pt}
    }
bibliography: magnetics.bib
csl: https://www.zotero.org/styles/ieee
# csl: https://www.zotero.org/styles/harvard-cite-them-right
link-citations: true
extensions:
  - +auto_identifiers
---

# Introduction

Hey, you fellow electric engineering student! Did you pass the basics of electrotechnics course and still the mere mention of magnetics makes you shiver? Don't worry, you're not alone. The little secret is that, depending on the area of specialization, even a seasoned engineer rarely encounter magnetics in their day-to-day work (making a living on a diet of Ohm's law). So I wrote this article to remind myself of the basics each time I forget them.

There are two ways to read this. Either follow my slightly idiosyncratic way of explaining, or just jump to the nice TLDR picture, curtuesy of [@erickson2001fundamentals].

Engineers love mental shortcuts and the first one that I'll make is to split the discussion into two phenomena: DC magnetics and AC magnetics. Ultimately both are covered by the same equations, but as an engineering mental model it's best to think of the two completely independent concepts.

At least the nicely follow one from another...

# DC magnetics

When a layman asks you how magnetism works, it might be tempting to answer that it's magic - even the first three letters match. But the truth is that magnetism is just a consequence of electricity and special relativity [@youtube2014special_relativity_magnets], [@purcell2013electricity] and especially Chapter 3 of [@schwartz1972principles]. While not exactly usefull to know as an engineer it's still nice to have the big picture.

As electrons move trough the wire, their "length" contracts due to relativistic effects, making them appear denser than the stationary protons in the wire, resulting in the wire appearing positively charged. This is what we call magnetism. "Hey!" you say: "electrons are moving trough the wire very slowly". Yes, they are; but since electric force is much, much, stronger than other forces, even a tiny relativistic effect creates the powerfull magnetic field.

One consequence really matters: current is one of the two[^1] sources of magnetism. It gives us the magnetic field intensity - the driving "force":

$$\oint \vec{H} \cdot d\vec{l} = I_{enclosed}$$

What the equation (Ampere's law) tells us is this: more current means more magnetic field intensity. If you want to push the same field around a longer magnetic path, you need more ampere-turns. From the equation you extract the unit for magnetic field intensity $\vec{H}$ as A/m. Field intensity is not a lump like total mass; it is already a quantity spread out along length. And one more useful observation: the equation does not contain the any material properties. Only the current and geometry set $\vec{H}$.

```{=latex}
\begin{figure}[htbp]
\centering
\input{figures/tikz/core-h-loop.tex}
\caption{A single turn drives current $i(t)$ around a magnetic core, while the magnetic field intensity $\\vec{H}$ finds the path of least reluctance in the core.}
\label{fig:core-h-loop}
\end{figure}
```

This is not yet the whole story. Ampere's law gives us the field intensity $\vec{H}$: it tells us how hard we are pushing magnetically around the path. But engineers usually care about what actually ends up inside the material. That is the magnetic flux density $\vec{B}$. The bridge between the two is the material itself:

$$\vec{B} = \mu\vec{H} = \mu_0\mu_r\vec{H}$$

And once you have $\vec{B}$, the total magnetic flux $\Phi$ is just that density spread over area:

$$\Phi = \int \vec{B} \cdot d\vec{A}$$

Now the causal chain is complete:

$$
i(t)
\;\longrightarrow\;
Ni
\;\longrightarrow\;
H = \frac{Ni}{l}
\;\longrightarrow\;
B = \mu H
\;\longrightarrow\;
\Phi = BA
$$

In the ideal DC world, the material is just a passive medium that doesn't consume any energy, it just transforms the field intensity into flux density. The magnetism is essentially a static field of relativistically compressed charges. It also follows that it is a conservative field (as it conserves energy).

# Real materials

As you might have already guessed, the equation above are (some of) the Maxwell's equations. They are only strictly valid in vacuum.

In the real world, the material is not just a passive medium. It has its own internal structure, and that structure can be changed by the magnetic field. The most common example of this is **ferromagnetic** materials, which have domains of aligned magnetic moments. When you apply a magnetic field, these domains can grow or shrink, and this process consumes energy (converts it to heat). This is why real materials exhibit hysteresis. And once all the domains are aligned, the material cannot produce more flux density, no matter how much you increase the field intensity - this is why we have a non-linear B-H curve:

```{=latex}
\begin{figure}[htbp]
\centering
\input{figures/tikz/b-h-loop.tex}
\caption{B-H curve with hysteresis}
\label{fig:b-h-loop}
\end{figure}
```

Atoms have their electrons clouds (= moving charge); when an external magnetic field is introduced, it changes the magnetic flux passing through the electron orbits. According to Lenz's Law, this change induces a tiny current loop in the atom that creates a magnetic field opposing the external one. This effect is called **diamagnetism** and it is present in all materials, although usually very weak. And in a very special case it's extremely strong: superconductors expel all magnetic flux from their interior, creating a perfect diamagnetic response.

The diamagnetism effect is purely reactive. Once the external field is removed, the electron orbits return to normal, and the induced magnetism vanishes instantly. Unlike other forms of magnetism, diamagnetic susceptibility is independent of temperature because it is a fundamental orbital response not affected by thermal randomization.

In some materials, the atomic structure allows for unpaired electrons that can align with an external magnetic field, creating a stronger magnetic response. This is called **paramagnetism** and it is actually the best fit for the idealised $\vec{B} = \mu_0 \mu_r \vec{H}$ relationship.

Maxwell’s equations describe how fields behave beautifully, but they treat materials as smooth, continuous constants. They don't explain why a material has a certain permeability ($\mu_r$).

Maxwell treats magnetism as moving charges (current loops). But most magnetism in solids comes from electron spin, a purely quantum property that has no classical analog.

# AC magnetics

So far the causal chain has been one-directional: current drives field intensity, field intensity drives flux density. But Maxwell's equations are symmetric. Faraday's law closes the loop in the other direction: a changing flux induces a voltage.

$$v(t) = -N\frac{d\Phi(t)}{dt}$$

The negative sign is Lenz's law: the induced voltage always opposes the change that caused it. Physically, if you try to increase the flux in a coil, the coil fights back with a voltage that would drive a current to reduce the flux. This is why inductors resist changes in current.

## Reluctance - the magnetic Ohm's law

To make the chain complete we need a way to link the H-side and the B-side. The tool for this is **magnetic reluctance**. Reluctance $\mathcal{R}_m$ plays the same role for magnetic circuits that resistance plays for electric ones:

$$\mathcal{R}_m = \frac{l}{\mu A} \quad [\mathrm{A/Vs}]$$

where $l$ is the length of the magnetic path, $A$ is its cross-sectional area, and $\mu = \mu_0\mu_r$ is the permeability of the material. With reluctance in hand, this is a direct analogue of Ohm's law:

$$NI = \Phi \cdot \mathcal{R}_m$$

Compare this to the Ampere-law expression $\mathcal{F} = NI$ and you get the magnetic circuit equation:

$$\Phi = \frac{NI}{\mathcal{R}_m}$$

One extremely useful consequence: if the core has a small air gap, the total reluctance is dominated by the gap. Air has $\mu_r = 1$, so even a tiny gap length $l_g$ contributes $\mathcal{R}_g = l_g/(\mu_0 A)$, which can easily be orders of magnitude larger than the reluctance of the surrounding ferrite.

## Inductance

Combining Faraday's law with the reluctance model gives the definition of inductance. Start with $\Phi = NI/\mathcal{R}_m$, multiply both sides by $N$, and define the **flux linkage** $\psi = N\Phi$:

$$\psi = \frac{N^2}{\mathcal{R}_m}\,I = LI$$

So inductance is:

$$L = \frac{N^2}{\mathcal{R}_m} = \frac{N^2 \mu A}{l}$$

And Faraday's law becomes the familiar inductor voltage equation:

$$v(t) = \frac{d\psi}{dt} = L\frac{di(t)}{dt}$$

For sinusoidal excitation $\Phi(t) = B_{max} A \sin(2\pi f t)$, integrating Faraday's law and taking the RMS value gives the **transformer equation**:

$$E_{rms} = \frac{2\pi}{\sqrt{2}} \cdot f \cdot N \cdot B_{max} \cdot A \approx 4.44 \cdot f \cdot N \cdot B_{max} \cdot A$$

This is the key core-design equation: given a supply voltage and frequency, it sets the minimum $N \cdot B_{max} \cdot A$ product before the core saturates.

The full causal chain is now visible in the TLDR figure: $i(t)$ drives $H$, which drives $B$ and $\Phi$ through the material, and any change in $\Phi$ is reported back as a terminal voltage $v(t)$. The inductance $L$ is the single number that summarises the whole magnetic geometry for a circuit designer.

## AC core losses

In DC magnetics the core was an ideal, lossless medium. AC operation breaks that assumption in two ways.

First, the hysteresis loss already described in the previous chapter now repeats every cycle. The power dissipated is proportional to the area of the B-H loop and to the switching frequency: $P_\text{hys} \propto f \cdot B_\text{peak}^\alpha$ (Steinmetz exponent $\alpha \approx 1.6\text{–}2$ for common ferrites).

Second, the changing flux induces **eddy currents** directly inside the conductive core material. By Faraday's law, any closed conducting loop inside the core sees a changing flux and therefore carries a circulating current that dissipates power as $I^2 R$. Eddy current loss scales as $f^2 B_\text{peak}^2$, which is why high-frequency magnetics use laminated steel or powdered/ferrite cores - both strategies break up the conducting loops to increase the effective resistance and throttle the eddy currents.

# Radiation

So far we have been thinking about magnetics as a way to store and transfer energy through a core - a closed, guided path. But a changing magnetic field does not have to stay inside a core. Faraday's law tells us that a time-varying magnetic field produces an electric field, and Maxwell's correction to Ampere's law tells us the reverse: a time-varying electric field produces a magnetic field. The two fields regenerate each other and, if the geometry permits it, they detach from the source and propagate through space as an electromagnetic wave.

# TLDR

```{=latex}
\begin{figure}[htbp]
\centering
\input{figures/tikz/tldr.tex}
\caption{Magnetics summary}
\label{fig:tldr}
\end{figure}
```

# Footnotes

[^1]: The other source is intrinsic spin of the electron. That's where the permanent magnets come from.

# References
