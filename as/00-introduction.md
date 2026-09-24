# Introduction

The mental model behind these notes follows the chain **modeling → analysis → control**, but notes stops at just hinting the last part. Modeling (the next chapter) turns a physical system into equations, analysis squeezes behaviour out of those equations, and control runs the other way, from desired behaviour to a system that delivers it. All of it rests on one class of systems, the linear time-invariant (LTI) ones.

## Common vocabulary

This is material you have met before; it is here only as a reminder and to fix the notation.

- System — a box that turns inputs into outputs. Where the box ends is the modeler's choice.
- Element — the smallest part we do not split further. An ideal element is *lumped* and dimensionless: one relation between the quantities at its terminals.
- Signal — a variable carrying information. The input $u(t)$ and the output $y(t)$ are what crosses the border; the state $\vec{x}(t)$ is the internal signal that remembers the past. A water tank: inflow rate, outflow rate, and level.
- Test signals — the unit step $1(t)$ (Heaviside), equal to $1$ for $t \ge 0$ and $0$ before, switches an input on. The unit impulse $\delta(t)$ (Dirac) is zero everywhere except at $t = 0$ and has unit area, $\int \delta(t)\,dt = 1$. It picks out a value, $\int f(t)\,\delta(t - \tau)\,dt = f(\tau)$ (the sifting property), and it is the derivative of the step.
- Direction of travel — *analysis* goes from system to behaviour; *synthesis* goes from desired behaviour to a system. Neither works without a model, and you cannot design what you cannot analyze.

## Classification of systems

Only a few distinctions actually change the mathematics, so these are the ones we keep:

- *Static* — memoryless, the output depending only on the present input, $y = f(u)$, versus *dynamic* with memory, where the past lingers and forces a differential equation and a state.
- *Lumped*: finitely many state variables obeying an ODE, so the model is finite-dimensional. *Distributed*: the state is a field $w(t, \vec{r})$, a function of space as well as time, obeying a PDE, so there are infinitely many states. Limit between the two: connections $d < \frac{\lambda}{20}$
- *Continuous-time*: signals are defined at every instant. *Discrete-time*: only at samples $kT$.
- *Deterministic*: the same initial state and input always produce the same trajectory. *Stochastic*: randomness enters, and only statistics are predictable.
- *Homogeneous*: no input; the system runs on its initial state alone. *Non-homogeneous*: an input drives it.

To get our mathematical tools, we need two properties: *linear*, *time-invariant*.

### Is it linear?

A system is linear when it obeys **superposition**: adding inputs adds their responses, and scaling an input scales its response. That is the linear-map condition you already know — for any $u_1, u_2$ and any constants $a, b$,

$$L(a u_1 + b u_2) = a\,L(u_1) + b\,L(u_2).$$

The two halves have names — additivity, $L(u_1 + u_2) = L(u_1) + L(u_2)$, and homogeneity, $L(a u) = a\,L(u)$ — and both must hold.

Linearity is one and the same property whether $L$ acts on scalars, vectors, or signals — only the space it acts on changes.

For a linear system the test is algebraic: every term must be proportional to one signal. Products ($y u$, $y_1 y_2$), powers ($y^2$, $u^2$), and nonlinear functions ($e^y$, $\sin u$, $\sqrt{y}$) break it. A term that involves neither the output nor the input — a prescribed forcing such as $4t$ — is not a nonlinearity, though it can destroy time invariance. A constant term is harmless only when it is an input; as a fixed offset it breaks linearity, as the example below shows.

```{=latex}
\begin{example}[frametitle={Example - testing linearity}]
```

Test the system $y = \alpha u + \beta$: a gain with a constant offset.

Homogeneity demands $L(au) = a\,L(u)$ for every $a$, and $a = 0$ alone forces $L(0) = 0$. Here $u = 0$ gives $y = \beta$, so any nonzero offset breaks linearity by itself — the map is affine, not linear. Additivity fails with it: two separate inputs give $\alpha(u_1 + u_2) + 2\beta$, while the input $u_1 + u_2$ gives only $\alpha(u_1 + u_2) + \beta$.

