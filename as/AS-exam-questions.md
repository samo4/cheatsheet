# Analysis of Systems — oral exam questions

Recollections of the oral exam (sets A–K), normalized into English, deduplicated and grouped by topic. Where a student wrote down the expected answer, it is kept as a short *hint*. Questions marked **(added)** are not from the reports — they are written from chapters 01–06 of these notes.

What the reports agree on:

- The exam is usually **three questions**: one easy definition, one modeling example, one computation.
- The professor also asks **examples that were only worked at the lecture** and never appear on the slides — those are worth re-reading.
- Almost every question is "state the definition, then one step further": derive it, give a circuit example, or compute it.
- Do not overcomplicate. Set up the state equations only when the question actually asks for them.

## 1. System classification and properties

- What is a observable system? 
- **Static vs. dynamic**: define both, and say what changes mathematically — memoryless $y = f(u)$ versus memory that forces a differential equation and a state.
- Give an **electrical-circuit example** of each. *Hint: a purely resistive network is static; put a capacitor or an inductor in it and it becomes dynamic.*
- Give an electrical example for the **four combinations** of static/dynamic and time-invariant/time-varying.
- **Time-invariant vs. time-varying**: define both. What does time invariance require physically? *Hint: an ideal circuit — one that does not age and whose parameters do not drift.*
- What does it mean for a system to be **linear**? Write the condition down and "prove" it — superposition: additivity $L(u_1+u_2)=L(u_1)+L(u_2)$ and homogeneity $L(au)=aL(u)$, both required.
- Show why a **constant offset** breaks linearity (taking $a=0$ alone forces $L(0)=0$), and when a constant term is harmless instead.
- **Deterministic vs. stochastic**: what changes? *Hint: same state and input give the same trajectory, versus only statistics being predictable.*
- **Homogeneous vs. non-homogeneous**: what does "homogeneous" mean for the state equation? *Hint: no excitation — the system runs on the initial state alone.*
- **Black box test**: how would you find out whether a system is static or dynamic without opening it? *Hint: send an excitation in and look at the response — instantaneous means static, a transient means dynamic.*
- Which **input signals** are best for that test? *Hint: the step was accepted, but the professor wanted to hear unit impulse.*
- **Convolution**: what is it, what does it let you do for an LTI system, and how does it connect to the impulse response?

## 2. Modeling

- **Modeling electrical circuits**: what are the potentials, what are the node equations, what are the unknowns?
- How do we get the **additional equations** beyond KCL at the nodes?
- Why do we need **one extra equation per voltage source**, and which new variable does a voltage source bring into the circuit? *Hint: the source current, e.g. $i_g$.*
- Why do we need **an extra equation per reactive element**?
- Why does **a capacitor need two equations**, and why does its current appear in two node equations?
- Why are the state variables of an inductor/capacitor network the **inductor current and the capacitor voltage**, and not the other way round?
- Only **resistive circuits**: potentials, node equations, what the unknowns are, and how the extra equations are produced.
- Given a circuit, **in what way would you solve it** — which route (node equations, state equations, impedance/divider) and why?
- **Mechanical and rotational modeling**: how do you get from the physical system to the first-order state equations?
- **Modeling a pandemic (SIR)**: derive the model, then use it. Reported chain: *difference between a static and a dynamic model → derive the SIR model → how do you get the discrete state-transition matrix at the end?*
- **Frequency-domain circuit example**: inductor in series with a capacitor that has a resistor in parallel; express the voltage across the resistor in the frequency domain. *Hint (from the student): combine the parallel RC into a single impedance, then treat it as a voltage divider between the inductor impedance and that impedance, and read the voltage across the RC impedance — no state equations needed.*

## 3. State equations and the state-transition matrix (continuous time)

