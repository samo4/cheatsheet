---
title: "Signals, Systems and Control"
subtitle: "A plan: representation → evolution → design → implementation"
author: "Samo F."
---

# About this

> **A plan, not a text.** This is a table of contents with intent: seventy-one
> chapters building one continuous argument, from the mathematics of signals to the
> design of systems that behave and the machinery that runs them. Each chapter is
> described by the questions it answers rather than by the material it reviews.
>
> The sequence is one-directional on purpose. Nothing appears before it is needed,
> and nothing is needed before it appears: mathematics first, then uncertainty and
> computation, then signals, then systems, then control, then the machinery, then
> the cases where linearity runs out.
>
> Chapters in bold are the hinges — the few places the whole structure turns on.
> Where a chapter closes a loop with an earlier one, the cross-reference says so.

## The chain

The plan follows one sentence: **modeling → analysis → control → implementation**.
Every chapter sits somewhere on that arrow.

Three objects carry the argument, and each brings its own natural tool:

| Object | Question it answers | Natural tool |
| --- | --- | --- |
| the *signal* | what is in this waveform? | Fourier (representation) |
| the *state* | what does this system do? | Laplace and $z$ (evolution) |
| the *closed loop* | what makes it behave? | $s$-plane geometry, frequency design |

Fourier suits signals of infinite extent with no initial condition: steady state,
power, stationarity. Laplace suits causal evolution *from* an initial condition:
transients, growth, decay. The tool follows the question, not the fashion.

## Two objects carry the whole structure

Everything else is a change of coordinates. Two exceptions are worth naming early,
because they are where one chapter hands over to the next:

- **the impulse response** — a single measurement that fixes the entire input–output
  behaviour of a linear time-invariant system, and the object from which
  convolution, the transfer function and the frequency response are all read.
- **the sampling period** — the one number that turns a continuous system into a
  discrete one, and the pivot from which the discrete transform, the digital filter
  and the digital controller all follow.

## Reading paths

- **Survey (one semester).** 1–6 · 12–19 · 26 · 29–34 · 36–37 · 43–45
- **Signals first.** 1–28, in order
- **Systems and control first.** 1–11, then 29–51
- **Everything.** 1–71, in order

---

# Part I — Mathematical foundations

*Six chapters, each one needed by something later. The last one is the idea the
rest of the plan exploits: every transform here is the same expansion, read on a
different contour.*

### 1. Complex numbers, exponentials, phasors
- complex arithmetic, polar form, Euler's relation
- phasors and the geometry of rotation
- complex exponentials as the building block of everything that follows

### 2. Sequences, series, improper integrals
- limits, convergence, uniform convergence
- power series, Taylor and Maclaurin series
- improper integrals and the conditions under which they exist
- summation formulae used later for discrete-time series

### 3. Linear algebra: vector spaces, matrices, rank, determinant, inverse, linear systems
- vector spaces, linear independence, basis, dimension
- matrix multiplication, determinant, inverse
- rank, consistency, and the solution set of a linear system
- inner products and orthogonality

### 4. Eigenvalues, diagonalization, algebraic vs. geometric multiplicity, Cayley–Hamilton
- the characteristic polynomial, eigenvalues and eigenvectors
- diagonalization and when it fails
- algebraic and geometric multiplicity; defective matrices
- the Cayley–Hamilton theorem, and an arbitrary function of a matrix

### 5. Transforms: Laplace, $z$, Fourier — one table, three contours
- definition, region of convergence, and inverse for each
- the standard pairs and properties, side by side
- partial fractions and how inversion is actually done
- initial- and final-value theorems

### 6. **The eigenfunction view: one transform, three contours**
- a transform is an expansion in the eigenfunctions of a shift-invariant operator
- $e^{st}$ ↔ the mode $\vec{v}_i e^{\lambda_i t}$ ↔ a Fourier coefficient ↔ $z^k$
- Fourier is Laplace evaluated on the imaginary axis; the DFT is the $z$-transform on the unit circle, $z = e^{j\omega T}$
- what each contour buys: $\sigma$ decay, $\omega$ rotation, $|z|$ per-sample decay
- why every later chapter is a change of coordinates within this one picture

---

# Part II — Uncertainty and computation

