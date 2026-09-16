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
- [x] Black box test: how would you find out whether a system is static or dynamic without opening it? *Hint: kill the excitation and watch — a static system sits at 0 while anything still settling means a state. Or use best testing signal: the unit impulse: anything shown in output after t=0 indicates a dynamic system.* PS: pedantic answer is: you can't tell if it's static, but you can tell if it's dynamic.
  - [x] Which input signals are best for that test? *Hint: unit impulse — it is the shortest probe, no probllem if the system is integrating and it reaveals syetem memory instantly.*
- [x] Convolution:
  - [x] what is it *Hint: convolution is the superposition integral — it takes every past value of the input, scales it by how the system answers a kick, and adds the lot up*
  - [x] what does it let you do for an LTI system *Hint: one measurment gives you everything you need to predict the response to any input*
  - [x] how does it connect to the impulse response?

## 2. Modeling

- [x] Modeling electrical circuits:
  - [x] what are the potentials
  - [x] what are the node equations
  - [x] what are the unknowns?
- [x] How do we get the additional equations beyond KCL at the nodes? *Hint: from the elements — $v = Ri$, $i_C = C\dot{v}_C$, $v_L = L\dot{i}_L$.*
- [x] Why do we need one extra equation per voltage source, and which new variable does a voltage source bring into the circuit? *Hint: $i_g$.*
- [x] Why do we need an extra equation per reactive element? *Hint: each brings a new unknown (a state), and with it its own law, $C\dot{v}_C = i_C$.*
- [x] Why does a capacitor need two equations, and why does its current appear in two node equations? *Hint: two unknowns — its voltage (a state) and its current (a branch current, so KCL at both ends mentions it).*
- [x] Why are the state variables of an inductor/capacitor network the inductor current and the capacitor voltage, and not the other way round? *Hint: energy variable cannot jump and we need equations that include non-derviative and derviative $C\dot{v}_C = i_C$ works*
- [x] Only resistive circuits:
  - [x] potentials *Hint: node voltages, one node grounded.*
  - [x] node equations *Hint: KCL at every non-ground node, currents as $V/R$.*
  - [x] what the unknowns are *Hint: only the node potentials.*
  - [x] how the extra equations are produced *Hint: none — every element is already known through $V/R$.*
- [x] Given a circuit, in what way would you solve it — which route (node equations, state equations, impedance/divider) and why? *Hint: whichever leaves fewest unknowns; state equations only if states are asked for.*
- [x] Mechanical and rotational modeling: how do you get from the physical system to the first-order state equations? *Hint: one state per storage, so position and velocity; signs from the elements, then $x_1 = x$, $x_2 = \dot{x}$.*
- [x] Modeling a pandemic (SIR): 
  - [x] derive the model, then use it.
  - [x] how do you get the discrete state-transition matrix at the end?
- [ ] Frequency-domain circuit example:
  - [ ] inductor in series with a capacitor that has a resistor in parallel; express the voltage across the resistor in the frequency domain. *Hint: combine the parallel RC into a single impedance, then treat it as a voltage divider between the inductor impedance and that impedance, and read the voltage across the RC impedance — no state equations needed.*

### Kindly provided by LLM

- [x] Turn a third-order ODE into a system of first-order equations. *Hint: $x_1 = y$, $x_2 = \dot{y}$, $x_3 = \ddot{y}$*
  - [x] Why is that always possible, and what ends up in the state vector? *Hint: solve the ODE for its highest derivative; the state is the variable plus its derivatives up to $n-1$.*
- [x] Why is the choice of state variables not unique? *Hint: any invertible $\vec{z} = \mathbf{T}\vec{x}$ is another valid state.*
- [x] In the car suspension model, why does $mg$ disappear once $x$ is measured from the static equilibrium, and what does the constant input do to the equilibrium if it is not? *Hint: the static spring force already carries the weight, so the two cancel; otherwise $mg$ only shifts the equilibrium.*
- [ ] Why are the inductor current and the capacitor voltage the natural state variables? *Hint: same reason as above — the energy variables that cannot jump.*
- [x] Show that a purely resistive network has no state at all.

## 3. State equations and the state-transition matrix (continuous time)

- [x] Write the general state equation (and the output equation)
  - [x] say what each matrix means
- [x] General solution of the state equation — homogeneous and non-homogeneous parts.
- [x] What is the state-transition matrix $\Phi(t)$, and what properties does it have? *Hint: 1. $\Phi(0)=\mathbf{I}$ (with $\dot\Phi=\mathbf{A}\Phi$ this is the definition) 2. $\Phi(t+\tau)=\Phi(t)\Phi(\tau)$ 3. $\Phi^{-1}(t)=\Phi(-t)$, so nonsingular for every $t$ — it is not diagonal in general, that is only the case $\mathbf{A}$ diagonal 4. $\dot\Phi=\mathbf{A}\Phi=\Phi\mathbf{A}$, both orders.*
- [ ] All the methods for determining $\Phi$ *Hint: Taylor (terminates only for nilpotent, or $\lambda\mathbf{I}+\mathbf{N}$), diagonalization $\mathbf{V}e^{\boldsymbol\Lambda t}\mathbf{V}^{-1}$ (fastest when eigenvectors are easy, dies on defectiveness), Cayley–Hamilton $e^{\mathbf{A}t}=\sum_{k<n}\alpha_k(t)\mathbf{A}^k$ (always works — the only option when defective), Laplace $\mathcal L^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$ (small matrices, repeated poles, and it hands you $G(s)$ too).*
- [x] Cayley–Hamilton: what does the theorem actually say, and how do we use it to produce the forms we then apply to the exercises? *Hint: $p(\mathbf{A})=\mathbf{0}$ kills every power $k\ge n$, so $g(\mathbf{A})=\sum_{k<n}c_k\mathbf{A}^k$; the $c_k$ come from matching $g$ at the eigenvalues, $r(\lambda_i)=g(\lambda_i)$ — plus the derivative conditions $r^{(m)}(\lambda_i)=g^{(m)}(\lambda_i)$ when an eigenvalue repeats, which is where $te^{\lambda t}$ enters. Eigenvalue-wise it reads $\operatorname{eig}(g(\mathbf{A}))=g(\operatorname{eig}(\mathbf{A}))$, and it works without eigenvectors, so it is the only route that survives a defective $\mathbf{A}$.*
- [x] Controllability: what does it mean, and derive the criterion.
- [x] How do you compute an arbitrary function of a matrix with Cayley–Hamilton?

### Kindly provided by LLM

- [ ] Derive the non-homogeneous solution.
  - [ ] Why does the substitution trick give the convolution integral with $\Phi(t-\tau)$, and what breaks when the lower limit is not $0$?
- [ ] Why is a triangular $\mathbf{A}$ "half the jackpot" when computing $\Phi$?
- [ ] Compare the four methods.
  - [ ] Which do you reach for when, and which one is the only option in some cases?

## 4. State equations and the state-transition matrix (discrete time)

- [x] Write the discrete state equation.
  - [x] How would you compute $x[m]$ (or $x[k]$)?
- [x] Difference equation versus differential equation: write one down and say which it is, and why.*PS: they are only analogues, not identical.*
- [x] How is the index $k$ in a discrete equation related to time?
- [ ] What is the discrete state-transition matrix $A^k$, and how do you compute it? *asked repeatedly*
- [ ] General solution for $x[k]$ — homogeneous plus forced part.
- [ ] Deriving the discrete state-transition matrix at the end of a modeling derivation (e.g. after the SIR model).

### Kindly provided by LLM

- [x] Are the equilibrium, controllability and observability criteria the same in discrete time as in continuous time?

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




