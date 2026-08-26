# State-space

## 1. State-space variables and equations

A system is captured by its state — the smallest set of variables that fully summarizes its past — plus how that state evolves and how it shapes the outputs. State variables are usually chosen as directly measurable or physically meaningful quantities: in electrical circuits the inductor currents and capacitor voltages, in mechanical systems the displacements and velocities. MIMO (multiple-input, multiple-output) systems bundle this into one picture, with the state vector living inside the system:

```{=latex}
\input{tikz/state-space-mimo.tex}
```

$\vec{u}$ collects the inputs, $\vec{y}$ the outputs, and $\vec{x}$ the states. In general (nonlinear, time-varying) systems the state and output equations read

$$
\dot{\vec{x}} = \mathbf{f}(\vec{x}, \vec{u}, t), \qquad
\vec{y} = \mathbf{g}(\vec{x}, \vec{u}, t)
$$

For linear time-invariant (LTI) systems they collapse to Kalman's matrix form:

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}
$$
$$
\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}
$$

with $\mathbf{A}$ ($n\times n$) the dynamics, $\mathbf{B}$ ($n\times p$) the input coupling, $\mathbf{C}$ ($q\times n$) the output coupling, and $\mathbf{D}$ ($q\times p$) the direct feedthrough — typically $\mathbf{D} = \mathbf{0}$. The outputs are generally not the states themselves — that is exactly what $\mathbf{C}$ and $\mathbf{D}$ capture.

The state variables are not unique. For the second-order ODE $\ddot{y} + 2\dot{y} + 3y = 4u$, the Modeling chapter chose $x_1 = y$, $x_2 = \dot{y}$:

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u, \qquad y = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}
$$

but swapping the order, $z_1 = \dot{y}$, $z_2 = y$, gives an equally valid triple with the same input–output behaviour:

$$
\dot{\vec{z}} = \begin{bmatrix} -2 & -3 \\ 1 & 0 \end{bmatrix}\vec{z} + \begin{bmatrix} 4 \\ 0 \end{bmatrix}u, \qquad y = \begin{bmatrix} 0 & 1 \end{bmatrix}\vec{z}
$$

In general, any invertible $\mathbf{T}$ defines new states $\tilde{\vec{x}} = \mathbf{T}^{-1}\vec{x}$ and yields the equivalent representation $\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}$, $\tilde{\mathbf{B}} = \mathbf{T}^{-1}\mathbf{B}$, $\tilde{\mathbf{C}} = \mathbf{C}\mathbf{T}$, $\tilde{\mathbf{D}} = \mathbf{D}$.

## 2. State-space representation

The state-space representation is a geometric view of the dynamics: at every instant the system sits at a point $\vec{x}(t)$ in state space, and the equations $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ push that point along a curve — the *trajectory*. For the example system from the Modeling chapter, $\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x}$ with $\vec{x}(0) = (1, 0)$, the state spirals into the origin (markers at integer times):

```{=latex}
\input{tikz/state-spiral.tex}
```

The decay and the oscillation come straight from the eigenvalues of $\mathbf{A}$ — here $-1 \pm j\sqrt{2}$, the negative real part damping the spiral, the imaginary part driving the rotation.

## 3. Homogeneous Solution

$$\dot{\vec{x}} = \mathbf{A}\vec{x}$$ 

with initial condition $\vec{x}(0) = \vec{x}_0$ is a linear ODE. The solution can be expressed in terms of the matrix exponential:

For the trivial case of homogeneous equations (homogeneous: no input, $\vec{u} = 0$), let's try solving it with scalars first:

$$
\dot{x} = a x
$$
$$
\dot{x} - a x = 0
$$

Then we insert $x = e^{\lambda t}$ (which per chain rule gives $\dot{x} = \lambda e^{\lambda t}$) and get:

$$
\lambda e^{\lambda t} - a e^{\lambda t} = 0
$$
$$
\lambda - a = 0
$$
$$
\lambda = a
$$

So $\lambda = a$ is the only root and the general solution is $x(t) = C e^{at}$, with $C$ fixed by the initial condition $x(0) = x_0$:

$$
x(t_0) = C e^{a{t_0}} \quad\Longrightarrow\quad C = x_0 e^{-a{t_0}} \quad\Longrightarrow\quad x(t) = x_0 e^{a(t-t_0)}.
$$

Where the last part is the solution of scalar homogeneous ODE. The solution of the vector case is a straightforward generalization.

