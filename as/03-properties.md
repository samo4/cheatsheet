# Properties of systems

## Modes of an LTI system

The (free) response of an LTI system is set entirely by the eigenvalues of $\mathbf{A}$. From the homogeneous solution, $\vec{x}(t) = e^{\mathbf{A}t}\vec{x}_0$, and diagonalizing gives $e^{\mathbf{A}t} = \mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}$, so the response is a linear combination of the exponentials

$$
e^{\lambda_1 t},\; e^{\lambda_2 t},\; \dots,\; e^{\lambda_n t}
$$

each a **mode** of the system. The spectrum of $\mathbf{A}$ — its eigenvalues $\lambda_i$ — therefore maps one-to-one onto the modes of the response: to the $n$ eigenvalues of $\mathbf{A}$ belong $n$ modes of the system. A real $\lambda$ gives a growing or decaying exponential; a conjugate pair $\sigma \pm j\omega$ gives an oscillation with envelope $e^{\sigma t}$.

These eigenvalues are also the **poles** of the transfer function $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$: its denominator is $\det(s\mathbf{I}-\mathbf{A})$, so the poles are exactly the eigenvalues of $\mathbf{A}$ — at least for a minimal (controllable and observable) realization. An eigenvalue belonging to an uncontrollable or unobservable mode cancels out of $G(s)$ and is not a pole.

Everything that follows — stability, controllability, observability — is decided by these modes.

## Controllability

A system $(\mathbf{A}, \mathbf{B})$ is **controllable** if, for any initial state $\vec{x}_0$ and any target state $\vec{x}_1$, there exists an input $\vec{u}(t)$ that drives the state from $\vec{x}_0$ to $\vec{x}_1$ in finite time — the input can steer the state anywhere in state space.

The **controllability matrix** collects the columns that matter:

$$
M = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}
$$

and the system is controllable iff $\operatorname{rank}M = n$.

Why exactly those columns? Take the state response with $\vec{x}(0) = \vec{0}$; reaching $\vec{x}$ at time $t$ requires

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

A state is reachable exactly when it lies in the column space of $\mathcal{C}$, so every state is reachable iff $\operatorname{rank}\mathcal{C} = n$. Powers $\mathbf{A}^k$ with $k \ge n$ contribute nothing new — Cayley–Hamilton folds them back into $\mathbf{A}^0, \dots, \mathbf{A}^{n-1}$.

```{=latex}
\begin{example}[frametitle={Example - controllability of a diagonal system}]
```

$\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$, $\mathbf{B} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$.

$$
\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} \end{bmatrix}
= \begin{bmatrix} 1 & -1 & 1 \\ 1 & -2 & 4 \\ 1 & -3 & 9 \end{bmatrix}, \qquad
\det\mathcal{C} = -2 \ne 0
$$

so $\operatorname{rank}\mathcal{C} = 3 = n$ and the system is controllable — every mode is driven by the input. With $\mathbf{B} = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$ the second mode is decoupled from the input and

$$
\mathcal{C} = \begin{bmatrix} 1 & -1 & 1 \\ 0 & 0 & 0 \\ 1 & -3 & 9 \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{C} = 2 < 3
$$

so the system is **not** controllable.

```{=latex}
\end{example}
```

## Observability

A system $(\mathbf{A}, \mathbf{C})$ is **observable** if the initial state $\vec{x}_0$ can be reconstructed from the output $\vec{y}(t)$ (and the known input $\vec{u}(t)$) over a finite time interval — every mode eventually shows up in the output.

The **observability matrix** collects the rows that matter:

$$
N = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}
$$

and the system is observable iff $\operatorname{rank}N = n$.

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

The known functions $\alpha_k(t)$ let the output pin down each $\mathbf{C}\mathbf{A}^k\vec{x}_0$; stacking them,

$$
\begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}\vec{x}_0 = \vec{z}
$$

is a linear system for $\vec{x}_0$ with a unique solution iff $\mathcal{O}$ has full column rank $n$. Powers $\mathbf{A}^k$ with $k \ge n$ add nothing new — Cayley–Hamilton folds them back into $\mathbf{A}^0, \dots, \mathbf{A}^{n-1}$.

Note the duality: observability of $(\mathbf{A}, \mathbf{C})$ is controllability of $(\mathbf{A}^T, \mathbf{C}^T)$ — here, with $\mathbf{C} = \mathbf{B}^T$, the observability matrix is exactly $\mathcal{O} = \mathcal{C}^T$.

```{=latex}
\begin{example}[frametitle={Example - observability of a diagonal system}]
```

Same $\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$, $\mathbf{C} = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$.

$$
\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \end{bmatrix}
= \begin{bmatrix} 1 & 1 & 1 \\ -1 & -2 & -3 \\ 1 & 4 & 9 \end{bmatrix}, \qquad
\det\mathcal{O} = -2 \ne 0
$$

so $\operatorname{rank}\mathcal{O} = 3 = n$ and the system is observable — every mode shows up in the output. With $\mathbf{C} = \begin{bmatrix} 1 & 0 & 1 \end{bmatrix}$ the second mode is invisible in the output:

$$
\mathcal{O} = \begin{bmatrix} 1 & 0 & 1 \\ -1 & 0 & -3 \\ 1 & 0 & 9 \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{O} = 2 < 3
$$

so the system is **not** observable.

```{=latex}
\end{example}
```

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

Whether trajectories actually end up at the equilibrium is exactly what the next section, Stability, formalizes.

## Stability

For $\dot{\vec{x}} = \mathbf{A}\vec{x}$ stability is decided by the eigenvalues of $\mathbf{A}$ — the poles — i.e. by where they sit relative to the imaginary axis. All plots below use the family $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -3 & a \end{bmatrix}$, whose poles are $\lambda = \frac{a \pm j\sqrt{12-a^2}}{2}$; the grey half-plane is the stable region, the dashed line its boundary.

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