*Probability, statistics, optimization and numerics: the four things the rest of the
plan leans on and never supplies. The fifth chapter spends them — with a differential
equation and a solver, a model can be run before anything is designed.*

### 7. Probability and random variables
- axioms, conditional probability, independence, Bayes
- random variables; distribution and density; expectation, variance, moments
- the common distributions: uniform, Gaussian, exponential, Poisson, chi-square
- joint, marginal, conditional; correlation and covariance
- functions of random variables; why the Gaussian is closed under addition
- convergence, law of large numbers, central limit theorem

### 8. Statistics and estimation
- samples and estimators: bias, variance, consistency, efficiency
- maximum likelihood, MAP, and least squares as an estimator
- confidence intervals; hypothesis testing; Neyman–Pearson
- spectral estimation: periodogram, Welch, the bias–variance tradeoff
- the Cramér–Rao bound, and why chapter 67 cannot beat it

### 9. Optimization
- unconstrained: gradient, Newton, quasi-Newton, step-size rules
- least squares: normal equations, QR, regularization, recursive least squares
- convexity: sets, functions, duality, KKT conditions
- quadratic programming — the form LQR and MPC are actually written in
- gradient-free methods, and local minima as a fact of identification life

### 10. Numerical computation
- floating point, round-off, catastrophic cancellation
- conditioning and stability; forward vs. backward error
- LU, QR, SVD, Cholesky — when each is the right tool
- computing $e^{\mathbf{A}t}$ and $\mathbf{A}^k$ in practice: Padé, scaling-and-squaring, eigendecomposition pitfalls (links ch. 32, 41)
- the FFT as an algorithm: complexity, real input, leakage (links ch. 28)
- stiffness and the choice of solver

### 11. Simulation of dynamic systems
*What chapters 1–10 are enough to compute: an ODE and a solver. Realizing a modelled
system comes later, once there is a transfer function to realize — the forward
references below say exactly where.*
- what simulation is for: verification, Monte Carlo, virtual commissioning
- from an ODE to an algorithm: the three families — indirect, direct, implicit
- numerical integration: method selection, truncation error, stability, predictor–corrector
- step size, stiffness, and when an implicit method is the only one that survives
- causal vs. acausal modelling, and when each is the right frame
- **forward:** realizing a transfer function as an integrator network (ch. 36), simulating dead time (ch. 39), digital simulation of a sampled model (ch. 41), and reading performance indices off a simulation (ch. 44)

---

# Part III — Signals: how a signal is described

*How a waveform is described, decomposed, measured, and finally turned into
numbers. The last three chapters are the pivot into discrete time.*

### 12. Signals: definitions and classification
- definition of a signal; physical real signals and their properties
- divisions: continuous vs. discrete, deterministic vs. random, energy vs. power
- discrete, quantized, and numeric (digital) signals defined
- what crosses a system boundary: input $u$, output $y$, and the state as an internal signal

### 13. Energy and power signals
- energy and power signals; power and energy of periodic signals
- necessary condition for a signal to be an energy signal
- examples of periodic and random signals of unbounded power

### 14. Representation by basis functions
- why represent at all; how an approximation is built
- criteria for judging the quality of an approximation
- scalar product in the vector space of energy signals on a finite interval
- optimality conditions under the mean-square-error criterion
- existence of a solution, and the procedure for finding the parameters
- orthogonality and orthonormality; why orthogonal bases are chosen
- completeness of a basis sequence; examples of basis functions

### 15. Harmonic analysis of periodic signals
- expressing a signal in basis functions; complex Fourier series
- Dirichlet conditions; real Fourier series; the relation between the two
- complex spectrum; real, imaginary, amplitude and phase spectra
- properties of the spectra of real periodic signals
- physical interpretation; what amplitude and phase spectra each tell you

### 16. Autocorrelation and power spectrum of periodic signals
- correlation of periodic signals; autocorrelation — definition, properties
- the map from a periodic signal to its autocorrelation
- power spectrum of periodic signals
- Parseval's equation — statement, properties

### 17. Cross-correlation and convolution of periodic signals
- cross-correlation of periodic signals
- convolution of periodic signals — definition, properties
- the relation between correlation and convolution, periodic case
- the periodic delta function