By the analogy with the scalar case, we can try the same exponential solution for the vector case $\dot{\vec{x}} = \mathbf{A}\vec{x}$ (still homogeneous, $\vec{u} = 0$). Try the same exponential:


$$
\vec{X}_H = \vec{x}_0\, e^{\mathbf{A}(t-t_0)}
$$

which indeed satisfies $\vec{X}_H(t_0) = \vec{x}_0\, e^{\mathbf{A}(t_0-t_0)} = \vec{x}_0\, \mathbf{I} = \vec{x}_0$.

Solutions for the scalar case can be expressed as a Taylor series:

$$
e^{at} = 1 + at + \frac{(at)^2}{2!} + \frac{(at)^3}{3!} + \dots
$$

And since matrices are happily multipliable:

$$
e^{\mathbf{A}t} = \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!}
$$

And because mathematicians don't like writing/typing they decided to shorthand the $e^{\mathbf{A}(t-t_0)}$ to $\Phi(t)$ and call it the state transition matrix. So we can write the solution as:

$$
\vec{X}_H = \Phi(t) \vec{x}_0
$$

State transition matrix has the following properties:

1. $\Phi(0) = \mathbf{I}$ (identity matrix)
2. $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$
3. $\Phi(t_1 - t_2) = \Phi(t_1)\Phi^{-1}(t_2)$
4. $\frac{d}{dt}\Phi(t) = \mathbf{A}\Phi(t)$

## 4. Nonhomogeneous Solution

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}, \qquad \vec{x}(t_0) = \vec{x}_0
$$

Multiplying both sides by $e^{-\mathbf{A}t}$ a.k.a. $\Phi^{-1}(t)$ and moving the terms gives:

$$
e^{-\mathbf{A}t} \dot{\vec{x}} - e^{-\mathbf{A}t} \mathbf{A}\vec{x} = e^{-\mathbf{A}t} \mathbf{B}\vec{u}
$$

Then we notice that the left-hand side is a derivative of a product:
$$
\frac{d}{d\tau}\left(e^{-\mathbf{A}\tau} \vec{x}\right) = e^{-\mathbf{A}\tau} \dot{\vec{x}} - e^{-\mathbf{A}\tau} \mathbf{A}\vec{x}
$$

and we integrate both sides from $t_0$ to $t$:
$$
\int_{t_0}^{t} \frac{d}{d\tau}\left(e^{-\mathbf{A}\tau} \vec{x}\right) d\tau = \int_{t_0}^{t} e^{-\mathbf{A}\tau} \mathbf{B}\vec{u} d\tau
$$

By the fundamental theorem of calculus, the left-hand side evaluates to:

$$
\left[ e^{-\mathbf{A}\tau} \vec{x}(\tau) \right]_{t_0}^{t} = \int_{t_0}^{t} e^{-\mathbf{A}\tau} \mathbf{B}\vec{u}(\tau)\, d\tau
$$

Expanding the brackets:

$$
e^{-\mathbf{A}t} \vec{x}(t) - e^{-\mathbf{A}t_0} \vec{x}(t_0) = \int_{t_0}^{t} e^{-\mathbf{A}\tau} \mathbf{B}\vec{u}(\tau)\, d\tau
$$

Multiplying through by $e^{\mathbf{A}t}$ and recalling $\vec{x}(t_0) = \vec{x}_0$ gives the solution of the nonhomogeneous case:

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\vec{x}(t) = e^{\mathbf{A}(t-t_0)} \vec{x}(t_0) + \int_{t_0}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B}\vec{u}(\tau)\, d\tau
$}
\endgroup
\]
```

Where the first part is the homogeneous solution (response to initial conditions) and the second part is the particular solution (response to the input signal) in the form of a convolution integral:

$$
\int f(t-\tau) g(\tau) d\tau = f * g
$$

## 5. Obtaining the state-transition matrix

### $\Phi$ via the Taylor series

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via Taylor series}]
```

$\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. First compute the powers of $\mathbf{A}$:

$$
\mathbf{A}^2 = \mathbf{A}\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}
= \begin{bmatrix} 4 & 0 \\ -3 & 1 \end{bmatrix}
$$

$$
\mathbf{A}^3 = \mathbf{A}^2\mathbf{A} = \begin{bmatrix} 4 & 0 \\ -3 & 1 \end{bmatrix}\begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}
= \begin{bmatrix} -8 & 0 \\ 7 & -1 \end{bmatrix}
$$

