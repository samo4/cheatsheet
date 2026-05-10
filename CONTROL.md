---
title: "Classical Control Theory notes"
author: "Samo F."
date: "2025"
header-includes:
	- |
		\usepackage{tikz}
		\usetikzlibrary{arrows.meta,calc,positioning}
---

# Introduction

Control system is mechanism that alters the future state of a system. Control theory is a strategy to select the approriate inputs.

You could just try out all the values, but that's not a particulary efficient method.

Control theory is converting unstable open loop systems to stable closed loop systems, which are really just open loop systems again :). Common definition of control theory includes expected/target value of the output, but that's not really the case - control theory is modifying the behaviour of the system so that expected value is achievable under given constraints.

Inputs to the process of designing a control system are:

- objective
- criteria (goals)
- information about the system
- current state of the system
- constraints

# Systems and signals

Processes:

- continuous
- discrete
- batch

Energy of signal:

$$ E = \int_{t_1}^{t_2} |x(t)|^2\, dt $$

(Average) power of signal:

$$ P = \frac{1}{t_2 - t_1} \int_{t_1}^{t_2} |x(t)|^2\, dt $$

Shannon:

$$ f > 2f_m $$

Signals:

- constant
- linearly increasing
- step $1(t) = u(t)$
- exponential
- sinusoidal
- exponentially damped sinusoidal
- square impulse
- Dirac delta $\int_{-\infty}^{\infty} \delta(t)\, dt = 1$
- impulse train

# Modeling

All models are wrong, but some are useful; most commonly for prediction, control, optimization and training.

Best model should cover only the essential aspects of the system, depending on the objective of the modelling.

Models usually start from LTI (linear time invariant) descriptions and then are extended to include nonlinearities, time variance, stochasticity, etc. And event then we try to get back to LTI usually by linearization around the operating point (small signal response).

Conditions for LTI are:

- superposition
  - additivity $T(x_1 + x_2) = T(x_1) + T(x_2)$
  - homogeneity $T(ax) = aT(x)$
- time invariance

Model can be made from purely theoritical first principles, from data (system identification) or from a combination of the two.

.. see [AS notes](AS.md).. see book pp. 86 (Primer 3.1 Modeliranje avtomobilskega vzmetenja)

## Laplace transform

LTI systems can be described by linear differential equations, which can be solved either painfully or with Laplace transform.

$$ \mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st} f(t)\, dt $$

Each time you use Laplace transform, you'll be likely handed a table. But you should keep these simple rules in mind anyway:

- linearity
- addition
- nth derivative with 0 initial state: $\mathcal{L}\{f^{(n)}(t)\} = s^nF(s)$
- integral: $\mathcal{L}\{\int_0^t f(\tau)\, d\tau\} = \frac{1}{s}F(s)$ a.k.a $\mathcal{L}\{1(t)\} = \frac{1}{s}$
- final value theorem: $\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$
- initial value theorem: $\lim_{t \to 0^+} f(t) = \lim_{s \to \infty} sF(s)$



# Sources

https://www.youtube.com/playlist?list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk
