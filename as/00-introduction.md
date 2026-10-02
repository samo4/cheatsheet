# Introduction

These notes are about predicting what a dynamic system will do, from its equations alone. First of all, you should never again be unsure what is and isn't an LTI system, and what the difference costs you (this chapter). Along the way you will build a mathematical toolbox to:

- write the state equations of a mechanical or electrical system (Modeling),
- compute its response to an initial state and an input (State space),
- read stability, controllability and observability off the model (Properties),
- describe the input–output behaviour with a transfer function (Transfer functions),
- recognize when a nonlinear system behaves as an LTI one near an operating point, so the same toolbox still applies (Linearization),
- do all of the above for sampled, discrete-time systems (Discrete).

The Linear algebra chapter supplies the matrix tools the rest relies on.

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
- *Lumped*: finitely many state variables obeying an ODE, so the model is finite-dimensional. *Distributed*: the state is a field $w(t, \vec{r})$, a function of space as well as time, obeying a PDE, so there are infinitely many states. A rule of thumb for circuits: they can be treated as lumped while the connections are shorter than $d < \frac{\lambda}{20}$.
- *Continuous-time*: signals are defined at every instant. *Discrete-time*: only at samples $kT$.
- *Deterministic*: the same initial state and input always produce the same trajectory. *Stochastic*: randomness enters, and only statistics are predictable.
- *Homogeneous*: no input; the system runs on its initial state alone. *Non-homogeneous*: an input drives it.

Our mathematical tools need two more properties: *linear* and *time-invariant*.

### Is it linear?

A system is linear when it obeys **superposition**: adding inputs adds their responses, and scaling an input scales its response. This is the linear-map condition you already know: for any $u_1, u_2$ and any constants $a, b$,

$$L(a u_1 + b u_2) = a\,L(u_1) + b\,L(u_2).$$

The two halves are called additivity, $L(u_1 + u_2) = L(u_1) + L(u_2)$, and homogeneity, $L(a u) = a\,L(u)$; both must hold.

Linearity is the same property whether $L$ acts on scalars, vectors or signals; only the space changes.

For a linear system the test is algebraic: every term must be proportional to one signal. Products ($y u$, $y_1 y_2$), powers ($y^2$, $u^2$), and nonlinear functions ($e^y$, $\sin u$, $\sqrt{y}$) break it. A term that involves neither the output nor the input (a prescribed forcing such as $4t$) is not a nonlinearity, though it can destroy time invariance. A constant term is harmless only when it is an input; as a fixed offset it breaks linearity, as the example below shows.

```{=latex}
\begin{example}[frametitle={Example - testing linearity}]
```

Test the system $y = \alpha u + \beta$: a gain with a constant offset.

Homogeneity demands $L(au) = a\,L(u)$ for every $a$, and $a = 0$ alone forces $L(0) = 0$. Here $u = 0$ gives $y = \beta$, so any nonzero offset breaks linearity by itself: the map is affine, not linear. Additivity fails with it: two separate inputs give $\alpha(u_1 + u_2) + 2\beta$, while the input $u_1 + u_2$ gives only $\alpha(u_1 + u_2) + \beta$.

The same additive term is harmless in $\dot{y} = 5y + 4t$, because there it is the input rather than a fixed part of the system.

```{=latex}
\end{example}
```

When there is no equation, only a box on the bench, superposition becomes an experiment instead.

```{=latex}
\begin{example}[frametitle={Example - testing linearity on the bench}]
```

Take an unknown box, say an audio amplifier, with a function generator on its input and an oscilloscope on its output. Start each run from rest, so that only the input drives the output.

**Zero in, zero out.** Switch the generator off. Any steady output voltage is the offset $\beta$ from the example above, and it breaks linearity on its own.

**Homogeneity.** Feed a sine of amplitude $U$, then $2U$, then $4U$. A linear box doubles its output every time.

