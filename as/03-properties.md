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
\operatorname{Re}\lambda_i < 0 \ \ \forall i & \iff & \text{asymptotically stable}
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

A system is **controllable** if, for any initial state $\vec{x}_0$ and any target state $\vec{x}_1$, there exists an input $\vec{u}(t)$ that drives the state from $\vec{x}_0$ to $\vec{x}_1$ in finite time — the input can steer the state anywhere in state space.

Controllability is a practical requirement, not just a theoretical one. Take a car with no throttle: you might get it to drift to a position, but you can never place it where you want. The input reaches the state only through $\mathbf{B}$, and with no throttle that path is missing, so no input moves the state; how much that hurts depends on the output matrices, since the engine rpm can do as it likes while you try to park.

Following @ogata2002modern, the reachable states fall out of the state response: with $\vec{x}(0) = \vec{0}$, reaching $\vec{x}(t)$ at time $t$ requires

$$
\vec{x}(t) = \int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\vec{u}(\tau)\, d\tau
$$

For LTI, reachability from the origin is the same as controllability, since $e^{\mathbf{A}t}$ is always invertible. And we can exploit Cayley–Hamilton to express $e^{\mathbf{A}s}$ as a polynomial:

$$
e^{\mathbf{A}s} = \alpha_0(s)\mathbf{I} + \alpha_1(s)\mathbf{A} + \cdots + \alpha_{n-1}(s)\mathbf{A}^{n-1}
$$

Substituting and pulling the constant matrices $\mathbf{A}^k\mathbf{B}$ out of the integral leaves $n$ fixed directions, each scaled by a weight the input alone decides:

$$
\vec{x}(t) = \sum_{k=0}^{n-1} \mathbf{A}^k\mathbf{B} \underbrace{\int_0^t \alpha_k(t-\tau)\vec{u}(\tau)\, d\tau}_{\vec{w}_k}
= \mathbf{B}\vec{w}_0 + \mathbf{A}\mathbf{B}\vec{w}_1 + \cdots + \mathbf{A}^{n-1}\mathbf{B}\vec{w}_{n-1}
$$

Each weight is the $k$-th Cayley–Hamilton coefficient convolved with the input, $\vec{w}_k(t) = (\alpha_k * \vec{u})(t)$. Stacking the weights into a single vector turns the sum into one matrix product, in which only the vector depends on the input:

$$
\vec{x}(t) = \underbrace{\begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}}_{\mathcal{C}}
\underbrace{\begin{bmatrix} \vec{w}_0 \\ \vec{w}_1 \\ \vdots \\ \vec{w}_{n-1} \end{bmatrix}}_{\vec{w}}
= \mathcal{C}\vec{w}
$$

Vary $\vec{u}$ over $[0,t]$ and $\vec{w} \in \mathbb{R}^{nm}$ ($n$ blocks of length $m$, with $m$ the number of inputs) ranges over whatever that input can produce. The direction, though, is out of the input's hands: every reachable state is $\mathcal{C}\vec{w}$ for some $\vec{w}$ — the easy direction of Cayley–Hamilton, that reachable states lie in the column space of $\mathcal{C}$.

The containment is the half Cayley–Hamilton gives directly; the converse — that full row rank really is enough, with no direction wasted — is the classical theorem, taken as given here. Either way, the input reaches *every* state of $\mathbb{R}^n$ exactly when the $nm$ columns of $\mathcal{C}$ span it, i.e. when $\mathcal{C}$ has full row rank $n$. The matrix collecting exactly those columns is the *controllability matrix*:

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

When the rank falls short, the directions it misses are exactly the uncontrollable modes from the chapter opening: in the BIBO example above $\mathcal{C} = \begin{bmatrix} 0 & 0 \\ 1 & -2 \end{bmatrix}$ has rank $1 < 2$, and the direction the input never gets a grip on is the runaway mode $+1$.

As you could intuitively deduce, controllability therefore involves only $(\mathbf{A}, \mathbf{B})$: the output matrices $\mathbf{C}$ and $\mathbf{D}$ are irrelevant, since they say nothing about where the state can be driven.

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

A system is **observable** if the initial state $\vec{x}_0(t_0)$ can be reconstructed from the output $\vec{y}(t)$ measured over finite interval $$[t_0, t_1]$ together with the known input $\vec{u}(t)$).

Rolling on the car example from the previous section, the sensors are the $\mathbf{C}$: what never reaches them can never be reconstructed, so observability (pun intended) is about $\mathbf{A}$ and $\mathbf{C}$ alone.

Following @ogata2002modern again, but from the other end of the loop — the sensor equation itself. The state is what we cannot see, the output is what we can:

