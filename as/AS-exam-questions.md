# Analysis of Systems — oral exam questions

- The exam is usually **three questions**: one easy definition, one modeling example, one computation.
- The professor also asks **examples that were only worked at the lecture** and never appear on the slides — those are worth re-reading.
- Almost every question is "state the definition, then one step further": derive it, give a circuit example, or compute it.
- Do not overcomplicate. Set up the state equations only when the question actually asks for them.

## 1. System classification and properties

- [x] What is an observable system? 
- [x] Static vs. dynamic
  - [x] Give an electrical-circuit example of each
- [x] Define time-invariant vs. time-varying
  - [x] What does time invariance require physically? *Hint: an ideal circuit — one that does not age and whose parameters do not drift.*
  - [x] Give an electrical example
- [x] What does it mean for a system to be linear?
  - [x] Write the condition down and "prove" it
- [x] Show why a constant offset breaks linearity
- [x] Deterministic vs. stochastic: what changes? *Hint: same state and input give the same trajectory, versus only statistics being predictable.*
- [x] Homogeneous vs. non-homogeneous: what does "homogeneous" mean for the state equation?
- [x] Black box test: how would you find out whether a system is static or dynamic without opening it? *Hint: send an excitation in and look at the response — instantaneous means static, a transient means dynamic.* PS: pedantic answer is: you can't tell if it's static, but you can tell if it's dynamic.
  - [x] Which input signals are best for that test? *Hint: the step was accepted, but the professor wanted to hear unit impulse.*
- [x] Convolution:
  - [x] what is it *Hint: convolution is the superposition integral — it takes every past value of the input, scales it by how the system answers a kick, and adds the lot up*
  - [x] what does it let you do for an LTI system *Hint: one measurment gives you everything you need to predict the response to any input*
  - [x] how does it connect to the impulse response?

## 2. Modeling

- [x] Modeling electrical circuits:
  - [x] what are the potentials
  - [x] what are the node equations
  - [x] what are the unknowns?
- [ ] How do we get the additional equations beyond KCL at the nodes?
- [ ] Why do we need one extra equation per voltage source, and which new variable does a voltage source bring into the circuit? *Hint: the source current, e.g. $i_g$.*
- [ ] Why do we need an extra equation per reactive element?
- [ ] Why does a capacitor need two equations, and why does its current appear in two node equations?
- [ ] Why are the state variables of an inductor/capacitor network the inductor current and the capacitor voltage, and not the other way round?
- [ ] Only resistive circuits:
  - [ ] potentials
  - [ ] node equations
  - [ ] what the unknowns are
  - [ ] how the extra equations are produced
- [ ] Given a circuit, in what way would you solve it — which route (node equations, state equations, impedance/divider) and why?
- [ ] Mechanical and rotational modeling: how do you get from the physical system to the first-order state equations?
- [ ] Modeling a pandemic (SIR): derive the model, then use it.
  - [ ] Reported chain: *difference between a static and a dynamic model → derive the SIR model → how do you get the discrete state-transition matrix at the end?*
- [ ] Frequency-domain circuit example:
  - [ ] inductor in series with a capacitor that has a resistor in parallel; express the voltage across the resistor in the frequency domain. *Hint: combine the parallel RC into a single impedance, then treat it as a voltage divider between the inductor impedance and that impedance, and read the voltage across the RC impedance — no state equations needed.*

### Kindly provided by LLM

- [ ] Turn a third-order ODE into a system of first-order equations.
  - [ ] Why is that always possible, and what ends up in the state vector?
- [ ] Why is the choice of state variables not unique?
  - [ ] Produce a second valid state vector for the same circuit and the invertible map between them.
- [ ] In the car suspension model, why does $mg$ disappear once $x$ is measured from the static equilibrium, and what does the constant input do to the equilibrium if it is not?
- [ ] Why are the inductor current and the capacitor voltage the natural state variables?
- [ ] Show that a purely resistive network has no state at all.

