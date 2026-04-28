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

As electrons move trough the wire, their "length" contracts due to relativistic effects, making them appear denser than the stationary protons in the wire, resulting in the wire appearing positively charged. This is what we call magnetism. "Hey!" you say: "electrons are moving trough the wire very slowly". Yes, they are; but since electric force is much, much, stronger than other forces, even a tiny relativistic effect creates the powerfull magnetic field.

One consequence really matters: current is one of the two[^1] sources of magnetism. It gives us the magnetic field intensity - the driving "force":

$$\oint \vec{H} \cdot d\vec{l} = I_{enclosed}$$

What the equation (Ampere's law) tells us is this: more current means more magnetic field intensity. If you want to push the same field around a longer magnetic path, you need more ampere-turns. From the equation you extract the unit for magnetic field intensity $\vec{H}$ as A/m. Field intensity is not a lump like total mass; it is already a quantity spread out along length. And one more useful observation: the equation does not contain the any material properties. Only the current and geometry set $\vec{H}$.

```{=latex}
\begin{figure}[htbp]
\centering
\begin{tikzpicture}
	% Front face of the core
	\coordinate (A) at (0,0);
	\coordinate (B) at (4.8,0);
	\coordinate (C) at (4.8,4.2);
	\coordinate (D) at (0,4.2);

	% Inner window
	\coordinate (E) at (1.3,1.1);
	\coordinate (F) at (3.5,1.1);
	\coordinate (G) at (3.5,3.1);
	\coordinate (H) at (1.3,3.1);

	% Core body
	\filldraw[fill=gray!18, draw=black, thick] (A) -- (B) -- (C) -- (D) -- cycle;
	\filldraw[fill=white, draw=black, thick] (E) -- (F) -- (G) -- (H) -- cycle;
	\filldraw[fill=gray!10, draw=black, thick] (D) -- (C) -- cycle;
	\filldraw[fill=gray!12, draw=black, thick] (B) -- (C) -- cycle;
	\filldraw[fill=gray!6, draw=black, thick] (H) -- (G) -- cycle;
	\filldraw[fill=gray!8, draw=black, thick] (F) -- (G) -- cycle;

  % H loop
	\draw[very thick, red!75!black, -{Latex[length=3mm]}, rounded corners=8pt]
		(0.7,0.7) -- (4.1,0.7) -- (4.1,3.45) -- (0.7,3.45) -- cycle;
	\node[red!75!black, fill=white, inner sep=1pt] at (2.45,3.75) {$\oint \vec{H}\cdot d\vec{l}$};
	\draw[thick, -{Latex[length=3mm]}, red!75!black] (4.1,1.95) -- (4.1,2.95);

	% I loop
	\draw[very thick, rounded corners=4pt, blue!65!black]
		(-1.0,2.4) -- (0,2.4);
	\draw[very thick, rounded corners=4pt, blue!65!black]
		(1.3,2.4) -- (2.2,2.4) -- (2.2,1.8) -- (-1.0,1.8);
	\draw[thick, -{Latex[length=3mm]}, blue!65!black] (-0.95,2.4) -- (-0.15,2.4);
	\node[above, blue!65!black] at (-0.55,2.4) {$i(t)$};

\end{tikzpicture}
\caption{A single turn drives current $i(t)$ around a magnetic core, while the magnetic field intensity $\vec{H}$ finds the path of least reluctance in the core.}
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
\begin{tikzpicture}
	\begin{axis}[very thick,
		domain=-7:7,
		samples=200,
		xlabel={$H$},
		ylabel={$B$},
		xmin=-7,xmax=7,ymin=-4,ymax=4,
		axis x line=middle,axis y line=middle,
		ticks=none]
		\addplot[red, name path=A] {5/(1 + exp(-1.7*x+1.5))-2.5};
		\addplot[red, name path=B] {5/(1 + exp(-1.7*x-1.5))-2.5};
	\end{axis}
\end{tikzpicture}
\caption{B-H curve with hysteresis}
\label{fig:b-h-loop}
\end{figure}
```

Materials also exhibit other quantum effects such as Larmor precession (used in NMR), diamagnetism, and paramagnetism.

# AC magnetics

So far the causal chain has been one-directional: current drives field intensity, field intensity drives flux density. But Maxwell's equations are symmetric. Faraday's law closes the loop in the other direction: a changing flux induces a voltage.

$$v(t) = -N\frac{d\Phi(t)}{dt}$$

The negative sign is Lenz's law: the induced voltage always opposes the change that caused it. Physically, if you try to increase the flux in a coil, the coil fights back with a voltage that would drive a current to reduce the flux. This is why inductors resist changes in current — not because of any resistance, but because of this electromagnetic feedback.

Notice: in DC magnetics the flux was static so $d\Phi/dt = 0$ and no voltage appeared. AC magnetics is exactly the regime where flux changes, and only then does Faraday's law have anything to say.

## Reluctance — the magnetic Ohm's law

To make the chain complete we need a way to link the H-side and the B-side. The tool for this is **magnetic reluctance**. Reluctance $\mathcal{R}_m$ plays the same role for magnetic circuits that resistance plays for electric ones:

$$\mathcal{R}_m = \frac{l}{\mu A} \quad [\mathrm{A/Vs}]$$

where $l$ is the length of the magnetic path, $A$ is its cross-sectional area, and $\mu = \mu_0\mu_r$ is the permeability of the material. With reluctance in hand, the magneto-motive force (MMF) obeys a direct analogue of Ohm's law:

$$\mathcal{F} = \Phi \cdot \mathcal{R}_m$$

Compare this to the Ampere-law expression $\mathcal{F} = NI$ and you get the magnetic circuit equation:

$$\Phi = \frac{NI}{\mathcal{R}_m}$$

One extremely useful consequence: if the core has a small air gap, the total reluctance is dominated by the gap. Air has $\mu_r = 1$, so even a tiny gap length $l_g$ contributes $\mathcal{R}_g = l_g/(\mu_0 A)$, which can easily be orders of magnitude larger than the reluctance of the surrounding ferrite.

## Inductance

Combining Faraday's law with the reluctance model gives the definition of inductance. Start with $\Phi = NI/\mathcal{R}_m$, multiply both sides by $N$, and define the **flux linkage** $\lambda = N\Phi$:

$$\lambda = \frac{N^2}{\mathcal{R}_m}\,I = LI$$

So inductance is:

$$L = \frac{N^2}{\mathcal{R}_m} = \frac{N^2 \mu A}{l}$$

And Faraday's law becomes the familiar inductor voltage equation:

$$v(t) = \frac{d\lambda}{dt} = L\frac{di(t)}{dt}$$

The full causal chain is now visible in the TLDR figure: $i(t)$ drives $H$, which drives $B$ and $\Phi$ through the material, and any change in $\Phi$ is reported back as a terminal voltage $v(t)$. The inductance $L$ is the single number that summarises the whole magnetic geometry for a circuit designer.

## AC core losses

In DC magnetics the core was an ideal, lossless medium. AC operation breaks that assumption in two ways.

First, the hysteresis loss already described in the previous chapter now repeats every cycle. The power dissipated is proportional to the area of the B-H loop and to the switching frequency: $P_\text{hys} \propto f \cdot B_\text{peak}^\alpha$ (Steinmetz exponent $\alpha \approx 1.6\text{–}2$ for common ferrites).

Second, the changing flux induces **eddy currents** directly inside the conductive core material. By Faraday's law, any closed conducting loop inside the core sees a changing flux and therefore carries a circulating current that dissipates power as $I^2 R$. Eddy current loss scales as $f^2 B_\text{peak}^2$, which is why high-frequency magnetics use laminated steel or powdered/ferrite cores — both strategies break up the conducting loops to increase the effective resistance and throttle the eddy currents.

# Radiation

So far we have been thinking about magnetics as a way to store and transfer energy through a core — a closed, guided path. But a changing magnetic field does not have to stay inside a core. Faraday's law tells us that a time-varying magnetic field produces an electric field, and Maxwell's correction to Ampere's law tells us the reverse: a time-varying electric field produces a magnetic field. The two fields regenerate each other and, if the geometry permits it, they detach from the source and propagate through space as an electromagnetic wave.

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

# Footnotes

[^1]: The other source is intrinsic spin of the electron. That's where the permanent magnets come from.

# References
