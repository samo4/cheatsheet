# Discrete systems

Sampled-time systems evolve in discrete steps rather than continuously. The continuous time $t$ is replaced by $kT$ where $T$ is the fixed sampling period and $k$ the integer sample index. And as we don't like typing, we usually drop the $T$. Discrete indexing gets square brackets — $x[k]$ in place of the continuous $x(t)$ — the same convention most programming languages use. Incidentally, computers are the primary reason why we discuss the discrete case at all, their step nature fits perfectly with the discrete-time model, without even resorting to numerical integration.

## Difference equations

The discrete analogue of an ODE is a **difference equation**. In matrix form it is the discrete state-space equations — next state on the left, the direct counterpart of the continuous $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$:

$$
\underbrace{\vec{x}[k+1]}_{\text{next}} = \mathbf{A}\underbrace{\vec{x}[k]}_{\text{current}} + \mathbf{B}\underbrace{\vec{u}[k]}_{\text{current}}, \qquad
\vec{y}[k] = \mathbf{C}\vec{x}[k] + \mathbf{D}\vec{u}[k]
$$

Given the initial state $\vec{x}[0]$, the first equation steps the state forward one sample at a time.

## Modeling examples

```{=latex}
\begin{example}[frametitle={Example - people moving to the city}]
```

A region holds $x_1$ people in the city and $x_2$ people in the surroundings. Each year a fraction $\alpha$ of the city-dwellers move out to the surroundings, and a fraction $\beta$ of the surrounding dwellers move into the city — nobody enters or leaves the region:

$$
\begin{bmatrix} x_1[k+1] \\ x_2[k+1] \end{bmatrix}
= \begin{bmatrix} 1-\alpha & \beta \\ \alpha & 1-\beta \end{bmatrix}\begin{bmatrix} x_1[k] \\ x_2[k] \end{bmatrix}
$$

Each entry $A_{ij}$ tells how much of current $x_j$ ends up in next year's $x_i$:

- $A_{11} = 1-\alpha$ — current city people contribute to next year's city, minus the fraction $\alpha$ who moved out to the surroundings.
- $A_{12} = \beta$ — the fraction $\beta$ of current surrounding people who move into the city.
- $A_{21} = \alpha$ — the fraction $\alpha$ of current city people who moved out to the surroundings.
- $A_{22} = 1-\beta$ — current surrounding people contribute to next year's surroundings, minus the fraction $\beta$ who moved into the city.

