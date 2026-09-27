# Linear algebra

This chapter collects the linear algebra used throughout the rest of the notes. It mostly follows chapter 3 of @chen1999linear. Chen writes $\mathbf{Q}$ for any basis matrix; here $\mathbf{T}$ is a general basis and $\mathbf{Q}$ an orthonormal one. Another source is the lecture series @abbott2012linear.

## Matrix multiplication

Matrix multiplication is *row by column*: entry $(i,j)$ of $\mathbf{A}\mathbf{B}$ is row $i$ of $\mathbf{A}$ dotted with column $j$ of $\mathbf{B}$. The inner dimensions must match, $(m \times n)(n \times p) = (m \times p)$.

```{=latex}
\begin{example}[frametitle={Example - 2×3 times 3×2}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}$. Since $\mathbf{A}$ is $2\times3$ and $\mathbf{B}$ is $3\times2$, the product is $2\times2$:

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}
$$

Entry by entry (just one) :

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

## Vectors, bases and norms

*Linear independence.* a set of vectors is independent when $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{0}$ iff all $c_i = 0$, i.e. none is a combination of the others. As matrix columns: rank $k$. In $\mathbb{R}^n$ at most $n$ of them.

*Basis.* $n$ independent vectors, stacked as columns of $\mathbf{T}$, form a basis; every $\vec{x}$ has unique coordinates $\tilde{\vec{x}}$ in it:

$$
\vec{x} = \mathbf{T}\tilde{\vec{x}}, \qquad \tilde{\vec{x}} = \mathbf{T}^{-1}\vec{x}, \qquad \tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}
$$

Same vector, new description. ($\mathbf{T}^{-1}$ exists because the columns are independent; inverses are covered under linear algebraic equations.)

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
- $\lVert\vec{x}\rVert_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} = \sqrt{3^2 + 4^2} = 5$: as the crow flies.
- $\lVert\vec{x}\rVert_\infty = \max(|x_1|, |x_2|, \dots, |x_n|) = \max(3, 4) = 4$: moves of a chess king (the *Chebyshev* distance).

```{=latex}
\end{example}
```

*Dot product.* Multiply matching entries and add them up $\vec{x}^T\vec{y}$. The result is a single number, not a vector. Geometrically, $\vec{x}^T\vec{y} = \lVert\vec{x}\rVert_2\,\lVert\vec{y}\rVert_2\cos\theta$, with $\theta$ the angle between the two arrows, so it measures how much they point the same way.

*Orthonormal.* Two vectors are orthogonal when their dot product is zero. A vector is *normal* (normalized) when it has unit length, $\vec{q}^T\vec{q} = 1$.\footnote{Order matters. Mulitplying a vector by its transposed self gives the inner product — a single number. If you swap it around you get a matrix. Incidently: dot product and inner product are not strictly the same thing.} Why it is worth having? Stack the basis as columns of $\mathbf{Q}$. Entry $(i,j)$ of $\mathbf{Q}^T\mathbf{Q}$ is exactly $\vec{q}_i^T\vec{q}_j$, so the conditions above say $\mathbf{Q}^T\mathbf{Q} = \mathbf{I}$ — the inverse comes free by transposing:

$$
\mathbf{Q}^{-1} = \mathbf{Q}^T, \qquad \tilde{\vec{x}} = \mathbf{Q}^T\vec{x}, \qquad \tilde{x}_i = \vec{q}_i^T\vec{x}
$$

Each coordinate is simply the shadow of $\vec{x}$ on one basis vector. In a general basis $\mathbf{T}$ the coordinates are coupled and you have to solve $\mathbf{T}\tilde{\vec{x}} = \vec{x}$. Lengths and angles also survive the change. Such $\mathbf{Q}$ are rotations and reflections — they move the grid but never stretch it.

```{=latex}
\begin{example}[frametitle={Example - coordinates in a rotated grid}]
```

Take the axes rotated by 45°:

$$
\vec{q}_1 = \tfrac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ 1 \end{bmatrix}, \qquad
\vec{q}_2 = \tfrac{1}{\sqrt{2}}\begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$

Check: $\vec{q}_1^T\vec{q}_2 = \tfrac{1}{2}(-1 + 1) = 0$ and $\vec{q}_1^T\vec{q}_1 = \vec{q}_2^T\vec{q}_2 = \tfrac{1}{2}(1 + 1) = 1$, so orthonormal. The coordinates of $\vec{x} = \tvec{3, 1}$ are two dot products:

$$
\tilde{x}_1 = \vec{q}_1^T\vec{x} = \tfrac{3 + 1}{\sqrt{2}} = 2\sqrt{2}, \qquad
\tilde{x}_2 = \vec{q}_2^T\vec{x} = \tfrac{-3 + 1}{\sqrt{2}} = -\sqrt{2}
$$

Rebuild to confirm: $2\sqrt{2}\,\vec{q}_1 - \sqrt{2}\,\vec{q}_2 = \tvec{2, 2} - \tvec{-1, 1} = \tvec{3, 1}$. Length is unchanged too: $3^2 + 1^2 = 10 = (2\sqrt{2})^2 + (\sqrt{2})^2$.

```{=latex}
\end{example}
```

## Linear algebraic equations

The rank $r = \operatorname{rank}\mathbf{A}$ is the number of linearly independent rows (or columns). Multiplying by an invertible matrix never changes it, which is why row operations (left-multiplication by invertible elementary matrices) are safe for finding the rank. For a system $\mathbf{A}\vec{x} = \vec{b}$ with $n$ unknowns:

- No solution if $\operatorname{rank}[\mathbf{A}\mid\vec{b}] > \operatorname{rank}\mathbf{A}$.
- Exactly one solution if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] = n$.
- Infinitely many solutions if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] < n$.

The homogeneous system $\mathbf{A}\vec{x} = \vec{0}$ always has the trivial solution $\vec{x} = \vec{0}$, and has nontrivial ones exactly when $\operatorname{rank}\mathbf{A} < n$, i.e. when $\mathbf{A}$ is singular ($\det\mathbf{A} = 0$).

*Range space and null space.* Two subspaces sort out the answers above:

- range space (column space): all combinations of the columns, i.e. all $\mathbf{A}\vec{x}$. $\mathbf{A}\vec{x} = \vec{b}$ is solvable exactly when $\vec{b}$ lies in it. Its dimension is the rank $r$.
- null space (kernel): $\ker\mathbf{A} = \{\vec{x} : \mathbf{A}\vec{x} = \vec{0}\}$. Its dimension, the nullity, is $n - r$, one per free variable.

Together they give the rank–nullity theorem: every column is either a pivot or a free variable, so for $n$ columns

$$
\text{number of columns of } \mathbf{A} = \operatorname{rank}\mathbf{A} + \operatorname{nullity}\mathbf{A}
$$

The rank is the dimension of the range space.

```{=latex}
\begin{example}[frametitle={Example - a range space you can see}]
```

$$
\mathbf{A} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}, \qquad
\vec{y} = \mathbf{A}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} x_1 + x_3 \\ x_2 + x_3 \end{bmatrix}
$$

Only two rows, so every output lives in $\mathbb{R}^2$ and the rank can be at most $2$, however many columns there are. Columns 1 and 2 are already the two unit vectors $\vec{e}_1, \vec{e}_2$, so they reach every direction of the plane. Column 3 is column 1 $+$ column 2 and adds nothing. The range space is all of $\mathbb{R}^2$, and $\operatorname{rank}\mathbf{A} = 2$.

So every $\vec{b}$ is reachable, e.g. $\mathbf{A}\vec{x} = \tvec{1, 2}$ with $\vec{x} = \tvec{1, 2, 0}$. With $n = 3$ columns and rank $2$, the nullity is $1$: the same dependency, read as $\text{col}_1 + \text{col}_2 - \text{col}_3 = \vec{0}$, gives $\ker\mathbf{A} = \operatorname{span}\{\tvec{1, 1, -1}\}$. So the solution is not unique: $\vec{x} = \tvec{1, 2, 0} + t\,\tvec{1, 1, -1}$ for any $t$. Three unknowns, two equations, one direction left free.

```{=latex}
\end{example}
```

*Structure of the solution.* If $\vec{x}_p$ is any one solution, every solution is $\vec{x} = \vec{x}_p + \vec{x}_h$ with $\vec{x}_h \in \ker\mathbf{A}$, unique exactly when $\ker\mathbf{A} = \{\vec{0}\}$. This is the same particular-plus-homogeneous split as for linear ODEs. The notes use both spaces: eigenvectors span $\ker(\mathbf{A} - \lambda\mathbf{I})$ (geometric multiplicity is its nullity), and reachable states form the range space of $\mathcal{C}$ (controllability).

*Rank of a product.* Read $\mathbf{A}\mathbf{B}$ by columns and by rows. Each column of $\mathbf{A}\mathbf{B}$ is $\mathbf{A}$ times a column of $\mathbf{B}$, so it is a combination of the columns of $\mathbf{A}$, and there cannot be more independent ones than $\operatorname{rank}\mathbf{A}$. Each row of $\mathbf{A}\mathbf{B}$ is a combination of the rows of $\mathbf{B}$, weighted by a row of $\mathbf{A}$, so there cannot be more independent ones than $\operatorname{rank}\mathbf{B}$. Together:

$$
\operatorname{rank}(\mathbf{A}\mathbf{B}) \le \min(\operatorname{rank}\mathbf{A}, \operatorname{rank}\mathbf{B})
$$

Put simply, multiplying can never raise the rank, only keep it or lower it. An invertible factor keeps it, because it can be undone. That is why row operations are safe, and why controllability and observability don't change when the state coordinates change. It also caps each block of $\mathcal{C}$: $\operatorname{rank}(\mathbf{A}^k\mathbf{B}) \le \operatorname{rank}\mathbf{B} \le m$.

```{=latex}
\begin{example}[frametitle={Rank}]
```

$$ \mathcal{O} = \begin{bmatrix} C \\ CA \end{bmatrix} = \begin{bmatrix} -1 & -1 \\ 3 & 7 \end{bmatrix}  $$

$\mathcal{O}$ is $2\times2$, so $n = 2$. Row-reduce — rank is unchanged by row operations, and the point is to force a zero under the first pivot, the column-by-column drill detailed under Gauss elimination below. This time the leading entry is $-1$, and the cheapest first move is to flip the row: $-R_1$ turns it into the favourite pivot $+1$ and spares every sign from here on — rank never minds a row being multiplied by $-1$. Then clear column 1 with $R_2 - 3R_1$:

$$
\mathcal{O} \sim \begin{bmatrix} 1 & 1 \\ 0 & 4 \end{bmatrix}
$$

($-R_1$: $[-1\ -1] \to [1\ 1]$; then $3 - 3\cdot1 = 0$, $7 - 3\cdot1 = 4$). Now independence is plain to see: with a $0$ in its first slot, row 2 could only be a multiple of row 1 if it were the *zero* multiple — any $\alpha\begin{bmatrix}1 & 1\end{bmatrix}$ starts with $\alpha$, which vanishes only for $\alpha = 0$ — and row 2 is not the zero row. Two pivots, one per row, so the rows are linearly independent and

$$
\operatorname{rank}\mathcal{O} = 2 = n,
$$

i.e. $\mathcal{O}$ has *full rank*.

Rectangular matrices work the same way, the rank is just capped by the smaller dimension, $\operatorname{rank}\mathbf{A} \le \min(m, n)$. A tall $3\times2$ has the same shape as an $\mathcal{O}$ with $n = 2$ states; here row 2 was planted as $2\times$ row 1:

$$
\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 7 \end{bmatrix}
\xrightarrow{R_2 - 2R_1, \ R_3 - 3R_1}
\begin{bmatrix} 1 & 2 \\ 0 & 0 \\ 0 & 1 \end{bmatrix}
$$

Row 2 collapses to zero, but row 3 still leaves a pivot in column 2, so $\operatorname{rank}\mathbf{A} = 2 = n$, which is *full column rank*. That is exactly what the observability test $\operatorname{rank}\mathcal{O} = n$ asks for. A redundant row costs nothing, as long as the other rows $\mathbf{C}\mathbf{A}^k$ still supply all $n$ directions.

```{=latex}
\end{example}
```

### Determinant

The determinant is a single number attached to a square matrix. It decides invertibility ($\det\mathbf{A} \ne 0$) and, geometrically, how much the matrix scales volumes. $\det\mathbf{A} = 0$ means the rows (or columns) are linearly dependent.

For a $2\times2$ matrix:

$$
\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
$$

For $n\times n$, expand along a row or column; signs alternate $+,-,+,\dots$.

*Square shortcut.* $full rank ⇔ \det\mathbf{A} \ne 0$ When the matrix is square, one number settles full rank: for $n\times n$ $\mathbf{A}$, $\operatorname{rank}\mathbf{A} = n$ exactly when $\det\mathbf{A} \ne 0$ — dependent rows or columns are precisely what make the determinant vanish, and their absence *is* full rank. This is the often the cheapest route to any rank tests of square matrices that you might encounter.

Also useful later: $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$ and $\det(\mathbf{A}^{-1}) = 1/\det\mathbf{A}$. Swapping two rows or two columns multiplies the determinant by $-1$ — so reordering the columns of an eigenvector matrix only flips the sign.

### Inverse of a matrix

The inverse $\mathbf{A}^{-1}$ is the matrix with $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. Two standard ways to compute it: Gaussian elimination and the adjugate formula with cofactors.

#### Existence of inverse

A square matrix is invertible (nonsingular) iff $\det\mathbf{A} \ne 0$.

```{=latex}
\begin{example}[frametitle={Example - for which $a$ is the matrix invertible?}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 4 & a \end{bmatrix}$.

$$
\det\mathbf{A} = 1\begin{vmatrix} 3 & 4 \\ 4 & a \end{vmatrix} - 2\begin{vmatrix} 2 & 4 \\ 3 & a \end{vmatrix} + 3\begin{vmatrix} 2 & 3 \\ 3 & 4 \end{vmatrix} = (3a - 16) - 2(2a - 12) + 3(8 - 9) = 5 - a
$$

so $\mathbf{A}$ is invertible exactly for $a \ne 5$. At $a = 5$ the third row is a linear combination of the first two: $[3\ 4\ 5] = -[1\ 2\ 3] + 2[2\ 3\ 4]$.

```{=latex}
\end{example}
```

#### Gauss elimination

Row-reduce the augmented matrix $[\mathbf{A} \mid \mathbf{I}]$ until the left block is $\mathbf{I}$; the right block is then $\mathbf{A}^{-1}$.

```{=latex}
\begin{example}[frametitle={Example - Gauss saving your PFE}]
```

The same moves solve $\mathbf{A}\vec{x} = \vec{b}$ directly: augment with the single column $\vec{b}$ instead of $\mathbf{I}$. Partial fractions are where this pays off: matching coefficients leaves you with two equations in two unknowns,

$$
\begin{bmatrix} 1 & 1 \\ 2 & 1 \end{bmatrix}\begin{bmatrix} A \\ B \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}
$$