### 18. Fourier transform of aperiodic signals
- effect of lengthening the period on the spectrum; the Fourier integral
- physical interpretation of the Fourier-integral representation
- Fourier transform and inverse transform; Dirichlet conditions
- generalized Fourier transform; complex spectrum of aperiodic signals
- real, imaginary, amplitude and phase spectra, and what they mean
- properties of the spectra of real aperiodic signals
- properties of the Fourier transform
- Fourier transform of periodic signals
- signals invariant under the Fourier transform

### 19. The delta function
- explicit and implicit definitions; the sifting property
- $\mathcal{L}\{\delta\} = 1$; $\delta$ as the expansion of a flat spectrum
- (the core of everything): the impulse as the elementary test

### 20. Correlation and convolution of aperiodic signals
- autocorrelation — definition, properties; the signal → autocorrelation map
- energy spectrum of aperiodic signals; Parseval's equation
- cross-correlation — definition, properties
- cross-correlation as a measure of similarity; relation between distance and correlation
- convolution — definition, properties; correlation ↔ convolution

### 21. Windowing
- effect of windowing on the spectrum
- desirable characteristics of window functions

### 22. Random signals
- definition of a random signal; generalizations in random-signal processing
- phase space of a random signal; deterministic characteristics
- stationarity of the source that emits the random signal
- can a stationary random source emit an energy signal?
- autocorrelation of stationary random signals

### 23. Statistical description of random processes
- sample mean; expressing the sample mean via expectation
- correlation and covariance
- strict stationarity vs. wide-sense stationarity
- time average; equality of sample and time averages (ergodicity)
- autocorrelation via time and via ensemble average
- the Poisson random process; examples of stationary random signals

### 24. LTI systems and random inputs
*A random input, a linear system, and the two correlations that connect them.*
- definition of a linear stationary system; what the impulse response is and its properties
- output autocorrelation and input–output cross-correlation in terms of the excitation and $h$
- determining $h$ and the transfer function when the input is a random signal from a stationary source
- models for computing the autocorrelation of common stationary random signals
- spectral characterization: $S_y(\omega) = |H(\omega)|^2 S_u(\omega)$ — the target of the whole block

### 25. Comparing signal classes, and detection
- comparison of processing procedures and properties across signal groups
- describing spectral characteristics; common and differing properties of autocorrelation
- detecting and locating a periodic component against a noise background
- the autocorrelation procedure; the cross-correlation procedure; choosing between them
- pitch detection in speech

### 26. Sampling
- definition of sampling; Shannon's sampling theorem
- sampling at different rates and its consequences; aliasing
- frequency limitation and time limitation of a signal
- **handoff:** the validity condition for $\mathbf{A}_D = e^{\mathbf{A}_cT}$ in chapter 41

### 27. Quantization
- definition of quantization; the quantization error
- time-domain properties of the quantization-error signal
- estimate of the mean power of the error in terms of $q$
- spectrum of the quantization error
- signal-to-quantization-noise ratio: assumptions and dependence on $q$

### 28. The discrete Fourier transform
- what procedure the DFT is; DFT vs. FFT
- definition and properties of the DFT
- the DFT and linear stationary systems
- relation between the FT and the DFT; quality of the DFT approximation to the FT

---

# Part IV — Systems: how a system is described

*What a system is, what it remembers, and how it evolves — in the time domain, in
the complex plane, and in discrete steps. This is the analysis half of the chain.*

### 29. Classification and properties of systems
- static vs. dynamic, lumped vs. distributed, continuous vs. discrete, deterministic vs. stochastic, homogeneous vs. non-homogeneous
- linearity (additivity + homogeneity) and time invariance, with the counter-examples
- the LTI class and what it leaves out

### 30. Modeling
- higher-order ODEs as first-order systems
- the energy perspective: one state per independent storage
- translational, rotational, and electrical systems; node and state equations
- mechanical/electrical analogy; electrical-element laws as the source of the extra equations

### 31. State variables and state equations
- $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$
- meaning of each matrix; non-uniqueness of the state
- properties of $\Phi$: $\Phi(0)=\mathbf{I}$, semigroup, invertibility, $\dot\Phi = \mathbf{A}\Phi = \Phi\mathbf{A}$

### 32. Solving the continuous state equation
- homogeneous solution; non-homogeneous solution and the convolution integral
- $\Phi$ via Taylor series; via Laplace ($\mathcal{L}^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$); via diagonalization; via Cayley–Hamilton
- algebraic vs. geometric multiplicity; defective matrices; choosing between the four methods