- Write the **general state equation** (and the output equation); say what each matrix means.
- **General solution** of the state equation — homogeneous and non-homogeneous parts.
- What is the **state-transition matrix** $\Phi(t)$, and what properties does it have?
- **All the methods for determining $\Phi$** (reported "all three"): know them and know when to pick which.
- **Cayley–Hamilton**: what does the theorem actually say, and how do we use it to produce the forms we then apply to the exercises? *Hint: it turns any matrix function (or a power $A^k$) into a polynomial of degree at most $n-1$, with the coefficients from the scalar eigenvalue identities.*
- **Controllability**: what does it mean, and derive the criterion.
- How do you compute an **arbitrary function of a matrix** with Cayley–Hamilton?

## 4. State equations and the state-transition matrix (discrete time)

- Write the **discrete state equation**. How would you compute $x[m]$ (or $x[k]$)?
- Difference equation versus differential equation: write one down and say which it is, and why.
- How is the index $k$ in a discrete equation **related to time**?
- What is the **discrete state-transition matrix** $A^k$, and how do you compute it? *(asked repeatedly)*
- **General solution for $x[k]$** — homogeneous plus forced part.
- Deriving the **discrete state-transition matrix at the end of a modeling derivation** (e.g. after the SIR model).

## 5. Transfer functions, stability, and the toolbox

- **Transfer function**: what is it, and where does it come from?
- **Stability**: asymptotically stable versus marginally stable; where do the eigenvalues have to lie?
- **Bounded-input bounded-output stability**, and how it differs from asymptotic stability.
- **Observability**: state it and give the criterion.
- How do eigenvalues, modes, poles, and the transfer function all hang together?

## Added questions (from chapters 01–06 of these notes)

### 01 Modeling

- **(added)** Turn a third-order ODE into a system of first-order equations. Why is that always possible, and what ends up in the state vector?
- **(added)** Why is the choice of state variables not unique? Produce a second valid state vector for the same circuit and the invertible map between them.
- **(added)** Write the constitutive relation and the stored energy for the spring, the damper and the mass — then for their rotational counterparts.
- **(added)** In the car suspension model, why does $mg$ disappear once $x$ is measured from the static equilibrium, and what does the constant input do to the equilibrium if it is not?
- **(added)** State the passive sign convention and show how the signs in $v = L\,\dot{i}$ and in the damper force follow from the chosen voltage/current references. What changes if one reference is flipped?
- **(added)** Why are the inductor current and the capacitor voltage the natural state variables? Connect it to energy and to the constitutive relations giving the derivatives directly.
- **(added)** Show that a purely resistive network has no state at all.

### 02 State-space

- **(added)** Verify the properties of $\Phi(t)$: $\Phi(0)=\mathbf{I}$, $\Phi(t+\tau)=\Phi(t)\Phi(\tau)$, $\Phi^{-1}(t)=\Phi(-t)$, and the two forms of its derivative.
- **(added)** Derive the non-homogeneous solution. Why does the substitution trick give the convolution integral with $\Phi(t-\tau)$, and what breaks when the lower limit is not $0$?
- **(added)** Solve the hanging-mass example by the Taylor series route, then check the initial position and velocity as a sanity check.
- **(added)** Laplace route: get $\Phi$ from the inverse transform of $(s\mathbf{I}-\mathbf{A})^{-1}$. Why is the resolvent such a useful object?
- **(added)** Diagonalization route: what does it require, what do $\mathbf{V}$ and $\mathbf{V}^{-1}$ do, and what is different when $\mathbf{A}$ is defective?
- **(added)** Why is a triangular $\mathbf{A}$ "half the jackpot" when computing $\Phi$?
- **(added)** Compare the four methods. Which do you reach for when, and which one is the only option in some cases?

### 03 Properties

- **(added)** What are the modes of an LTI system, and how do they relate to the eigenvalues? Which modes reach the output?
- **(added)** Classify the equilibrium by eigenvalue location: asymptotically stable, marginally stable, unstable.
- **(added)** Sketch the basic phase portraits (focus, node, saddle, centre) and say what selects each type.
- **(added)** Give a system that is BIBO stable but not asymptotically stable, and explain the minimality caveat. *(pole–zero cancellation)*
- **(added)** Why is marginal stability so sensitive to small parameter changes?
- **(added)** Define controllability and derive the rank criterion. Why is a determinant not the test?
- **(added)** Define observability and derive its criterion; why is it the dual of controllability?