$$
\underbrace{\vec{y}(t)}_{\text{measured}} = \mathbf{C}\underbrace{\vec{x}(t)}_{\text{hidden}} + \mathbf{D}\vec{u}(t)
$$

Feeding in the state solution of the State-space chapter,

$$
\vec{x}(t) = e^{\mathbf{A}t}\vec{x}(0) + \int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\vec{u}(\tau)\, d\tau
$$

leaves the unknown in a single term:

$$
\underbrace{\vec{y}(t)}_{\text{measured}} = \underbrace{\mathbf{C}e^{\mathbf{A}t}\vec{x}(0)}_{\text{initial-state response}} + \underbrace{\mathbf{C}\int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\vec{u}(\tau)\, d\tau + \mathbf{D}\vec{u}(t)}_{\text{known, given the input}}
$$

The record is the sum of two responses: one driven by the initial state, one by the input. The input is ours, so its contribution can be computed and subtracted off — from here on we take $\vec{u} = \vec{0}$ and keep only

$$
\vec{y}(t) = \mathbf{C}e^{\mathbf{A}t}\vec{x}(0)
$$

Everything on the left is known for every $t$; the right side hides the one thing we want. Cayley–Hamilton again, this time with $\mathbf{C}$ distributed over the terms, expands the record into $n$ known functions of time, each multiplying one unknown vector:

$$
\vec{y}(t) = \alpha_0(t)\,\mathbf{C}\vec{x}(0) + \alpha_1(t)\,\mathbf{C}\mathbf{A}\vec{x}(0) + \cdots + \alpha_{n-1}(t)\,\mathbf{C}\mathbf{A}^{n-1}\vec{x}(0)
$$

The record is known, so each of those coefficients is recoverable on its own: differentiating brings down one power of $\mathbf{A}$ at a time, since $\frac{d^k}{dt^k}e^{\mathbf{A}t} = \mathbf{A}^k e^{\mathbf{A}t}$, and at $t = 0$ the exponential is the identity,

$$
\vec{y}^{(k)}(t) = \mathbf{C}\mathbf{A}^k e^{\mathbf{A}t}\vec{x}(0)
\quad\Longrightarrow\quad
\vec{y}^{(k)}(0) = \mathbf{C}\mathbf{A}^k\vec{x}(0)
$$

Stacking the first $n$ of these known vectors,

$$
\begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}\vec{x}(0)
= \underbrace{\begin{bmatrix} \vec{y}(0) \\ \vec{y}'(0) \\ \vdots \\ \vec{y}^{(n-1)}(0) \end{bmatrix}}_{\vec{z}}
$$

leaves one linear system for $\vec{x}(0)$, with a unique solution iff $\mathcal{O}$ has full column rank $n$. Powers $\mathbf{A}^k$ with $k \ge n$ add nothing new — Cayley–Hamilton folds them back into $\mathbf{A}^0, \dots, \mathbf{A}^{n-1}$. The matrix collecting exactly those rows is the *observability matrix*:

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

When the rank falls short, the rows it misses are exactly the unobservable modes from the chapter opening: in the example below $\det\mathcal{O}$ vanishes, and the mode that never reaches the sensor is $\lambda = -1$ — the very factor $(s+1)$ that cancels out of the transfer functions.

Note the duality: observability of $(\mathbf{A}, \mathbf{C})$ is controllability of $(\mathbf{A}^T, \mathbf{C}^T)$ — the controllability matrix of that transposed pair is exactly $\mathcal{O}^T$, so the two tests are one and the same condition.

```{=latex}
\begin{example}[frametitle={Example - observability, the Taylor route}]
```

Same starting point, same unknown:

$$
\vec{y}(t) = \mathbf{C}e^{\mathbf{A}t}\vec{x}(0), \qquad
e^{\mathbf{A}t} = \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!}
$$

Inserting the defining series and collecting by powers of $t$ puts one unknown vector behind each known coefficient:

$$
\vec{y}(t) = \sum_{k=0}^{\infty} \frac{t^k}{k!}\,\underbrace{\mathbf{C}\mathbf{A}^k\vec{x}(0)}_{\text{unknown}}
$$

Nothing has to be regrouped first: differentiate term by term and set $t = 0$, where only the $k$-th term of the $k$-th derivative survives,

$$
\vec{y}^{(k)}(0) = \mathbf{C}\mathbf{A}^k\vec{x}(0),
$$