A few heuristics for choosing the moves:

- *Work one column at a time, left to right.* The leading $1$ in row 1 is the pivot; kill everything below it with $R_i - a_{i1}R_1$ — the multiplier is always entry-over-pivot.
- *Favor a pivot of $1$.* Swap a row with a $1$ up, or flip a $-1$ with $-R_i$, rather than dragging fractions along.
- *Rows above the current pivot are finished* — leave them alone until the end, then eliminate upward until the left block is $\mathbf{I}$.

Row operations act on every column the same way, so nothing stops you carrying $\vec{b}$ *and* $\mathbf{I}$ along at once, $[\mathbf{A} \mid \vec{b} \mid \mathbf{I}]$ — one reduction, two answers:

$$
\left[\begin{array}{cc|c|cc} 1 & 1 & 1 & 1 & 0 \\ 2 & 1 & 3 & 0 & 1 \end{array}\right]
\xrightarrow{R_2 - 2R_1}
\left[\begin{array}{cc|c|cc} 1 & 1 & 1 & 1 & 0 \\ 0 & -1 & 1 & -2 & 1 \end{array}\right]
$$

$$
\xrightarrow{-R_2}
\left[\begin{array}{cc|c|cc} 1 & 1 & 1 & 1 & 0 \\ 0 & 1 & -1 & 2 & -1 \end{array}\right]
\xrightarrow{R_1 - R_2}
\left[\begin{array}{cc|c|cc} 1 & 0 & 2 & -1 & 1 \\ 0 & 1 & -1 & 2 & -1 \end{array}\right]
$$

