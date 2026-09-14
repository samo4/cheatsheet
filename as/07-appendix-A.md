# Appendix A: Math review

## Linear algebra

### Matrix multiplication

Two matrices can be multiplied only when the number of columns of the left one equals the number of rows of the right one. If $\mathbf{A}$ is $m \times n$ and $\mathbf{B}$ is $n \times p$, then $\mathbf{C} = \mathbf{A}\mathbf{B}$ is $m \times p$ with entries

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj},
$$

i.e. entry $(i,j)$ is the dot product of row $i$ of $\mathbf{A}$ with column $j$ of $\mathbf{B}$.

```{=latex}
\begin{example}[frametitle={Remember - row by column}]
```

Matrix multiplication is **row by column**: row $i$ of the left matrix against column $j$ of the right matrix, entry by entry. The inner dimensions must match: columns of the left = rows of the right.

```{=latex}
\end{example}
```

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

Side note: strictly, Gauss elimination is not the same as the (eigen)diagonalization below. Row reduction only left-multiplies $\mathbf{A}$ by elementary matrices, so it does **not** preserve eigenvalues — diagonalization is a similarity $\mathbf{P}^{-1}\mathbf{A}\mathbf{P}$ and needs column operations too. What elimination does give you is the rank, and that is exactly what detects the singularity behind $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$.

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

i.e. $\mathcal{O}$ has **full rank**.

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

**Square shortcut.** $full rank ⇔ \det\mathbf{A} \ne 0$ When the matrix is square, one number settles full rank: for $n\times n$ $\mathbf{A}$, $\operatorname{rank}\mathbf{A} = n$ exactly when $\det\mathbf{A} \ne 0$ — dependent rows or columns are precisely what make the determinant vanish, and their absence *is* full rank. This is the cheap route to the controllability and observability tests whenever the matrix comes out square: $\mathcal{C}$ is square only for a single input ($m = 1$), $\mathcal{O}$ only for a single output ($p = 1$). For rectangular matrices $\det$ is not even defined, so row-reduction is the only way.

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

**The question.** How do you compute an arbitrary function $f(\mathbf{A})$ of a matrix with Cayley–Hamilton? This is the general case of the $\Phi$ computation in the State-space chapter (there the scalar function was $e^{\lambda t}$); here it is on $\sin\mathbf{A}$.

#### The idea

Cayley–Hamilton says $\mathbf{A}$ satisfies its own characteristic equation, so every power $\mathbf{A}^k$ with $k \ge n$ folds back into $\mathbf{I}, \mathbf{A}, \dots, \mathbf{A}^{n-1}$. Dividing $f$ by the characteristic polynomial $g(\lambda) = \det(\lambda\mathbf{I} - \mathbf{A})$ therefore leaves a remainder of degree at most $n - 1$ — and the $q$-term dies when the matrix is substituted:

$$
f(\lambda) = q(\lambda)\,g(\lambda) + \alpha_0 + \alpha_1\lambda + \cdots + \alpha_{n-1}\lambda^{n-1}
\qquad\Longrightarrow\qquad
f(\mathbf{A}) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A} + \cdots + \alpha_{n-1}\mathbf{A}^{n-1}
$$

because $g(\mathbf{A}) = \mathbf{0}$. So any analytic matrix function collapses to a polynomial of degree at most $n-1$ in $\mathbf{A}$, and the only unknowns are the $n$ scalars $\alpha_j$.

#### The recipe

1. Write the characteristic polynomial $g(\lambda) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_0$, i.e. find the eigenvalues **with their multiplicities**.
2. Ansatz: $f(\mathbf{A}) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A} + \cdots + \alpha_{n-1}\mathbf{A}^{n-1}$, together with its scalar twin $f(\lambda) = \alpha_0 + \alpha_1\lambda + \cdots + \alpha_{n-1}\lambda^{n-1}$.
3. Substitute each distinct eigenvalue. At $\lambda_i$ the $q$-term dies too ($g(\lambda_i) = 0$), which gives one linear equation per eigenvalue:
   $$f(\lambda_i) = \alpha_0 + \alpha_1\lambda_i + \cdots + \alpha_{n-1}\lambda_i^{n-1}$$
