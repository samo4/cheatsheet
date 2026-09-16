# Analysis of Systems — oral exam questions

## 1. System classification and properties

- [ ] **1.1** What is an observable system?
- [ ] **1.2** Static vs. dynamic
  - [ ] **1.2.1** Give an electrical-circuit example of each
- [ ] **1.3** Define time-invariant vs. time-varying
  - [ ] **1.3.1** What does time invariance require physically?
  - [ ] **1.3.2** Give an electrical example
- [ ] **1.4** What does it mean for a system to be linear?
  - [ ] **1.4.1** Write the condition down and "prove" it
- [ ] **1.5** Show why a constant offset breaks linearity
- [ ] **1.6** Deterministic vs. stochastic: what changes?
- [ ] **1.7** Homogeneous vs. non-homogeneous: what does "homogeneous" mean for the state equation?
- [ ] **1.8** Black box test: how would you find out whether a system is static or dynamic without opening it?
  - [ ] **1.8.1** Which input signals are best for that test?
- [ ] **1.9** Convolution:
  - [ ] **1.9.1** what is it
  - [ ] **1.9.2** what does it let you do for an LTI system
  - [ ] **1.9.3** how does it connect to the impulse response?

## 2. Modeling

- [ ] **2.1** Modeling electrical circuits:
  - [ ] **2.1.1** what are the potentials
  - [ ] **2.1.2** what are the node equations
  - [ ] **2.1.3** what are the unknowns?
- [ ] **2.2** How do we get the additional equations beyond KCL at the nodes?
- [ ] **2.3** Why do we need one extra equation per voltage source, and which new variable does a voltage source bring into the circuit?
- [ ] **2.4** Why do we need an extra equation per reactive element?
- [ ] **2.5** Why does a capacitor need two equations, and why does its current appear in two node equations?
- [ ] **2.6** Why are the state variables of an inductor/capacitor network the inductor current and the capacitor voltage, and not the other way round?
- [ ] **2.7** Only resistive circuits:
  - [ ] **2.7.1** potentials
  - [ ] **2.7.2** node equations
  - [ ] **2.7.3** what the unknowns are
  - [ ] **2.7.4** how the extra equations are produced
- [ ] **2.8** Given a circuit, in what way would you solve it — which route (node equations, state equations, impedance/divider) and why?
- [ ] **2.9** Mechanical and rotational modeling: how do you get from the physical system to the first-order state equations?
- [ ] **2.10** Modeling a pandemic (SIR):
  - [ ] **2.10.1** derive the model, then use it.
  - [ ] **2.10.2** how do you get the discrete state-transition matrix at the end?
- [ ] **2.11** Frequency-domain circuit example:
  - [ ] **2.11.1** inductor in series with a capacitor that has a resistor in parallel; express the voltage across the resistor in the frequency domain.

### Kindly provided by LLM

- [ ] **2.12** Turn a third-order ODE into a system of first-order equations.
  - [ ] **2.12.1** Why is that always possible, and what ends up in the state vector?
- [ ] **2.13** Why is the choice of state variables not unique?
- [ ] **2.14** In the car suspension model, why does $mg$ disappear once $x$ is measured from the static equilibrium, and what does the constant input do to the equilibrium if it is not?
- [ ] **2.15** Why are the inductor current and the capacitor voltage the natural state variables?
- [ ] **2.16** Show that a purely resistive network has no state at all.

## 3. State equations and the state-transition matrix (continuous time)

- [ ] **3.1** Write the general state equation (and the output equation)
  - [ ] **3.1.1** say what each matrix means
- [ ] **3.2** General solution of the state equation — homogeneous and non-homogeneous parts.
- [ ] **3.3** What is the state-transition matrix $\Phi(t)$, and what properties does it have?
- [ ] **3.4** All the methods for determining $\Phi$
- [ ] **3.5** Cayley–Hamilton: what does the theorem actually say, and how do we use it to produce the forms we then apply to the exercises?
- [ ] **3.6** Controllability: what does it mean, and derive the criterion.
- [ ] **3.7** How do you compute an arbitrary function of a matrix with Cayley–Hamilton?

