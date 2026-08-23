# Discrete systems

Sampled-time systems evolve in discrete steps rather than continuously. The continuous time $t$ is replaced by $kT$ — $T$ the fixed sampling period, $k$ the integer sample index — and the $T$ is usually dropped, writing $x[k] = x(kT)$.

## Difference equations

The discrete analogue of an ODE is a **difference equation**. It has two equivalent notations, using forward or backward shifts:

$$
y[k+1] + a_0 y[k] = b_0 u[k+1] + b_1 u[k], \qquad
y[k] + a_0 y[k-1] = b_0 u[k] + b_1 u[k-1]
$$

In general an $n$-th order difference equation reads

$$
y[k+n] + a_{n-1}y[k+n-1] + \cdots + a_0 y[k] = b_m u[k+m] + \cdots + b_0 u[k]
$$

and needs $n$ initial conditions (e.g. $y[0], \dots, y[n-1]$).

## Modeling examples

```{=latex}
\begin{example}[frametitle={Example - population migration}]
```

Each year, $a$ of the townspeople move to the suburbs and $b$ of the suburbanites move into the city:

$$
x_1[k+1] = (1-a)x_1[k] + b\,x_2[k], \qquad
x_2[k+1] = a\,x_1[k] + (1-b)x_2[k]
$$

In matrix form this is exactly the discrete state equation $\vec{x}[k+1] = \mathbf{A}\vec{x}[k]$ with

$$
\mathbf{A} = \begin{bmatrix} 1-a & b \\ a & 1-b \end{bmatrix}
$$

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - Samuelson's national income model}]
```

National income $y$, consumption $c$, investment $i$ and government spending $g$ satisfy $y[k] = c[k] + i[k] + g[k]$ with $c[k] = \alpha\,y[k-1]$ and $i[k] = \beta(c[k] - c[k-1])$. Substituting gives the second-order difference equation

$$
y[k] - \alpha(1+\beta)\,y[k-1] + \alpha\beta\, y[k-2] = g[k]
$$

with the government spending as input, and the income of the two previous periods as initial conditions.

```{=latex}
\end{example}
```

## Z-transform

The $z$-transform maps a sequence into a function of $z$:

$$
X(z) = \mathcal{Z}\{x[k]\} = \sum_{k=0}^{\infty} x[k]\, z^{-k}
$$

It turns shifts into algebra, exactly as the Laplace transform turns derivatives into algebra:

- **Linearity** — $\mathcal{Z}\{a x[k] + b y[k]\} = aX(z) + bY(z)$
- **Right shift (delay)** — $\mathcal{Z}\{x[k-1]\} = z^{-1}X(z)$
- **Left shift (advance)** — $\mathcal{Z}\{x[k+1]\} = z(X(z) - x[0])$
- **Convolution** — $\mathcal{Z}\{(x * y)[k]\} = X(z)Y(z)$, with $(x*y)[k] = \sum_i x[i]\,y[k-i]$

A few common pairs (inverse transform works by partial fractions, as with Laplace):

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

Exactly the same four ways as for $e^{\mathbf{A}t}$, with $\lambda_i^k$ in place of $e^{\lambda_i t}$:

- **Z-transform** — $\mathbf{A}^k = \mathcal{Z}^{-1}\{z(z\mathbf{I}-\mathbf{A})^{-1}\}$.
- **Diagonalization** — $\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}$, with $\boldsymbol{\Lambda}^k$ diagonal (entries $\lambda_i^k$); only if $\mathbf{A}$ is diagonalizable.
- **Cayley–Hamilton** — $\mathbf{A}^k = \alpha_0(k)\mathbf{I} + \cdots + \alpha_{n-1}(k)\mathbf{A}^{n-1}$, the $\alpha_i$ following from $\lambda_i^k = \alpha_0 + \alpha_1\lambda_i + \cdots$ (differentiate for repeated eigenvalues); works even for defective matrices.

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
