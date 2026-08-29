# Appendix A: Math review

## Linear algebra

### Matrix multiplication

Two matrices can be multiplied only when the number of columns of the left one equals the number of rows of the right one. If $\mathbf{A}$ is $m \times n$ and $\mathbf{B}$ is $n \times p$, then $\mathbf{C} = \mathbf{A}\mathbf{B}$ is $m \times p$ with entries

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj},
$$

i.e. entry $(i,j)$ is the dot product of row $i$ of $\mathbf{A}$ with column $j$ of $\mathbf{B}$.

```{=latex}
\begin{example}[frametitle={Example - 2×3 times 3×2}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}$. Since $\mathbf{A}$ is $2\times3$ and $\mathbf{B}$ is $3\times2$, the product is $2\times2$:

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}
$$

Entry by entry (just one to illustrate) :

$$
c_{11} = 1\cdot7 + 2\cdot9 + 3\cdot11 = 58
$$

hence

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 58 & 64 \\ 139 & 154 \end{bmatrix}.
$$

Note the order matters: $\mathbf{B}\mathbf{A}$ is $3\times3$, so it cannot equal the $2\times2$ $\mathbf{A}\mathbf{B}$. Matrix multiplication is **not** commutative.

```{=latex}
\end{example}
```

### Matrix determinant

The determinant is a single number attached to a square matrix. It decides invertibility ($\det\mathbf{A} \ne 0$) and, geometrically, how much the matrix scales volumes.

For a $2\times2$ matrix:

$$
\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc
$$

For $n\times n$, expand along a row or column (Laplace expansion); signs alternate $+,-,+,\dots$. For $3\times3$ along the first row:

$$
\det\begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}
= a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix}
- a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix}
+ a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}
$$

$\det\mathbf{A} = 0$ means the rows (or columns) are linearly dependent — the matrix crushes a volume to zero.

Also useful later: $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$ and $\det(\mathbf{A}^{-1}) = 1/\det\mathbf{A}$.

### Inverse of a matrix

The inverse $\mathbf{A}^{-1}$ is the matrix with $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. Two standard ways to compute it.

#### Existence of inverse

A square matrix is invertible (nonsingular) iff $\det\mathbf{A} \ne 0$.

```{=latex}
\begin{example}[frametitle={Example - for which $a$ is the matrix invertible?}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 4 & a \end{bmatrix}$.

$$
\det\mathbf{A} = 1\cdot(3a - 16) - 2\cdot(2a - 12) + 3\cdot(8 - 9) = 5 - a
$$

so $\mathbf{A}$ is invertible exactly for $a \ne 5$. At $a = 5$ the third row is a linear combination of the first two: $[3\ 4\ 5] = -[1\ 2\ 3] + 2[2\ 3\ 4]$.

```{=latex}
\end{example}
```

#### Gauss elimination

Row-reduce the augmented matrix $[\mathbf{A} \mid \mathbf{I}]$ until the left block is $\mathbf{I}$; the right block is then $\mathbf{A}^{-1}$.

```{=latex}
\begin{example}[frametitle={Example - inverse via Gauss elimination}]
```

$\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix}$. Augment and reduce:

$$
\left[\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 5 & 3 & 0 & 1 \end{array}\right]
\xrightarrow{R_1/2}
\left[\begin{array}{cc|cc} 1 & \frac12 & \frac12 & 0 \\ 5 & 3 & 0 & 1 \end{array}\right]
$$

$$
\xrightarrow{R_2 - 5R_1}
\left[\begin{array}{cc|cc} 1 & \frac12 & \frac12 & 0 \\ 0 & \frac12 & -\frac52 & 1 \end{array}\right]
\xrightarrow{2R_2}
\left[\begin{array}{cc|cc} 1 & \frac12 & \frac12 & 0 \\ 0 & 1 & -5 & 2 \end{array}\right]
$$

$$
\xrightarrow{R_1 - \frac12 R_2}
\left[\begin{array}{cc|cc} 1 & 0 & 3 & -1 \\ 0 & 1 & -5 & 2 \end{array}\right]
\quad\Longrightarrow\quad
\mathbf{A}^{-1} = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}
$$

```{=latex}
\end{example}
```

#### With cofactors

The adjugate formula

$$
\mathbf{A}^{-1} = \frac{1}{\det\mathbf{A}}\operatorname{adj}\mathbf{A},
$$

where $\operatorname{adj}\mathbf{A}$ is the transpose of the matrix of cofactors. For a $2\times2$ matrix where $a,b$ is the first row and $c,d$ the second row, this collapses to the famous formula

$$
\mathbf{A}^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix},
$$

