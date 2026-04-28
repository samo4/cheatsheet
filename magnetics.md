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

When a layman asks you how magnetism works, it might be tempting to answer that it's magic - even the first three letters match. But the truth is that magnetism is just a consequence of electricity and special relativity [@youtube2014special_relativity_magnets], [@purcell2013electricity], [@schwartz1972principles]. While not exactly usefull to know as an engineer it's still nice to have the big picture.

As electrons move trough the wire, their "length" contracts due to relativistic effects, making them appear denser than the stationary protons in the wire, resulting in the wire appearing positively charged. This is what we call magnetism. "Hey!" you say: "electrons are moving trough the wire very slowly". Yes, they are; but since electric force is much, much, stronger than other forces, so even a tiny relativistic effect creates the powerfull magnetic field.

For an ordinary engineer, one consequence really matters: the current is the ultimate and the only source of all magnetism — there is no other (Both AC perspective nor the quantum perspective mentioned below don't change that!). It gives us the magnetic field intensity - the driving "force":

$$\oint \vec{H} \cdot d\vec{l} = I_{enclosed}$$

What the equation (Ampere's law) tells us is this: more current means more magnetic field intensity. If you want to push the same field around a longer magnetic path, you need more ampere-turns. From the equation you extract the unit for magnetic field intensity $\vec{H}$ as A/m. Field intensity is not a lump like total mass; it is already a quantity spread out along length. And one more useful observation: the equation does not contain the any material properties. Only the current and geometry set $\vec{H}$.

**fig:core-h-loop**

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

**fig:b-h-loop**

Materials also exhibit other quantum non-idealities such as Larmor precession (used in NMR).

# AC magnetics

# Radiation

So far we have been thinking about magnetics as a way to store and transfer energy through a core — a closed, guided path. But a changing magnetic field does not have to stay inside a core. Faraday's law tells us that a time-varying magnetic field produces an electric field, and Maxwell's correction to Ampere's law tells us the reverse: a time-varying electric field produces a magnetic field. The two fields regenerate each other and, if the geometry permits it, they detach from the source and propagate through space as an **electromagnetic wave**.

The condition for this to happen efficiently is that the physical size of the structure is comparable to the wavelength $\lambda = c/f$. At power-electronics frequencies (kHz range) $\lambda$ is measured in kilometres, so radiation from a transformer core is negligible. At RF and microwave frequencies the same changing currents that a magnetics engineer would call "leakage" become intentional antennas.

The energy radiated per cycle is, like hysteresis loss, non-recoverable — it leaves the circuit entirely. The power radiated by a small current loop of area $A$ carrying current $I$ at frequency $f$ is:

$$P_{rad} = \frac{\pi}{3} \eta_0 \left(\frac{2\pi f}{c}\right)^4 (IA)^2$$

where $\eta_0 = 377\,\Omega$ is the impedance of free space. The $f^4$ dependence is the key engineering takeaway: radiation becomes a serious loss mechanism only at high frequencies. Below that threshold, good shielding and closed-core geometry keep it entirely out of the picture.

# TLDR

```{=latex}
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[node distance=2cm, auto]
  \node[bignode] (current) {$i(t)$};

  \node[right=of current] (ampere) {};

  \node[center-style, above=of ampere] (permeability) {
    $\mu_0 = 4\pi \times 10^{-7}\ [\mathrm{Vs/Am}]$
  };

  \node[bignode, right=of ampere] (mmf) {
    $H(t)\ [\mathrm{A/m}]$\\[4pt]
    $\mathcal{F} = \sum Hl = IN\ [\mathrm{A}]$
  }
  edge[pil] node[above] {Ampere's law} (current.east);

  \node[above=of permeability] (faraday) {};

  \node[bignode, left=of faraday] (voltage) {
    $v(t) = -N\dfrac{d\Phi(t)}{dt}$
  };

  \node[bignode, right=of faraday] (flux) {
    $B(t)\ [\mathrm{Vs/m^2}]$\\[4pt]
    $\Phi(t) = A \cdot B(t)\ [\mathrm{Vs}]$
  }
  edge[pil] node[above] {Faraday's law} (voltage.east)
  edge[pil] node[right, text width=2cm] {
    $B=f(H)$\\
    $\mathcal{F}=\Phi \cdot R_m$\\
    $\Phi=\frac{IN}{R_\mathrm{air}}$
  } (mmf.north);

\end{tikzpicture}
\caption{Magnetics summary}
\label{fig:tldr}
\end{figure}
```

# References