Now insert these into the series $e^{\mathbf{A}t} = \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!}$, writing out the first four terms ($k = 0, 1, 2, 3$):

$$
e^{\mathbf{A}t} = \mathbf{I} + t\mathbf{A} + \frac{t^2}{2!}\mathbf{A}^2 + \frac{t^3}{3!}\mathbf{A}^3 + \dots
$$

$$
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
+ t \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}
+ \frac{t^2}{2} \begin{bmatrix} 4 & 0 \\ -3 & 1 \end{bmatrix}
+ \frac{t^3}{6} \begin{bmatrix} -8 & 0 \\ 7 & -1 \end{bmatrix} + \dots
$$

Adding these elementwise builds up one big matrix:

$$
e^{\mathbf{A}t} = \begin{bmatrix}
1 - 2t + \frac{4t^2}{2} - \frac{8t^3}{6} + \dots & 0 \\
t - \frac{3t^2}{2} + \frac{7t^3}{6} + \dots & 1 - t + \frac{t^2}{2} - \frac{t^3}{6} + \dots
\end{bmatrix}
$$

Taking a sharp look at each entry, we recognize familiar series $\sum x^k/k! = e^x$. Hence:

$$
\Phi(t) = e^{\mathbf{A}t} = \begin{bmatrix}
e^{-2t} & 0 \\
e^{-t} - e^{-2t} & e^{-t}
\end{bmatrix}
$$

```{=latex}
\end{example}
```

### $\Phi$ via the Laplace transform

Transform the whole ODE instead of guessing exponentials. Apply $\mathcal{L}$ to both sides of

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}
$$

using linearity and $\mathcal{L}\{\dot{\vec{x}}\} = s\mathbf{X}(s) - \vec{x}(0)$:

$$
s\mathbf{X}(s) - \vec{x}(0) = \mathbf{A}\mathbf{X}(s) + \mathbf{B}\mathbf{U}(s)
$$

Grouping the $\mathbf{X}(s)$ terms extracts $s\mathbf{I} - \mathbf{A}$:

$$
(s\mathbf{I} - \mathbf{A})\mathbf{X}(s) = \vec{x}(0) + \mathbf{B}\mathbf{U}(s)
$$

Multiplying through by $(s\mathbf{I} - \mathbf{A})^{-1}$:

$$
\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\vec{x}(0) + (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)
$$

Inverse-transforming term by term ($\vec{x}(0) = \vec{x}_0$):

$$
\vec{x}(t) = \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\}\vec{x}_0 + \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)\right\}
$$

The first term is the homogeneous response, the second is the convolution with $\vec{u}$, so comparing with the boxed solution of Section 4 identifies