The left block is $\mathbf{I}$, so the middle column is the solution, $(A, B) = (2, -1)$, and the right block is the inverse,

$$
\mathbf{A}^{-1} = \begin{bmatrix} -1 & 1 \\ 2 & -1 \end{bmatrix}, \qquad
\mathbf{A}\mathbf{A}^{-1} = \begin{bmatrix} -1+2 & 1-1 \\ -2+2 & 2-1 \end{bmatrix} = \mathbf{I}.
$$

Once you have $\mathbf{A}^{-1}$, any other right-hand side is just a multiplication, $\vec{x} = \mathbf{A}^{-1}\vec{b}$, with no reduction to redo. Row operations, swaps included, never scramble the variables: a row is one *equation*, and $A, B$ stay glued to columns 1 and 2. Only swapping *columns* would relabel them.

Sanity check against the original, not the reduced system: $2 - 1 = 1$, $2(2) - 1 = 3$.

Side note: strictly, Gauss elimination is not the same as the (eigen)diagonalization below. Row reduction only left-multiplies $\mathbf{A}$ by elementary matrices, so it does *not* preserve eigenvalues — diagonalization is a similarity $\mathbf{T}^{-1}\mathbf{A}\mathbf{T}$ and needs column operations too. What elimination does give you is the rank, and that is exactly what detects the singularity behind $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$.

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

## Eigenvalues and eigenvectors

A common use for matrices is to describe linear transformations. A transformation $\vec{x}  \mapsto \mathbf{A}\vec{x}$ can stretch, shrink, rotate, or reflect vectors. Eigenvectors are the special directions that are only stretched or shrunk, not rotated.

A nonzero vector $\vec{x}$ is an eigenvector of $\mathbf{A}$ if multiplying by $\mathbf{A}$ just scales it:

$$
\mathbf{A}\vec{x} = \lambda\vec{x}
$$

The scalar $\lambda$ is the eigenvalue. Rearranging gives $(\mathbf{A} - \lambda\mathbf{I})\vec{x} = \vec{0}$, so the eigenvectors are the null space of $\mathbf{A} - \lambda\mathbf{I}$ (without $\vec{0}$), called the eigenspace. A nonzero one exists iff that null space is nontrivial, i.e. $\mathbf{A} - \lambda\mathbf{I}$ is singular (rank below $n$, not invertible). Hence the eigenvalues are the roots of the characteristic polynomial

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

```{=latex}
\begin{example}[frametitle={Note - triangular matrices}]
```
If $\mathbf{A}$ is triangular (lower or upper), the determinant is just the product of the diagonal entries, so the eigenvalues are exactly the diagonal entries $a_{11}, a_{22}, \dots, a_{nn}$. This is why triangular (and diagonal) matrices are so convenient — no characteristic polynomial to solve.
```{=latex}
\end{example}
```

