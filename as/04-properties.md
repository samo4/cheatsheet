# Properties of systems

## Modes of an LTI system

The shape of the (zero-input) response of an LTI system is set by the eigenvalues of $\mathbf{A}$. From the homogeneous solution, $\vec{x}(t) = e^{\mathbf{A}t}\vec{x}_0$, and diagonalizing gives $e^{\mathbf{A}t} = \mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}$, so the response is a linear combination of the exponentials

$$
e^{\lambda_1 t},\; e^{\lambda_2 t},\; \dots,\; e^{\lambda_n t}
$$

each called a **mode** of the system; the eigenvalues of $\mathbf{A}$ set the modes. A real $\lambda$ gives a growing or decaying exponential (or a constant for $\lambda = 0$); a conjugate pair $\sigma \pm j\omega$ gives an oscillation with envelope $e^{\sigma t}$.

The exception is a defective $\mathbf{A}$: when a repeated eigenvalue has fewer independent eigenvectors than its multiplicity, it brings a factor $t$ instead of a second independent exponential, so $n$ eigenvalues need not give $n$ modes. The Jordan form says which. The block sizes tell you in advance which terms the free response can contain: a $k\times k$ Jordan block at $\lambda$ contributes $e^{\lambda t}, t e^{\lambda t}, \dots, t^{k-1}e^{\lambda t}$ (see $\Phi$ via the Jordan form in the State-space chapter). This is the state-space version of a repeated pole in partial fractions.

These eigenvalues are also the **poles** of the transfer function $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$ (which we get to properly in the transfer-function chapter): its denominator is $\det(s\mathbf{I}-\mathbf{A})$, so the poles are the eigenvalues of $\mathbf{A}$, at least for a minimal realization (controllable and observable, both defined below). An uncontrollable or unobservable mode cancels out of $G(s)$; its eigenvalue is not a pole unless another, controllable and observable, mode shares it.

Everything that follows is decided by these modes and by how the inputs and outputs couple to them: the equilibrium behaviour and stability first, then controllability and observability.

## Equilibrium states and phase portraits

An *equilibrium state* $\vec{x}_e$ is where the system stays put, $\dot{\vec{x}} = \vec{0}$ at $\vec{x} = \vec{x}_e$. For the linear system $\dot{\vec{x}} = \mathbf{A}\vec{x}$ the equilibria solve $\mathbf{A}\vec{x}_e = \vec{0}$: the origin $\vec{x}_e = \vec{0}$ when $\mathbf{A}$ is nonsingular, or a whole subspace of equilibria when $\mathbf{A}$ is singular. (With a constant input, $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ has equilibria where $\mathbf{A}\vec{x}_e + \mathbf{B}\vec{u} = \vec{0}$, and possibly none: an integrator under a constant input never comes to rest.)

The phase portrait, with trajectories plotted together in state space, shows how the state moves and whether it reaches the equilibrium. Near an equilibrium the behaviour is set by the eigenvalues of $\mathbf{A}$, i.e. the modes from the beginning of this chapter:

- *Node* — real eigenvalues of the same sign: trajectories run into (both negative) or away from (both positive) the equilibrium without circling. They are straight only along the eigenvectors; otherwise they curve in tangent to the slower one.
- *Saddle* — real eigenvalues of opposite signs: it approaches along one eigenvector and escapes along the other; always unstable.
- *Focus* (spiral) — complex pair $\sigma \pm j\omega$: it spirals into the equilibrium for $\sigma < 0$, away for $\sigma > 0$.
- *Center* — purely imaginary $\pm j\omega$: closed elliptical orbits; it neither settles nor escapes.

For the example system of the State-space chapter, $\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x}$ (eigenvalues $-1 \pm j\sqrt{2}$), the origin is the only equilibrium and a stable focus: every trajectory spirals into it.

```{=latex}
\input{tikz/phase-portrait-focus.tex}
```

The same response, read one state at a time, is two decaying sinusoids, and the spiral combines the two. The real part of the eigenvalues sets the decay, the imaginary part the oscillation:

