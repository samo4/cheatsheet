# Appendix A: Math review

## Calculus

### Taylor series

Near a point $x_0$ a smooth function is its polynomial expansion — value, slope, curvature and all higher derivatives matched there:

$$
f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
= f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \cdots
$$

The $k!$ is the leftover from differentiating $x^k$ $k$ times, and the coefficients are read off the derivatives at $x_0$. Expanding at $x_0 = 0$ is the Maclaurin series, and three of those do all the work in these notes:

$$
e^{x} = \underbrace{1}_{\cos} + \underbrace{x}_{\sin} + \underbrace{\frac{x^{2}}{2!}}_{\cos} + \underbrace{\frac{x^{3}}{3!}}_{\sin} + \underbrace{\frac{x^{4}}{4!}}_{\cos} + \underbrace{\frac{x^{5}}{5!}}_{\sin} + \cdots
$$

The underbraces sort the terms by parity — the even powers build $\cos$, the odd powers build $\sin$.

Cutting after the linear term leaves the tangent line $f(x) \approx f(x_0) + f'(x_0)(x-x_0)$, good while the deviation $|x - x_0|$ is small and off by the size of the first discarded term — see the Linearization chapter.

## Linear algebra

### Matrix multiplication

Matrix multiplication is *row by column*: entry $(i,j)$ of $\mathbf{A}\mathbf{B}$ is row $i$ of $\mathbf{A}$ dotted with column $j$ of $\mathbf{B}$. The inner dimensions must match, $(m \times n)(n \times p) = (m \times p)$.

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

Note the order matters: $\mathbf{B}\mathbf{A}$ is $3\times3$, so it cannot equal the $2\times2$ $\mathbf{A}\mathbf{B}$. Matrix multiplication is *not* commutative.

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

Also useful later: $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$ and $\det(\mathbf{A}^{-1}) = 1/\det\mathbf{A}$. Swapping two rows or two columns multiplies the determinant by $-1$ — so reordering the columns of an eigenvector matrix only flips the sign.

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

```{=latex}
\begin{example}[frametitle={Example - Gauss saving your PFE}]
```

When doing lots of partial fraction expansion, Gauss can save you some writing. Your PFE brought you 3 equations in 3 unknowns, and you rewrite them to:

$$
\begin{bmatrix} 1 & 1 & 1 \\ 7 & 9 & 10 \\ 2 & 3 & 3 \end{bmatrix}\begin{bmatrix} A \\ B \\ C \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

Pack everything into one augmented matrix and row-reduce. A few heuristics for choosing the moves:

- *Work one column at a time, left to right.* The leading $1$ in row 1 is the pivot; kill everything below it by subtracting multiples of the pivot row, $R_i - a_{i1}R_1$ — here $R_2 - 7R_1$ and $R_3 - 2R_1$.
- *Favor a pivot of $1$.* The next pivot sits in column 2; row 3 already has a $1$ there, so swap it up ($R_2 \leftrightarrow R_3$) instead of pivoting on the $2$ and dragging fractions along.
- *The multiplier is always entry-over-pivot.* After the swap, column 2 of the bottom row holds a $2$ over pivot $1$, so the move is $R_3 - 2R_2$.
- *Rows above the current pivot are finished* — leave them alone. At the end, either back-substitute from the bottom, or keep eliminating upward ($R_i - a_{ic}R_p$) until the left block is $\mathbf{I}$ and read the answer off the last column.

$$
\left[\begin{array}{ccc|c} 1 & 1 & 1 & 0 \\ 7 & 9 & 10 & 0 \\ 2 & 3 & 3 & 1 \end{array}\right]
\xrightarrow{row_2 - 7row_1, \ row_3 - 2row_1}
\left[\begin{array}{ccc|c} 1 & 1 & 1 & 0 \\ 0 & 2 & 3 & 0 \\ 0 & 1 & 1 & 1 \end{array}\right]
$$

Swap the last two rows and eliminate again:

$$
\xrightarrow{row_2 \leftrightarrow row_3}
\left[\begin{array}{ccc|c} 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 \\ 0 & 2 & 3 & 0 \end{array}\right]
\xrightarrow{row_3 - 2row_2}
\left[\begin{array}{ccc|c} 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & -2 \end{array}\right]
$$

Now kill the entries above the pivots, top to bottom:

$$
\xrightarrow{row_2 - row_3, \ row_1 - row_3}
\left[\begin{array}{ccc|c} 1 & 1 & 0 & 2 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & -2 \end{array}\right]
\xrightarrow{row_1 - row_2}
\left[\begin{array}{ccc|c} 1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & -2 \end{array}\right]
$$