Geometrically, each eigenspace is a subspace through the origin, and on it $\mathbf{A}$ acts as plain scaling by $\lambda$. Take a matrix with eigenvalues $\lambda = 7$ and $\lambda = -4$ [@lay2015linear]. Solving $(\mathbf{A} - 7\mathbf{I})\vec{x} = \vec{0}$ gives $x_1 = x_2$, and $(\mathbf{A} + 4\mathbf{I})\vec{x} = \vec{0}$ gives $5x_1 + 6x_2 = 0$, so

$$
E_7 = \operatorname{span}\left\{\begin{bmatrix} 1 \\ 1 \end{bmatrix}\right\},
\qquad
E_{-4} = \operatorname{span}\left\{\begin{bmatrix} -6 \\ 5 \end{bmatrix}\right\}.
$$

Both are lines crossing at $\vec{0}$. A vector on $E_7$ is stretched 7 times along its own line; one on $E_{-4}$ is stretched 4 times and flipped, but stays on its line. Any other vector, e.g. $\vec{w} = (-\tfrac12, -1)$ with $\mathbf{A}\vec{w} = (-\tfrac{13}{2}, -\tfrac92)$, is knocked off its line:

```{=latex}
\input{tikz/eigenspaces-lay.tex}
```

Granted, it it might be hard to visualize in higher dimensions, but the principle is the same: each eigenspace is a subspace where the matrix acts as simple scaling.

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

#### Algebraic multiplicity

An single eigenvalue can be a repeated root of the characteristic polynomial. The number of times it repeats is its algebraic multiplicity $m_a$.

#### Geometric multiplicity

The geometric multiplicity $m_g$ of an eigenvalue is the number of linearly independent eigenvectors belonging to it. In practice it is the number of free variables left when you solve $(\mathbf{A} - \lambda\mathbf{I})\vec{x} = \vec{0}$. Geometrically, it says whether the eigenspace is a line ($m_g = 1$), a plane ($m_g = 2$), and so on. It always satisfies $1 \le m_g \le m_a$. Both $2\times2$ matrices below have $\lambda = 1$ with $m_a = 2$:

- $\mathbf{I}$ scales every vector by 1, so its eigenspace is the whole plane: $m_g = 2$.
- The shear $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ leaves only the $x_1$ axis in place, so its eigenspace is that one line: $m_g = 1$.

When $m_g < m_a$ for some eigenvalue, the matrix is *defective*. Its eigenvectors cannot span the whole space.

## Similarity transformation