### Kindly provided by LLM

- [ ] **3.8** Derive the non-homogeneous solution.
  - [ ] **3.8.1** Why does the substitution trick give the convolution integral with $\Phi(t-\tau)$, and what breaks when the lower limit is not $0$?
- [ ] **3.9** Why is a triangular $\mathbf{A}$ "half the jackpot" when computing $\Phi$?
- [ ] **3.10** Compare the four methods.
  - [ ] **3.10.1** Which do you reach for when, and which one is the only option in some cases?
- [ ] **3.11** Algebraic vs. geometric multiplicity of eigenvalues.

## 4. State equations and the state-transition matrix (discrete time)

- [ ] **4.1** Write the discrete state equation.
  - [ ] **4.1.1** How would you compute $x[m]$ (or $x[k]$)?
- [ ] **4.2** Difference equation versus differential equation: write one down and say which it is, and why. *PS: they are only analogues, not identical.*
- [ ] **4.3** How is the index $k$ in a discrete equation related to time?
- [ ] **4.4** What is the discrete state-transition matrix $\mathbf{A}^k$, and how do you compute it? *asked repeatedly*
- [ ] **4.5** General solution for $x[k]$ — homogeneous plus forced part.
- [ ] **4.6** Deriving the discrete state-transition matrix at the end of a modeling derivation (e.g. after the SIR model).

### Kindly provided by LLM

- [ ] **4.7** Are the equilibrium, controllability and observability criteria the same in discrete time as in continuous time?

## 5. Transfer functions, stability, and the toolbox

- [ ] **5.1** Transfer function: what is it, and where does it come from?
- [ ] **5.2** Stability:
  - [ ] **5.2.1** asymptotically stable versus marginally stable
  - [ ] **5.2.2** where do the eigenvalues have to lie?
- [ ] **5.3** Bounded-input bounded-output stability, and how it differs from asymptotic stability.
- [ ] **5.4** Observability: state it and give the criterion.
- [ ] **5.5** Controllability: state it and give the criterion.
- [ ] **5.6** How do eigenvalues, modes, poles, and the transfer function all hang together?

### Kindly provided by LLM

- [ ] **5.7** Derive $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$.
- [ ] **5.8** What do the poles and zeros of $G(s)$ tell you, and how do they relate to the eigenvalues and to the reachable/observable modes?
- [ ] **5.9** Why does the impulse response determine the response to every input?
  - [ ] **5.9.1** State the convolution theorem.
- [ ] **5.10** What information is lost when converting a state-space model to a transfer function and back.
- [ ] **5.11** What are the modes of an LTI system, and how do they relate to the eigenvalues?
  - [ ] **5.11.1** Which modes reach the output?
- [ ] **5.12** Sketch the basic phase portraits (focus, node, saddle, centre) and say what selects each type.
- [ ] **5.13** Why is marginal stability so sensitive to small parameter changes?

# Hints

One-liners for the questions above; the numbers match.

## 1. System classification and properties