### 04 Transfer functions

- **(added)** Derive $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$. What is $\mathbf{D}$, and what does $\mathbf{D} \ne 0$ mean physically?
- **(added)** What do the poles and zeros of $G(s)$ tell you, and how do they relate to the eigenvalues and to the reachable/observable modes?
- **(added)** Why does the impulse response determine the response to every input? State the convolution theorem.
- **(added)** What are the Heaviside step and the Dirac impulse, and which of their properties does the course use?
- **(added)** Derive the closed-loop transfer function for a feedback loop and say what the loop does to the poles.
- **(added)** Block diagrams: how do you move a summing junction past a block, and a pickoff point past a block? Why can you not move a pickoff across a summing junction?
- **(added)** Convert a state-space model to a transfer function and back. What information is lost?

### 05 Linearization

- **(added)** What is an operating point (equilibrium)? Linearize a scalar $f(x)$ about $x_0$ and give the geometric reading.
- **(added)** Multivariable case: how do the gradient and the Jacobian enter?
- **(added)** Linearize $\dot{\vec{x}} = f(\vec{x}, \vec{u})$ at an equilibrium. Where do constant terms go, and why is the equilibrium shifted to the origin first?
- **(added)** Linearize the SIR model. What do the eigenvalues say near the disease-free equilibrium, and what happens at the endemic one?
- **(added)** Linearize Lotka–Volterra around the coexistence point. What kind of equilibrium comes out, and what does that say about the original system?
- **(added)** What behaviour does a linear model destroy (multiple equilibria, saturation, hysteresis, chaos), and which assumptions do we silently need (lumped, deterministic)?

### 06 Discrete systems

- **(added)** Solve $x[k+1] = a\,x[k] + b\,u[k]$. Write the general solution and interpret $|a| < 1$.
- **(added)** The index versus time: what is a sample physically, and why is the input weighted by $A^{k-m}$ when it is applied at step $m$?
- **(added)** Use the Z-transform, with its shift property and initial conditions, to solve a difference equation.
- **(added)** Derive $A^k$ by all three routes: Z-transform, diagonalization, Cayley–Hamilton.
- **(added)** When must you split $X(z)/z$ rather than $X(z)$ before partial fractions, and why?
- **(added)** Discretizing a continuous model: the Euler method versus the integral approximation — what $\mathbf{A}_d$ and $\mathbf{B}_d$ does each give?
- **(added)** Discrete stability: why does the condition become $|\lambda| < 1$, and what happens to the BIBO statement?
- **(added)** Are the equilibrium, controllability and observability criteria the same in discrete time as in continuous time?
- **(added)** Write the difference equation for the people-moving-to-the-city model and for Samuelson's national income model, and say what the coefficients mean.

## Provenance

| set | what was asked |
| --- | --- |
| A | "what is a *spoznaven* system", modeling the pandemic, frequency-domain voltage divider |
| B | same three as A; divider clarified as parallel-RC impedance in a divider with the inductor |
| C | static/dynamic systems, discrete state equation $x[m]$, discrete state-transition matrix, SIR derivation |
| D | time-varying/invariant systems, modeling electrical circuits, discrete state-transition matrix |
| E | static/dynamic, time-varying/invariant, circuit examples for both, general state equation, all three methods for the state-transition matrix |
| F | resistive circuits only: potentials, node equations, unknowns, extra equations |
| G | static/dynamic, time-varying/invariant, a circuit example and how to solve it, discrete state equation, general solution for $x[k]$ |
| H | static/dynamic, stochastic/deterministic, convolution, discrete state equation, controllability and its criterion, matrix function via Cayley–Hamilton |
| I | linearity ("prove it"), how we solve circuits, extra equation per voltage source (adds $i_g$), extra equations for reactive elements, capacitor needs two equations, why $(i_L, u_C)$ are the states, general solution for $x[k]$ |
| K | static/dynamic, black-box test (best excitation: unit impulse), continuous state equations, homogeneity condition, Cayley–Hamilton statement and how its forms are used |