so the rows are read straight off the coefficients. Let's cheat and ask ourselves what Cayley–Hamilton has to say: $\mathbf{A}^k$ folds back into $\mathbf{I}, \dots, \mathbf{A}^{n-1}$ so powers $k \ge n$ add nothing and stacking the first $n$ gives

$$
\underbrace{\begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}}_{\mathcal{O}}\vec{x}(0)
= \begin{bmatrix} \vec{y}(0) \\ \vec{y}'(0) \\ \vdots \\ \vec{y}^{(n-1)}(0) \end{bmatrix},
$$

so $\vec{x}(0)$ is recoverable iff $\operatorname{rank}\mathcal{O} = n$ — the same matrix, without ever solving for an $\alpha_k(t)$.

The two routes are the same derivation in two orders: Cayley–Hamilton regroups the series into $n$ known functions of $t$ and then differentiates, Taylor differentiates first and reads the rows off the coefficients. Taylor is shorter; Cayley–Hamilton is what tells you $n$ rows suffice. 

Taylor route also exists for controllability test.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - observability, and a pole that cancels}]
```

This is Ogata's example: $\mathbf{A} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix}$, $\mathbf{B} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$, $\mathbf{C} = \begin{bmatrix} 4 & 5 & 1 \end{bmatrix}$, $\mathbf{D} = 0$. Only $\mathbf{A}$ and $\mathbf{C}$ enter the test; $\mathbf{B}$ rides along for the transfer functions below.

$$
\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \end{bmatrix}
= \begin{bmatrix} 4 & 5 & 1 \\ -6 & -7 & -1 \\ 6 & 5 & -1 \end{bmatrix}, \qquad
\det\mathcal{O} = 0, \qquad \operatorname{rank}\mathcal{O} = 2 < 3
$$

The third row is $-6$ times the first minus $5$ times the second, so the rows are dependent and the system is **not** observable. (A single output makes $\mathcal{O}$ square, so this is one of the cases where the determinant is meaningful — it vanishes.) The pair $(\mathbf{A}, \mathbf{B})$ is nonetheless controllable, so this is purely an observability failure.

Which mode is lost? The characteristic polynomial factors,

$$
\det(s\mathbf{I}-\mathbf{A}) = s^3 + 6s^2 + 11s + 6 = (s+1)(s+2)(s+3)
$$

and the driven states carry all three modes, while the output keeps only two. With $\mathbf{B} = \vec{e}_3$ the state solution gives, with zero initial state,

$$
\frac{X_1(s)}{U(s)} = \frac{1}{(s+1)(s+2)(s+3)}, \qquad
\frac{X_2(s)}{U(s)} = \frac{s}{(s+1)(s+2)(s+3)}, \qquad
\frac{X_3(s)}{U(s)} = \frac{s^2}{(s+1)(s+2)(s+3)}
$$

so $X_1$ holds every mode — the pair $(\mathbf{A}, \mathbf{B})$ being controllable, the input can excite all of them. What $\mathbf{C}$ then does to the first state has a zero sitting exactly on the pole $s = -1$:

$$
\frac{Y(s)}{X_1(s)} = s^2 + 5s + 4 = (s+1)(s+4)
$$

Multiplying the two,

$$
\frac{Y(s)}{U(s)} = \frac{Y(s)}{X_1(s)}\cdot\frac{X_1(s)}{U(s)}
= \frac{\xcancel{(s+1)}(s+4)}{\xcancel{(s+1)}(s+2)(s+3)}
$$

the $(s+1)$ is gone: the state does carry the mode $e^{-t}$, but the zero at $s = -1$ in the $x_1 \to y$ map annihilates it, and the input–output transfer function ends up one order thinner than the system.

Where it hides: $\lambda = -1$ has eigenvector $\vec{v} = \tvec{-1,1,-1}$ — check $\mathbf{A}\vec{v} = -\vec{v}$ — and $\mathbf{C}\vec{v} = -4+5-1 = 0$. The sensor is blind to it for all time, since $\mathbf{C}\mathbf{A}^k\vec{v} = (-1)^k\mathbf{C}\vec{v} = \vec{0}$, which is exactly $\mathcal{O}\vec{v} = \vec{0}$: the rank drops by one, and the state combination $-x_1 + x_2 - x_3$ decays as $e^{-t}$ unseen. The cancelled $(s+1)$ is that blindness, read in the frequency domain.

```{=latex}
\end{example}
```

Everything in this chapter is decided by one spectrum: the stability classes by where the eigenvalues sit relative to the imaginary axis, controllability and observability by how $\mathbf{B}$ and $\mathbf{C}$ couple to the eigenvectors. The next chapter views the same system from the outside — the transfer function $G(s)$ and the frequency domain.