$$
\mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\} = e^{\mathbf{A}t} = \Phi(t)
$$

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via Laplace transform}]
```

Same $\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$:

$$
s\mathbf{I} - \mathbf{A} = \begin{bmatrix} s+2 & 0 \\ -1 & s+1 \end{bmatrix}, \qquad
\det(s\mathbf{I} - \mathbf{A}) = (s+2)(s+1)
$$

$$
(s\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(s+2)(s+1)}\begin{bmatrix} s+1 & 0 \\ 1 & s+2 \end{bmatrix}
= \begin{bmatrix} \frac{1}{s+2} & 0 \\ \frac{1}{(s+1)(s+2)} & \frac{1}{s+1} \end{bmatrix}
$$

Inverse-transforming entry by entry ($\frac{1}{(s+1)(s+2)} = \frac{1}{s+1} - \frac{1}{s+2}$ by partial fractions, and $\mathcal{L}^{-1}\{\frac{1}{s+a}\} = e^{-at}$):

$$
\Phi(t) = \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\} = \begin{bmatrix}
e^{-2t} & 0 \\
e^{-t} - e^{-2t} & e^{-t}
\end{bmatrix}
$$

which (shockingly, I know!) matches the Taylor result.

```{=latex}
\end{example}
```

### $\Phi$ via diagonalization

Powers of a diagonal matrix are trivial, because for a diagonal matrix

$$
\boldsymbol{\Lambda}^k = \begin{bmatrix}
d_1^k & & \\
& \ddots & \\
& & d_n^k
\end{bmatrix}
$$

off-diagonal entries stay zero. Consequently $e^{\mathbf{A}t}$ Taylor-expands very nicely: the exponential of a diagonal matrix is the diagonal of scalar exponentials,

$$
e^{\mathbf{A}t} = \mathbf{I} + t\mathbf{A} + \frac{t^2}{2!}\mathbf{A}^2 + \frac{t^3}{3!}\mathbf{A}^3 + \dots = \begin{bmatrix} e^{d_1 t} & & \\ & \ddots & \\ & & e^{d_n t} \end{bmatrix} = \begin{bmatrix} \Phi_{11} & & \\ & \ddots & \\ & & \Phi_{nn} \end{bmatrix}
$$

i.e. entrywise $\Phi_{nn}(t) = \sum_{k=0}^{\infty} \frac{(d_n t)^k}{k!} = e^{d_n t}$.

#### Eigenvalues

Let's go on a little tangent and see how to diagonalize a matrix. The eigenvalues of $\mathbf{A}$ are the scalars $\lambda$ for which

$$
\mathbf{A}\vec{v} = \lambda\vec{v}
$$

has a nonzero solution $\vec{v} \ne 0$ — the eigenvector. Geometrically, $\mathbf{A}$ just stretches $\vec{v}$ by $\lambda$ without rotating it. Rearranging gives $(\mathbf{A} - \lambda\mathbf{I})\vec{v} = 0$, which has a nontrivial solution iff the matrix is singular, i.e.

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

So eigenvalues are the roots of the characteristic polynomial $\det(\mathbf{A} - \lambda\mathbf{I})$. For an $n \times n$ matrix this is a polynomial of degree $n$, so by the fundamental theorem of algebra there are $n$ eigenvalues counting multiplicity. Each eigenvalue carries two numbers:

- **Algebraic multiplicity** $m_{a,i}$ — how many times $\lambda_i$ occurs as a root of the characteristic polynomial. These sum to the matrix dimension: $\sum_i m_{a,i} = n$.
- **Geometric multiplicity** $m_{g,i}$ — the dimension of the eigenspace $\ker(\mathbf{A} - \lambda_i\mathbf{I})$, i.e. the number of linearly independent eigenvectors belonging to $\lambda_i$. Computed as the nullity $m_{g,i} = n - \operatorname{rank}(\mathbf{A} - \lambda_i\mathbf{I})$.

They are always related by $1 \le m_{g,i} \le m_{a,i}$. The gap $m_{a,i} - m_{g,i}$ measures how "defective" $\mathbf{A}$ is at $\lambda_i$: if $m_{g,i} < m_{a,i}$ there are not enough eigenvectors, and diagonalization fails.

In practice:

1. Solve $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ for the eigenvalues — factor the polynomial, use the quadratic formula for $2\times 2$, or numerical methods for larger matrices.
2. For each $\lambda_i$, solve $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v} = 0$; the number of free parameters in the solution is $m_{g,i}$.

$\mathbf{A}$ is diagonalizable iff $m_{g,i} = m_{a,i}$ for every $i$. This is always the case when all eigenvalues are distinct, since then $m_{g,i} = m_{a,i} = 1$.

```{=latex}
\begin{example}[frametitle={Example - eigenvalues and eigenvectors}]
```

Find the eigenvalues and eigenvectors of $\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$.

The characteristic polynomial (upper-triangular, so the eigenvalues sit on the diagonal):

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 1-\lambda & 0 & 0 \\ 0 & 2-\lambda & 1 \\ 0 & 0 & 2-\lambda \end{vmatrix} = (1-\lambda)(2-\lambda)^2 = 0
$$

so $\lambda_1 = 1$ with $\alpha_1 = 1$, and $\lambda_2 = 2$ with $\alpha_2 = 2$.

For $\lambda_1 = 1$, solve $(\mathbf{A} - \mathbf{I})\vec{v} = 0$:

$$
\begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}\vec{v} = 0
\quad\Longrightarrow\quad
v_3 = 0,\ v_2 = 0,\ v_1 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
$$

For $\lambda_2 = 2$, solve $(\mathbf{A} - 2\mathbf{I})\vec{v} = 0$:

$$
\begin{bmatrix} -1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}\vec{v} = 0
\quad\Longrightarrow\quad
v_1 = 0,\ v_3 = 0,\ v_2 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

Here $\gamma_2 = 1 < \alpha_2 = 2$: only two linearly independent eigenvectors exist, so $\mathbf{A}$ is defective and **not** diagonalizable.

```{=latex}
\end{example}
```

#### Diagonalization

When $m_{g,i} = m_{a,i}$ for every eigenvalue, there are exactly $n$ linearly independent eigenvectors $\vec{v}_1, \dots, \vec{v}_n$. Stack them as columns:

$$
\mathbf{V} = \begin{bmatrix} \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \end{bmatrix}
$$

Each eigenpair satisfies $\mathbf{A}\vec{v}_i = \lambda_i \vec{v}_i$, so all of them at once read

$$
\mathbf{A}\mathbf{V} = \mathbf{V}\boldsymbol{\Lambda}, \qquad
\boldsymbol{\Lambda} = \begin{bmatrix}
\lambda_1 & & \\
& \ddots & \\
& & \lambda_n
\end{bmatrix}
$$

Independence makes $\mathbf{V}$ invertible, so multiplying by $\mathbf{V}^{-1}$ from the right gives the factorization

$$
\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}
$$

This is the whole trick: $\mathbf{A}$ is just a diagonal matrix in a different basis. Powers pass through the same similarity ($\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}$), so the Taylor series telescopes into

$$
e^{\mathbf{A}t} = \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!}
= \mathbf{V} \left( \sum_{k=0}^{\infty} \frac{(\boldsymbol{\Lambda}t)^k}{k!} \right) \mathbf{V}^{-1}
= \mathbf{V} e^{\boldsymbol{\Lambda}t} \mathbf{V}^{-1}
$$

and since $e^{\boldsymbol{\Lambda}t}$ is the diagonal of scalar exponentials,

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\Phi(t) = e^{\mathbf{A}t} = \mathbf{V} e^{\boldsymbol{\Lambda}t} \mathbf{V}^{-1} = \mathbf{V} \begin{bmatrix}
e^{\lambda_1 t} & & \\
& \ddots & \\
& & e^{\lambda_n t}
\end{bmatrix} \mathbf{V}^{-1}
$}
\endgroup
\]
```

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via diagonalization}]
```

$\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. The characteristic equation $\det(\mathbf{A} - \lambda\mathbf{I}) = (-2-\lambda)(-1-\lambda) = 0$ gives distinct eigenvalues $\lambda_1 = -2$, $\lambda_2 = -1$, so $m_{g,i} = m_{a,i} = 1$ and $\mathbf{A}$ is diagonalizable.

Eigenvectors from $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v}_i = 0$, one eigenvalue at a time.

For $\lambda_1 = -2$: $(\mathbf{A} - (-2)\mathbf{I}) = \mathbf{A} + 2\mathbf{I}$, so

$$
(\mathbf{A} + 2\mathbf{I}) = \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}, \qquad
\begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}\vec{v}_1 = 0
\quad\Longrightarrow\quad
v_1 + v_2 = 0,\ v_1 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

For $\lambda_2 = -1$: $(\mathbf{A} - (-1)\mathbf{I}) = \mathbf{A} + \mathbf{I}$, so

$$
(\mathbf{A} + \mathbf{I}) = \begin{bmatrix} -1 & 0 \\ 1 & 0 \end{bmatrix}, \qquad
\begin{bmatrix} -1 & 0 \\ 1 & 0 \end{bmatrix}\vec{v}_2 = 0
\quad\Longrightarrow\quad
v_1 = 0,\ v_2 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

Assemble the pieces ($\det\mathbf{V} = 1$, so inversion is trivial):

$$
\mathbf{V} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}, \qquad
\mathbf{V}^{-1} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \qquad
\boldsymbol{\Lambda} = \begin{bmatrix} -2 & 0 \\ 0 & -1 \end{bmatrix}
$$

Putting it together,

$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{V} e^{\boldsymbol{\Lambda}t} \mathbf{V}^{-1}
= \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} e^{-2t} & 0 \\ 0 & e^{-t} \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}
= \begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}
$$

which (surprise, surprise) matches the Taylor and Laplace results. 

```{=latex}
\end{example}
```

The diagonalization method is perhaps the most elegant, but it fails for defective matrices. The Laplace method above and Cayley–Hamilton\footnote{A. Cayley coined the name \emph{matrix}; W. R. Hamilton invented the quaternions, which, like matrices, refuse to commute.} method below both work even for defective matrices.

### $\Phi$ via Cayley–Hamilton

The Cayley–Hamilton theorem states that every matrix satisfies its own characteristic equation.

$$
\det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_0
$$

Substituting the matrix for the scalar gives the zero matrix:

$$
\mathbf{A}^n + c_{n-1}\mathbf{A}^{n-1} + \cdots + c_0\mathbf{I} = \mathbf{0}
$$

So every power $\mathbf{A}^k$ with $k \ge n$ reduces to a combination of $\mathbf{I}, \mathbf{A}, \dots, \mathbf{A}^{n-1}$, and the matrix exponential must have the form

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A} + \cdots + \alpha_{n-1}(t)\mathbf{A}^{n-1}
$$

This is the whole power of the theorem: dividing any polynomial $p(\lambda)$ by the characteristic polynomial $g(\lambda) = \det(\lambda\mathbf{I}-\mathbf{A})$ leaves a remainder $r(\lambda)$ of degree at most $n-1$, and since $g(\mathbf{A}) = \mathbf{0}$,

$$
p(\mathbf{A}) = r(\mathbf{A})
$$

For an analytic function\footnote{An analytic function has derivatives of all orders and can be represented by a convergent power series (e.g. $e^{\mathbf{A}t}$ or $\sin\mathbf{A}$)} the same holds after expanding it in a Taylor series and reducing term by term.

Two ideas just came together: (1) $e^{\mathbf{A}t}$ collapses to the low-degree polynomial above because Cayley–Hamilton folds every power $\mathbf{A}^k$, $k \ge n$, back into $\mathbf{I}, \dots, \mathbf{A}^{n-1}$; (2) the coefficients are found by applying the same remainder trick to the *scalar* function $e^{\lambda t}$. Dividing $e^{\lambda t}$ by the characteristic polynomial $g(\lambda) = \det(\lambda\mathbf{I}-\mathbf{A})$ leaves a remainder of degree at most $n-1$,

$$
e^{\lambda t} = q(\lambda)\,g(\lambda) + \alpha_0(t) + \alpha_1(t)\lambda + \cdots + \alpha_{n-1}(t)\lambda^{n-1}
$$

whose coefficients are exactly the $\alpha_j(t)$ above — because $g(\mathbf{A}) = \mathbf{0}$ kills the $q(\mathbf{A})g(\mathbf{A})$ term the same way. At an eigenvalue, $g(\lambda_i) = 0$ by definition, so the $q(\lambda)g(\lambda)$ term drops out and each eigenvalue yields one scalar equation:

$$
e^{\lambda_i t} = \alpha_0(t) + \alpha_1(t)\lambda_i + \cdots + \alpha_{n-1}(t)\lambda_i^{n-1}, \qquad i = 1, \dots, n
$$

Think of it as interpolation: $r(\lambda) = \alpha_0 + \alpha_1\lambda + \cdots$ is the unique degree-$(n-1)$ polynomial whose graph passes through $(\lambda_i,\, e^{\lambda_i t})$ at every eigenvalue. Matching there fixes all $n$ unknowns $\alpha_j(t)$ — no infinite series needed.

Solving this Vandermonde system gives the $\alpha_j(t)$. If an eigenvalue $\lambda_i$ has algebraic multiplicity $m_{a,i}$, evaluating at $\lambda_i$ yields only one equation; the missing $m_{a,i}-1$ come from differentiating $f(\lambda) = r(\lambda)$ with respect to $\lambda$, $m_{a,i}-1$ times — each eigenvalue contributes exactly as many equations as its multiplicity. Unlike diagonalization, this works even for defective matrices (see the eigenvalues example).

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via Cayley–Hamilton}]
```