The same additive term is harmless in $\dot{y} = 5y + 4t$, because there it is the input rather than a fixed part of the system.

```{=latex}
\end{example}
```

### Is it time invariant?

A system is time-invariant if delaying the input by $\tau$ delays the output by exactly $\tau$:

$$
\text{if } u(t) \mapsto y(t), \qquad \text{then } u(t - \tau) \mapsto y(t - \tau) \quad \text{for every } \tau.
$$

For an ODE the rule is to look for an explicit $t$: a coefficient or forcing written in $t$ makes the system time-varying, constant coefficients make it time-invariant.

```{=latex}
\begin{example}[frametitle={Example - testing time invariance}]
```

**$\dot{y} = 5y + 4t$ — time-varying.** The coefficient $5$ is constant, but the forcing $4t$ depends explicitly on $t$: at $t = 0$ it drives with $0$, at $t = 10$ with $40$. A shift in time changes the equation, not merely the response.

**$\dot{y} = 5y + u$ — time-invariant.** The same dynamics with the clock removed. Feed the ramp in as the input, $u(t) = 4t$: then $u(t - \tau) = 4(t - \tau)$ gives exactly the delayed response. Either way $\dot{y} = 5y + 4t$ is *linear*; it is time-invariant only if the $4t$ is the input rather than part of the model. The two properties are independent and must be checked separately.

```{=latex}
\end{example}
```

## The LTI class of dynamic systems

One combination of mathematical classification (or properties) does nearly all the work in practice: *linear*, *time-invariant*, *lumped*, *continuous-time*, *deterministic*.

These are the linear time-invariant (LTI) systems.

For them the mathematical toolbox is unusually complete: superposition, the eigenvalues and modes of the system, Laplace transforms, transfer functions, convolution, and with them stability, controllability, and observability. Each of those tools rests on linearity and time invariance and will be discussed in the following chapters.

The justification is not that the world is LTI, but that a system can often be made LTI where and when we need it. Linearize around an equilibrium or along a trajectory and the deviations obey an LTI model (Linearization chapter); sample a continuous system and get a discrete-time one (Discrete chapter). Between them, a great many nonlinear, time-varying, and sampled systems become reachable.

Linearization does not help with the other two assumptions: the model must be lumped (finitely many states, an ODE — no partial differential equations, no delays) and deterministic (no noise). And even where linearization does apply, it erases phenomena no linear model can recover: multiple equilibria, hysteresis, saturation, chaos.

Two kinds of systems fall outside.

## What LTI leaves out

### Distributed systems