4. If $\lambda_i$ has algebraic multiplicity $m_i$, that one equation is not enough — differentiate the scalar identity $m_i - 1$ times, matching the derivatives as well:
   $$f^{(j)}(\lambda_i) = \left.\frac{d^j}{d\lambda^j}\left(\alpha_0 + \alpha_1\lambda + \cdots + \alpha_{n-1}\lambda^{n-1}\right)\right|_{\lambda = \lambda_i}, \qquad j = 0, 1, \dots, m_i - 1$$
5. Solve the resulting $n \times n$ Vandermonde system for the $\alpha_j$ and put them back into the ansatz.

Read it as **interpolation**: $f(\mathbf{A})$ is the unique degree-$\le n-1$ polynomial in $\mathbf{A}$ that matches $f$ — and, at a repeated eigenvalue, also matches $f', f'', \dots$ — at the eigenvalues. Nothing here is special to $e^{\lambda t}$; the same five steps give $e^{\mathbf{A}t}$, $\sin\mathbf{A}$, $\cos\mathbf{A}$, $\sqrt{\mathbf{A}}$, $\mathbf{A}^{-1}$.

#### $2\times2$ closed forms

Distinct eigenvalues $\lambda_1 \ne \lambda_2$:

$$
f(\mathbf{A}) = \frac{f(\lambda_1)(\mathbf{A} - \lambda_2\mathbf{I}) - f(\lambda_2)(\mathbf{A} - \lambda_1\mathbf{I})}{\lambda_1 - \lambda_2}
$$

which is the same as $\alpha_1 = \dfrac{f(\lambda_1) - f(\lambda_2)}{\lambda_1 - \lambda_2}$ and $\alpha_0 = \dfrac{\lambda_1 f(\lambda_2) - \lambda_2 f(\lambda_1)}{\lambda_1 - \lambda_2}$.

Double eigenvalue $\lambda$ (the two eigenvalues of the Vandermonde system merge into a value and a slope):

$$
f(\mathbf{A}) = f(\lambda)\mathbf{I} + f'(\lambda)(\mathbf{A} - \lambda\mathbf{I})
$$

#### Example — $\sin$ of a $2\times2$ matrix, distinct eigenvalues

Take

$$
\mathbf{A} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \qquad
g(\lambda) = \det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^2 - 1 = (\lambda - 1)(\lambda + 1), \qquad \lambda_{1,2} = \pm 1
$$

With $n = 2$, $\sin\mathbf{A} = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}$ and $\sin\lambda = \alpha_0 + \alpha_1\lambda$. Two eigenvalues, two equations — evaluating at the eigenvalues is the only place the actual $f$ enters:

$$
\lambda = 1: \quad \sin 1 = \alpha_0 + \alpha_1, \qquad
\lambda = -1: \quad \sin(-1) = -\sin 1 = \alpha_0 - \alpha_1
$$

Adding gives $2\alpha_0 = 0$; subtracting gives $2\alpha_1 = 2\sin 1$:

$$
\alpha_0 = 0, \qquad \alpha_1 = \sin 1
\qquad\Longrightarrow\qquad
\sin\mathbf{A} = (\sin 1)\,\mathbf{A} = \begin{bmatrix} 0 & \sin 1 \\ \sin 1 & 0 \end{bmatrix}
$$

**Check without Cayley–Hamilton.** $\mathbf{A}^2 = \mathbf{I}$, so every even power is $\mathbf{I}$ and every odd power is $\mathbf{A}$, and the series collapses term by term:

$$
\sin\mathbf{A} = \mathbf{A} - \frac{\mathbf{A}^3}{3!} + \frac{\mathbf{A}^5}{5!} - \cdots
= \left(1 - \frac{1}{3!} + \frac{1}{5!} - \cdots\right)\mathbf{A} = (\sin 1)\,\mathbf{A}
$$

#### Example — $\sin$ of a $2\times2$ matrix with a double eigenvalue