- **1.1** — From $y(t)$ over a finite interval, with the input known, you can reconstruct $\vec{x}(t_0)$ — every state leaves a trace in the output. Criterion: $\operatorname{rank}[\mathbf{C};\mathbf{C}\mathbf{A};\dots;\mathbf{C}\mathbf{A}^{n-1}]=n$.
- **1.2** — Static: the output depends only on the present input, $y=f(u)$, no memory. Dynamic: memory — a differential or difference equation, and a state.
- **1.2.1** — Static: a resistive divider. Dynamic: any RC or RL network — the capacitor (or inductor) holds a state.
- **1.3** — Shifting the input in time shifts the output by the same amount: the response depends on elapsed time, not on what the clock reads.
- **1.3.1** — An ideal circuit — one that does not age and whose parameters do not drift.
- **1.3.2** — Invariant: a fixed R, C, L network. Time-varying: a potentiometer turned mid-experiment, or a switched converter.
- **1.4** — Superposition: additivity plus homogeneity, $f(a u_1 + b u_2) = a f(u_1) + b f(u_2)$ — which already forces zero input to give zero output.
- **1.4.1** — Write the condition down, then "prove" it: compute the two single responses, scale and add them, and compare with the response to the combined input.
- **1.5** — $y = f(u) + c$: zero input gives $c \neq 0$, and scaling the input leaves the offset unscaled — additivity and homogeneity both fail.
- **1.6** — Deterministic: same state and input give the same trajectory. Stochastic: only the statistics are predictable.
- **1.7** — Homogeneous: $\vec{u} = \vec{0}$, so only the initial state drives the motion ($\dot{\vec{x}} = \mathbf{A}\vec{x}$). Non-homogeneous: the input term is present.
- **1.8** — Kill the excitation and watch: a static system sits at 0, anything still settling means a state. With a unit impulse, anything in the output after $t=0$ means memory. Pedantically: you can prove dynamic, not static.
- **1.8.1** — The unit impulse: the shortest probe, it reveals memory instantly, and it still works when the system is integrating.
- **1.9.1** — The superposition integral: take every past value of the input, scale it by how the system answers a kick, and add the lot up.
- **1.9.2** — One measurement of $h$ gives everything: the response to any input is $h * u$.
- **1.9.3** — $h$ *is* the response to the unit impulse, so $y = h * u$: the impulse response is the kernel of the convolution.

## 2. Modeling

- **2.1.1** — Node voltages, one node taken as ground (0 V).
- **2.1.2** — KCL at every non-ground node: currents in equal currents out, each branch current written through the node potentials.
- **2.1.3** — At first only the node potentials; every extra unknown (source currents, and then the states) must arrive with its own equation.
- **2.2** — From the elements: $v = Ri$, $i_C = C\dot{v}_C$, $v_L = L\dot{i}_L$.
- **2.3** — A voltage source fixes a potential but its current is unknown, so it needs its own equation; the new variable is that source current $i_g$.
- **2.4** — Each reactive element brings a new unknown (its state) and supplies its own law, $C\dot{v}_C = i_C$ (or $L\dot{i}_L = v_L$).
- **2.5** — Two unknowns: its voltage (a state) and its current (a branch current, so KCL at both ends mentions it).
- **2.6** — They are the energy variables that cannot jump, and the element laws give the derivative forms we need ($C\dot{v}_C = i_C$, $L\dot{i}_L = v_L$).
- **2.7.1** — Node voltages, one node grounded.
- **2.7.2** — KCL at every non-ground node, currents as $V/R$.
- **2.7.3** — Only the node potentials.
- **2.7.4** — None are needed: every element is already known through $V/R$.
- **2.8** — Whichever route leaves fewest unknowns; state equations only if the states themselves are asked for.
- **2.9** — One state per storage, so position and velocity; signs from the elements, then $x_1 = x$, $x_2 = \dot{x}$.
- **2.10.1** — $S, I, R$ with $N = S + I + R$ fixed: $\dot{S} = -\beta SI$, $\dot{I} = \beta SI - \gamma I$, $\dot{R} = \gamma I$ (two of the three suffice); the disease-free equilibrium is stable iff $R_0 = \beta N/\gamma < 1$.
- **2.10.2** — Model → $\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$ → $\mathbf{A}^k = \mathcal{Z}^{-1}\{z(z\mathbf{I}-\mathbf{A})^{-1}\}$ (or diagonalization, or Cayley–Hamilton) → $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$ plus the forced sum. If the model came out continuous, discretize first: $\mathbf{A}_D = e^{\mathbf{A}_c T}$.
- **2.11.1** — Combine the parallel RC into one impedance, then treat it as a voltage divider between the inductor impedance and that impedance, and read the voltage across the RC impedance — no state equations needed.
- **2.12** — $x_1 = y$, $x_2 = \dot{y}$, $x_3 = \ddot{y}$ — one state per derivative up to $n-1$.
- **2.12.1** — Always possible: solve the ODE for its highest derivative; the state is the variable plus its derivatives up to $n-1$.
- **2.13** — Any invertible $\vec{z} = \mathbf{T}\vec{x}$ is another valid state: the physics is unchanged, only the description.
- **2.14** — The static spring force already carries the weight, so the two cancel; without shifting the origin, $mg$ only moves the equilibrium.
- **2.15** — They are the energy variables that cannot jump (inductor current and capacitor voltage are continuous), and they are exactly what the derivative element laws hand you.
- **2.16** — No storage, no memory: KCL and KVL give a purely algebraic system, so the output follows the input instantly — nothing to remember.