A matrix describes a linear map in a particular basis. Take the map $\vec{y} = \mathbf{A}\vec{x}$ and describe both vectors in a new basis. To picture it, it is exactly the eigenspace figure above, with $\vec{x} = \vec{w}$ and $\vec{y} = \mathbf{A}\vec{w}$. With an invertible $\mathbf{T}$ whose columns are the new basis vectors written in the old coordinates, the old coordinates follow from the new ones as

$$
\underbrace{\vec{x}}_{\text{old}} = \mathbf{T}\underbrace{\tilde{\vec{x}}}_{\text{new}}, \qquad \underbrace{\vec{y}}_{\text{old}} = \mathbf{T}\underbrace{\tilde{\vec{y}}}_{\text{new}}
$$

Where:

- $\mathbf{A}$ is the map. It moves vectors, $\vec{w} \mapsto \mathbf{A}\vec{w}$.
- $\mathbf{T}$ is a change of coordinates (hence $\mathbf{T}$, for transformation). It only relabels the same vector in a new grid.

Substitute into $\vec{y} = \mathbf{A}\vec{x}$ and solve for $\tilde{\vec{y}}$:

$$
\mathbf{T}\tilde{\vec{y}} = \mathbf{A}\mathbf{T}\tilde{\vec{x}} \quad\Longrightarrow\quad \tilde{\vec{y}} = \underbrace{\mathbf{T}^{-1}\mathbf{A}\mathbf{T}}_{\tilde{\mathbf{A}}}\,\tilde{\vec{x}}
$$

Read right to left: $\mathbf{T}$ translates the input from new to old coordinates, $\mathbf{A}$ acts there, and $\mathbf{T}^{-1}$ translates the result back to new coordinates. Two matrices related this way are called similar:

$$
\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}
$$

Same map, different coordinates. So everything that belongs to the map, not to the coordinates, is left unchanged. The characteristic polynomial carries over because $\mathbf{T}^{-1}\mathbf{T} = \mathbf{I}$ can be slipped under the determinant:

$$
\det(\tilde{\mathbf{A}} - \lambda\mathbf{I}) = \det\!\big(\mathbf{T}^{-1}(\mathbf{A} - \lambda\mathbf{I})\mathbf{T}\big) = \det\mathbf{T}^{-1}\,\det(\mathbf{A} - \lambda\mathbf{I})\,\det\mathbf{T} = \det(\mathbf{A} - \lambda\mathbf{I})
$$

and with it everything the polynomial encodes:

- the eigenvalues with their algebraic multiplicities,
- $\det\tilde{\mathbf{A}} = \det\mathbf{A} = \prod_i \lambda_i$ and $\operatorname{tr}\tilde{\mathbf{A}} = \operatorname{tr}\mathbf{A} = \sum_i \lambda_i$,
- the rank, and the geometric multiplicities (since $\tilde{\mathbf{A}} - \lambda\mathbf{I}$ is similar to $\mathbf{A} - \lambda\mathbf{I}$).

The eigenvectors are *not* unchanged. They are the same arrows, but their coordinates change: if $\mathbf{A}\vec{v} = \lambda\vec{v}$, then $\tilde{\mathbf{A}}(\mathbf{T}^{-1}\vec{v}) = \lambda(\mathbf{T}^{-1}\vec{v})$.

```{=latex}
\begin{example}[frametitle={Example - the same map in a basis rotated by 45°}]
```

Old basis: the usual orthonormal $\vec{e}_1 = \tvec{1, 0}$, $\vec{e}_2 = \tvec{0, 1}$. New basis: the same pair rotated by 45°, still orthonormal,

$$
\vec{t}_1 = \tfrac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ 1 \end{bmatrix}, \qquad
\vec{t}_2 = \tfrac{1}{\sqrt{2}}\begin{bmatrix} -1 \\ 1 \end{bmatrix}, \qquad
\mathbf{T} = [\vec{t}_1\ \vec{t}_2] = \tfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}
$$

$\mathbf{T}$ is a rotation, so its inverse is free: $\mathbf{T}^{-1} = \mathbf{T}^\mathsf{T}$ (true for any orthonormal columns). Take the map

$$
\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}
$$

In the old basis it is hard to read: it both stretches and turns each basis vector ($\vec{e}_1 \mapsto \tvec{2, 1}$). In the new one:

$$
\tilde{\mathbf{A}} = \mathbf{T}^\mathsf{T}\mathbf{A}\mathbf{T}
= \tfrac{1}{2}\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}
= \tfrac{1}{2}\begin{bmatrix} 3 & 3 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}
= \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}
$$