The columns of $\mathbf{A}$ sum to $1$, so the total population is conserved.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - Samuelson's national income model}]
```

$y$ is the **national income** — the total output the economy produces in a year — split between consumption $c$, investment $i$ and government spending $g$:

$$
y[k] = c[k] + i[k] + g[k]
$$

- $\alpha$ — **marginal propensity to consume**: the fraction of last year's income spent on consumption this year, $c[k] = \alpha\,y[k-1]$.
- $\beta$ — **accelerator**: how strongly investment reacts to the *change* in consumption, $i[k] = \beta(c[k] - c[k-1])$.

Putting the pieces together — $c[k] = \alpha y[k-1]$ and $c[k-1] = \alpha y[k-2]$, so $i[k] = \alpha\beta(y[k-1] - y[k-2])$ — the identity becomes the second-order difference equation

$$
y[k] - \alpha(1+\beta)\,y[k-1] + \alpha\beta\, y[k-2] = g[k]
$$

Stack the two previous incomes into the state $\vec{x}[k] = \begin{bmatrix} y[k-2] \\ y[k-1] \end{bmatrix}$, next state on the left:

$$
\begin{bmatrix} y[k-1] \\ y[k] \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ -\alpha\beta & \alpha(1+\beta) \end{bmatrix}\begin{bmatrix} y[k-2] \\ y[k-1] \end{bmatrix}
+ \begin{bmatrix} 0 \\ 1 \end{bmatrix}g[k]
$$

Each entry tells how much of current $x_j$ ends up in next year's $x_i$:

- $A_{11} = 0$ — the oldest income $y[k-2]$ contributes nothing directly to next year's $y[k-1]$; the two-year window simply slides forward.
- $A_{12} = 1$ — current $y[k-1]$ *is* next year's $x_1$: last year's income shifts into the oldest slot.
- $A_{21} = -\alpha\beta$ — income from two years ago *lowers* this year's income: a large $y[k-2]$ means consumption was high last year, so the change $c[k] - c[k-1]$ — and with it the accelerator investment — is small.
- $A_{22} = \alpha(1+\beta)$ — last year's income feeds this year's through both channels: consumption $\alpha\,y[k-1]$ plus the accelerator's positive leg $\alpha\beta\,y[k-1]$.
- $B_1 = 0,\ B_2 = 1$ — government spending enters the identity one-for-one, and only into the newest slot $y[k]$.

government spending the input, the two previous incomes the initial conditions.

```{=latex}
\end{example}
```

## Z-transform

Same idea as the Laplace transform, but for sequences. Where Laplace tames derivatives, the $z$-transform tames **shifts** — and it does it with a single trick: a one-sample delay is just a factor of $z^{-1}$. Shifting in time then becomes multiplying by a power of $z$, so a difference equation collapses into a plain algebraic equation.

The transform itself tags every sample with the delay it has accumulated and sums:

$$
F(z) = \mathcal{Z}\{f[k]\} = \sum_{k=0}^{\infty} f[k]\, z^{-k}
$$

so $f[k]$ is the coefficient of $z^{-k}$, and $z^{-1}$ is the delay operator. It is a *one-sided* transform: the sum runs over $k \ge 0$, so negative indices never appear. By convention we treat the sequence as *causal* — $f[k] = 0 \ \forall k < 0$ — and that convention is exactly what makes the shift rules below asymmetric. Remember what a shift does to the powers of $z$, and the whole rulebook \footnote{Equivalently, a causal sequence satisfies $f[k] = f[k]\,u[k]$ — we could carry the unit-step factor through every rule below, but that would only clutter the notation.} follows:

- Z-transforms are *linear*, so transform piece by piece and add: $\mathcal{Z}\{a f + b g\} = aF + bG$.
- *Delay* aka shift to the right — each sample of delay costs $z^{-1}$: $\mathcal{Z}\{f[k-1]\} = z^{-1}F$.
- *Advance* aka shift to the left — pull it one sample earlier and multiply by $z$, but the sample that falls off the front has to be subtracted back in: $\mathcal{Z}\{f[k+1]\} = zF - zf[0]$.
- *Convolution* — multiplying two transforms convolves the sequences in time: $\mathcal{Z}\{f * g\} = FG$, exactly the same trade as with Laplace: convolution in time is multiplication in frequency, and vice versa.

A few workhorse pairs (inversion by partial fractions, as with Laplace):

$$
\delta[k] \leftrightarrow 1, \qquad
u[k] \leftrightarrow \frac{z}{z-1}, \qquad
a^k \leftrightarrow \frac{z}{z-a}, \qquad
k \leftrightarrow \frac{z}{(z-1)^2}
$$

```{=latex}
\begin{example}[frametitle={Example - partial fraction expansion like we never left Laplace}]
```
$$
y[z] = \frac{z(z-1)}{\left(z+\frac{1}{2}\right)\left(z-\frac{1}{2}\right)(z+1)}
$$

This one is quite tricky as a first example. We could just do the PFE straight on $y[z]$ — for simple poles that gives the standard terms $K/(z-p)$, no $z$ on top\footnote{This is not one of the pairs above — it is just what partial-fraction decomposition hands us.} — but inverting those costs a borrowed $z^{-1}$: a one-sample delay that leaves a stray $K p^{k-1}$ in the answer. The pair we want, $a^k \leftrightarrow \frac{z}{z-a}$, wants a $z$ on top, so instead expand $\frac{y[z]}{z}$. Dividing by $z$ is exactly a one-sample delay ($\frac{y[z]}{z} \leftrightarrow y[k-1]$), but we undo it immediately by multiplying back by $z$ before inverting — so no shift ever reaches the final answer. All that survives is the $z$ in the numerator, exactly where the pair wants it:

$$
\frac{y[z]}{z} = \frac{z-1}{\left(z+\frac{1}{2}\right)\left(z-\frac{1}{2}\right)(z+1)} = \frac{A}{z+\frac{1}{2}} + \frac{B}{z-\frac{1}{2}} + \frac{C}{z+1}
$$

Now, let's get A,B,C by equating coefficients of powers of $z$:

$$
z - 1 = (A+B+C)z^2 + \left(\frac{1}{2}A+\frac{3}{2}B\right)z + \left(-\frac{1}{2}A+\frac{1}{2}B-\frac{1}{4}C\right)
$$
$$
A + B + C = 0
$$
$$
\frac{1}{2}A + \frac{3}{2}B = 1
$$
$$
-\frac{1}{2}A + \frac{1}{2}B - \frac{1}{4}C = -1
$$

Solving gives $A = 3$, $B = -\frac{1}{3}$, $C = -\frac{8}{3}$, so multiplying back by $z$ our $y[z]$ becomes:

$$
y[z] = \frac{3z}{z+\frac{1}{2}} - \frac{\frac{1}{3}\,z}{z-\frac{1}{2}} - \frac{\frac{8}{3}\,z}{z+1}
$$

**Back to time.** Each term is now exactly the pair $\frac{Kz}{z-p} \leftrightarrow K p^k$ — no delay trick needed, powers of $k$ straight away:

$$
y[k] = \mathcal{Z}^{-1}\{y[z]\} = \left[3\left(-\frac{1}{2}\right)^k - \frac{1}{3}\left(\frac{1}{2}\right)^k - \frac{8}{3}(-1)^k\right]u[k]
$$

the two real modes decaying ($|{-}\frac{1}{2}|, |\frac{1}{2}| < 1$) and the alternating mode $(-1)^k$ — the discrete echo of a pole on the unit circle, neither decaying nor growing.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - another PFE}]
```