**A sine in, the same sine out.** Look at the output spectrum (the oscilloscope's FFT mode). An LTI box can change only the amplitude and phase of a sine, so a single line at the input frequency $f$ should come out.

**Additivity.** Use both generator channels and feed the sum of two sines at different frequencies $f_1 \neq f_2$. A linear box answers with the sum of the two separate responses, so the spectrum shows lines only at $f_1$ and $f_2$, each the same as with that sine alone. A nonlinear term such as $u^2$ mixes the two and adds lines at $f_1 \pm f_2$ (intermodulation). Any output power at other frequencies measures how nonlinear the box is.

An experiment can disprove linearity but never prove it: passing every test shows only that the box is linear over the amplitudes and frequencies you tried. Real systems are linear only in a limited range.

```{=latex}
\end{example}
```

### Is it time invariant?

A system is time-invariant if delaying the input by $\tau$ delays the output by the same $\tau$:

$$
\text{if } u(t) \mapsto y(t), \qquad \text{then } u(t - \tau) \mapsto y(t - \tau) \quad \text{for every } \tau.
$$

For an ODE the rule is to look for an explicit $t$: a coefficient or forcing written in $t$ makes the system time-varying, constant coefficients make it time-invariant.

```{=latex}
\begin{example}[frametitle={Example - testing time invariance}]
```

**$\dot{y} = 5y + 4t$ — time-varying.** The coefficient $5$ is constant, but the forcing $4t$ depends explicitly on $t$: at $t = 0$ it drives with $0$, at $t = 10$ with $40$. A shift in time changes the equation, not merely the response.

**$\dot{y} = 5y + u$ — time-invariant.** The same dynamics with the clock removed. Feed the ramp in as the input, $u(t) = 4t$: then $u(t - \tau) = 4(t - \tau)$ gives the delayed response. Either way $\dot{y} = 5y + 4t$ is *linear*; it is time-invariant only if the $4t$ is the input rather than part of the model. The two properties are independent and must be checked separately.

```{=latex}
\end{example}
```

## The LTI class of dynamic systems

One combination of properties does nearly all the work in practice: *linear*, *time-invariant*, *lumped*, *continuous-time*, *deterministic*.

These are the linear time-invariant (LTI) systems.

For them the mathematical toolbox is unusually complete: superposition, the eigenvalues and modes of the system, Laplace transforms, transfer functions, convolution, and with them stability, controllability, and observability. Each of those tools rests on linearity and time invariance and will be discussed in the following chapters.

The justification is not that the world is LTI, but that a system can often be made LTI where and when we need it. Linearize around an equilibrium or along a trajectory and the deviations obey an LTI model (Linearization chapter); sample a continuous system and get a discrete-time one (Discrete chapter). Between them, a great many nonlinear, time-varying and sampled systems can be handled this way.

Linearization does not help with the other two assumptions: the model must be lumped (finitely many states and an ODE: no partial differential equations, no delays) and deterministic (no noise). And even where linearization does apply, it erases phenomena no linear model can recover: multiple equilibria, hysteresis, saturation, chaos.

Two kinds of systems fall outside.

## What LTI leaves out

### Distributed systems

A drum is one of the two classical archetypes of a *distributed* system (the other being the telegrapher's equation). Its skin is a membrane: every point can move, so it has infinitely many states: not a finite vector $\vec{x}$ but a field $w(t, r, \theta)$, the displacement of each point. The governing equation is the two-dimensional wave equation, a partial differential equation in space and time,

$$
\frac{\partial^2 w}{\partial t^2} = c^2\left(\frac{\partial^2 w}{\partial r^2} + \frac{1}{r}\frac{\partial w}{\partial r} + \frac{1}{r^2}\frac{\partial^2 w}{\partial \theta^2}\right),
$$

whose modes are Bessel-function shapes. Hitting the drum excites all of those modes at once, and no finite system of ODEs reproduces what you hear. A lumped model could keep only a few of them. A plucked guitar string has the same problem in one dimension, though its harmonics fall on integers. Neither can be analyzed by the LTI toolbox.

### Stochastic systems

When you add randomness, the same initial state and input no longer give the same response, and only statistics are (hopefully) predictable. How much of the toolbox survives depends on where the randomness enters. In the first example only the *input* is random and the dynamics are LTI, so the model still describes the average behaviour. In the second the state itself jumps at random times: there is no deterministic model left to linearize, and LTI analysis does not apply at all.

```{=latex}
\begin{example}[frametitle={Example - thermal noise in an RC circuit}]
```

Thermal agitation of the electrons in a resistor puts a random voltage across it (Johnson–Nyquist noise), with zero mean and a flat spectrum $S_v = 4 k_B T R$. The RC low-pass filter is the textbook LTI system, with one capacitor and one state, yet its output cannot be predicted, only described statistically.

The dynamics are LTI, but the *input* is random. Two identical experiments give different traces, though nothing about the circuit changed. The toolbox predicts trajectories; here only the statistics are predictable.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - a packet queue}]
```

Packets arrive at a router buffer at random instants and are served one at a time at mean rate $\mu$; the state is the number of packets in the system, an integer. There is no differential equation to write: the count stays constant, then jumps by one at a random time. The questions worth asking are probabilistic from the start: the mean delay, or the probability that the buffer overflows and a packet is lost.

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

Together, linearity and time invariance give far more than either does alone. Any input can be split into delayed, scaled copies of one elementary test signal: linearity makes the responses add, and time invariance makes every copy respond identically. So one experiment is enough: measure the response to a single short kick, the *impulse response*, and the response to any other input follows by superposition. The whole input–output behaviour is fixed by that one measurement.

### What if $a$ is $\mathbf{A}$?

What the toolbox has to do is easiest to see on the simplest dynamic system there is, solved the way you already know from calculus.

```{=latex}
\begin{example}[frametitle={Example - discharging a capacitor}]
```

A capacitor $C$, charged to $x_0$, is switched across a resistor $R$ at $t = 0$.

**Step 1 — model**\
The capacitor voltage $x = v_C$ is the state: it is what the circuit remembers. The capacitor current $i_C = C\dot{x}$ is the only current through the resistor, which carries $x/R$ in the opposite direction, so KCL gives

$$
C\dot{x} + \frac{x}{R} = 0 \quad\Longrightarrow\quad \dot{x} = a x, \qquad a = -\frac{1}{RC}.
$$

**Step 2 — separate the variables**

$$
\frac{dx}{x} = a\,dt
$$

**Step 3 — integrate** from $0$ to $t$

$$
\ln x(t) - \ln x_0 = a t
$$

**Step 4 — exponentiate**

$$
x(t) = x_0\,e^{at} = x_0\,e^{-t/RC}
$$

The voltage decays with the time constant $\tau = RC$: down to $37\,\%$ after $\tau$, below $1\,\%$ after $5\tau$. With $a > 0$ it would instead grow without bound.

**Step 5 — check**\
$\dot{x} = a\,x_0 e^{at} = a x$, and $x(0) = x_0$.

```{=latex}
\end{example}
```

Now couple a few such circuits together. Every capacitor and inductor brings a state, and each derivative depends on all of them, so $a$ becomes a matrix:

$$
\dot{\vec{x}} = \mathbf{A}\vec{x}, \qquad \vec{x}(0) = \vec{x}_0.
$$

Steps 2 to 4 break at once: there is no dividing by a vector and no logarithm of one. The answer still has the same form,

$$
\vec{x}(t) = e^{\mathbf{A}t}\vec{x}_0,
$$

provided $e^{\mathbf{A}t}$ can be given a meaning, and the check of Step 5 goes through unchanged once $\frac{d}{dt}e^{\mathbf{A}t} = \mathbf{A}e^{\mathbf{A}t}$. Getting the state equations is the Modeling chapter, and making sense of $e^{\mathbf{A}t}$ is the State space chapter. Everything else follows the same pattern, the scalar result with a matrix in place of $a$:

- the exponential $e^{at}$ becomes the matrix exponential $e^{\mathbf{A}t}$ (Linear algebra, State space),
- the sign of $a$ becomes the eigenvalues of $\mathbf{A}$ (Properties),
- the transfer function $\frac{b}{s-a}$ becomes $\mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}$ (Transfer functions),
- $a^k$ becomes $\mathbf{A}^k$ (Discrete).

The only new questions (can the input reach every state, can the output see every state) are the ones a single state cannot ask.

The number of states can be large but must be finite: with infinitely many, as in the drum, $\mathbf{A}$ is no longer a matrix.