$$
\mathbf{A} = \begin{bmatrix} \pi/2 & 1 \\ 0 & \pi/2 \end{bmatrix}, \qquad
g(\lambda) = \left(\lambda - \frac{\pi}{2}\right)^2
$$

Now $m = 2$ for the single eigenvalue $\lambda = \pi/2$, so evaluating $\sin\lambda = \alpha_0 + \alpha_1\lambda$ at $\pi/2$ gives only one equation; the second one comes from differentiating it, i.e. from $\cos\lambda = \alpha_1$:

$$
\sin\frac{\pi}{2} = \alpha_0 + \alpha_1\frac{\pi}{2}, \qquad
\cos\frac{\pi}{2} = \alpha_1
$$

So $\alpha_1 = 0$ (that is why no $\mathbf{A}$ survives) and $\alpha_0 = 1$:

$$
\sin\mathbf{A} = \mathbf{I} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

**Check without Cayley–Hamilton.** Write $\mathbf{A} = \frac{\pi}{2}\mathbf{I} + \mathbf{N}$ with $\mathbf{N} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ and $\mathbf{N}^2 = \mathbf{0}$. Since $\mathbf{N}$ is nilpotent, $\sin\mathbf{N} = \mathbf{N}$ and $\cos\mathbf{N} = \mathbf{I}$, so

$$
\sin\left(\frac{\pi}{2}\mathbf{I} + \mathbf{N}\right)
= \sin\frac{\pi}{2}\cos\mathbf{N} + \cos\frac{\pi}{2}\sin\mathbf{N}
= \mathbf{I}\cdot\mathbf{I} + 0\cdot\mathbf{N} = \mathbf{I}
$$

The same $f'$ pattern holds for a Jordan block with any $\lambda$:

$$
\sin\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}
= \begin{bmatrix} \sin\lambda & \cos\lambda \\ 0 & \sin\lambda \end{bmatrix}
$$

#### Example — complex eigenvalues

Complex eigenvalues need no special machinery — the same two equations, only the scalar identities change. For

$$
\mathbf{A} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}, \qquad \lambda_{1,2} = \pm i
$$

$$
\alpha_1 = \frac{\sin i - \sin(-i)}{i - (-i)} = \frac{\sin i}{i} = \sinh 1, \qquad
\alpha_0 = \sin i - \alpha_1 i = i\sinh 1 - i\sinh 1 = 0
$$

using $\sin(-z) = -\sin z$ and $\sin i = i\sinh 1$. Hence

$$
\sin\mathbf{A} = (\sinh 1)\,\mathbf{A} = \begin{bmatrix} 0 & -\sinh 1 \\ \sinh 1 & 0 \end{bmatrix}
$$

**Check without Cayley–Hamilton.** $\mathbf{A}^2 = -\mathbf{I}$, so $\mathbf{A}^{2k+1} = \mathbf{A}(\mathbf{A}^2)^k = (-1)^k\mathbf{A}$ and the two sign flips cancel:

$$
\sin\mathbf{A} = \mathbf{A} - \frac{\mathbf{A}^3}{3!} + \frac{\mathbf{A}^5}{5!} - \cdots
= \mathbf{A}\left(1 + \frac{1}{3!} + \frac{1}{5!} + \cdots\right) = (\sinh 1)\,\mathbf{A}
$$

#### The exam answer in three sentences

- Cayley–Hamilton makes $\mathbf{A}$ satisfy its own characteristic polynomial, so any analytic function of $\mathbf{A}$ reduces to a polynomial of degree at most $n-1$ in $\mathbf{A}$ — that is the remainder of dividing $f(\lambda)$ by $g(\lambda)$.
- The $n$ coefficients are fixed by matching $f$ at the eigenvalues, one equation per eigenvalue, plus $f', f'', \dots$ at any eigenvalue that repeats (multiplicity $m$: differentiate $m-1$ times).
- Then solve the Vandermonde system and substitute back — for a matrix with eigenvalues $\pm 1$ it gives $\sin\mathbf{A} = (\sin 1)\mathbf{A}$.

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