The left block is $\mathbf{I}$, so the augmented column is the solution — read it off directly, because row swaps cannot scramble your variables: a row is one *equation*, and columns keep their meaning, so $A,B,C$ stay glued to columns 1, 2, 3 no matter how you shuffle the rows. Only swapping *columns* would relabel the variables — and then you'd have to swap the names $A,B,C$ to match. $(A, B, C) = (-1, \ 3, \ -2)$

Side note: strictly, Gauss elimination is not the same as the (eigen)diagonalization below. Row reduction only left-multiplies $\mathbf{A}$ by elementary matrices, so it does *not* preserve eigenvalues — diagonalization is a similarity $\mathbf{P}^{-1}\mathbf{A}\mathbf{P}$ and needs column operations too. What elimination does give you is the rank, and that is exactly what detects the singularity behind $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$.

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

### Vectors, bases and norms

*Linear independence.* $\vec{v}_1, \dots, \vec{v}_k$ are independent when $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{0}$ forces all $c_i = 0$, i.e. none is a combination of the others. As matrix columns: rank $k$. In $\mathbb{R}^n$ at most $n$ of them.

*Basis.* $n$ independent vectors, stacked as columns of $\mathbf{T}$, form a basis; every $\vec{x}$ has unique coordinates $\tilde{\vec{x}}$ in it:

$$
\vec{x} = \mathbf{T}\tilde{\vec{x}}, \qquad \tilde{\vec{x}} = \mathbf{T}^{-1}\vec{x}, \qquad \tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}
$$

Same vector, new description.

*Orthonormal basis.* Orthogonal ($\vec{q}_i^T\vec{q}_j = 0$, $i \ne j$) plus normal ($\vec{q}_i^T\vec{q}_i = 1$). Then $\mathbf{Q}^{-1} = \mathbf{Q}^T$ and coordinates are dot products, $\tilde{x}_i = \vec{q}_i^T\vec{x}$.

*Vector norms.* A norm $\lVert\vec{x}\rVert$ measures the length of a vector and must satisfy:

- positivity: $\lVert\vec{x}\rVert \ge 0$, and $\lVert\vec{x}\rVert = 0$ only for $\vec{x} = \vec{0}$
- scaling: $\lVert c\vec{x}\rVert = |c|\,\lVert\vec{x}\rVert$
- triangle inequality: $\lVert\vec{x} + \vec{y}\rVert \le \lVert\vec{x}\rVert + \lVert\vec{y}\rVert$

Every norm defines a distance (a metric), $d(\vec{x}, \vec{y}) = \lVert\vec{x} - \vec{y}\rVert$, and the three properties above are exactly what a distance needs.

```{=latex}
\begin{example}[frametitle={Example - three ways to measure a street walk}]
```

In a city with a square street grid, the destination is 3 blocks east and 4 blocks north, $\vec{x} = \tvec{3, 4}$.

- $\lVert\vec{x}\rVert_1 = |x_1| + |x_2| + \cdots + |x_n| = 3 + 4 = 7$: a taxi has to follow the streets (the *Manhattan* distance).
- $\lVert\vec{x}\rVert_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} = \sqrt{3^2 + 4^2} = 5$: (as the crow flies.
- $\lVert\vec{x}\rVert_\infty = \max(|x_1|, |x_2|, \dots, |x_n|) = \max(3, 4) = 4$: moves of a chess king.

```{=latex}
\end{example}
```

### Linear algebraic equations

The rank $r = \operatorname{rank}\mathbf{A}$ is the number of linearly independent rows (or columns). For a system $\mathbf{A}\vec{x} = \vec{b}$ with $n$ unknowns:

- No solution if $\operatorname{rank}[\mathbf{A}\mid\vec{b}] > \operatorname{rank}\mathbf{A}$ (inconsistent).
- Exactly one solution if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] = n$.
- Infinitely many solutions if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] < n$; then there are $n - r$ free variables.

The homogeneous system $\mathbf{A}\vec{x} = \vec{0}$ always has the trivial solution $\vec{x} = \vec{0}$, and has nontrivial ones exactly when $\operatorname{rank}\mathbf{A} < n$, i.e. when $\mathbf{A}$ is singular ($\det\mathbf{A} = 0$). That is the exact condition behind the eigenvalue problem below.

*Range space and null space.* Two subspaces sort out the answers:

- range space (column space): all combinations of the columns, i.e. all $\mathbf{A}\vec{x}$. $\mathbf{A}\vec{x} = \vec{b}$ is solvable exactly when $\vec{b}$ lies in it. Its dimension is the rank $r$.
- null space (kernel): $\ker\mathbf{A} = \{\vec{x} : \mathbf{A}\vec{x} = \vec{0}\}$. Its dimension, the nullity, is $n - r$, one per free variable.

Together they give the rank–nullity theorem: every column is either a pivot or a free variable, so for $n$ columns

$$
n = \operatorname{rank}\mathbf{A} + \operatorname{nullity}\mathbf{A}
$$

The rank is the dimension of the range space.

*Structure of the solution.* If $\vec{x}_p$ is any one solution, every solution is $\vec{x} = \vec{x}_p + \vec{x}_h$ with $\vec{x}_h \in \ker\mathbf{A}$, unique exactly when $\ker\mathbf{A} = \{\vec{0}\}$. This is the same particular-plus-homogeneous split as for linear ODEs. The notes use both spaces: eigenvectors span $\ker(\mathbf{A} - \lambda\mathbf{I})$ (geometric multiplicity is its nullity), and reachable states form the range space of $\mathcal{C}$ (controllability).

```{=latex}
\begin{example}[frametitle={Rank}]
```

$$ \mathcal{O} = \begin{bmatrix} C \\ CA \end{bmatrix} = \begin{bmatrix} -1 & -1 \\ 3 & 7 \end{bmatrix}  $$

$\mathcal{O}$ is $2\times2$, so $n = 2$. Row-reduce — rank is unchanged by row operations, and the point is to force a zero under the first pivot, the same column-by-column drill as in the Gauss example above. This time the leading entry is $-1$, and the cheapest first move is to flip the row: $-R_1$ turns it into the favourite pivot $+1$ and spares every sign from here on — rank never minds a row being multiplied by $-1$. Then clear column 1 with $R_2 - 3R_1$:

$$
\mathcal{O} \sim \begin{bmatrix} 1 & 1 \\ 0 & 4 \end{bmatrix}
$$

($-R_1$: $[-1\ -1] \to [1\ 1]$; then $3 - 3\cdot1 = 0$, $7 - 3\cdot1 = 4$). Now independence is plain to see: with a $0$ in its first slot, row 2 could only be a multiple of row 1 if it were the *zero* multiple — any $\alpha\begin{bmatrix}1 & 1\end{bmatrix}$ starts with $\alpha$, which vanishes only for $\alpha = 0$ — and row 2 is not the zero row. Two pivots, one per row, so the rows are linearly independent and

$$
\operatorname{rank}\mathcal{O} = 2 = n,
$$

i.e. $\mathcal{O}$ has *full rank*.

Rectangular matrices work the same way, the rank is just capped by the smaller dimension, $\operatorname{rank}\mathbf{A} \le \min(m, n)$: a $3\times4$ matrix can carry at most three pivots. Take one with a dependency planted inside — row 3 was written as row 1 $+$ row 2:

$$
\mathbf{A} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 2 & 3 & 4 & 5 \\ 3 & 4 & 5 & 6 \end{bmatrix}
$$

Same drill — clear column 1 below the pivot ($R_2 - 2R_1$, $R_3 - 3R_1$), then column 2 ($R_3 - R_2$):

$$
\xrightarrow{R_2 - 2R_1, \ R_3 - 3R_1}
\begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 1 & 2 & 3 \end{bmatrix}
\xrightarrow{R_3 - R_2}
\begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Rows 2 and 3 came out identical, so one collapses to a zero row — row 3 added no new direction. Only two pivots survive, so

$$
\operatorname{rank}\mathbf{A} = 2 < 3,
$$

one short of full row rank. That is the same question the observability test $\operatorname{rank}\mathcal{O} = n$ asks: every row $\mathbf{C}\mathbf{A}^k$ must add a genuinely new direction, or the state cannot be reconstructed.

```{=latex}
\end{example}
```

*Square shortcut.* $full rank ⇔ \det\mathbf{A} \ne 0$ When the matrix is square, one number settles full rank: for $n\times n$ $\mathbf{A}$, $\operatorname{rank}\mathbf{A} = n$ exactly when $\det\mathbf{A} \ne 0$ — dependent rows or columns are precisely what make the determinant vanish, and their absence *is* full rank. This is the cheap route to the controllability and observability tests whenever the matrix comes out square: $\mathcal{C}$ is square only for a single input ($m = 1$), $\mathcal{O}$ only for a single output ($p = 1$). For rectangular matrices $\det$ is not even defined, so row-reduction is the only way.

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