### 33. Modes, equilibria and phase portraits
- modes of an LTI system and their relation to eigenvalues
- equilibrium states; focus, node, saddle, centre, and what selects each
- which modes reach the output

### 34. Stability
- asymptotic, marginal, unstable; where the eigenvalues must lie
- sensitivity of marginal stability to small parameter changes
- bounded-input bounded-output stability and how it differs from asymptotic stability
- discrete twin: inside / on / outside the unit circle

### 35. Controllability, observability, realization
- controllability: meaning, criterion, dependence on $(\mathbf{A},\mathbf{B})$ only
- observability: meaning, criterion, dependence on $(\mathbf{A},\mathbf{C})$ only
- minimal realization, uncontrollable/unobservable mode cancellation, Kalman decomposition
- why this is the feasibility condition for chapter 49 — the design boundary

### 36. Transfer functions
- scalar transfer function from the ODE
- impulse response and convolution; $h(t) = \mathbf{C}\Phi(t)\mathbf{B} + \mathbf{D}\delta(t)$
- $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$; poles are the eigenvalues
- block diagrams; feedback; moving summing junctions and pickoff points
- realization: from a transfer function to an integrator network — nested, canonical, partial-fraction and cascade forms (the counterpart of ch. 11)
- conversion to and from state space; what is lost in each direction

### 37. **Frequency response**
*The hinge. Everything before it was time domain or the full complex plane;
everything after it is design. From here, $G(s)$ and $H(\omega)$ are one object.*
- $G(j\omega) = G(s)\big|_{s=j\omega}$, and $G(j\omega) = \mathcal{F}\{h\}$
- Bode magnitude and phase plots, asymptotes, corner frequencies
- polar plot and the Nyquist contour; resonance peak, bandwidth, damping from the plot
- minimum-phase and all-pass systems; non-minimum-phase zeros and what they do to the response
- analog filter prototypes: Butterworth, Chebyshev, Bessel — the systematic version of "design a magnitude shape"
- from prototype to circuit: Sallen–Key and active RC realization (links ch. 57)
- **payoff:** Bode, bandwidth and resonance become available to control design (ch. 45)

### 38. Closed-loop algebra
- $G_r(s) = \dfrac{G(s)}{1 + G(s)H(s)}$
- characteristic equation; closed-loop poles
- disturbance and measurement-noise transfer functions
- sensitivity $S$ and complementary sensitivity $T$, $S + T = 1$; why they cannot both be small

### 39. System type and steady-state behaviour
- proportional (type 0), integral (type 1, 2, …), derivative systems
- first- and second-factor gain forms; $K_{ss}$ vs. $k$
- first-order $\dfrac{k}{\tau s + 1}$ and second-order $\dfrac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$ step responses
- overdamped, critically damped, underdamped, undamped
- dead-time systems $G(s) = e^{-sT}$
- simulating dead time: Padé approximants and delay-free substitutes (the counterpart of ch. 11)

### 40. Linearization
- single-variable and multivariable Taylor expansion
- linearizing state-space systems around an equilibrium
- two worked models: Lotka–Volterra, SIR
- what linearization erases: multiple equilibria, hysteresis, saturation, chaos

### 41. Discrete systems
- difference equations; index $k$ and time $kT$
- $z$-transform: shifts become powers, convolution becomes multiplication
- higher-order difference equations as first-order systems
- discretizing continuous systems: Euler, integral approximation, zero-order hold, $\mathbf{A}_D = e^{\mathbf{A}_cT}$
- solving the discrete state equations; $\mathbf{A}^k$ via $z$-transform, diagonalization, Cayley–Hamilton
- discrete transfer function; discrete equilibrium, stability, controllability, observability

### 42. **Discrete frequency response and digital filter design**
- $z = e^{j\omega T}$; the unit circle as the discrete frequency axis
- aliasing revisited from the systems side (links ch. 26)
- bilinear transform and pre-warping; comparing discretization methods in the frequency domain
- mapping the $s$-plane strip to the unit circle; what a sampled pole becomes
- DFT of a state sequence; the DFT as $H(z)$ evaluated on the unit circle (links ch. 28)
- **filter design:** from the analog prototype (ch. 37) through the bilinear transform to a working $H(z)$
- FIR design: windowing (links ch. 21), frequency sampling, linear phase
- IIR design: impulse invariance vs. bilinear — why one aliases and the other warps
- multirate: decimation, interpolation, polyphase, the half-band filter