So there was never any turning: the map stretches by 3 along the diagonal $\vec{t}_1$ and leaves the anti-diagonal $\vec{t}_2$ alone. The rotated basis just happens to line up with what $\mathbf{A}$ does.

*Follow one vector through.* Take $\vec{x} = \vec{e}_1 = \tvec{1, 0}$.

- Old coordinates: $\vec{y} = \mathbf{A}\vec{x} = \tvec{2, 1}$.
- New coordinates: $\tilde{\vec{x}} = \mathbf{T}^\mathsf{T}\vec{x} = \tfrac{1}{\sqrt{2}}\tvec{1, -1}$, then $\tilde{\vec{y}} = \tilde{\mathbf{A}}\tilde{\vec{x}} = \tfrac{1}{\sqrt{2}}\tvec{3, -1}$.
- Back to old: $\mathbf{T}\tilde{\vec{y}} = \tfrac{3}{2}\tvec{1, 1} - \tfrac{1}{2}\tvec{-1, 1} = \tvec{2, 1}$. Same arrow, as it must be.

*What survived and what didn't.*

- Eigenvalues $3, 1$ in both. $\operatorname{tr} = 4$ and $\det = 3$ in both.
- The eigenvectors are the same arrows but not the same numbers: $\vec{t}_1, \vec{t}_2$ in old coordinates, $\tvec{1, 0}, \tvec{0, 1}$ in new ones.
- The entries of the matrix did not survive at all. The off-diagonal 1s were a property of the coordinates, not of the map.

This is diagonalization in miniature: the columns of $\mathbf{T}$ are exactly the eigenvectors of $\mathbf{A}$, which is why $\tilde{\mathbf{A}}$ came out diagonal.

```{=latex}
\end{example}
```

*Functions pass through.* In a power the inner $\mathbf{T}\mathbf{T}^{-1}$ pairs cancel, $\tilde{\mathbf{A}}^k = \mathbf{T}^{-1}\mathbf{A}^k\mathbf{T}$, and so does every power series built from powers:

$$
f(\mathbf{T}^{-1}\mathbf{A}\mathbf{T}) = \mathbf{T}^{-1}f(\mathbf{A})\,\mathbf{T}, \qquad\text{e.g.}\quad e^{\mathbf{A}t} = \mathbf{T}\,e^{\tilde{\mathbf{A}}t}\,\mathbf{T}^{-1}
$$

This is the practical reason to change basis: pick $\mathbf{T}$ so that $\tilde{\mathbf{A}}$ makes $f$ easy, compute $f(\tilde{\mathbf{A}})$, and transform back.

*In state space* a similarity is simply a new choice of state variables, $\vec{x} = \mathbf{T}\tilde{\vec{x}}$. The same substitution as above, now into $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ and $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$, gives

$$
\mathbf{T}\dot{\tilde{\vec{x}}} = \mathbf{A}\mathbf{T}\tilde{\vec{x}} + \mathbf{B}\vec{u} \quad\Longrightarrow\quad \dot{\tilde{\vec{x}}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}\,\tilde{\vec{x}} + \mathbf{T}^{-1}\mathbf{B}\,\vec{u}, \qquad \vec{y} = \mathbf{C}\mathbf{T}\,\tilde{\vec{x}} + \mathbf{D}\vec{u}
$$

so $(\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}) \mapsto (\mathbf{T}^{-1}\mathbf{A}\mathbf{T},\ \mathbf{T}^{-1}\mathbf{B},\ \mathbf{C}\mathbf{T},\ \mathbf{D})$. Here only the state changes coordinates; $\vec{u}$ and $\vec{y}$ are untouched, which is why $\mathbf{B}$ gets only a $\mathbf{T}^{-1}$ and $\mathbf{C}$ only a $\mathbf{T}$. Poles, stability and the transfer function do not notice it.

*Diagonalization.* The easiest $\tilde{\mathbf{A}}$ of all is diagonal, and the basis that gets you there is made of eigenvectors. Put $n$ independent eigenvectors in the columns of $\mathbf{T} = \mathbf{V}$. Then $\mathbf{A}\vec{v}_i = \lambda_i\vec{v}_i$, stacked column by column, reads $\mathbf{A}\mathbf{V} = \mathbf{V}\boldsymbol{\Lambda}$, i.e.