## 3. State equations and the state-transition matrix (continuous time)

- **3.1** — $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ and $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$ — first derivative on the left, no derivatives of the input.
- **3.1.1** — $\mathbf{A}$: how the states drive each other (the dynamics). $\mathbf{B}$: how the inputs enter. $\mathbf{C}$: which combinations of states are observed. $\mathbf{D}$: the direct input-to-output path (often $\mathbf{0}$).
- **3.2** — $\vec{x}(t) = \Phi(t-t_0)\vec{x}(t_0) + \int_{t_0}^{t}\Phi(t-\tau)\mathbf{B}\vec{u}(\tau)\,d\tau$ — homogeneous (from the initial state) plus forced (the input convolved with the impulse response).
- **3.3** — $\Phi(t) = e^{\mathbf{A}t}$, carrying the state from one time to another. Properties: $\Phi(0) = \mathbf{I}$; $\Phi(t_1+t_2) = \Phi(t_1)\Phi(t_2)$ (semigroup — the state is a complete summary of the past); $\Phi^{-1}(t) = \Phi(-t)$, so never singular, even when $\mathbf{A}$ is; $\dot\Phi = \mathbf{A}\Phi = \Phi\mathbf{A}$, both orders. The first three make $\{\Phi(t)\}$ a one-parameter group generated by $\mathbf{A}$.
- **3.4** — Taylor: general and from first principles, but tedious. Diagonalization $\mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}$: fastest when the eigenvectors are easy, dies on a defective $\mathbf{A}$. Cayley–Hamilton $\sum_{k<n}\alpha_k(t)\mathbf{A}^k$: always works — the only option when defective. Laplace $\mathcal{L}^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$: small matrices, repeated poles, and it hands you $G(s)$ too.
- **3.5** — $p(\mathbf{A}) = \mathbf{0}$ kills every power $k \ge n$, so $f(\mathbf{A}) = \sum_{k<n}c_k\mathbf{A}^k$, with the $c_k$ from matching $f$ at the eigenvalues, $r(\lambda_i) = f(\lambda_i)$ — plus derivative conditions when an eigenvalue repeats, which is where $te^{\lambda t}$ comes from. No eigenvectors needed, so it survives a defective $\mathbf{A}$.
- **3.6** — Any $\vec{x}_0$ can be driven to any $\vec{x}_1$ in finite time. Criterion: $\operatorname{rank}[\mathbf{B}\ \mathbf{A}\mathbf{B}\ \cdots\ \mathbf{A}^{n-1}\mathbf{B}] = n$ (full row rank). Depends on $(\mathbf{A},\mathbf{B})$ only, and for LTI it coincides with reachability from the origin because $\Phi$ is always invertible.
- **3.7** — $f(\mathbf{A}) = \sum_{k<n}\alpha_k\mathbf{A}^k$, with the $\alpha_k$ solving $f(\lambda_i) = \sum_k\alpha_k\lambda_i^k$ at every eigenvalue (differentiate when repeated) — the same machinery as $e^{\mathbf{A}t}$, with $f$ in place of the exponential.
- **3.8** — Multiply by $e^{-\mathbf{A}t}$: the left side becomes an exact derivative, $\frac{d}{d\tau}(e^{-\mathbf{A}\tau}\vec{x})$; integrate from $t_0$ to $t$, then multiply back by $e^{\mathbf{A}t}$.
- **3.8.1** — Each slice of input is a kick at $\tau$ that then free-evolves for $t-\tau$, so the kernel depends only on the difference — that is the substitution $u = t-\tau$. With $t_0 \ne 0$ the window becomes $[t-t_0,\,t]$ and the integral stops being a convolution.
- **3.9** — The eigenvalues come free (the determinant is already factored, they are the diagonal entries), but the eigenvectors and $\Phi$ still need work — unlike the diagonal case, where $\Phi$ is entrywise.
- **3.10** — Taylor: most general, no shortcuts, tedious. Diagonalization: elegant, quickest when the eigenvectors are readable, fails when defective. Laplace: good for small matrices and repeated poles, and it hands you $G(s)$. Cayley–Hamilton: no eigenvectors, no matrix inversion, survives everything — the default.
- **3.10.1** — Diagonalization when the eigenvectors are easy; Laplace when the resolvent is small or poles repeat; Cayley–Hamilton when the matrix is defective, has repeated eigenvalues, or is symbolic — and it is the only route that works for a defective $\mathbf{A}$.
- **3.11** — Algebraic multiplicity $m_a$: how many times $\lambda$ roots $\det(\lambda\mathbf{I}-\mathbf{A})$. Geometric $m_g$: the number of independent eigenvectors, $n - \operatorname{rank}(\mathbf{A}-\lambda\mathbf{I})$. Always $1 \le m_g \le m_a$; diagonalizable iff $m_g = m_a$ for every $\lambda$, otherwise defective (and the modes pick up a $t$ factor).

