# Appendix D: Review questions

Questions for self-study, grouped by topic. Try to answer each one without the notes, then check against the relevant chapter.

## System classification and properties

1. What is the difference between a static and a dynamic system?
2. Define time-invariant and time-varying systems. What does time invariance require physically?
3. What does it mean for a system to be linear?
4. Show why a constant offset breaks linearity.
5. What changes between a deterministic and a stochastic system?
6. What does "homogeneous" mean for the state equation?
7. How would you find out whether a black-box system is static or dynamic without opening it?
8. What is convolution, and how does it connect to the impulse response?

## Modeling

1. When modeling an electrical circuit, what are the potentials, what are the node equations, and what are the unknowns?
2. Why does each voltage source add one equation, and which new variable does it bring into the circuit?
3. Why does each reactive element add an equation, and why does a capacitor's current appear in two node equations?
4. Why are the inductor current and the capacitor voltage the natural state variables, and not the other way round?
5. Why does a purely resistive network have no state?
6. Given a circuit, which route would you take to solve it (node equations, state equations, impedance/divider), and why?
7. How do you get from a mechanical or rotational system to its first-order state equations?
8. Derive the SIR model of a pandemic. How do you get the discrete state-transition matrix at the end?
9. An inductor is in series with a capacitor that has a resistor in parallel. Express the voltage across the resistor in the frequency domain.
10. Turn a third-order ODE into a system of first-order equations. Why is that always possible?
11. Why is the choice of state variables not unique?
12. In the car suspension model, why does $mg$ disappear once $x$ is measured from the static equilibrium?

## Continuous-time State equations

1. Write the general state equation and the output equation, and say what each matrix means.
2. Derive the general solution of the state equation. Why does the convolution integral contain $\Phi(t-\tau)$, and why does its lower limit matter?
3. What is the state-transition matrix $\Phi(t)$, and what properties does it have?
4. Compare the four methods for computing $\Phi$. Which do you use when, and which one is the only option in some cases?
5. What does a triangular $\mathbf{A}$ make easier when computing $\Phi$, and what does it not?
6. What does the Cayley–Hamilton theorem say, and how do you use it to compute an arbitrary function of a matrix?
7. What are the algebraic and geometric multiplicities of an eigenvalue?
8. What does controllability mean? Derive the criterion.

## Discrete-time State equations

1. Write the discrete state equation and its general solution.
2. In what sense are difference and differential equations analogues but not identical?
3. How is the index $k$ in a discrete equation related to time?
4. What is the discrete state-transition matrix $\mathbf{A}^k$, and how do you compute it?
5. Are the equilibrium, stability, controllability and observability criteria the same in discrete time as in continuous time?

## Transfer functions, stability

1. What is a transfer function? Derive $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$, and relate it to the convolution theorem.
2. What is the difference between asymptotic and marginal stability, and where do the eigenvalues have to lie for each?
3. What is bounded-input bounded-output stability, and how does it differ from asymptotic stability?
4. What is observability, and what is the criterion?
5. What are the modes of an LTI system? How do eigenvalues, modes, poles and the transfer function relate, and which modes reach the output?
6. What do the zeros of $G(s)$ tell you?
7. What information is lost when converting a state-space model to a transfer function and back?
8. Sketch the basic phase portraits (focus, node, saddle, centre) and say what determines each type.
9. Why is marginal stability so sensitive to small parameter changes?
