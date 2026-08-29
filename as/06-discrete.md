# Discrete systems

Sampled-time systems evolve in discrete steps rather than continuously. The continuous time $t$ is replaced by $kT$ where $T$ is the fixed sampling period and $k$ the integer sample index. And as we don't like typing, we usually drop the $T$. Discrete indexing gets square brackets — $x[k]$ in place of the continuous $x(t)$ — the same convention most programming languages use.

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
X(z) = \mathcal{Z}\{x[k]\} = \sum_{k=0}^{\infty} x[k]\, z^{-k}
$$

so $x[k]$ is the coefficient of $z^{-k}$, and $z^{-1}$ is the delay operator. Remember what a shift does to the powers of $z$, and the whole rulebook follows:

- Z-transforms are *linear*, so transform piece by piece and add: $\mathcal{Z}\{a x + b y\} = aX + bY$.
- *Delay* — push the sequence one sample later and multiply by $z^{-1}$; each extra sample of delay costs another $z^{-1}$: $\mathcal{Z}\{x[k-1]\} = z^{-1}X$.
- *Advance* — pull it one sample earlier and multiply by $z$, but the sample that falls off the front has to be subtracted back in: $\mathcal{Z}\{x[k+1]\} = zX - z\,x_0$.
- *Convolution* — multiplying two transforms convolves the sequences in time: $\mathcal{Z}\{x * y\} = X\,Y$, exactly the same trade as with Laplace.

A few workhorse pairs (inversion by partial fractions, as with Laplace):

$$
\delta[k] \leftrightarrow 1, \qquad
u[k] \leftrightarrow \frac{z}{z-1}, \qquad
a^k \leftrightarrow \frac{z}{z-a}, \qquad
k \leftrightarrow \frac{z}{(z-1)^2}
$$

## From a difference equation to state space

As for ODEs, an $n$-th order difference equation becomes a first-order vector equation — the discrete state space $\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$, $\vec{y}[k] = \mathbf{C}\vec{x}[k] + \mathbf{D}\vec{u}[k]$ — by stacking the delayed outputs. For $y[k+2] + a_1 y[k+1] + a_0 y[k] = b_0 u[k]$ take $x_1[k] = y[k]$, $x_2[k] = y[k+1]$:

$$
\vec{x}[k+1] = \begin{bmatrix} 0 & 1 \\ -a_0 & -a_1 \end{bmatrix}\vec{x}[k] + \begin{bmatrix} 0 \\ b_0 \end{bmatrix}u[k]
$$

the discrete companion form, the exact analogue of the continuous one.

## Discretizing continuous systems

Given $\dot{\vec{x}} = \mathbf{A}_c\vec{x} + \mathbf{B}_c\vec{u}$ and the sampling period $T$:

- **Exact (zero-order hold)** — keep $u$ constant between samples and integrate the continuous solution from $kT$ to $(k+1)T$:

$$
\mathbf{A} = e^{\mathbf{A}_c T}, \qquad
\mathbf{B} = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau\, \mathbf{B}_c
$$

  the continuous poles map as $z_i = e^{s_i T}$, and the approximation improves as $T$ shrinks.

- **Euler** — first-order approximation $\mathbf{A} \approx \mathbf{I} + \mathbf{A}_c T$, $\mathbf{B} \approx \mathbf{B}_c T$: simpler, but less accurate for the same $T$.

```{=latex}
\begin{example}[frametitle={Example - discretizing for $T = 0.1$ s}]
```

$\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u$ with $T = 0.1$ (eigenvalues $-1 \pm j\sqrt{2}$, so $z = e^{(-1\pm j\sqrt2)\cdot 0.1} = 0.9048\, e^{\pm j\,0.1414}$):

$$
\mathbf{A} = e^{\mathbf{A}_c T} \approx \begin{bmatrix} 0.986 & 0.090 \\ -0.271 & 0.806 \end{bmatrix}, \qquad
\mathbf{B} = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau\, \mathbf{B}_c \approx \begin{bmatrix} 0.019 \\ 0.361 \end{bmatrix}
$$

```{=latex}
\end{example}
```

## Solving the state equations

- **Homogeneous** — $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$; $\mathbf{A}^k$ is the **discrete state-transition matrix**, mapping the initial state to the state at step $k$.
- **Nonhomogeneous** —

$$
\vec{x}[k] = \mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1} \mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i]
$$

  the sum being a discrete convolution.

## Obtaining the discrete state-transition matrix $\mathbf{A}^k$

Nothing new here — all three methods are exact copies of the continuous-time ones from the State-space chapter, with only the notation swapped: $\lambda_i^k$ in place of $e^{\lambda_i t}$, and the $z$-transform in place of the Laplace transform. Same ideas, same caveats.

### $\mathbf{A}^k$ via the Z-transform

Invert the resolvent, exactly as the Laplace transform did in the continuous case:

$$
\mathbf{A}^k = \mathcal{Z}^{-1}\left\{z\left(z\mathbf{I} - \mathbf{A}\right)^{-1}\right\}
$$

### $\mathbf{A}^k$ via diagonalization

Powers of a diagonal matrix are entrywise powers, so with $\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$,

$$
\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}, \qquad
\boldsymbol{\Lambda}^k = \operatorname{diag}\left(\lambda_1^k, \dots, \lambda_n^k\right)
$$

— only if $\mathbf{A}$ is diagonalizable.

### $\mathbf{A}^k$ via Cayley–Hamilton

Cayley–Hamilton folds every power $\mathbf{A}^k$ ($k \ge n$) back into a polynomial of degree at most $n-1$:

$$
\mathbf{A}^k = \alpha_0(k)\mathbf{I} + \alpha_1(k)\mathbf{A} + \cdots + \alpha_{n-1}(k)\mathbf{A}^{n-1}
$$

the coefficients following from the scalar identities $\lambda_i^k = \alpha_0 + \alpha_1\lambda_i + \cdots + \alpha_{n-1}\lambda_i^{n-1}$ (differentiate for repeated eigenvalues); works even for defective matrices.

### Final remarks

As in the continuous case, Cayley–Hamilton returns as the tool of choice for controllability and observability.

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
- **Controllability** — the same controllability matrix $\mathcal{C} = [\mathbf{B}\ \mathbf{A}\mathbf{B}\ \cdots\ \mathbf{A}^{n-1}\mathbf{B}]$ and rank test as for continuous systems.
- **Observability** — the same observability matrix $\mathcal{O}$ and rank test as for continuous systems.