$$X[z] = \frac{z^2}{(z-3)(z-5)}$$

TLDR: we store the $z$ on the left side and we bring it back at final inverse transform.

$$\frac{X[z]}{z} = \frac{z}{(z-3)(z-5)} = \frac{A}{z-3} + \frac{B}{z-5}$$

Clear denominators and equate coefficients of powers of $z$:

$$z = A(z-5) + B(z-3) = (A+B)z - 5A - 3B
\quad\rightarrow\quad
A + B = 1, \quad -5A - 3B = 0
\quad\rightarrow\quad
A = -\frac{3}{2},\quad B = \frac{5}{2}$$

multiply back by $z$ and read off the pair $\frac{Kz}{z-p} \leftrightarrow K p^k$:

$$X[z] = -\frac{3}{2}\,\frac{z}{z-3} + \frac{5}{2}\,\frac{z}{z-5}
\quad\rightarrow\quad
x[k] = \left[-\frac{3}{2}\,3^k + \frac{5}{2}\,5^k\right]u[k]$$

Sanity check: $x[0] = -\frac{3}{2} + \frac{5}{2} = 1$, matching $X[z] \to 1$ as $z \to \infty$. For the nitpickers: $k \ge 0$.

```{=latex}
\end{example}
```

## Higher-order difference equations as first-order systems

Say we have (too lazy to write the $n$-th order case, so let's just start with third-order):

$$
y[k+3] + a_2 y[k+2] + a_1 y[k+1] + a_0 y[k] = b_0 u[k], \quad y[0] = y_0, \quad y[1] = y_1, \quad y[2] = y_2
$$

To get everything on the left in terms of $k+1$, we introduce new state variables that simply shift the output along:

$$x_1[k] = y[k]$$
$$x_2[k] = y[k+1]$$
$$x_3[k] = y[k+2]$$

The form we want has $k+1$ on the left, so we shift the index by one — each state steps into the next, and the last row comes straight from the starting difference equation, the same companion form as in the continuous case:

$$x_1[k+1] = x_2[k] = y[k+1]$$
$$x_2[k+1] = x_3[k] = y[k+2]$$
$$x_3[k+1] = -a_0 x_1[k] - a_1 x_2[k] - a_2 x_3[k] + b_0 u[k]$$

Or in matrix form (and extending to $n$-th order):

$$
\begin{bmatrix} x_1[k+1] \\ x_2[k+1] \\ \vdots \\ x_n[k+1] \end{bmatrix}
=
\begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix}
\begin{bmatrix} x_1[k] \\ x_2[k] \\ \vdots \\ x_n[k] \end{bmatrix}
+
\begin{bmatrix} 0 \\ 0 \\ \vdots \\ b_0 \end{bmatrix} u[k]
$$