Applying it to the same $\mathbf{A}$ above ($ad - bc = 1$):

$$
\mathbf{A}^{-1} = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix},
$$

which matches the Gauss result.

### System of equations and rank

The rank $r = \operatorname{rank}\mathbf{A}$ is the number of linearly independent rows (or columns). Vectors are linearly independent when none of them is a linear combination of the others. For a system $\mathbf{A}\vec{x} = \vec{b}$ with $n$ unknowns:

- **No solution** if $\operatorname{rank}[\mathbf{A}\mid\vec{b}] > \operatorname{rank}\mathbf{A}$ (inconsistent).
- **Exactly one solution** if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] = n$.
- **Infinitely many solutions** if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] < n$; then there are $n - r$ free variables.

The homogeneous system $\mathbf{A}\vec{x} = \vec{0}$ always has the trivial solution $\vec{x} = \vec{0}$, and has nontrivial ones exactly when $\operatorname{rank}\mathbf{A} < n$, i.e. when $\mathbf{A}$ is singular ($\det\mathbf{A} = 0$). That is the exact condition behind the eigenvalue problem below.

### Eigenvalues and eigenvectors

A common use for matrices is to describe linear transformations. A transformation $\vec{x}  \mapsto \mathbf{A}\vec{x}$ can stretch, shrink, rotate, or reflect vectors. Eigenvectors are the special directions that are only stretched or shrunk, not rotated.

A nonzero vector $\vec{x}$ is an eigenvector of $\mathbf{A}$ if multiplying by $\mathbf{A}$ just scales it:

$$
\mathbf{A}\vec{x} = \lambda\vec{x}
$$

The scalar $\lambda$ is the eigenvalue. Rearranging gives $(\mathbf{A} - \lambda\mathbf{I})\vec{x} = \vec{0}$, which has a nontrivial solution iff $\mathbf{A} - \lambda\mathbf{I}$ is singular (square, not invertable). Hence the eigenvalues are the roots of the characteristic polynomial

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

```{=latex}
\begin{example}[frametitle={Note - triangular matrices}]
```
If $\mathbf{A}$ is triangular (lower or upper), the determinant is just the product of the diagonal entries, so

$$\det(\mathbf{A} - \lambda\mathbf{I}) = \prod_i (a_{ii} - \lambda)$$

