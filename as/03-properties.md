# Properties of systems

## Modes of an LTI system

The shape of the (free) response of an LTI system is set by the eigenvalues of $\mathbf{A}$. From the homogeneous solution, $\vec{x}(t) = e^{\mathbf{A}t}\vec{x}_0$, and diagonalizing gives $e^{\mathbf{A}t} = \mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}$, so the response is a linear combination of the exponentials

$$
e^{\lambda_1 t},\; e^{\lambda_2 t},\; \dots,\; e^{\lambda_n t}
$$

each a **mode** of the system, so the eigenvalues of $\mathbf{A}$ are the modes of the response. A real $\lambda$ gives a growing or decaying exponential; a conjugate pair $\sigma \pm j\omega$ gives an oscillation with envelope $e^{\sigma t}$.

The exception is a defective $\mathbf{A}$: with fewer independent eigenvectors than eigenvalues, a repeated eigenvalue brings a factor $t$ instead of a second independent exponential, so $n$ eigenvalues need not give $n$ modes.

These eigenvalues are also the **poles** of the transfer function $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$ (which we get to properly in the transfer-function chapter): its denominator is $\det(s\mathbf{I}-\mathbf{A})$, so the poles are exactly the eigenvalues of $\mathbf{A}$ — at least for a minimal realization (controllable and observable, both defined below). An eigenvalue belonging to an uncontrollable or unobservable mode cancels out of $G(s)$ and is not a pole.

Everything that follows is decided by these modes and by how the inputs and outputs couple to them: the equilibrium behaviour and stability first, then controllability and observability.

## Equilibrium states and phase portraits

An **equilibrium state** $\vec{x}_e$ is where the system stays put, $\dot{\vec{x}} = \vec{0}$ at $\vec{x} = \vec{x}_e$. For the linear system $\dot{\vec{x}} = \mathbf{A}\vec{x}$ the equilibria solve $\mathbf{A}\vec{x}_e = \vec{0}$: the origin $\vec{x}_e = \vec{0}$ when $\mathbf{A}$ is nonsingular, or a whole subspace of equilibria when $\mathbf{A}$ is singular. (With a constant input, $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ has equilibria where $\mathbf{A}\vec{x}_e + \mathbf{B}\vec{u} = \vec{0}$.)

The **phase portrait** — trajectories plotted together in state space — shows how the state moves and whether it reaches the equilibrium. Near an equilibrium the behaviour is set by the eigenvalues of $\mathbf{A}$, i.e. the modes from the beginning of this chapter:

- **Node** — real eigenvalues of the same sign: the state moves straight along the eigenvectors, into (both negative) or away from (both positive) the equilibrium.
- **Saddle** — real eigenvalues of opposite signs: it approaches along one eigenvector and escapes along the other — always unstable.
- **Focus** (spiral) — complex pair $\sigma \pm j\omega$: it spirals into the equilibrium for $\sigma < 0$, away for $\sigma > 0$.
- **Center** — purely imaginary $\pm j\omega$: closed elliptical orbits; it neither settles nor escapes.

For the example system of the State-space chapter, $\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x}$ (eigenvalues $-1 \pm j\sqrt{2}$), the origin is the only equilibrium and a stable focus — every trajectory spirals into it:

```{=latex}
\input{tikz/phase-portrait-focus.tex}
```

The same response, read one state at a time, is two decaying sinusoids — the spiral is those two oscillations stitched together. The real part of the eigenvalues sets the decay, the imaginary part the oscillation:

```{=latex}
\input{tikz/state-components.tex}
```

Whether trajectories actually end up at the equilibrium is exactly what the next section, Stability, formalizes.

## Stability