The state-space form is the same as in continuous time — only the indexing changes, from the derivative $\dot{\vec{x}}$ to the shift $\vec{x}[k+1]$:

$$\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$$
$$\vec{y}[k] = \mathbf{C}\vec{x}[k] + \mathbf{D}\vec{u}[k]$$

But the *matrices* are not the same as in the continuous case — if you're mixing continuous and discrete systems, be careful to use the right ones. In the following section we add indexing to distinguish the two: $A_D$ and $A_c$, $B_D$ and $B_c$, etc.


## Discretizing continuous systems

### Euler method

We start from AB state space form:

$$\dot{\vec{x}} = \mathbf{A}_c\vec{x} + \mathbf{B}_c\vec{u}$$

and approximate the derivative with a finite difference (aka Euler's method):

$$\dot{\vec{x}} \approx \frac{\vec{x}[k+1] - \vec{x}[k]}{T}$$

which gives the Euler discretization:

$$\vec{x}[(k+1)T] \approx \underbrace{(\mathbf{I} + T\mathbf{A}_c)}_{\mathbf{A}_D}\vec{x}[kT] + \underbrace{T\mathbf{B}_c}_{\mathbf{B}_D}\vec{u}[kT]$$

Giving us a simple set of transformations

$$ \mathbf{A}_D = \mathbf{I} + T\mathbf{A}_c, \quad  \mathbf{B}_D = T\mathbf{B}_c, \quad \mathbf{C}_D = \mathbf{C}_c, \quad \mathbf{D}_D = \mathbf{D}_c$$

As always, each methods has its pros and cons. Euler's is simple, but we need a small $T$ to get a good approximation.

### Integral approximation

We want the step from $t_1 = kT$ to $t_2 = (k+1)T$, but the system is time-invariant: the step over *any* sample period is identical to the step over the very first one. So we derive it once for the first period, $t \in [0, T]$ (i.e. $k = 0$), and put the general $k$ back at the end.

Start from the exact solution of the continuous system:

$$\vec{x}(t) = e^{\mathbf{A}_c t}\vec{x}(0) + \int_0^t e^{\mathbf{A}_c (t-\tau)}\mathbf{B}_c\vec{u}(\tau)\, d\tau$$

At $t = T$, with a zero-order hold\footnote{Strictly, what the plant sees is not the sequence but the *held* staircase — the output of a D/A converter that pins $\vec{u}[k]$ for a whole period, $\vec{u}_h(t) = \vec{u}[k]$ for $kT \le t < (k+1)T$.} keeping $\vec{u}(\tau) = \vec{u}[0]$ constant over the whole period:

$$\vec{x}(T) = e^{\mathbf{A}_c T}\vec{x}(0) + \int_0^T e^{\mathbf{A}_c (T-\tau)}\, d\tau\, \mathbf{B}_c\, \vec{u}[0]$$

The substitution $\tau' = T - \tau$ ($d\tau = -d\tau'$, limits flip) turns the integral into the familiar form,

$$\int_0^T e^{\mathbf{A}_c (T-\tau)}\, d\tau = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau$$

so the first period reads

$$\vec{x}(T) = \underbrace{e^{\mathbf{A}_c T}}_{\mathbf{A}_D}\vec{x}(0) + \underbrace{\left(\int_0^T e^{\mathbf{A}_c \tau}\, d\tau\right)\mathbf{B}_c}_{\mathbf{B}_D}\, \vec{u}[0]$$

By time-invariance every period looks the same — just shift $0 \to kT$ and $T \to (k+1)T$:

$$\vec{x}((k+1)T) = \mathbf{A}_D \vec{x}(kT) + \mathbf{B}_D\, \vec{u}[k]$$

Where:

$$
\mathbf{A}_D = e^{\mathbf{A}_c T}, \qquad
\mathbf{B}_D = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau\, \mathbf{B}_c  = (\mathbf{A}_D - \mathbf{I})\mathbf{A}_c^{-1}\mathbf{B}_c \qquad
\mathbf{C}_D = \mathbf{C}_c, \quad \mathbf{D}_D = \mathbf{D}_c$$