$$
\mathbf{V}^{-1}\mathbf{A}\mathbf{V} = \boldsymbol{\Lambda} = \operatorname{diag}(\lambda_1, \dots, \lambda_n), \qquad f(\mathbf{A}) = \mathbf{V}\operatorname{diag}\big(f(\lambda_1), \dots, f(\lambda_n)\big)\mathbf{V}^{-1}
$$

The 45° example was exactly this with $\mathbf{V} = \mathbf{T}$. For the eigenvalue example above, $\mathbf{V} = [\vec{x}_1\ \vec{x}_2\ \vec{x}_3]$ gives $\operatorname{diag}(1, 2, 3)$. In state space the new states are the *modes*: each $\dot{\tilde{x}}_i = \lambda_i\tilde{x}_i + (\mathbf{V}^{-1}\mathbf{B}\vec{u})_i$ evolves on its own, and $\Phi(t) = \mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}$. The State space chapter works this through in detail.

The catch is the word *independent*: there must be $n$ of them, i.e. $m_g = m_a$ for every eigenvalue. A defective matrix has too few, and then *no* $\mathbf{T}$ at all makes it diagonal. Take $\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$. If it were similar to a diagonal matrix, that matrix would carry the eigenvalues $2, 2$, so it would be $2\mathbf{I}$. But $\mathbf{T}^{-1}(2\mathbf{I})\mathbf{T} = 2\mathbf{I} \ne \mathbf{A}$ for every $\mathbf{T}$. The best one can do is the Jordan form, and this $\mathbf{A}$ already is one. See $\Phi$ via the Jordan form in the State space chapter.

## Functions of a square matrix

Starting with Cayley in 1858, people asked whether run-of-the-mill scalar functions such as $\sqrt{x}$, $e^x$, $\sin x$ and $\cos x$ have any meaning when applied to a matrix. As a matter of fact, they do for square matrices.

A function of a square matrix is defined by its power series: if the scalar function's Taylor series $f(\lambda) = \sum_k c_k\lambda^k$ converges, then $f(\mathbf{A}) = \sum_k c_k\mathbf{A}^k$. That is what $e^{\mathbf{A}t}$, $\sin\mathbf{A}$ or $\mathbf{A}^k$ mean. The infinite series is useless by hand, but Cayley–Hamilton theorem (introduced in the State space chapter) collapses it: $\mathbf{A}$ satisfies its own characteristic equation, so every power $\mathbf{A}^k$ with $k \ge n$ folds back into $\mathbf{I}, \mathbf{A}, \dots, \mathbf{A}^{n-1}$. Dividing $f$ by the characteristic polynomial $g(\lambda) = \det(\lambda\mathbf{I} - \mathbf{A})$ therefore leaves a remainder of degree at most $n - 1$, and the $q$-term dies when the matrix is substituted:

$$
f(\lambda) = q(\lambda)\,g(\lambda) + \alpha_0 + \alpha_1\lambda + \cdots + \alpha_{n-1}\lambda^{n-1}
\qquad\Longrightarrow\qquad
f(\mathbf{A}) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A} + \cdots + \alpha_{n-1}\mathbf{A}^{n-1}
$$

because $g(\mathbf{A}) = \mathbf{0}$. So any analytic matrix function collapses to a polynomial of degree at most $n-1$ in $\mathbf{A}$, and the only unknowns are the $n$ scalars $\alpha_j$. The recipe, for any $f$:

1. Find the eigenvalues of $\mathbf{A}$.
2. Write the ansatz $f(\mathbf{A}) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A} + \cdots + \alpha_{n-1}\mathbf{A}^{n-1}$.
3. Match the scalar twin $f(\lambda_i) = \alpha_0 + \alpha_1\lambda_i + \cdots + \alpha_{n-1}\lambda_i^{n-1}$ at every eigenvalue. An eigenvalue with algebraic multiplicity $m_a$ gives only one equation, so also match the first $m_a - 1$ derivatives with respect to $\lambda$ there.
4. Solve for the $\alpha_j$ and substitute back into the ansatz.

The main text uses this recipe with two particular functions: $f(\lambda) = e^{\lambda t}$ gives the state-transition matrix $\Phi(t) = e^{\mathbf{A}t}$ (State space chapter), and $f(\lambda) = \lambda^k$ gives $\mathbf{A}^k$ (Discrete chapter). When $\mathbf{A}$ is diagonalizable, the result equals $\mathbf{V}\operatorname{diag}\big(f(\lambda_1), \dots, f(\lambda_n)\big)\mathbf{V}^{-1}$ from the previous section. Cayley–Hamilton just gets there without the eigenvectors, and it also works for defective matrices.

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