and the eigenvalues are exactly the diagonal entries $a_{11}, a_{22}, \dots, a_{nn}$. This is why triangular (and diagonal) matrices are so convenient — no characteristic polynomial to solve.
```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - eigenvalues and eigenvectors}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 0 & -1 \\ 1 & 2 & 1 \\ 2 & 2 & 3 \end{bmatrix}$. The characteristic polynomial:

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 1-\lambda & 0 & -1 \\ 1 & 2-\lambda & 1 \\ 2 & 2 & 3-\lambda \end{vmatrix} = (1-\lambda)(\lambda-2)(\lambda-3)
$$

so $\lambda_1 = 1$, $\lambda_2 = 2$, $\lambda_3 = 3$ — all distinct, hence $\mathbf{A}$ is diagonalizable.

For $\lambda = 1$, solve $(\mathbf{A} - \mathbf{I})\vec{x} = \vec{0}$:

$$
\begin{bmatrix} 0 & 0 & -1 \\ 1 & 1 & 1 \\ 2 & 2 & 2 \end{bmatrix}\vec{x} = \vec{0}
\quad\Longrightarrow\quad
x_3 = 0,\ x_1 + x_2 = 0
\quad\Longrightarrow\quad
\vec{x}_1 = \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}
$$

For $\lambda = 2$: $(\mathbf{A} - 2\mathbf{I})\vec{x} = \vec{0}$:

$$
\begin{bmatrix} -1 & 0 & -1 \\ 1 & 0 & 1 \\ 2 & 2 & 1 \end{bmatrix}\vec{x} = \vec{0}
\quad\Longrightarrow\quad
x_3 = -x_1,\ x_1 = -2x_2
\quad\Longrightarrow\quad
\vec{x}_2 = \begin{bmatrix} -2 \\ 1 \\ 2 \end{bmatrix}
$$

For $\lambda = 3$: $(\mathbf{A} - 3\mathbf{I})\vec{x} = \vec{0}$:

$$
\begin{bmatrix} -2 & 0 & -1 \\ 1 & -1 & 1 \\ 2 & 2 & 0 \end{bmatrix}\vec{x} = \vec{0}
\quad\Longrightarrow\quad
x_3 = -2x_1,\ x_2 = -x_1
\quad\Longrightarrow\quad
\vec{x}_3 = \begin{bmatrix} 1 \\ -1 \\ -2 \end{bmatrix}
$$

Sanity check: $\mathbf{A}\vec{x}_1 = \vec{x}_1$, $\mathbf{A}\vec{x}_2 = 2\vec{x}_2$, $\mathbf{A}\vec{x}_3 = 3\vec{x}_3$.

```{=latex}
\end{example}
```

Obviously a single eigenvalue can occur multiple times. We call this algebraic multiplicity and denote it as $m_a$. The number of linearly independent eigenvectors belonging to it is the geometric multiplicity $m_g$, always $1 \le m_g \le m_a$.

## Continuous-time math

### ODE

A linear ODE is one whose left-hand side is a linear operator $L$. Linearity is two properties bundled together:

- **Additivity**: $L[y_1 + y_2] = L[y_1] + L[y_2]$
- **Homogeneity**: $L[cy] = c\,L[y]$

Together, $L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2]$. The key consequence is **superposition**: if $y_1, y_2$ solve the homogeneous equation $L[y] = 0$, so does any linear combination $c_1 y_1 + c_2 y_2$. For example, $L[y] = \ddot{y} + 2\dot{y} + y$ is linear, whereas $L[y] = \dot{y}^2$ is not.

**Time invariance** means the system does not care when we start the clock: if $x(t)$ is the response to input $u(t)$, then $x(t - \tau)$ is the response to $u(t - \tau)$.

The state-space equation $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ is a linear, time-invariant (LTI) system — these two properties are exactly what let us use the Laplace transform and the matrix exponential below.

### Laplace

The Laplace transform maps a time function to a function of the complex variable $s$:

$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty f(t)\, e^{-st}\, dt
$$

Its superpower is that it turns differentiation into algebra (integration by parts):

$$
\mathcal{L}\{\dot{f}(t)\} = sF(s) - f(0)
$$

the $f(0)$ term carrying the initial condition. Along with linearity this is why an ODE becomes an algebraic equation — exactly what Section 5 does to $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$. A few workhorse pairs:

$$
\mathcal{L}\{1\} = \frac{1}{s}, \qquad
\mathcal{L}\{t\} = \frac{1}{s^2}, \qquad
$$
$$
\mathcal{L}\{e^{at}\} = \frac{1}{s-a}, \qquad
\mathcal{L}\{t e^{at}\} = \frac{1}{(s-a)^2}
$$
$$
\mathcal{L}\{\sin\omega t\} = \frac{\omega}{s^2+\omega^2}, \qquad
\mathcal{L}\{\cos\omega t\} = \frac{s}{s^2+\omega^2}
$$

### Partial fraction decomposition

Inverse Laplace transforms are read off a table, so the goal is to split a rational function $F(s) = N(s)/D(s)$ (with $\deg N < \deg D$) into pieces that match table entries. Factor $D(s)$ and decompose:

- **Distinct linear factors** $(s-a)(s-b)$: $\ \dfrac{A}{s-a} + \dfrac{B}{s-b}$
- **Repeated factors** $(s-a)^2$: $\ \dfrac{A}{s-a} + \dfrac{B}{(s-a)^2}$
- **Irreducible quadratic** $s^2 + \omega^2$: $\ \dfrac{As + B}{s^2 + \omega^2}$ ($\to$ sines and cosines)

```{=latex}
\begin{example}[frametitle={Example - partial fractions}]
```

Split $\dfrac{1}{(s+1)^2(s+2)}$ — a repeated factor plus a distinct one, so three coefficients:

$$
\frac{1}{(s+1)^2(s+2)} = \frac{A}{s+1} + \frac{B}{(s+1)^2} + \frac{C}{s+2}
$$

Multiplying through by $(s+1)^2(s+2)$:

$$
1 = A(s+1)(s+2) + B(s+2) + C(s+1)^2
$$

Plug in the roots to kill terms: $s = -2$ gives $1 = C$, and $s = -1$ gives $1 = B$. The last coefficient comes from the $s^2$ terms: $0 = A + C$, so $A = -1$:

$$
\frac{1}{(s+1)^2(s+2)} = -\frac{1}{s+1} + \frac{1}{(s+1)^2} + \frac{1}{s+2}
$$

With $\mathcal{L}^{-1}\{\frac{1}{s+a}\} = e^{-at}$ and $\mathcal{L}^{-1}\{\frac{1}{(s+a)^2}\} = t e^{-at}$:

$$
\mathcal{L}^{-1}\left\{\frac{1}{(s+1)^2(s+2)}\right\} = -e^{-t} + t e^{-t} + e^{-2t}
$$

```{=latex}
\end{example}
```