---

# Part V — Control: how a system is made to behave

*Design in the frequency domain first, because that is where the intuition lives;
then in state space, where it generalizes. This is where the chain stops describing
and starts prescribing.*

### 43. The control problem
- open vs. closed loop; tracking vs. regulation
- block structure of a feedback loop; where disturbances enter
- feedback's four effects: sensitivity reduction, disturbance rejection, time-constant reduction, and the price paid

### 44. Performance specifications
- dead time $T_d$, rise time $T_r$, settling time $T_s$, overshoot $M_p$, steady-state error $e_{ss}$
- their dependence on dominant-pole location (the circle, the vertical line, the angle)
- steady-state error for step/ramp/parabolic references; error constants by system type
- bandwidth and the speed–noise–robustness tradeoff; what specs cannot all be met at once

### 45. **Classical design in the frequency domain**
*The design counterpart of chapter 37: margins, loci and compensators.*
- gain and phase margin as design numbers, read off the Bode plot
- the Nyquist stability criterion and how it handles dead time
- root locus: rules, sketching, and the effect of adding poles and zeros
- lead, lag and lead-lag compensators; when each is the right instrument
- design to specification on Bode, and the design-to-root-locus equivalence

### 46. PID control
- ideal and real (filtered) PID forms
- effect of each term on $T_r$, $M_p$, $T_s$, $e_{ss}$ and stability
- Ziegler–Nichols: step-response method and ultimate-gain method; Chien–Hrones–Reswick
- rules of thumb ($T_i = \tau$ cancels the dominant lag)
- implementation: derivative filtering and sensor noise, anti-windup, actuator saturation, bumpless transfer

### 47. Closed-loop stability and robustness
- BIBO stability of the closed loop; Routh–Hurwitz
- gain margin as sensitivity reduction to process-gain changes
- independence of stability from the reference signal
- caveats that break the conclusions: non-unity feedback, disturbances, nonlinearity, actuator limits
- robustness margins revisited as $|S|$ and $|T|$ bounds

### 48. Feedforward and disturbance observers
- feedforward from a measured disturbance, and why it wins whenever the disturbance is available early
- two-degree-of-freedom structure: reference shaping separated from disturbance rejection
- disturbance observers, and the equivalent-input-disturbance view
- the price of feedforward: a model, a sensor, and no guarantee once the model is wrong
- how this reappears as cascade, ratio and selective control in process loops (ch. 60)

### 49. **State feedback**
*The step from one loop to a design that places every mode.*
- pole placement by state feedback; the characteristic polynomial as a design target
- controllability as the necessary and sufficient feasibility condition (links ch. 35)
- feedforward gain for reference tracking
- LQR: the quadratic cost, the Riccati equation, and the weight matrices
- comparison with PID: what is gained beyond one loop

### 50. **Observers and estimation**
*What to do when the state cannot be measured — the payoff for chapters 22–24.*
- observability as the feasibility condition for reconstruction (links ch. 35)
- the Luenberger observer; observer poles and convergence rate
- the separation principle: design the controller and the observer independently
- the Kalman filter as the stochastic observer
- the LQG structure: LQR + Kalman

### 51. **Digital control**
- the sampler and zero-order hold inside the loop; where the delay comes from
- discretizing a continuous controller vs. designing in the $z$-domain
- discrete design by pole placement; deadbeat control
- computational delay and its effect on achievable bandwidth (links ch. 26, 42)

---

# Part VI — Measurement and implementation

*Where the loop meets the world: what can be measured, what can be computed in
time, and what has to be safe before any of it is allowed to run.*

### 52. Measurement and instrumentation
- the measurement chain: sensor → conditioning → anti-alias filter → ADC
- quantization revisited as a measurement error (links ch. 27)
- outliers and statistical control; Type A and Type B uncertainties
- combining uncertainties; expressing a result; error vs. accuracy
- choosing sampling rate and resolution from the requirement, not the datasheet
- basics of electrotechnics; SI units and prefixes