A drum is one of the two classical archetypes of a *distributed* system (the other being the telegrapher's equation). Its skin is a membrane: every point can move, so it has infinitely many states — not a finite vector $\vec{x}$ but a field $w(t, r, \theta)$, the displacement of each point. The governing equation is the two-dimensional wave equation, a partial differential equation in space and time,

$$
\frac{\partial^2 w}{\partial t^2} = c^2\left(\frac{\partial^2 w}{\partial r^2} + \frac{1}{r}\frac{\partial w}{\partial r} + \frac{1}{r^2}\frac{\partial^2 w}{\partial \theta^2}\right),
$$

whose modes are Bessel-function shapes. Hitting the drum excites all of those modes at once, and no finite system of ODEs reproduces what you hear. A lumped model could keep only a few of them. A plucked guitar string has the same problem in one dimension, though its harmonics fall on integers. Neither can be analyzed by the LTI toolbox.

### Stochastic systems

When you add randomness, the same initial state and input no longer give the same response, and only statistics are (hopefully) predictable. How much of our powerful toolbox survives depends on where the randomness enters. In the first example only the *input* is random and the dynamics are perfectly LTI, so the model still describes the average behaviour. In the second the state itself jumps at random times: there is no deterministic skeleton left to linearize, and LTI-based analysis has no entry point at all.

```{=latex}
\begin{example}[frametitle={Example - thermal noise in an RC circuit}]
```

Thermal agitation of the electrons in a resistor puts a random voltage across it — Johnson–Nyquist noise — with zero mean and a flat spectrum $S_v = 4 k_B T R$. The RC low-pass filter is the textbook LTI system — one capacitor, one state — yet its output cannot be predicted, only described statistically.

The dynamics are perfectly LTI, but the *input* is not. Two identical experiments give different traces, though nothing about the circuit changed. The toolbox predicts trajectories; here only the statistics are predictable.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - a packet queue}]
```

Packets arrive at a router buffer at random instants and are served one at a time at mean rate $\mu$; the state is the number of packets in the system, an integer. There is no differential equation to write — the count sits still, then jumps by one at a random time — and the questions worth asking are already probabilistic: the mean delay, or the probability that the buffer overflows and a packet is lost.

There is nothing to linearize. The state is a count, not a real vector, and the jump times are random, so two runs of the same experiment give different sample paths.

```{=latex}
\end{example}
```

## More examples

```{=latex}
\begin{example}[frametitle={Example - classifying three systems}]
```

$$\dot{y} = 5y + 4t$$

- *Linear* — the forcing $4t$ involves no output or input, so it does not count as a nonlinearity.
- *Time-varying* — that forcing is pinned to the clock.
- Also *lumped*, *continuous-time*, *deterministic*, *non-homogeneous*.

$$\dot{y} = e^y + 4y + g$$

- *Nonlinear* — the term $e^y$ alone settles it.
- *Time-invariant* — the coefficients are constant and $g$ is the input, so any dependence on $t$ lives in the input, not in the system.
- Also *lumped*, *continuous-time*, *deterministic*, *non-homogeneous*.
- Around an equilibrium $y_e$ (where $e^{y_e} + 4y_e + g = 0$) the tangent to $e^y$ gives an LTI model valid nearby (Linearization chapter).

$$\frac{\partial^2 w(t,x)}{\partial t^2} = c^2\,\frac{\partial^2 w(t,x)}{\partial x^2}, \qquad x \in (0, L), \; t > 0$$

- *Linear* — $\partial^2/\partial t^2$ and $\partial^2/\partial x^2$ are linear operators, so the equation is linear in the field $w$.
- *Time-invariant* — the wave speed $c$ is constant, and no coefficient depends explicitly on $t$.
- *Homogeneous* — no input term; the field moves only under its boundary and initial conditions.
- *Distributed* — the unknown $w(t,x)$ depends on space as well as time, so the state is a field, not a finite vector $\vec{x}$: infinitely many states, no finite-dimensional model.
- Its only lumped approximation is a discretization of $x$ on a grid (the method of lines, as in finite elements).

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - is the integrator LTI?}]
```

The integrator is the simplest dynamic system, $y(t) = \int_0^t u(\tau)\,d\tau$.

**Linear.** Integration is additive and homogeneous, so superposition holds exactly:

$$
\int_0^t \left(a u_1 + b u_2\right) d\tau = a\int_0^t u_1\,d\tau + b\int_0^t u_2\,d\tau.
$$

**Time-invariant.** With signals starting at $t = 0$, the delayed input integrates to

$$
\int_0^t u(\tau - \tau_0)\,d\tau = \int_{-\tau_0}^{t-\tau_0} u(\sigma)\,d\sigma = \int_0^{t-\tau_0} u(\sigma)\,d\sigma,
$$

which is the output delayed by $\tau_0$ and nothing else.

It passes both tests, so the integrator is LTI.

```{=latex}
\end{example}
```

## What can we then do with the toolbox and what can't?

The drum fails because it is distributed, stochastic systems because they are random; either way there is no finite deterministic ODE, and both stay outside the toolbox of these notes. The honest title of these notes would be *lumped deterministic LTI systems*.

Together, linearity and time invariance give far more than either does alone. Any input can be split into delayed, scaled copies of one elementary test signal: linearity makes the responses add, and time invariance makes every copy respond identically. So one experiment is enough — measure the response to a single short kick, the *impulse response* — and the response to any other input follows by superposition. The whole input–output behaviour is fixed by that one measurement.