```{=latex}
\input{tikz/state-components.tex}
```

Whether trajectories actually end up at the equilibrium is what we investigate next.

## Stability

Stability asks what the free response $\dot{\vec{x}} = \mathbf{A}\vec{x}$ does from an arbitrary initial state. The equilibrium $\vec{x}_e = \vec{0}$ is

- *stable in the sense of Lyapunov* if every trajectory stays bounded,
- *asymptotically stable* if, in addition, every trajectory converges to $\vec{0}$,
- *marginally stable* if it is Lyapunov stable but not asymptotically stable: the states stay bounded, but not all of them decay,
- *unstable* if some trajectory grows without bound.

Since the free response is built from the modes, all of this is decided by the eigenvalues of $\mathbf{A}$, by where they sit relative to the imaginary axis:

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\begin{array}{lcl}
\operatorname{Re}\lambda_i < 0 \ \ \forall i & \iff & \text{asymptotically stable} \\[4pt]
\operatorname{Re}\lambda_i \le 0 \ \ \forall i, \text{ some on the axis, all simple} & \Longrightarrow & \text{marginally stable} \\[4pt]
\text{some } \operatorname{Re}\lambda_i > 0 & \Longrightarrow & \text{unstable}
\end{array}
$}
\endgroup
\]
```

All plots below use the family $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -3 & a \end{bmatrix}$, whose eigenvalues are $\lambda = \frac{a \pm j\sqrt{12-a^2}}{2}$, complex while $a^2 < 12$, real beyond that. The grey half-plane is the stable region, the dashed line its boundary.

### Asymptotically stable

Every mode decays, so from any initial condition the trajectory converges to the equilibrium $\vec{x}_e = \vec{0}$. All eigenvalues lie strictly inside the shaded left half-plane:

```{=latex}
\input{tikz/stability-asymptotic.tex}
```

### Marginally stable

No eigenvalue lies in the right half-plane, and those on the imaginary axis are simple.^["Simple" is sufficient but not necessary. The exact condition is that every eigenvalue on the axis has only $1\times1$ Jordan blocks ($m_g = m_a$; Jordan form). For a stable eigenvalue the exponential decay wins over the polynomial, and $t^j e^{\lambda t} \to 0$. With $\operatorname{Re}\lambda = 0$ there is no decay to counter the polynomial, and a block of size $\ge 2$ makes the response grow without bound. This is the one case where the eigenvalues alone do not decide stability. $\dot{\vec{x}} = \mathbf{0}_{2\times2}\,\vec{x}$ (two separate integrators, blocks $1+1$) has $\lambda = 0$ twice and stays put, so it is marginally stable. The double integrator $\ddot{x} = 0$, with $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ (one $2\times2$ block), has the same eigenvalues but drifts as $x(t) = x_0 + \dot{x}_0 t$, so it is unstable.] The axis modes neither grow nor decay: a pair $\pm j\omega$ gives a sustained oscillation, $\lambda = 0$ a constant. Here the eigenvalues sit on the dashed boundary:

```{=latex}
\input{tikz/stability-marginal.tex}
```

```{=latex}
\begin{example}[frametitle={Example - what the eigenvalues can't tell you, but the Jordan form can}]
```

Compare

$$
\mathbf{A}_1 = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}, \qquad
\mathbf{A}_2 = \begin{bmatrix} -1 & c \\ 0 & -1 \end{bmatrix}, \quad c \ne 0.
$$

Same eigenvalues, $\lambda = -1$ twice, so both are asymptotically stable. Their Jordan forms differ, though: $\mathbf{A}_1$ is two $1\times1$ blocks, while $\mathbf{A}_2$ is one $2\times2$ block, $\mathbf{T}^{-1}\mathbf{A}_2\mathbf{T} = \mathbf{J}_2(-1)$ with $\mathbf{T} = \begin{bmatrix} c & 0 \\ 0 & 1 \end{bmatrix}$. The exponentials are

$$
e^{\mathbf{A}_1 t} = \begin{bmatrix} e^{-t} & 0 \\ 0 & e^{-t} \end{bmatrix}, \qquad
e^{\mathbf{A}_2 t} = \begin{bmatrix} e^{-t} & c\,t e^{-t} \\ 0 & e^{-t} \end{bmatrix}.
$$

Start both from $\vec{x}_0 = \tvec{0, 1}$. The first system shrinks straight to the origin, $\vec{x}(t) = e^{-t}\vec{x}_0$, and never gets farther away than it started. The second gets $x_1(t) = c\,t e^{-t}$: it climbs first, peaks at $t = 1$ with $x_1 = c/e$, and only then decays. For $c = 10$ the state swings out to about $3.7$ from a start of length $1$, before settling.

Both systems end at zero, as the eigenvalues predict. The eigenvalues say nothing about the way there. The $t e^{-t}$ mode, and with it the hump, comes from the $2\times2$ block. The height of the hump, $c$, sits in $\mathbf{T}$. In general a $t e^{\lambda t}$ mode with $\lambda < 0$ peaks at $t = 1/|\lambda|$, so the slower the pole, the later and larger the swing.

```{=latex}
\end{example}
```


### Unstable

Some eigenvalue lies in the right half-plane, or on the imaginary axis with a Jordan block of size $\ge 2$ (which brings a factor $t$; see the footnote under marginal stability). Some trajectories then grow without bound:

```{=latex}
\input{tikz/stability-unstable.tex}
```

### What if the parameters change a little?

The eigenvalues depend continuously on the entries of $\mathbf{A}$, so a small change moves each pole a little. The red circles below are the regions the poles can reach under a small perturbation. A circle that stays inside the shaded half-plane means the stability is robust, one that straddles the dashed boundary means it is not:

```{=latex}
\input{tikz/stability-perturbation.tex}
```

- *Asymptotic stability is robust*: the circles stay entirely inside the shaded left half-plane, so small perturbations keep the poles there (the margin is the distance from the boundary).
- *Marginal stability is not*: the circles straddle the dashed boundary, so a tiny change (here, $a$ crossing $0$) pushes the poles into one half-plane or the other, and the system becomes asymptotically stable or unstable.
- *Instability in the right half-plane is robust*: the circles stay there; pushing a pole back across the axis takes a finite change. (Instability from a Jordan block on the axis is as fragile as marginal stability.)

### Bounded-input bounded-output stability

The three classes above are about the state. A different question is whether a bounded input can ever produce an unbounded output (**BIBO stability**). It is answered by the poles of the transfer function rather than by the eigenvalues: every pole of $G(s)$ must lie in the open left half-plane. A pole on the axis is not enough: a step into an integrator, or a sine at the resonance frequency of an undamped oscillator, gives an output that grows without bound. So a marginally stable system whose axis mode reaches the output is not BIBO stable.

For a minimal realization the poles are the eigenvalues, so BIBO stability and asymptotic stability coincide. They differ when a pole cancels against a zero. Take

$$
\mathbf{A} = \begin{bmatrix} 1 & 0 \\ 0 & -2 \end{bmatrix}, \qquad
\mathbf{B} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \qquad
\mathbf{C} = \begin{bmatrix} 0 & 1 \end{bmatrix}, \qquad
\mathbf{D} = 0,
$$

for which $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} = \frac{1}{s+2}$: BIBO stable, since the only pole sits at $s = -2$. The state, however, runs away from $\vec{x}_0 = \tvec{1,0}$: the eigenvalue $+1$ belongs to a mode that no input can excite and no output reveals.

A hidden mode is harmless if it decays on its own. A system whose uncontrollable modes are all stable is called *stabilizable*, and one whose unobservable modes are all stable is *detectable*. The example above is neither: its hidden mode is the unstable $+1$.

BIBO stability is a statement about the input–output map, asymptotic stability about the state, and the second is the stronger of the two. This example is why the modes above come with a minimality caveat, and the next two sections say when a mode escapes through the input or the output.

## Controllability

A system is *controllable* if, for any initial state $\vec{x}_0$ and any target state $\vec{x}_1$, there exists an input $\vec{u}(t)$ that drives the state from $\vec{x}_0$ to $\vec{x}_1$ in finite time; the input can steer the state anywhere in state space.

Controllability is a practical requirement. Take a car with no throttle: it may drift somewhere, but you can never place it where you want. The input reaches the state only through $\mathbf{B}$, and without a throttle that path is missing. Not every uncontrollable state matters, though: while you park, the engine speed may do as it likes, as long as the position is under control.

Following @ogata2002modern, the reachable states follow from the state response: with $\vec{x}(0) = \vec{0}$, reaching $\vec{x}(t)$ at time $t$ requires

$$
\vec{x}(t) = \int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\vec{u}(\tau)\, d\tau
$$

For LTI, reachability from the origin is the same as controllability, since $e^{\mathbf{A}t}$ is always invertible. Cayley–Hamilton expresses $e^{\mathbf{A}\sigma}$, with $\sigma = t - \tau$ the elapsed time, as a polynomial:

$$
e^{\mathbf{A}\sigma} = \alpha_0(\sigma)\mathbf{I} + \alpha_1(\sigma)\mathbf{A} + \cdots + \alpha_{n-1}(\sigma)\mathbf{A}^{n-1}
$$

Substituting and pulling the constant matrices $\mathbf{A}^k\mathbf{B}$ out of the integral leaves $n$ fixed directions, each scaled by a weight that depends only on the input:

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

Vary $\vec{u}$ over $[0,t]$ and $\vec{w} \in \mathbb{R}^{nm}$ ($n$ blocks of length $m$, with $m$ the number of inputs) ranges over whatever that input can produce. The directions, however, are fixed by $\mathcal{C}$: every reachable state is $\mathcal{C}\vec{w}$ for some $\vec{w}$, so the reachable states lie in the range space of $\mathcal{C}$.

Cayley–Hamilton gives this containment directly. The converse, that full row rank is also enough, is the classical theorem, which we take as given. Together: the input reaches *every* state of $\mathbb{R}^n$ exactly when the $nm$ columns of $\mathcal{C}$ span it, i.e. when $\mathcal{C}$ has full row rank $n$. The matrix of these columns is the *controllability matrix*:

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

When the rank falls short, the missing directions belong to the uncontrollable modes from the chapter opening: in the BIBO example above $\mathcal{C} = \begin{bmatrix} 0 & 0 \\ 1 & -2 \end{bmatrix}$ has rank $1 < 2$, and the direction the input cannot reach is the unstable mode $+1$.

Controllability involves only $(\mathbf{A}, \mathbf{B})$: the output matrices $\mathbf{C}$ and $\mathbf{D}$ are irrelevant, since they say nothing about where the state can be driven.

```{=latex}
\begin{example}[frametitle={Example - controllability of a diagonal system}]
```

$\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$, $\mathbf{B} = \tvec{1, 1, 0}$.

$$
\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} \end{bmatrix}
= \begin{bmatrix} 1 & -1 & 1 \\ 1 & -2 & 4 \\ 0 & 0 & 0 \end{bmatrix}
$$

so $\operatorname{rank}\mathcal{C} = 2 < n$ and the system is not controllable. Note the test is $\operatorname{rank}\mathcal{C} = n$, not a determinant: since $\mathbf{B}$ is $n \times m$, $\mathcal{C}$ is $n \times nm$, which is square only for a single input ($m = 1$); in general $\det\mathcal{C}$ is not even defined. Here the zero third row already shows $\operatorname{rank}\mathcal{C} \le 2 < n$: the columns span a subspace of $\mathbb{R}^3$ but not all of it, so the input cannot reach every state.

**Interpretation.** The zero in the third row of $\mathbf{B}$ disconnects the third state from the input. Because $\mathbf{A}$ is diagonal, the input reaches state $i$ only through the entry $b_i$ of $\mathbf{B}$; with $b_3 = 0$ the third mode evolves on its own, untouched by $\vec{u}$. That is why the entire third row of $\mathcal{C}$ is zero: the input can never affect that mode.

```{=latex}
\end{example}
```

*Beyond diagonal: Jordan coordinates.* The same reading works for any $\mathbf{A}$ once it is brought to Jordan form, where controllability can be read off the transformed $\mathbf{B}$ (Gilbert's criterion). A useful consequence: if one eigenvalue has two or more Jordan blocks ($m_g \ge 2$), a single input cannot control the system, whatever $\mathbf{B}$ is. The input has to reach independent modes that share one $\lambda$, and they respond identically to it. In general, a system with $m$ inputs needs $m \ge \max_i m_{g,i}$. For actual testing, use the rank test above.^[For the Jordan-form tests in full, see @chen1999linear.]

Controllability as defined here is a yes-or-no question. In practice you may also care how hard it is to reach a particular state.

Finally, the rank test is not the only one. Alternatives, not covered here, such as the PBH (Popov–Belevitch–Hautus) test can be more convenient, depending on the system's structure.

## Observability

A system is **observable** if the initial state $\vec{x}(t_0)$ can be reconstructed from the output $\vec{y}(t)$ measured over a finite interval $[t_0, t_1]$, together with the known input $\vec{u}(t)$.

In the car example from the previous section, the sensors are $\mathbf{C}$: what never reaches them can never be reconstructed, so observability involves only $\mathbf{A}$ and $\mathbf{C}$.

Following @ogata2002modern again, start this time from the output equation. The state is what we cannot see, the output what we can:

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

The record is the sum of two responses: one driven by the initial state, one by the input. The input is ours, so its contribution can be computed and subtracted; from here on we take $\vec{u} = \vec{0}$ and keep only

$$
\vec{y}(t) = \mathbf{C}e^{\mathbf{A}t}\vec{x}(0)
$$

The left side is known for every $t$; the right side contains the unknown $\vec{x}(0)$. Differentiating the output brings down one power of $\mathbf{A}$ at a time, since $\frac{d^k}{dt^k}e^{\mathbf{A}t} = \mathbf{A}^k e^{\mathbf{A}t}$, and at $t = 0$ the exponential is the identity,

$$
\vec{y}^{(k)}(t) = \mathbf{C}\mathbf{A}^k e^{\mathbf{A}t}\vec{x}(0)
\quad\Longrightarrow\quad
\vec{y}^{(k)}(0) = \mathbf{C}\mathbf{A}^k\vec{x}(0)
$$

Stacking the first $n$ of these known vectors,

$$
\underbrace{\begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}}_{\mathcal{O}}\vec{x}(0)
= \begin{bmatrix} \vec{y}(0) \\ \vec{y}'(0) \\ \vdots \\ \vec{y}^{(n-1)}(0) \end{bmatrix}
$$

leaves one linear system for $\vec{x}(0)$, with a unique solution iff $\mathcal{O}$ has full column rank $n$. Powers $\mathbf{A}^k$ with $k \ge n$ add nothing new, because Cayley–Hamilton reduces them to $\mathbf{A}^0, \dots, \mathbf{A}^{n-1}$. The matrix of these rows is the *observability matrix*:

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

When the rank falls short, the missing directions belong to the unobservable modes from the chapter opening: in the example below $\det\mathcal{O}$ vanishes, and the mode that never reaches the sensor is $\lambda = -1$, the same factor $(s+1)$ that cancels out of the transfer functions.

Note the duality: observability of $(\mathbf{A}, \mathbf{C})$ is controllability of $(\mathbf{A}^T, \mathbf{C}^T)$. The controllability matrix of the transposed pair is $\mathcal{O}^T$, so the two tests are the same condition. The Jordan-form rule from controllability carries over too: if one eigenvalue has two or more Jordan blocks, a single output cannot observe the system, whatever $\mathbf{C}$ is, and $p$ outputs need $p \ge \max_i m_{g,i}$.

The controllability test can be derived the same way, without the Cayley–Hamilton coefficients: expanding $e^{\mathbf{A}(t-\tau)}$ as a series shows that the reachable states are spanned by the $\mathbf{A}^k\mathbf{B}$, and Cayley–Hamilton cuts the powers to $k < n$, which leaves the columns of $\mathcal{C}$.

```{=latex}
\begin{example}[frametitle={Example - observability, and a pole that cancels}]
```

This is Ogata's example: $\mathbf{A} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix}$, $\mathbf{B} = \tvec{0, 0, 1}$, $\mathbf{C} = \rvec{4, 5, 1}$, $\mathbf{D} = 0$. Only $\mathbf{A}$ and $\mathbf{C}$ enter the test; $\mathbf{B}$ is needed only for the transfer functions below.

$$
\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \end{bmatrix}
= \begin{bmatrix} 4 & 5 & 1 \\ -6 & -7 & -1 \\ 6 & 5 & -1 \end{bmatrix}, \qquad
\det\mathcal{O} = 0, \qquad \operatorname{rank}\mathcal{O} = 2 < 3
$$

The third row is $-6$ times the first minus $5$ times the second, so the rows are dependent and the system is **not** observable. (A single output makes $\mathcal{O}$ square, so this is one of the cases where the determinant is meaningful, and it vanishes.) The pair $(\mathbf{A}, \mathbf{B})$ is nonetheless controllable, so this is purely an observability failure.

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

so $X_1$ contains every mode: $(\mathbf{A}, \mathbf{B})$ is controllable, so the input can excite all of them. The map from $x_1$ to the output, however, has a zero on the pole $s = -1$:

$$
\frac{Y(s)}{X_1(s)} = s^2 + 5s + 4 = (s+1)(s+4)
$$

Multiplying the two,

$$
\frac{Y(s)}{U(s)} = \frac{Y(s)}{X_1(s)}\cdot\frac{X_1(s)}{U(s)}
= \frac{\xcancel{(s+1)}(s+4)}{\xcancel{(s+1)}(s+2)(s+3)}
$$

the $(s+1)$ is gone: the state does carry the mode $e^{-t}$, but the zero at $s = -1$ in the $x_1 \to y$ map cancels it, and the input–output transfer function is one order lower than the system.

Where the mode is hidden: $\lambda = -1$ has eigenvector $\vec{v} = \tvec{-1,1,-1}$ (check: $\mathbf{A}\vec{v} = -\vec{v}$), and $\mathbf{C}\vec{v} = -4+5-1 = 0$. The sensor never sees it, since $\mathbf{C}\mathbf{A}^k\vec{v} = (-1)^k\mathbf{C}\vec{v} = \vec{0}$, which is $\mathcal{O}\vec{v} = \vec{0}$: the rank drops by one. The combination of states that tracks this mode comes from the left eigenvector, $\vec{w}^T\mathbf{A} = -\vec{w}^T$ with $\vec{w} = \tvec{6, 5, 1}$: the modal coordinate $z = 6x_1 + 5x_2 + x_3$ obeys $\dot{z} = -z$ and decays as $e^{-t}$ unseen. The cancelled $(s+1)$ is that blindness, read in the frequency domain.

```{=latex}
\end{example}
```

Everything in this chapter is decided by one spectrum: the stability classes by where the eigenvalues sit relative to the imaginary axis, controllability and observability by how $\mathbf{B}$ and $\mathbf{C}$ couple to the eigenvectors. The next chapter views the same system from the outside: the transfer function $G(s)$ and the frequency domain.

The *tests* in this chapter are for linear systems. The definitions of stability carry over to nonlinear systems, but there stability becomes a property of each equilibrium, and controllability and observability need other tools. As a teaser: in a linear system, the farther left of the imaginary axis the poles are, the faster every mode decays. In a nonlinear system this can backfire: placing poles far left takes high gain, the transients peak (the *peaking phenomenon*), and a large enough peak can throw the state out of the region where the linear model holds.