For $\dot{\vec{x}} = \mathbf{A}\vec{x}$ stability is decided by the eigenvalues of $\mathbf{A}$ — the poles — i.e. by where they sit relative to the imaginary axis. All plots below use the family $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -3 & a \end{bmatrix}$, whose poles are $\lambda = \frac{a \pm j\sqrt{12-a^2}}{2}$ — complex while $a^2 < 12$, real beyond that; the grey half-plane is the stable region, the dashed line its boundary:

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\begin{array}{lcl}
\operatorname{Re}\lambda_i < 0 \ \ \forall i & \iff & \text{asymptotically stable} \\[3pt]
\operatorname{Re}\lambda_i \le 0, \ \text{imaginary-axis eigenvalues simple} & \iff & \text{marginal (stable)} \\[3pt]
\text{otherwise} & \iff & \text{unstable}
\end{array}
$}
\endgroup
\]
```

### Asymptotically stable

$\operatorname{Re}\lambda_i < 0$ for all $i$: every mode decays, so from any initial condition the trajectory converges to the equilibrium $\vec{x}_e = \vec{0}$. All poles lie strictly inside the shaded left half-plane:

```{=latex}
\input{tikz/stability-asymptotic.tex}
```

### Stable (marginal / Lyapunov)

No eigenvalue with $\operatorname{Re}\lambda_i > 0$, and the eigenvalues on the imaginary axis are simple. Trajectories stay bounded (e.g. the center of the previous section — closed orbits) but need not converge. The poles sit exactly on the dashed boundary:

```{=latex}
\input{tikz/stability-marginal.tex}
```

### Unstable

Some eigenvalue with $\operatorname{Re}\lambda_i > 0$, or a repeated eigenvalue on the imaginary axis (which brings a factor $t$ and grows). Trajectories diverge; the poles lie in the right half-plane, outside the stable region:

```{=latex}
\input{tikz/stability-unstable.tex}
```

### What if the parameters change just a little?

The eigenvalues depend continuously on the entries of $\mathbf{A}$, so a small change moves each pole a little. The red circles below are the regions the poles can wander into under a small perturbation — a circle that stays inside the shaded half-plane means the stability is robust, one that straddles the dashed boundary means it is not:

```{=latex}
\input{tikz/stability-perturbation.tex}
```

- **Asymptotic stability is robust**: the circles stay entirely inside the shaded left half-plane, so small perturbations keep the poles there (the margin is the distance from the boundary).
- **Marginal stability is not**: the circles straddle the dashed boundary, so a tiny change (here, $a$ crossing $0$) pushes the poles into one half-plane or the other — the system becomes asymptotically stable or unstable.
- **Instability is robust**: the circles stay in the right half-plane — pushing a pole back across the axis takes a finite change.

### Bounded-input bounded-output stability

The three classes above are about the state. A different question is whether a bounded input can ever produce an unbounded output — **BIBO stability** — and it is answered by the poles of the transfer function rather than by the eigenvalues: every pole of $G(s)$ must lie in the left half-plane.

For a minimal realization the poles are the eigenvalues, so BIBO stability and asymptotic stability coincide. They part company when a pole cancels against a zero. Take

$$
\mathbf{A} = \begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix}, \qquad
\mathbf{B} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \qquad
\mathbf{C} = \begin{bmatrix} 0 & 1 \end{bmatrix}, \qquad
\mathbf{D} = 0,
$$

for which $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} = \frac{1}{s+2}$: BIBO stable, since the only pole sits at $s = -2$. The state, however, runs away from $\vec{x}_0 = \tvec{1,0}$ — the eigenvalue $+1$ is a mode that no input can excite and no output reveals.

BIBO stability is a statement about the input–output map, asymptotic stability about the state, and the second is the stronger of the two. This example is why the modes above come with a minimality caveat, and the next two sections say exactly when a mode escapes through the input or the output.

## Controllability

A system $(\mathbf{A}, \mathbf{B})$ is **controllable** if, for any initial state $\vec{x}_0$ and any target state $\vec{x}_1$, there exists an input $\vec{u}(t)$ that drives the state from $\vec{x}_0$ to $\vec{x}_1$ in finite time — the input can steer the state anywhere in state space.

Controllability is a practical requirement, not just a theoretical one. Take a car with no throttle: you might get it to drift to a position, but you can never place it where you want. The input reaches the state only through $\mathbf{B}$, and with no throttle that path is missing, so no input moves the state; how much that hurts depends on the output matrices, since the engine rpm can do as it likes while you try to park.

The *controllability matrix* collects the columns that matter:

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{C} = n \iff \text{controllable}
$}
\endgroup
\]
```

Take the state response with $\vec{x}(0) = \vec{0}$; reaching $\vec{x}(t)$ at time $t$ requires

$$
\vec{x}(t) = \int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\vec{u}(\tau)\, d\tau
$$

(for LTI, reachability from the origin is the same as controllability, since $e^{\mathbf{A}t}$ is always invertible). By Cayley–Hamilton, $e^{\mathbf{A}s}$ is a polynomial in $\mathbf{A}$ of degree at most $n-1$:

$$
e^{\mathbf{A}s} = \sum_{k=0}^{n-1}\alpha_k(s)\mathbf{A}^k
$$

Substituting and pulling $\mathbf{A}^k\mathbf{B}$ out of the integral,

$$
\vec{x}(t) = \sum_{k=0}^{n-1} \mathbf{A}^k\mathbf{B} \underbrace{\int_0^t \alpha_k(t-\tau)\vec{u}(\tau)\, d\tau}_{\vec{w}_k}
= \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}\vec{w}
$$

Cayley–Hamilton alone gives the easy direction: reachable states lie in the column space of $\mathcal{C}$.\footnote{The converse — that full column rank really makes every state reachable — needs an explicit input. The controllability Gramian $\mathbf{W}_c(t) = \int_0^t e^{\mathbf{A}\tau}\mathbf{B}\mathbf{B}^T e^{\mathbf{A}^T\tau}\,d\tau$ provides one: it is nonsingular exactly when $\operatorname{rank}\mathcal{C} = n$, and $\vec{u}(\tau) = \mathbf{B}^T e^{\mathbf{A}^T(t-\tau)}\mathbf{W}_c^{-1}(t)\,\vec{x}_1$ drives $\vec{0} \to \vec{x}_1$ in exactly time $t$.}