## 4. State equations and the state-transition matrix (discrete time)

- **4.1** — $\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$, $\vec{y}[k] = \mathbf{C}\vec{x}[k] + \mathbf{D}\vec{u}[k]$ — next state on the left; a difference equation, stepped one sample at a time.
- **4.1.1** — Two ways: (1) by hand — step the recursion from $\vec{x}[0]$; (2) with the discrete state-transition matrix — $\vec{x}[k] = \mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1}\mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i]$, again homogeneous plus forced.
- **4.2** — A differential equation is instantaneous (a slope, $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$) and must be solved; a difference equation is already a recursion you can step by hand. Analogues, not identical — only their solutions look alike: both loop over the whole past with the state-transition matrix, an integral versus a sum.
- **4.3** — $k$ counts samples, so the actual time is $kT$, with $T$ the sampling period (dropped from the notation).
- **4.4** — $\mathbf{A}^k$ is the discrete state-transition matrix, $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$. Three ways: $\mathcal{Z}^{-1}\{z(z\mathbf{I}-\mathbf{A})^{-1}\}$, or $\mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}$, or Cayley–Hamilton with $\lambda_i^k$ in place of $e^{\lambda_i t}$.
- **4.5** — $\vec{x}[k] = \mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1}\mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i]$ — the discrete twin of the $\Phi$ solution.
- **4.6** — Model → $\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$ → $\mathbf{A}^k$ via the $z$-transform (split $X(z)/z$, cover-up, then $\frac{z}{z-a} \leftrightarrow a^k$) → $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$, then read the physics off the modes $\lambda_i^k$. Worked end-to-end in appendix B (tank battle).
- **4.7** — Yes, with the boundary moved: $|\lambda_i| < 1$ (strictly inside the unit circle) in place of $\operatorname{Re}\lambda_i < 0$, and the controllability and observability matrices and rank tests unchanged.

## 5. Transfer functions, stability, and the toolbox

