---
title: "Magnetics"
author: "Samo F."
date: "2025"
header-includes:
	- |
		\usepackage{tikz}
		\usetikzlibrary{arrows.meta,calc,positioning}
---

# Magnetics

Hey, you fellow electric engineering student! Did you pass the basics of electrotechnics course and still the mere mention of magnetics makes you shiver? Don't worry, you're not alone. The trick is that, depending on the area of specialization, even a seasoned engineer might rarely encounter magnetics in their day-to-day work (making a living on a diet of Ohm's law). I wrote this article to remind myself of the basics each time I forget them.

There are two ways to read this. Either follow my slightly idiosyncratic way of explaining, or just jump to the nice TLDR picture, curtuesy of [E. Maksimovič].

Imagine a spaceship traveling close to the speed of light. (Yes, yes, I assume that you also passed the physics course.) From the perspective of an observer on Earth, the spaceship contracts in the direction of motion due to relativistic effects. That same special-relativity machinery does not switch off just because the electrons in a wire move at a pedestrian speed. In fact, one useful way to think about magnetism is that electric and magnetic fields are two faces of the same relativistic story. Depending on the reference frame, what looks mostly electric in one frame picks up a magnetic component in another.

So my take is: magnetics is what electricity looks like when relativity shows up to the party.

For ordinary electrotechnics, only one consequence matters: currents create magnetic field intensity:

$$\oint \vec{H} \cdot d\vec{l} = I_{enclosed}$$

What the equation (Ampere's law) tells us is this: more current means more magnetic field intensity. If you want to push the same field around a longer magnetic path, you need more ampere-turns. Since you're already adept at extracting units from equations, you also plainly see that the unit of magnetic field intensity $\vec{H}$ is A/m. Field intensity is not a lump like total mass; it is already a quantity spread out along length. And one more useful observation: the equation does not contain the any material properties. Only the current and geometry set $\vec{H}$.

What the current gives us directly is not yet the whole story. Ampere's law gives us the field intensity $\vec{H}$: it tells us how hard we are pushing magnetically around the path. But engineers usually care about what actually ends up inside the material. That is the magnetic flux density $\vec{B}$. The bridge between the two is the material itself:

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