Same $\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. Characteristic equation:

$$
\det(\lambda\mathbf{I} - \mathbf{A}) = (\lambda+2)(\lambda+1) = \lambda^2 + 3\lambda + 2 = 0
$$

so $\mathbf{A}^2 + 3\mathbf{A} + 2\mathbf{I} = \mathbf{0}$, and with $n = 2$:

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A}
$$

Evaluate at the eigenvalues — a $2\times2$ linear system in the unknowns $(\alpha_0, \alpha_1)$ (the $t$ lives only in the known right-hand sides):

$$
\lambda_1 = -2: \quad e^{-2t} = \alpha_0 - 2\alpha_1
$$
$$
\lambda_2 = -1: \quad e^{-t} = \alpha_0 - \alpha_1
$$

Subtract the two equations to eliminate $\alpha_0$:

$$
e^{-2t} - e^{-t} = -\alpha_1 \quad\Longrightarrow\quad \alpha_1 = e^{-t} - e^{-2t}
$$

Back-substitute: $\alpha_0 = e^{-t} + \alpha_1 = 2e^{-t} - e^{-2t}$. Put the coefficients back into the matrix form $e^{\mathbf{A}t} = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}$ and multiply out:

$$
\Phi(t) = e^{\mathbf{A}t} = (2e^{-t} - e^{-2t})\mathbf{I} + (e^{-t} - e^{-2t})\mathbf{A}
= \begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}
$$

