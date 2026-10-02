# Review — Chapter 4, Properties of systems

Review of `04-properties.md`. Line numbers refer to the file as of 2026-09-30.

All calculations were checked by hand and are correct, except item 1: the pole formula for the $a$ family, the Jordan transform of $\mathbf{A}_2$ and its hump, the BIBO example, every $\mathcal{C}$ and $\mathcal{O}$, the row dependency and factorisations in Ogata's example, and the eigenvector $\vec v$. The phase-portrait and state-component figures match the $-1 \pm j\sqrt2$ system.

## Errors

### 1. Wrong combination for the hidden mode (line 375)

"the state combination $-x_1 + x_2 - x_3$ decays as $e^{-t}$ unseen" is wrong. $\vec v = [-1, 1, -1]^T$ is the *right* eigenvector: it gives the direction of the hidden mode. The combination of states that tracks the mode comes from the *left* eigenvector, $\vec w^T\mathbf{A} = -\vec w^T$, which gives $\vec w = [6, 5, 1]^T$.

Proposed replacement:

> … which is exactly $\mathcal{O}\vec{v} = \vec{0}$: the rank drops by one. The modal coordinate $z = 6x_1 + 5x_2 + x_3$ (from the left eigenvector, $\vec w^T\mathbf A = -\vec w^T$) obeys $\dot z = -z$, and the part of the state it carries, $z(t)\,\vec v/(\vec w^T\vec v)$, decays as $e^{-t}$ unseen.

### 2. Broken math in the observability definition (line 225)

`$$[t_0, t_1]$` opens display math, and the sentence ends with a stray `)`. The PDF currently shows "measured over finite interval $[0, 1] together with…". Also, $\vec{x}_0(t_0)$ should be $\vec{x}(t_0)$.

Proposed replacement:

> A system is **observable** if the initial state $\vec{x}(t_0)$ can be reconstructed from the output $\vec{y}(t)$ measured over a finite interval $[t_0, t_1]$, together with the known input $\vec{u}(t)$.

### 3. "Instability is robust" is only half true (line 126)

This holds only for poles strictly in the right half-plane. Instability from an eigenvalue on the imaginary axis with a Jordan block is as fragile as marginal stability: perturbing the bottom row of the double integrator can make it stable.

Proposed replacement:

> - *Instability in the right half-plane is robust*: the circles stay there — pushing a pole back across the axis takes a finite change. (Instability from a Jordan block on the axis is as fragile as marginal stability.)

### 4. The car analogy contradicts line 196 (line 149)

The analogy says how much the missing input "hurts depends on the output matrices", but line 196 says controllability involves only $(\mathbf A, \mathbf B)$. The rpm aside is really about *output controllability* or *stabilizability*: an uncontrollable state may not matter.

Proposed replacement:

> Controllability is a practical requirement, not just a theoretical one. Take a car with no throttle: you might get it to drift to a position, but you can never place it where you want. The input reaches the state only through $\mathbf{B}$; with that path missing, no input moves the state. Whether that matters is a separate question — if the uncontrollable part decays on its own, or never shows in what you care about, you may not need to control it (stabilizability, output controllability).

### 5. The diagonal controllability reading needs distinct eigenvalues (line 211)

For a diagonal $\mathbf{A}$, $b_i \ne 0$ for every $i$ is sufficient only if the eigenvalues are distinct. Counterexample: $\mathbf A = -\mathbf I$ with $\mathbf B = [1, 1]^T$ is uncontrollable even though both $b_i \ne 0$.

Proposed addition, at the end of the Interpretation paragraph:

> The converse needs distinct eigenvalues: with $\mathbf A = -\mathbf I_2$ and $\mathbf B = [1, 1]^T$ both $b_i \ne 0$, yet the two modes respond identically to $u$ and cannot be steered apart — the $m_g \ge 2$ rule below.

## Imprecise claims

### 6. Marginal vs Lyapunov stability (line 63)

Lyapunov stability also includes asymptotic stability, as line 73 itself says ("a stronger version of Lyapunov stability"). "a.k.a" is missing its final period.

Proposed replacement:

> A system is *stable in the sense of Lyapunov* if the states remain bounded; it is *marginally stable* if it is Lyapunov stable but not asymptotically stable — the states may oscillate, but neither grow nor settle.

### 7. Phase-portrait classes (line 25)

- A trajectory moves straight along an eigenvector only if it starts on one. In general it curves in tangent to the slow eigenvector.
- The list leaves out repeated real eigenvalues (star or degenerate node) and zero eigenvalues (a line of equilibria, which line 21 mentions).

Proposed wording for the node:

> - *Node* — real eigenvalues of the same sign: trajectories run into (both negative) or away from (both positive) the equilibrium without circling; they travel straight only along the eigenvectors and otherwise curve in tangent to the slower one.

### 8. Poles vs eigenvalues (line 15)

An uncontrollable or unobservable eigenvalue stays a pole if the same $\lambda$ also belongs to a mode that is controllable and observable.

Proposed replacement for the last sentence:

> An uncontrollable or unobservable mode cancels out of $G(s)$; its eigenvalue is not a pole unless another, controllable and observable, mode shares it.

### 9. Modes (lines 11 and 13)

- "the eigenvalues of $\mathbf A$ are the modes": the modes are the exponentials, and the eigenvalues set them.
- "fewer independent eigenvectors than eigenvalues" should be "fewer independent eigenvectors than the multiplicity of the eigenvalue".
- A real $\lambda$ can also be $0$, which gives a constant mode.