## 3. State equations and the state-transition matrix (continuous time)

- [ ] Write the general state equation (and the output equation)
  - [ ] say what each matrix means
- [ ] General solution of the state equation — homogeneous and non-homogeneous parts.
- [ ] What is the state-transition matrix $\Phi(t)$, and what properties does it have?
- [ ] All the methods for determining $\Phi$ (reported "all three"): know them and know when to pick which.
- [ ] Cayley–Hamilton: what does the theorem actually say, and how do we use it to produce the forms we then apply to the exercises? *Hint: it turns any matrix function (or a power $A^k$) into a polynomial of degree at most $n-1$, with the coefficients from the scalar eigenvalue identities.*
- [ ] Controllability: what does it mean, and derive the criterion.
- [ ] How do you compute an arbitrary function of a matrix with Cayley–Hamilton?

### Kindly provided by LLM

- [ ] Verify the properties of $\Phi(t)$: $\Phi(0)=\mathbf{I}$, $\Phi(t+\tau)=\Phi(t)\Phi(\tau)$, $\Phi^{-1}(t)=\Phi(-t)$, and the two forms of its derivative.
- [ ] Derive the non-homogeneous solution.
  - [ ] Why does the substitution trick give the convolution integral with $\Phi(t-\tau)$, and what breaks when the lower limit is not $0$?
- [ ] Solve the hanging-mass example by the Taylor series route, then check the initial position and velocity as a sanity check.
- [ ] Laplace route: get $\Phi$ from the inverse transform of $(s\mathbf{I}-\mathbf{A})^{-1}$.
  - [ ] Why is the resolvent such a useful object?
- [ ] Diagonalization route:
  - [ ] what does it require
  - [ ] what do $\mathbf{V}$ and $\mathbf{V}^{-1}$ do
  - [ ] what is different when $\mathbf{A}$ is defective?
- [ ] Why is a triangular $\mathbf{A}$ "half the jackpot" when computing $\Phi$?
- [ ] Compare the four methods.
  - [ ] Which do you reach for when, and which one is the only option in some cases?

## 4. State equations and the state-transition matrix (discrete time)

- [ ] Write the discrete state equation.
  - [ ] How would you compute $x[m]$ (or $x[k]$)?
- [ ] Difference equation versus differential equation: write one down and say which it is, and why.
- [ ] How is the index $k$ in a discrete equation related to time?
- [ ] What is the discrete state-transition matrix $A^k$, and how do you compute it? *(asked repeatedly)*
- [ ] General solution for $x[k]$ — homogeneous plus forced part.
- [ ] Deriving the discrete state-transition matrix at the end of a modeling derivation (e.g. after the SIR model).

### Kindly provided by LLM

- [ ] Are the equilibrium, controllability and observability criteria the same in discrete time as in continuous time?

## 5. Transfer functions, stability, and the toolbox

- [ ] Transfer function: what is it, and where does it come from?
- [ ] Stability:
  - [ ] asymptotically stable versus marginally stable
  - [ ] where do the eigenvalues have to lie?
- [ ] Bounded-input bounded-output stability, and how it differs from asymptotic stability.
- [ ] Observability: state it and give the criterion.
- [ ] Controllability: state it and give the criterion.
- [ ] How do eigenvalues, modes, poles, and the transfer function all hang together?

### Kindly provided by LLM

- [ ] Derive $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$.
- [ ] What do the poles and zeros of $G(s)$ tell you, and how do they relate to the eigenvalues and to the reachable/observable modes?
- [ ] Why does the impulse response determine the response to every input?
  - [ ] State the convolution theorem.
- [x] What information is lost when converting a state-space model to a transfer function and back.
- [ ] What are the modes of an LTI system, and how do they relate to the eigenvalues?
  - [ ] Which modes reach the output?
- [x] Sketch the basic phase portraits (focus, node, saddle, centre) and say what selects each type.
- [x] Why is marginal stability so sensitive to small parameter changes?