Incidentally and without any proof-like discussion, note that the continuous poles map as $z_i = e^{s_i T}$.

```{=latex}
\begin{example}[frametitle={Example - discretizing for $T = 0.1$ s}]
```

Discretize $\dot{\vec{x}} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ 1 \end{bmatrix}u$ with $T = 0.1$ s.

We need the matrix exponential. Both discrete matrices are built from it — so the whole example is really about computing $e^{\mathbf{A}_c T}$.

**The general way.** The cleanest route is diagonalization: if $\mathbf{A}_c = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$ (eigenvectors in the columns of $\mathbf{V}$, eigenvalues on the diagonal of $\boldsymbol{\Lambda}$), then

$$e^{\mathbf{A}_c T} = \mathbf{V}\,e^{\boldsymbol{\Lambda} T}\,\mathbf{V}^{-1}, \qquad e^{\boldsymbol{\Lambda}T} = \operatorname{diag}\left(e^{\lambda_1 T}, \dots, e^{\lambda_n T}\right)$$

— exponentiating a matrix collapses to exponentiating its eigenvalues one scalar at a time. (If a matrix refuses to diagonalize, Cayley–Hamilton does the same job without the eigenvectors.) So the plan is: find the eigenvalues, then exponentiate.

**Step 1 — eigenvalues.** In this entire "book", when you don't know where to start, just calculate the eigenvalues. In this particular example, this is actually the first step.

$\det(\lambda\mathbf{I} - \mathbf{A}_c) = (\lambda + 2)(\lambda + 1)$, so the eigenvalues are real: $\lambda_1 = -2$ and $\lambda_2 = -1$.

**Step 2 — the discrete $\mathbf{A}_D$.** The eigenvalues are distinct, so $\mathbf{A}_c$ is diagonalizable and we run the recipe above. Eigenvectors: for $\lambda_1 = -2$ take $\vec{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$, for $\lambda_2 = -1$ take $\vec{v}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$. Hence

$$\mathbf{V} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}, \qquad \mathbf{V}^{-1} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \qquad \boldsymbol{\Lambda} = \begin{bmatrix} -2 & 0 \\ 0 & -1 \end{bmatrix}$$

With $e^{-0.2} = 0.8187$ and $e^{-0.1} = 0.9048$,

$$\mathbf{A}_D = e^{\mathbf{A}_c T} = \mathbf{V}e^{\boldsymbol{\Lambda}T}\mathbf{V}^{-1} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} e^{-0.2} & 0 \\ 0 & e^{-0.1} \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} e^{-0.2} & 0 \\ e^{-0.1}-e^{-0.2} & e^{-0.1} \end{bmatrix} \approx \begin{bmatrix} 0.819 & 0 \\ 0.086 & 0.905 \end{bmatrix}$$

**Step 3 — the discrete $\mathbf{B}_D$.** We pick the formula from above. It only works if $\mathbf{A}_c$ is invertible and it is ($\det\mathbf{A}_c = 2$).


$$\mathbf{A}_c^{-1} = \begin{bmatrix} -\frac{1}{2} & 0 \\ -\frac{1}{2} & -1 \end{bmatrix}$$

$$\mathbf{B}_D = (\mathbf{A}_D - \mathbf{I})\mathbf{A}_c^{-1}\mathbf{B}_c \approx \begin{bmatrix} 0 \\ 0.095 \end{bmatrix}$$

```{=latex}
\end{example}
```

Last, but not least, at the start of this chapter we decided that explicitly stating the sampling period $T$ is a nuisance, so we dropped it from the notation. But it is still there, lurking in the background — the discrete system is just a sampled version of the continuous one, and the mapping $\mathbf{A}_D = e^{\mathbf{A}_c T}$ is only valid for that particular $T$. If you change $T$, you have to recompute $\mathbf{A}_D$ and $\mathbf{B}_D$.

## Solving the discrete state equations

### Homogeneous state equations

So with some initial state $\vec{x}[0]$ and no input $\vec{u}[k] = 0$, the discrete state equations are:

$$\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$$
$$\vec{x}[1] = \mathbf{A}\vec{x}[0]$$
$$\vec{x}[2] = \mathbf{A}\vec{x}[1] = \mathbf{A}^2\vec{x}[0]$$
$$\vec{x}[3] = \mathbf{A}\vec{x}[2] = \mathbf{A}^3\vec{x}[0]$$
$$\vdots$$
$$\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$$
and since $\vec{u}[k] = 0$:
$$\vec{y}[k] = \mathbf{C}\mathbf{A}^k\vec{x}[0]$$

$\mathbf{A}^k$ is the **discrete state-transition matrix**, mapping the initial state to the state at step $k$.

### Nonhomogeneous state equations

Same thing as homogeneous, but now we have to account for the input $\vec{u}[k]$:

$$\vec{x}[1] = \mathbf{A}\vec{x}[0] + \mathbf{B}\vec{u}[0]$$
$$\vec{x}[2] = \mathbf{A}\vec{x}[1] + \mathbf{B}\vec{u}[1] = \mathbf{A}^2\vec{x}[0] + \mathbf{A}\mathbf{B}\vec{u}[0] + \mathbf{B}\vec{u}[1]$$
$$\vec{x}[3] = \mathbf{A}\vec{x}[2] + \mathbf{B}\vec{u}[2] = \mathbf{A}^3\vec{x}[0] + \mathbf{A}^2\mathbf{B}\vec{u}[0] + \mathbf{A}\mathbf{B}\vec{u}[1] + \mathbf{B}\vec{u}[2]$$
$$\vdots$$
$$\vec{x}[k] = \mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1} \mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i]$$
$$\vec{y}[k] = \mathbf{C}\mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1} \mathbf{C}\mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i] + \mathbf{D}\vec{u}[k]$$

## Obtaining the discrete state-transition matrix $\mathbf{A}^k$

Nothing new here — all three methods are exact copies of the continuous-time ones from the State-space chapter, with only the notation swapped: $\lambda_i^k$ in place of $e^{\lambda_i t}$, and the $z$-transform in place of the Laplace transform. Same ideas, same caveats.

### $\mathbf{A}^k$ via the Z-transform

Invert the resolvent, almost exactly\footnote{watch for that additional $z$} as the Laplace transform did in the continuous case:

$$
\mathbf{A}^k = \mathcal{Z}^{-1}\left\{z\left(z\mathbf{I} - \mathbf{A}\right)^{-1}\right\}
$$

How did we get here? Start from the homogeneous state equations, take the Z-transform, and solve for $\vec{X}(z)$. The advance rule $\mathcal{Z}\{\vec{x}[k+1]\} = z\vec{X}(z) - z\vec{x}[0]$ handles the left-hand side:

$$\vec{X}(z) = \mathcal{Z}\{\vec{x}[k]\} = \sum_{k=0}^{\infty} \vec{x}[k]\, z^{-k}$$
$$z\vec{X}(z) - z\vec{x}[0] = \mathbf{A}\vec{X}(z)$$
$$(z\mathbf{I} - \mathbf{A})\vec{X}(z) = z\vec{x}[0]$$
$$\vec{X}(z) = (z\mathbf{I} - \mathbf{A})^{-1} z\,\vec{x}[0]$$

Inverting and comparing with the homogeneous solution $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$ closes the loop:

$$\vec{x}[k] = \mathcal{Z}^{-1}\left\{(z\mathbf{I} - \mathbf{A})^{-1} z\right\}\vec{x}[0] = \mathbf{A}^k\vec{x}[0]
\quad\Longrightarrow\quad
\mathbf{A}^k = \mathcal{Z}^{-1}\left\{z\left(z\mathbf{I} - \mathbf{A}\right)^{-1}\right\}$$




```{=latex}
\begin{example}[frametitle={Example - $\mathbf{A}^k$ via the Z-transform}]
```

**TODO: verify.**

Take $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -0.1 & 0.7 \end{bmatrix}$. Since $\det(z\mathbf{I}-\mathbf{A}) = z^2 - 0.7z + 0.1 = (z-0.5)(z-0.2)$, the resolvent is

$$(z\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(z-0.5)(z-0.2)}\begin{bmatrix} z-0.7 & 1 \\ -0.1 & z \end{bmatrix}$$

Expanding it into pole/projection form,