### Cayley–Hamilton: an arbitrary function of a matrix

How do you compute an arbitrary function $f(\mathbf{A})$ of a matrix with Cayley–Hamilton? Let's take $\sin\mathbf{A}$ for example.

Cayley–Hamilton says $\mathbf{A}$ satisfies its own characteristic equation, so every power $\mathbf{A}^k$ with $k \ge n$ folds back into $\mathbf{I}, \mathbf{A}, \dots, \mathbf{A}^{n-1}$. Dividing $f$ by the characteristic polynomial $g(\lambda) = \det(\lambda\mathbf{I} - \mathbf{A})$ therefore leaves a remainder of degree at most $n - 1$ — and the $q$-term dies when the matrix is substituted:

$$
f(\lambda) = q(\lambda)\,g(\lambda) + \alpha_0 + \alpha_1\lambda + \cdots + \alpha_{n-1}\lambda^{n-1}
\qquad\Longrightarrow\qquad
f(\mathbf{A}) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A} + \cdots + \alpha_{n-1}\mathbf{A}^{n-1}
$$

because $g(\mathbf{A}) = \mathbf{0}$. So any analytic matrix function collapses to a polynomial of degree at most $n-1$ in $\mathbf{A}$, and the only unknowns are the $n$ scalars $\alpha_j$.

```{=latex}
\begin{example}[frametitle={Example - use C-H to calculate $\sin\mathbf{A}$}]
```

$$
\mathbf{A}= \begin{bmatrix} -3 & -1  \\ 0 & -2 \end{bmatrix}
$$

*Step 1 —* find the eigenvalues

We immediately clock that the matrix is triangular, so the eigenvalues are the diagonal entries: $\lambda_1 = -3$, $\lambda_2 = -2$.

With $n = 2$, C-H makes every higher power fold back — here $g(\lambda) = (\lambda+3)(\lambda+2) = \lambda^2 + 5\lambda + 6$, so $\mathbf{A}^2 = -5\mathbf{A} - 6\mathbf{I}$ — leaving a polynomial of degree at most $1$ in $\mathbf{A}$:

$$
\sin\mathbf{A} = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}
$$

*Step 2 —* the two unknowns need two equations. They come from the scalar twin $\sin\lambda = \alpha_0 + \alpha_1\lambda$ evaluated at the eigenvalues, where the $q(\lambda)g(\lambda)$ term dies — that is the whole reason C-H works — giving one equation per eigenvalue:

$$
\sin(-3) = \alpha_0 - 3\alpha_1, \qquad \sin(-2) = \alpha_0 - 2\alpha_1
$$

*Step 3 —* solve for $\alpha_0$ and $\alpha_1$. Subtracting the two equations kills $\alpha_0$, and what is left is the difference quotient:

$$
\alpha_1 = \frac{\sin(-3) - \sin(-2)}{-3 - (-2)} = \sin(-2) - \sin(-3) = \sin 3 - \sin 2
$$

then back-substitute into either equation, $\alpha_0 = \sin(-2) + 2\alpha_1 = 2\sin 3 - 3\sin 2$.

*Step 4 —* substitute back into the ansatz:

$$
\sin\mathbf{A} = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}
= (2\sin 3 - 3\sin 2)\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
+ (\sin 3 - \sin 2)\begin{bmatrix} -3 & -1 \\ 0 & -2 \end{bmatrix}
$$

$$
= \begin{bmatrix} 2\sin 3 - 3\sin 2 - 3\sin 3 + 3\sin 2 & -(\sin 3 - \sin 2) \\ 0 & 2\sin 3 - 3\sin 2 - 2\sin 3 + 2\sin 2 \end{bmatrix}
= \begin{bmatrix} -\sin 3 & \sin 2 - \sin 3 \\ 0 & -\sin 2 \end{bmatrix}
$$

Sanity check: $\mathbf{A}$ is triangular, so the answer must be triangular with $f$ applied on the diagonal — and it is, $-\sin 3$ and $-\sin 2$.

```{=latex}
\end{example}
```

## Continuous-time math

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

- Distinct linear factors $(s-a)(s-b)$: $\ \dfrac{A}{s-a} + \dfrac{B}{s-b}$
- Repeated factors $(s-a)^2$: $\ \dfrac{A}{s-a} + \dfrac{B}{(s-a)^2}$
- Irreducible quadratic $s^2 + \omega^2$: $\ \dfrac{As + B}{s^2 + \omega^2}$ ($\to$ sines and cosines)

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