### 53. Embedded and real-time control
- the control loop as a task: period, jitter, deadline, worst-case execution time
- fixed-point arithmetic: scaling, overflow, and quantization on the *controller* side
- interrupt latency; sensor buses (I²C, SPI, CAN); actuator PWM
- code generation from models: block diagram to C
- case study: a digital current loop

### 54. Sequential and logic control
- boolean algebra, combinational and sequential logic, state machines
- PLC programming: ladder, function block, structured text
- SFC/Grafcet: steps, transitions, actions
- interlocks, permissives, mode management, and the safe state
- the interface between continuous loops and sequencing: enable, bypass, cascade

### 55. Safety, reliability and fault diagnosis
- failure modes, FMEA, redundancy, common-cause failure
- functional safety: IEC 61508/61511, SIL, safe failure fraction
- watchdogs, voting, fail-safe vs. fail-operational architectures
- model-based fault detection: observers as residual generators (links ch. 50)
- condition monitoring, maintenance, and the cost of the loop being wrong

---

# Part VII — The physical plant

*What the models were made of. Until now $R$, $C$, $L$, $m$, $k$, $b$ were given;
these chapters are where they come from, how they are driven, what limits them, and
what the loop actually pushes against.*

### 56. Circuit theory and network analysis
- elements, KCL/KVL, node and mesh analysis — the derivation chapter 30 skips
- phasors, impedance, and the transfer functions of RLC networks
- two-ports, loading, Thevenin/Norton, source transformation
- transient response of first- and second-order circuits: the same mathematics as chapter 39
- dependent sources, and where feedback actually comes from

### 57. Electronics and feedback amplifiers
- devices as switches and amplifiers: diode, BJT, MOSFET
- operational amplifiers: ideal, real, bandwidth and slew limits
- negative feedback in amplifiers: gain desensitization, bandwidth extension, distortion reduction — chapter 47 applied
- active filters: realizing the chapter-37 prototypes
- comparators, PWM generation, H-bridges, gate drivers
- circuit noise: thermal, shot, flicker (links ch. 22)

### 58. Electromechanical energy conversion and drives
- magnetic circuits, reluctance, inductance, saturation
- core losses: hysteresis and eddy currents; AC magnetics
- DC machines: the model, back-EMF, torque constant — a two-state plant for chapter 30
- induction and permanent-magnet synchronous machines: the field-oriented picture
- drives: converter topologies, PWM, and the current–velocity–position cascade; encoders
- thermal limits and the torque–speed envelope

### 59. Sensors and actuators
- physical principles: resistive, capacitive, inductive, piezoelectric, optical, Hall
- sensor dynamics: bandwidth, delay, nonlinearity, hysteresis, drift, cross-sensitivity
- position, velocity, force, temperature, pressure, flow; encoders and resolvers
- actuators: motors, solenoids, valves, piezo, hydraulics, pneumatics
- choosing a sensor: resolution vs. noise vs. bandwidth vs. cost
- mounting, cabling, grounding, EMI — where good models go to die

### 60. Process dynamics and process control
- process characteristics: gain, dead time, time constants, inverse response, integrators
- loop tuning as practised: open-loop and closed-loop methods (links ch. 46)
- dead-time compensation: the Smith predictor and why it is fragile
- cascade, ratio, feedforward, split-range, override and selective control
- multivariable interaction: RGA, decoupling (links ch. 35, 66)
- batch and recipe control; the DCS and historian world

---

# Part VIII — Beyond linear

*Where the linear guarantees run out. Each chapter either turns a "for LTI" statement
into a "for a class" statement, or replaces the guarantee with a weaker but honest one.*

### 61. Lyapunov stability and nonlinear systems
- the gap: eigenvalue stability is linear, linearization is local (links ch. 34, 40)
- equilibria of nonlinear systems; invariant sets
- Lyapunov's direct method; positive definite functions; LaSalle's invariance principle
- the region of attraction, and how to estimate it
- passivity, and why energy is a stability certificate
- input–output stability and the small-gain theorem (the bridge to ch. 66)

### 62. Nonlinear control design
- feedback linearization: input–output and full-state, and when it fails
- sliding mode: the sliding surface, the reaching law, chattering and its mitigation
- backstepping; Lyapunov-based design
- describing functions, limit cycles, harmonic balance
- gain scheduling as the pragmatic version of all of the above