$$(z\mathbf{I} - \mathbf{A})^{-1} = \frac{\mathbf{P}_1}{z-0.5} + \frac{\mathbf{P}_2}{z-0.2}, \qquad
\mathbf{P}_1 = \frac{10}{3}\begin{bmatrix} -0.2 & 1 \\ -0.1 & 0.5 \end{bmatrix}, \qquad
\mathbf{P}_2 = -\frac{10}{3}\begin{bmatrix} -0.5 & 1 \\ -0.1 & 0.2 \end{bmatrix}$$

(one-liner check: $\mathbf{P}_1 + \mathbf{P}_2 = \mathbf{I}$). The extra $z$ in the inversion formula turns each term into the clean pair $\frac{z}{z-p} \leftrightarrow p^k$:

$$\mathbf{A}^k = \mathcal{Z}^{-1}\left\{\frac{z\mathbf{P}_1}{z-0.5} + \frac{z\mathbf{P}_2}{z-0.2}\right\} = 0.5^k\mathbf{P}_1 + 0.2^k\mathbf{P}_2 = \begin{bmatrix} -\frac{2}{3}0.5^k + \frac{5}{3}0.2^k & \frac{10}{3}(0.5^k - 0.2^k) \\[2pt] -\frac{1}{3}(0.5^k - 0.2^k) & \frac{5}{3}0.5^k - \frac{2}{3}0.2^k \end{bmatrix}$$

and at $k = 0$ this collapses to $\mathbf{A}^0 = \mathbf{P}_1 + \mathbf{P}_2 = \mathbf{I}$, as it must.

```{=latex}
\end{example}
```

### $\mathbf{A}^k$ via diagonalization

Powers of a diagonal matrix are entrywise powers, so with $\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$,

$$
\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}, \qquad
\boldsymbol{\Lambda}^k = \operatorname{diag}\left(\lambda_1^k, \dots, \lambda_n^k\right)
$$

— only if $\mathbf{A}$ is diagonalizable.


```{=latex}
\begin{example}[frametitle={Example - $\mathbf{A}^k$ via diagonalization}]
```

Again take $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -0.1 & 0.7 \end{bmatrix}$.

**Step 1 — eigenvalues:** $\det(\mathbf{A}-\lambda\mathbf{I}) = \lambda^2 - 0.7\lambda + 0.1 = (\lambda-0.5)(\lambda-0.2)$, so $\lambda_1 = 0.2$ and $\lambda_2 = 0.5$.

**Step 2 — eigenvectors $\mathbf{V}$ and $\mathbf{V}^{-1}$:** for $\lambda_1 = 0.2$ take $\vec{v}_1 = \begin{bmatrix} 1 \\ 0.2 \end{bmatrix}$, for $\lambda_2 = 0.5$ take $\vec{v}_2 = \begin{bmatrix} 1 \\ 0.5 \end{bmatrix}$, so

$$\mathbf{V} = \begin{bmatrix} 1 & 1 \\ 0.2 & 0.5 \end{bmatrix}, \qquad
\mathbf{V}^{-1} = \begin{bmatrix} \frac{5}{3} & -\frac{10}{3} \\ -\frac{2}{3} & \frac{10}{3} \end{bmatrix}$$

**Step 3 — $\mathbf{A}^k$:** with $\boldsymbol{\Lambda}^k = \operatorname{diag}(0.2^k, 0.5^k)$,

$$\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1} = \begin{bmatrix} 1 & 1 \\ 0.2 & 0.5 \end{bmatrix} \begin{bmatrix} 0.2^k & 0 \\ 0 & 0.5^k \end{bmatrix} \begin{bmatrix} \frac{5}{3} & -\frac{10}{3} \\ -\frac{2}{3} & \frac{10}{3} \end{bmatrix} = \begin{bmatrix} \frac{5}{3}0.2^k - \frac{2}{3}0.5^k & \frac{10}{3}(0.5^k - 0.2^k) \\[2pt] -\frac{1}{3}(0.5^k - 0.2^k) & \frac{5}{3}0.5^k - \frac{2}{3}0.2^k \end{bmatrix}$$

— the very same $\mathbf{A}^k$ the resolvent method produced; that is the point of showing both routes.  

```{=latex}
\end{example}
```

### $\mathbf{A}^k$ via Cayley–Hamilton