which (you guessed it) matches all previous methods. 

```{=latex}
\end{example}
```
```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ for non-diagonalizable A via Cayley–Hamilton}]
```
If we calculate eigenvalues for the following matrix:
$$
\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix}
$$
we find that it's not diagonalizable:
$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \det\begin{bmatrix} 1-\lambda & 0 & 0 \\ 1 & 1-\lambda & -3 \\ 0 & 0 & 1-\lambda \end{bmatrix} = (1-\lambda)^3
$$
so the only eigenvalue is $\lambda = 1$ with algebraic multiplicity $m_a = 3$, and geometric multiplicity $m_g = n - \operatorname{rank}(\mathbf{A} - \mathbf{I}) = 3 - 1 = 2 < 3 = m_a$ — defective, so diagonalization is out. We could use Laplace, but we're in the mood for Cayley–Hamilton.

**Step 1: set up the ansatz.** With $n = 3$ the exponential reduces to a degree-2 polynomial in $\mathbf{A}$:

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A} + \alpha_2(t)\mathbf{A}^2, \qquad
e^{\lambda t} = \alpha_0(t) + \alpha_1(t)\lambda + \alpha_2(t)\lambda^2
$$

**Step 2: handle the repeated eigenvalue by differentiating.** Evaluating the scalar equation at $\lambda = 1$ gives only one equation for three unknowns. The missing two come from differentiating with respect to $\lambda$ — the $\alpha_j$ depend on $t$, not on $\lambda$, so their $\lambda$-derivatives vanish:

$$
\frac{d}{d\lambda}:\quad t e^{\lambda t} = \alpha_1(t) + 2\alpha_2(t)\lambda
$$
$$
\frac{d^2}{d\lambda^2}:\quad t^2 e^{\lambda t} = 2\alpha_2(t)
$$

**Step 3: evaluate at $\lambda = 1$.** The single repeated eigenvalue contributes three equations, one per derivative order:

$$
e^{t} = \alpha_0 + \alpha_1 + \alpha_2, \qquad
t e^{t} = \alpha_1 + 2\alpha_2, \qquad
t^2 e^{t} = 2\alpha_2
$$

This triangular system solves bottom-up: $\alpha_2 = \frac{t^2}{2}e^t$, then $\alpha_1 = t e^t - 2\alpha_2 = e^t(t - t^2)$, and finally $\alpha_0 = e^t - \alpha_1 - \alpha_2 = e^t\!\left(1 - t + \frac{t^2}{2}\right)$.

**Step 4: assemble $\Phi(t)$.** First the needed power of $\mathbf{A}$:

$$
\mathbf{A}^2 = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix}
= \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & -6 \\ 0 & 0 & 1 \end{bmatrix}
$$

Substituting into $\Phi(t) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A} + \alpha_2\mathbf{A}^2$ and adding elementwise: every diagonal entry is $\alpha_0 + \alpha_1 + \alpha_2 = e^t$, while the only nonzero off-diagonals are $(2,1) = \alpha_1 + 2\alpha_2 = t e^t$ and $(2,3) = -3\alpha_1 - 6\alpha_2 = -3t e^t$. Hence

$$
\Phi(t) = e^{\mathbf{A}t} = \begin{bmatrix} e^t & 0 & 0 \\ t e^t & e^t & -3t e^t \\ 0 & 0 & e^t \end{bmatrix}
$$

```{=latex}
\end{example}
```

### Final remarks on obtaining $\Phi$

We have shown four ways to skin a cat, but at the end you still have the same dead cat. The Taylor series is the most general, flows nicely from rudimentary principles, but it is slow and tedious. Diagonalization is elegant, but fails for defective matrices. Laplace transform is a nice trick, but requires some algebraic manipulation. Cayley–Hamilton is a clever method, but requires solving a Vandermonde system. 

Cayley–Hamilton specifically will come in very handy when we'll talk about controllability and observability.

In practice, the choice of method depends on the specific matrix $\mathbf{A}$ and the context of the problem.