### 63. System identification
- the gap: chapter 24 estimates an impulse response from a random input; this is the discipline
- experiment design: PRBS, chirps, persistent excitation, SNR
- nonparametric: impulse and step response, correlation, spectral analysis
- parametric: ARX, ARMAX, OE, BJ; prediction-error and least-squares
- subspace methods, and state-space identification
- validation: residual analysis, cross-validation, bias vs. variance, model-structure choice
- grey-box: physical structure with identified parameters

### 64. Optimal control
- the cost, the constraint, and what "optimal" is allowed to mean
- calculus of variations and the Euler–Lagrange equation
- Pontryagin's maximum principle; the Hamiltonian; bang–bang and singular arcs
- dynamic programming and the Hamilton–Jacobi–Bellman equation
- LQR as the LTI special case (links ch. 49)
- computational optimal control: direct collocation and shooting

### 65. Model predictive control
- receding horizon: predict, optimize, apply the first move
- the QP formulation; constraints are the entire point
- feasibility, recursive feasibility, stability via terminal cost and terminal set
- tuning: horizons, weights, move blocking, computational budget
- linear vs. nonlinear MPC; explicit MPC
- why MPC became the industrial default

### 66. Robust control
- why nominal design is insufficient: uncertainty, unmodelled dynamics, dead time
- uncertainty models: additive, multiplicative, structured; singular values
- the small-gain theorem, and μ for structured uncertainty
- H∞ design: shaping $S$ and $T$ with weights (links ch. 38)
- loop shaping, and how it relates to lead/lag (ch. 45)
- the price: conservatism, controller order, and what robustness does not fix

### 67. State estimation beyond Kalman
- the general problem, and the Bayes filter as its root form
- the Kalman filter recap, and the linear-Gaussian assumption it cannot escape
- extended and unscented: linearize the model vs. propagate the distribution
- particle filters and Monte Carlo; the curse of dimensionality
- consistency, observability, divergence; tuning $Q$ and $R$
- joint state–parameter estimation; SLAM as the canonical example

### 68. Adaptive and learning-based control
- why adapt: parameters drift, plants change, models are wrong
- model reference adaptive control; self-tuning regulators
- recursive identification inside the loop (links ch. 9, 63)
- iterative learning control for repeating tasks
- reinforcement learning for control: policy gradient, actor–critic, and the safety problem
- data-driven and learning-enabled control: where the guarantees go

---

# Part IX — Discrete event and hybrid

*Not every system is described by a derivative. This is the half of the subject that
runs on sequences, modes and events — and it is what makes an automated plant more
than a collection of loops.*

### 69. Discrete-event systems
- the other automation: state, event, sequence — not a state *vector*
- languages and automata; regular languages; statecharts
- Petri nets: places, transitions, concurrency, reachability
- supervisory control: event controllability and observability; safety as a language property
- deadlock, livelock, and liveness analysis
- scheduling as optimization: job shop, resource allocation (links ch. 9)

### 70. Hybrid systems and mode logic
- continuous dynamics with discrete switching: the general model
- switched systems and switched stability; dwell time
- hybrid automata; Zeno behaviour
- mode management in practice: start-up, shutdown, fault modes, bumpless transfer (links ch. 54)
- verification: reachability for hybrid systems, and its limits

### 71. Discrete-event simulation and scheduling
- the event calendar: next-event time advance, random streams, reproducibility
- queueing: Little's law, M/M/1, and the packet-queue example from chapter 29 revisited
- throughput, utilization, bottleneck analysis
- batch and production scheduling, and its coupling back to control
- where the chain ends: modeling → analysis → control → implementation → *learning*

---

# Appendices

## A. The mastery tests

### Analytical

1. From a physical system, write the state equations by hand (ch. 30).
2. From $(\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D})$, produce $h(t)$, $G(s)$, $G(j\omega)$,
   $h[k]$, $\mathbf{A}^k$, the stability verdict and the controllability/observability
   verdict — without tables (ch. 32–36, 41).
3. From a waveform, get its Fourier series or transform, its energy or power, its
   autocorrelation, and the output spectrum through a given $H$ (ch. 15–24).