Cayley–Hamilton folds every power $\mathbf{A}^k$ ($k \ge n$) back into a polynomial of degree at most $n-1$:

$$
\mathbf{A}^k = \alpha_0(k)\mathbf{I} + \alpha_1(k)\mathbf{A} + \cdots + \alpha_{n-1}(k)\mathbf{A}^{n-1}
$$

the coefficients following from the scalar identities $\lambda_i^k = \alpha_0 + \alpha_1\lambda_i + \cdots + \alpha_{n-1}\lambda_i^{n-1}$ (differentiate for repeated eigenvalues); works even for defective matrices.

```{=latex}
\begin{example}[frametitle={Example - obtaining $\mathbf{A}^k$ via Cayley–Hamilton}]
```

Same $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -0.1 & 0.7 \end{bmatrix}$. Characteristic equation:

$$\det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^2 - 0.7\lambda + 0.1 = 0$$

so $\mathbf{A}^2 - 0.7\mathbf{A} + 0.1\mathbf{I} = \mathbf{0}$, and with $n = 2$:

$$\mathbf{A}^k = \alpha_0(k)\mathbf{I} + \alpha_1(k)\mathbf{A}, \qquad
\lambda^k = \alpha_0(k) + \alpha_1(k)\lambda$$

We already have the eigenvalues from the two examples above — $\lambda_1 = 0.2$ and $\lambda_2 = 0.5$ — so evaluate there, a $2\times2$ linear system in the unknowns $(\alpha_0, \alpha_1)$ (the $k$ lives only in the known right-hand sides):

$$\lambda_1 = 0.2: \quad 0.2^k = \alpha_0 + 0.2\alpha_1$$
$$\lambda_2 = 0.5: \quad 0.5^k = \alpha_0 + 0.5\alpha_1$$

Subtract the two equations to eliminate $\alpha_0$:

$$0.5^k - 0.2^k = 0.3\alpha_1 \quad\Longrightarrow\quad \alpha_1 = \frac{10}{3}(0.5^k - 0.2^k)$$

Back-substitute: $\alpha_0 = 0.2^k - 0.2\alpha_1 = \frac{5}{3}0.2^k - \frac{2}{3}0.5^k$. Put the coefficients back into $\mathbf{A}^k = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}$ and multiply out:

$$\mathbf{A}^k = \left(\frac{5}{3}0.2^k - \frac{2}{3}0.5^k\right)\mathbf{I} + \frac{10}{3}(0.5^k - 0.2^k)\mathbf{A}
= \begin{bmatrix} \frac{5}{3}0.2^k - \frac{2}{3}0.5^k & \frac{10}{3}(0.5^k - 0.2^k) \\[2pt] -\frac{1}{3}(0.5^k - 0.2^k) & \frac{5}{3}0.5^k - \frac{2}{3}0.2^k \end{bmatrix}$$

which matches both previous methods.

```{=latex}
\end{example}
```

### Final remarks

As in the continuous case, if you're not forced to use some other method, you always pick Cayley–Hamilton.

## Transfer function

From the discrete state equations with zero initial conditions,

$$
\mathbf{H}(z) = \mathbf{C}(z\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$$

the same rational-function picture as in the Transfer functions chapter, with the unit circle as the stability boundary. Block algebra (series, parallel, feedback) is identical.

## Equilibrium, stability, controllability, observability

Everything mirrors the continuous case:

- **Equilibrium** — with $u[k] = 0$, a linear discrete system has the single equilibrium at the origin $\vec{x}_e = \vec{0}$; the equilibrium types are the same as for continuous systems.
- **Stability** — the modes are $\lambda_i^k$, so the boundary is the **unit circle**: asymptotically stable if $|\lambda_i| < 1$ for all $i$; marginal if $|\lambda_i| \le 1$ with unit-circle eigenvalues simple; unstable if some $|\lambda_i| > 1$ or a repeated unit-circle eigenvalue.
- **Controllability** — the same controllability matrix $M = [\mathbf{B}\ \mathbf{A}\mathbf{B}\ \cdots\ \mathbf{A}^{n-1}\mathbf{B}]$ and rank test as for continuous systems.
- **Observability** — the same observability matrix $N$ and rank test as for continuous systems.