Controllability therefore involves only $(\mathbf{A}, \mathbf{B})$: the output matrices $\mathbf{C}$ and $\mathbf{D}$ are irrelevant, since they say nothing about where the state can be driven.

```{=latex}
\begin{example}[frametitle={Example - controllability of a diagonal system}]
```

$\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$, $\mathbf{B} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$.

$$
\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} \end{bmatrix}
= \begin{bmatrix} 1 & -1 & 1 \\ 1 & -2 & 4 \\ 0 & 0 & 0 \end{bmatrix}
$$

so $\operatorname{rank}\mathcal{C} = 2 < n$ and the system is not controllable. Note the test is $\operatorname{rank}\mathcal{C} = n$, not a determinant: since $\mathbf{B}$ is $n \times m$, $\mathcal{C}$ is $n \times nm$ — square only for a single input ($m = 1$), so in general $\det\mathcal{C}$ is not even defined. Here the zero third row already shows $\operatorname{rank}\mathcal{C} \le 2 < n$: the columns span a subspace of $\mathbb{R}^3$ but not all of it, so the input cannot reach every state.

**Interpretation** — the zero in the third row of $\mathbf{B}$ disconnects the third state from the input. Because $\mathbf{A}$ is diagonal, the input reaches state $i$ only through the entry $b_i$ of $\mathbf{B}$; with $b_3 = 0$ the third mode evolves on its own, untouched by $\vec{u}$. That is why the entire third row of $\mathcal{C}$ is zeros — the input can never get a grip on that mode.

```{=latex}
\end{example}
```

## Observability

A system $(\mathbf{A}, \mathbf{C})$ is **observable** if the initial state $\vec{x}_0$ can be reconstructed from the output $\vec{y}(t)$ (and the known input $\vec{u}(t)$) over a finite time interval — every mode eventually shows up in the output.

Rolling on the car example from the previous section, the sensors are the $\mathbf{C}$: what never reaches them can never be reconstructed, so observability (pun intended) is about $\mathbf{A}$ and $\mathbf{C}$ alone. The **observability matrix** collects the rows that matter:

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{O} = n \iff \text{observable}
$}
\endgroup
\]
```

Why exactly those rows? With $\vec{u} = \vec{0}$, the output is

$$
\vec{y}(t) = \mathbf{C}e^{\mathbf{A}t}\vec{x}_0
$$

and by Cayley–Hamilton, $e^{\mathbf{A}t}$ is a polynomial in $\mathbf{A}$ of degree at most $n-1$:

$$
e^{\mathbf{A}t} = \sum_{k=0}^{n-1}\alpha_k(t)\mathbf{A}^k
$$

so the output becomes

$$
\vec{y}(t) = \sum_{k=0}^{n-1}\alpha_k(t)\,\mathbf{C}\mathbf{A}^k\vec{x}_0
$$

The known output pins down each $\mathbf{C}\mathbf{A}^k\vec{x}_0$ — differentiating $\vec{y}$ $k$ times at $t = 0$ gives exactly $\vec{y}^{(k)}(0) = \mathbf{C}\mathbf{A}^k\vec{x}_0$ — so stacking them,

$$
\begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}\vec{x}_0 = \vec{z}
$$

is a linear system for $\vec{x}_0$ with a unique solution iff $\mathcal{O}$ has full column rank $n$. Powers $\mathbf{A}^k$ with $k \ge n$ add nothing new — Cayley–Hamilton folds them back into $\mathbf{A}^0, \dots, \mathbf{A}^{n-1}$.

Note the duality: observability of $(\mathbf{A}, \mathbf{C})$ is controllability of $(\mathbf{A}^T, \mathbf{C}^T)$ — the controllability matrix of that transposed pair is exactly $\mathcal{O}^T$, so the two tests are one and the same condition.

```{=latex}
\begin{example}[frametitle={Example - observability of a diagonal system}]
```

Same $\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$, $\mathbf{C} = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$.

$$
\mathcal{O}_1 = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \end{bmatrix}
= \begin{bmatrix} 1 & 1 & 1 \\ -1 & -2 & -3 \\ 1 & 4 & 9 \end{bmatrix}, \qquad
\det\mathcal{O}_1 = -2 \ne 0
$$

so $\operatorname{rank}\mathcal{O}_1 = 3 = n$ and the system is observable — every mode shows up in the output. With $\mathbf{C} = \begin{bmatrix} 1 & 0 & 1 \end{bmatrix}$ the second mode is invisible in the output:

$$
\mathcal{O}_2 = \begin{bmatrix} 1 & 0 & 1 \\ -1 & 0 & -3 \\ 1 & 0 & 9 \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{O}_2 = 2 < 3
$$

so the system is **not** observable.

```{=latex}
\end{example}
```

Everything in this chapter is decided by one spectrum: the stability classes by where the eigenvalues sit relative to the imaginary axis, controllability and observability by how $\mathbf{B}$ and $\mathbf{C}$ couple to the eigenvectors. The next chapter views the same system from the outside — the transfer function $G(s)$ and the frequency domain.