- **5.1** — $G(s) = Y(s)/U(s)$ with zero initial conditions — equivalently $\mathcal{L}\{h(t)\}$. From state space: $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$. Don't forget $\vec{x}(0) = \vec{0}$.
- **5.2.1** — Asymptotically stable: all $\operatorname{Re}\lambda_i < 0$ — every mode decays, so the state converges to the equilibrium and the transients die. Marginal: simple poles on the imaginary axis — bounded but not decaying: a sustained oscillation (imaginary pair, phase-portrait centre) or a constant that stays put (pole at the origin). A repeated axis pole grows like $t$ — that is unstable, not marginal.
- **5.2.2** — Strictly in the left half-plane for asymptotic stability; on the axis (simple) is marginal; any in the right half-plane is unstable. Discrete: inside, on, outside the unit circle.
- **5.3** — BIBO: every bounded input gives a uniformly bounded output — for LTI, $\int_0^\infty|h(t)|\,dt < \infty$, i.e. every pole of $G$ strictly in the left half-plane. It is about the input–output map, asymptotic stability about the state, and the latter is the stronger: it implies BIBO. They differ by cancellation — an uncontrollable or unobservable mode cancels out of $G$ and can be unstable while the output stays bounded (the two coincide only for a minimal realization).
- **5.4** — Reconstructing $\vec{x}(t_0)$ from the output over a finite interval, given the known input. Criterion: $\operatorname{rank}\mathcal{O} = n$ with $\mathcal{O} = [\mathbf{C};\mathbf{C}\mathbf{A};\dots;\mathbf{C}\mathbf{A}^{n-1}]$ (full column rank). Depends on $(\mathbf{A},\mathbf{C})$ only; it is the transpose twin of the controllability test.
- **5.5** — Driving any $\vec{x}_0$ to any $\vec{x}_1$ in finite time. Criterion: $\operatorname{rank}\mathcal{C} = n$ with $\mathcal{C} = [\mathbf{B}\ \mathbf{A}\mathbf{B}\ \cdots\ \mathbf{A}^{n-1}\mathbf{B}]$ (full row rank — no determinant in general). Depends on $(\mathbf{A},\mathbf{B})$ only.
- **5.6** — Eigenvalues of $\mathbf{A}$ are the exponents of the modes, $e^{\lambda_i t}$ (with a $t$ factor when $\mathbf{A}$ is defective), and they are the roots of $\det(s\mathbf{I}-\mathbf{A})$, hence the poles of $G$ — equal exactly when the realization is minimal, since an uncontrollable or unobservable mode cancels out of $G$ and stays a mode of the state. Zeros come from the numerator ($\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$ coupling) and weight or block modes rather than create them. That split is why BIBO and asymptotic stability can disagree.
- **5.7** — Laplace-transform $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ and $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$ with $\vec{x}(0) = \vec{0}$: $s\mathbf{X} = \mathbf{A}\mathbf{X} + \mathbf{B}U$, so $\mathbf{X} = (s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}U$ and $\vec{Y} = [\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}]U$. The denominator is $\det(s\mathbf{I}-\mathbf{A})$, so the poles are the eigenvalues of $\mathbf{A}$.
- **5.8** — Poles: where the system rings — the eigenvalues, stability, and which modes appear in $y$. Zeros: where transmission is blocked — they shape and weight the modes, and a zero on the axis kills that frequency. A pole cancelling against a zero means an unreachable or unobservable mode.
- **5.9** — Linearity plus time invariance: $y = h * u$ for every input, so $h$ alone fixes the input–output behaviour ($Y = GU$).
- **5.9.1** — Convolution in time equals multiplication in frequency: $\mathcal{L}\{h * u\} = H(s)U(s)$.
- **5.10** — Cancellation: an uncontrollable or unobservable mode disappears from $G$, so the round trip is not one-to-one (many realizations, one $G$). Also lost: which state is which, the initial state, and the MIMO structure collapses into a matrix of I/O pairs.
- **5.11** — $\vec{x}(t) = \sum_i c_i e^{\lambda_i t}\vec{v}_i$ (discrete: $\lambda_i^k$, with a $k$ factor when defective), with $c_i = (\mathbf{V}^{-1}\vec{x}_0)_i$ — eigenvalues are the modes, eigenvectors the directions they live in, and the initial state only sets the amounts.
- **5.11.1** — Those with $\mathbf{C}\vec{v}_i \ne 0$ (visible) *and* that the input can excite (the $\mathbf{B}$ coupling) — otherwise the mode cancels out of $G$ and never shows up in the output.
- **5.12** — Node (real, same sign: into or away), saddle (real, opposite signs: always unstable), focus (complex pair: spiral in or out), centre (purely imaginary: closed orbits, marginal). The type is selected by the eigenvalues of $\mathbf{A}$ — sign and reality of $\lambda$.
- **5.13** — The poles sit exactly on the boundary, so the response neither decays nor grows; an arbitrarily small parameter change pushes them into one half-plane or the other, flipping the system to asymptotically stable or unstable. Asymptotic stability is robust (the margin is the distance to the axis); marginal sits on the edge.