4. From specifications, design a compensator and justify it (ch. 44–49).
5. For any pair among the six coordinate systems — time, $\omega$, $s$, state, $z$,
   stochastic — state how to move to any other, and what is lost in the move (ch. 6).

### Engineering

6. From a measurement, state the uncertainty budget and justify the sampling rate
   and resolution you chose (ch. 26, 27, 52).
7. From a plant and an experiment you designed, identify a model and validate it (ch. 63).
8. From a nonlinear plant, prove or disprove a stability claim, then design the
   controller (ch. 61, 62).
9. From sequencing requirements, write safe interlock and mode logic, and simulate
   it (ch. 54, 69, 71).
10. From a specification with constraints and uncertainty, choose among PID,
    lead/lag, LQR, MPC and H∞, and defend the choice (ch. 45–49, 65, 66).

## B. Notation and conventions

The three subjects this plan spans are taught with different habits. These are the
rulings, fixed once so that no chapter has to re-define anything.

| Object | Symbol | Ruling |
| --- | --- | --- |
| Input signal | $u(t)$ | **never** the unit step |
| Unit step | $1(t)$ | keeps $u(t)$ free for the input; $\mathcal{L}\{1(t)\} = 1/s$ |
| Unit impulse | $\delta(t)$, $\delta[k]$ | Kronecker form in discrete time |
| State | $\vec{x}(t)$ | always a vector arrow; $\mathbf{x}$ only where a bare symbol is needed |
| Generic signal | $f(t)$, $g(t)$ | $x$ is reserved for state; a chapter that needs a signal called $x$ says so |
| Impulse response | $h(t)$, $h[k]$ | |
| Transfer function | $G(s)$ | |
| Frequency response | $G(j\omega) \equiv H(\omega)$ | one object, two notations — the whole point of chapter 37 |
| Eigenvalues | $\lambda_i$; $z_i = e^{\lambda_i T}$ | |
| Damping and frequency | $\zeta$, $\omega_n$ | |
| Autocorrelation | $R_{xx}(\tau)$, $R_{xx}[m]$ | ensemble or time average — stated per use |
| Power spectral density | $S_{xx}(\omega)$ | two-sided unless marked; state it every time |
| Quantization step | $q$; error $e_q$ | |
| Transforms | $\mathcal{L}$, $\mathcal{F}$, $\mathcal{Z}$, $\mathcal{D}$ | |
| Complex frequency | $s = \sigma + j\omega$; $z = e^{sT}$ | |
| Time base | $t_0 = 0$ | the clock starts with the experiment; zero initial state for $G(s)$ |
| Angles and units | rad/s for $\omega$, Hz for $f$, $T$ in seconds | SI everywhere, one exception noted per chapter |

## C. Worked examples and essays

Short, non-derivational pieces that sit beside the chapter they illuminate, in the
register already used by the drum, the packet queue and the thermal-noise examples.

| Essay | Beside |
| --- | --- |
| the drum and the plucked string — a system with infinitely many states | ch. 29 |
| thermal noise in an RC network — LTI dynamics, random input | ch. 24 |
| a packet queue — a state that jumps instead of flowing | ch. 29, 71 |
| eigenvectors in the wild — exchange spreads, cointegration, correlation spectra | ch. 4, 33 |
| a battle model — linearization, and the limits of the average | ch. 40 |

## F. What is deliberately out of scope

The rule that keeps this a spine rather than a degree: a topic belongs here if it
changes the **coordinate system** or the **guarantee**; it belongs elsewhere if it
changes the **hardware** or the **application**. Everything below fails that test,
which is exactly why the plan stays readable by an electrical, mechanical, aerospace
and process engineer alike.

| Adjacent subject | Why it is not in the spine |
| --- | --- |
| Communications | the natural consumer of Part III: modulation, matched filtering, information theory |
| Signal processing as a specialty | filter banks, multirate systems, adaptive filters, speech, images |
| Power systems and machines | generation, transmission, protection, grid stability — its own habits |
| Electromagnetic fields | the physics under chapter 58; needed for antennas and EMC, not for the loop |
| Computer science | programming, data structures, operating systems, networks — assumed, never taught |
| Machine learning | estimation and optimization at scale; overlaps ch. 8, 9, 68 but is its own discipline |
| Engineering practice | economics, standards, project management, ethics, human factors |