### 10. Equilibria with a constant input (line 21)

There may be none: if $\mathbf B\vec u \notin \operatorname{range}\mathbf A$, as for an integrator under a constant input, $\mathbf A\vec x_e + \mathbf B\vec u = \vec 0$ has no solution.

### 11. Unstable (line 110)

"the poles lie in the right half-plane" doesn't cover the Jordan-block case named in the same sentence. Write "some pole lies in the right half-plane, or on the axis with a Jordan block".

### 12. BIBO (line 130)

Write "the *open* left half-plane".

### 13. "The rows it misses" (line 288)

What goes missing is the null space of $\mathcal O$, the directions $\vec v$ with $\mathcal O \vec v = \vec 0$, not rows. Proposed wording: "When the rank falls short, the directions in the null space of $\mathcal O$ are exactly the unobservable modes…".

### 14. Closing paragraph (line 383)

- Typos: "futher", "abcissa", "sweetspot".
- "Left of the abscissa" should be "left of the imaginary axis"; the imaginary axis is the ordinate.
- "More stable" should say what it means: a larger decay rate or stability margin.
- Nonlinear systems use the same stability *definitions* but different *tests*, and stability becomes local to each equilibrium.
- The "too far left becomes unstable" teaser is defensible only as the *peaking phenomenon* (Sussmann & Kokotović, 1991): high-gain placement produces transient peaks that grow with the gain and can drive a nonlinear system out of its region of attraction, or into finite escape. It links back to the Jordan hump example.

Proposed replacement:

> Perhaps obvious, but worth emphasizing: the *tests* in this chapter are for linear systems. The definitions of stability carry over to nonlinear systems, but there stability becomes a property of each equilibrium, and controllability and observability need other tools. As a teaser: for a linear system, the farther left of the imaginary axis the poles sit, the faster every mode decays. In a nonlinear system this can backfire: placing poles far left takes high gain, the transients peak (the *peaking phenomenon*), and a large enough peak can throw the state out of the region where the linear model holds.

## Structure and wording

### 15. Observability is derived twice (lines 253–274 and 296–324)

The main text already uses the derivatives-at-0 route, and the "Taylor route" example repeats it almost word for word. The main text also sets up the $\alpha_k(t)$ expansion (line 256) and never uses it. Two options:

- **(a) Recommended:** make the main text use Cayley–Hamilton for what only it gives, necessity. If $\mathcal O \vec v = \vec 0$, then every term of the expansion vanishes, so $\vec y \equiv \vec 0$ for $\vec x(0) = \vec v$, and that state can't be told apart from the origin. That is the half the derivative route doesn't show, and the half item 1 relies on. Keep the Taylor example for sufficiency.
- **(b)** Cut the Taylor example down to its closing comparison paragraph.

### 16. $\mathcal O$ used before it is defined (lines 270–274)

Put the $\mathcal O$ underbrace on the stacked matrix, as the Taylor example does, and drop the unused label $\vec z$.

### 17. $s$ used as a time variable (line 157)

$e^{\mathbf As}$ with $\alpha_k(s)$ reuses the Laplace variable. Use $\sigma$ (or $\tau$) instead.

### 18. The "direction" pun (lines 178–180)

"the direction is out of the input's hands" and "the easy direction of Cayley–Hamilton" use "direction" in two senses.

Proposed replacement:

> Vary $\vec u$ over $[0, t]$ and $\vec w \in \mathbb R^{nm}$ ($n$ blocks of length $m$, with $m$ the number of inputs) ranges over whatever that input can produce, while the columns of $\mathcal C$ stay fixed. So every reachable state lies in the range of $\mathcal C$ — the easy half. The converse, that every state in that range is actually reached, is the classical theorem (proved via the controllability Gramian), taken as given here. Either way, the input reaches *every* state of $\mathbb R^n$ exactly when $\mathcal C$ has full row rank $n$.

### 19. Fragments and loose ends (lines 219, 221, 326)

- Line 219, proposed replacement: "Controllability as asked here is a yes-or-no question. How *hard* a state is to reach — how much input energy it takes — is measured by the controllability Gramian."
- Line 221: state the PBH test instead of only naming it. $(\mathbf A, \mathbf B)$ is controllable iff $\operatorname{rank}\begin{bmatrix}\lambda\mathbf I - \mathbf A & \mathbf B\end{bmatrix} = n$ for every eigenvalue $\lambda$ of $\mathbf A$. Equivalently, no left eigenvector of $\mathbf A$ is orthogonal to $\mathbf B$. This fits the closing line about $\mathbf B$ and $\mathbf C$ coupling to eigenvectors, and it is the test that item 1 uses implicitly.
- Line 326: "Taylor route also exists for controllability test." Either expand it (the reachable set as the span of $\mathbf A^k\mathbf B$ via the series of $e^{\mathbf A(t-\tau)}$) or cut it.

### 20. Informal phrasing

- Line 196: "As you could intuitively deduce" is filler; start with "Controllability therefore involves only…".
- Line 227: "Rolling on" should be "Carrying on", and "(pun intended)" has no pun; drop it.
- Line 315: "Let's cheat and ask ourselves what Cayley–Hamilton has to say" → "Cayley–Hamilton then says".

## Optional addition

### 21. Stabilizability and detectability

After the BIBO example (line 143), add one sentence:

> A system whose uncontrollable modes are all stable is *stabilizable*; one whose unobservable modes are all stable is *detectable*. The example above is neither: its hidden mode is the runaway $+1$.
