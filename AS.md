---
title: "Modeling and analysis of linear systems"
author: "Samo F."
header-includes:
  - |
    \usepackage[leftline,framemethod=TikZ]{mdframed}
    \usepackage{circuitikz}
    \newmdenv[
      linecolor=gray!55, linewidth=0.7pt,
      backgroundcolor=gray!6,
      innertopmargin=0.6em, innerbottommargin=0.6em,
      innerleftmargin=1em, innerrightmargin=1em,
      skipabove=0.8em, skipbelow=0.8em,
      frametitlefont=\bfseries\small,
      frametitlerule=true, frametitlerulewidth=0.3pt,
      frametitlebackgroundcolor=gray!15,
      frametitleaboveskip=0.3em, frametitlebelowskip=0.3em
    ]{example}
    \usepackage{xcolor}
    \usepackage{pifont}
    \makeatletter
    \renewcommand{\paragraph}{\@startsection{paragraph}{4}{\z@}{1.0em \@plus 0.3em \@minus 0.2em}{0.5em}{\normalfont\normalsize\bfseries\color{black!70}}}
    \renewcommand{\subparagraph}{\@startsection{subparagraph}{5}{\z@}{1.0em \@plus 0.3em \@minus 0.2em}{0.5em}{\normalfont\normalsize\bfseries\color{black!70}}}
    \makeatother
---

# Math review

Everything needed before we can touch linear systems: the matrix toolbox, eigenvalues, and the ODE–Laplace machinery.

## Matrix multiplication

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

Entry by entry (just one to illustrate):

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

## Matrix determinant

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

## Inverse of a matrix

The inverse $\mathbf{A}^{-1}$ is the matrix with $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. Two standard ways to compute it.

### Existence of inverse

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

### Gauss elimination

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

### With cofactors

The adjugate formula

$$
\mathbf{A}^{-1} = \frac{1}{\det\mathbf{A}}\operatorname{adj}\mathbf{A},
$$

where $\operatorname{adj}\mathbf{A}$ is the transpose of the matrix of cofactors. For $2\times2$ this collapses to the famous formula

$$
\mathbf{A}^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}.
$$

Applying it to the same $\mathbf{A}$ above ($ad - bc = 1$):

$$
\mathbf{A}^{-1} = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix},
$$

which matches the Gauss result.

## System of equations and rank

The rank $r = \operatorname{rank}\mathbf{A}$ is the number of linearly independent rows (or columns). For a system $\mathbf{A}\vec{x} = \vec{b}$ with $n$ unknowns:

- **No solution** if $\operatorname{rank}[\mathbf{A}\mid\vec{b}] > \operatorname{rank}\mathbf{A}$ (inconsistent).
- **Exactly one solution** if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] = n$.
- **Infinitely many solutions** if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] < n$; then there are $n - r$ free variables.

The homogeneous system $\mathbf{A}\vec{x} = \vec{0}$ always has the trivial solution $\vec{x} = \vec{0}$, and has nontrivial ones exactly when $\operatorname{rank}\mathbf{A} < n$, i.e. when $\mathbf{A}$ is singular ($\det\mathbf{A} = 0$). That is the exact condition behind the eigenvalue problem below.

## Eigenvalues and eigenvectors

A nonzero vector $\vec{x}$ is an eigenvector of $\mathbf{A}$ if multiplying by $\mathbf{A}$ just scales it:

$$
\mathbf{A}\vec{x} = \lambda\vec{x}
$$

The scalar $\lambda$ is the eigenvalue. Rearranging gives $(\mathbf{A} - \lambda\mathbf{I})\vec{x} = \vec{0}$, which has a nontrivial solution iff $\mathbf{A} - \lambda\mathbf{I}$ is singular. Hence the eigenvalues are the roots of the characteristic polynomial

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

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

This is the exact machinery used later to obtain the state-transition matrix $\Phi(t) = e^{\mathbf{A}t}$ via diagonalization.

## ODE

A linear ODE is one whose left-hand side is a linear operator $L$. Linearity is two properties bundled together:

- **Additivity**: $L[y_1 + y_2] = L[y_1] + L[y_2]$
- **Homogeneity**: $L[cy] = c\,L[y]$

Together, $L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2]$. The key consequence is **superposition**: if $y_1, y_2$ solve the homogeneous equation $L[y] = 0$, so does any linear combination $c_1 y_1 + c_2 y_2$.

**Time invariance** means the system does not care when we start the clock: if $x(t)$ is the response to input $u(t)$, then $x(t - \tau)$ is the response to $u(t - \tau)$.

The state-space equation $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ is a linear, time-invariant (LTI) system — these two properties are exactly what let us use the Laplace transform and the matrix exponential below.

## Laplace

The Laplace transform maps a time function to a function of the complex variable $s$:

$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty f(t)\, e^{-st}\, dt
$$

Its power is that it turns differentiation into algebra (integration by parts):

$$
\mathcal{L}\{\dot{f}(t)\} = sF(s) - f(0)
$$

the $f(0)$ term carrying the initial condition. Along with linearity this is why an ODE becomes an algebraic equation — exactly what Section 5 does to $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$. A few workhorse pairs:

$$
\mathcal{L}\{1\} = \frac{1}{s}, \qquad
\mathcal{L}\{t\} = \frac{1}{s^2}, \qquad
\mathcal{L}\{e^{at}\} = \frac{1}{s-a}, \qquad
\mathcal{L}\{\sin\omega t\} = \frac{\omega}{s^2+\omega^2}, \qquad
\mathcal{L}\{\cos\omega t\} = \frac{s}{s^2+\omega^2}
$$

## Partial fraction decomposition

Inverse Laplace transforms are read off a table, so the goal is to split a rational function $F(s) = N(s)/D(s)$ (with $\deg N < \deg D$) into pieces that match table entries. Factor $D(s)$ and decompose:

- **Distinct linear factors** $(s-a)(s-b)$: $\ \dfrac{A}{s-a} + \dfrac{B}{s-b}$
- **Repeated factors** $(s-a)^2$: $\ \dfrac{A}{s-a} + \dfrac{B}{(s-a)^2}$
- **Irreducible quadratic** $s^2 + \omega^2$: $\ \dfrac{As + B}{s^2 + \omega^2}$ (→ sines and cosines)

```{=latex}
\begin{example}[frametitle={Example - partial fractions}]
```

Split $\dfrac{1}{(s+1)(s+2)}$:

$$
\frac{1}{(s+1)(s+2)} = \frac{A}{s+1} + \frac{B}{s+2}
$$

Multiplying through by $(s+1)(s+2)$: $1 = A(s+2) + B(s+1)$. Set $s = -2$ to get $B = -1$, and $s = -1$ to get $A = 1$:

$$
\frac{1}{(s+1)(s+2)} = \frac{1}{s+1} - \frac{1}{s+2}
$$

This is the exact identity used in Example 3, and with $\mathcal{L}^{-1}\{\frac{1}{s+a}\} = e^{-at}$:

$$
\mathcal{L}^{-1}\left\{\frac{1}{(s+1)(s+2)}\right\} = e^{-t} - e^{-2t}
$$

```{=latex}
\end{example}
```

# Modeling

TODO

## Example of state-space modeling

For this example we want to write down the state-space equations of the circuit in matrix form
$\dot{\vec{x}} = \mathbf{A} \vec{x} + \mathbf{B} \vec{u}$ and $\vec{y} = \mathbf{C} \vec{x} + \mathbf{D} \vec{u}$,
where $\vec{x} = \begin{bmatrix} i_L \\ v_c \end{bmatrix}$ and $\vec{u} = \begin{bmatrix} v_g \end{bmatrix}$ and $\vec{y} = \begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix}$.

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages]
  \draw (0,3) to[V=$v_g$] (0,0)
              (0,3) to[R=$R_1$, v>=$v_{R_1}$] (3,3)
              to[L=$L$, i>^=$i_L$] (6,3)
              (6,3) to[C] (6,0)
              (6,3) -- (8,3)
              to[R=$R_2$] (8,0)
              to[short] (0,0);
  \node[left=14pt] at (6,1.5) {$C$};
  \node at (6.25,1.9) {$+$};
  \node[right=14pt] at (6,1.5) {$v_c$};
\end{circuitikz}
\end{center}
```

Let's select one node as ground. Although any node can be ground, we try to choose it in a way that will make the resulting equation as easy as possible. Generally, pick the node with the most element connections to reduce the number of unknown node voltages. In our case, we can select the bottom node as ground.\footnote{In simulation software (e.g., SPICE), the ground node choice can influence numerical stability, but picking the one with most connections is a still good rule of thumb.}

Then we proceed to mark the remaining nodes.

Passive sign convention (PSC) defines an element’s voltage positive at the terminal where the reference current enters; then power is positive when the element absorbs energy. For voltage source, according to PSC, we must mark the reference current in such a way that current entering the element will absorb power and when leaving (minus sign) give power to the rest of the circuit. That means that arrow should point into the + of voltage source. For capacitor we have defined polarity: we apply the PSC convention to $i_c$ (arrow into +). And for the inductor we have defined the current $i_L$. Although $v_L$ is not required here, we could define its polarity according to PSC as well ($V_2$ is positive in relation to $V_3$).

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages]
  \draw (0,3) node[circ,label=above:$V_1$]{} to[V=$v_g$, i>^=$i_g$] (0,0) node[ground]{};
  \draw (0,3) to[R=$R_1$, v>=$v_{R_1}$] (3,3) node[circ,label=above:$V_2$]{}
              to[L=$L$, i>^=$i_L$] (6,3) node[circ,label=above:$V_3$]{}
              -- (8,3) to[R=$R_2$] (8,0) to[short] (0,0);
  \draw (6,3) to[C, i>^=$i_C$ ] (6,0);
  \node[left=14pt] at (6,1.5) {$C$};
  \node at (6.25,1.9) {$+$};
  \node[right=14pt] at (6,1.5) {$v_c$};
\end{circuitikz}
\end{center}
```

Common approaches for deriving state-space equations include node-voltage and mesh-current methods. Here we apply a combination of both. It might be described as node-voltage formulation with selected element state variables.

First we observe the $V_1 = v_g$ and $v_c = V_3$.

We write down the equations for each node using Kirchhoff's current law. When expressing currents through resistors, we start with the current node voltage (so currents are taken as leaving the node: plus sign in our equations).

$$\frac{V_1 - V_2}{R_1} + i_g = 0$$

When node is connected to an inductor, we express the current through the inductor as a state variable. Note that the direction of current for $i_L$ is defined as flowing out of $V_2$. For $V_2$ we get:

$$\frac{V_2 - V_1}{R_1} + i_L = 0$$

And the same for capacitors: we express the current through the capacitor as a state variable. For the capacitor we take its voltage $v_c$ as the state variable (more standard); current follows $i_C = C\,\dot{v}_c$ under PSC.

Next, we write down the equations for the energy-storing elements using their constitutive relations. Note that $i_L$ is chosen from $V_2$ to $V_3$. Lenz’s law is not ignored; its effect was already built into the sign of the inductor’s voltage when we adopted PSC. Faraday’s law gives $v = L\,\dot{i}$ for the chosen polarity (voltage drop in the direction of the reference current). If you had defined the voltage polarity opposite to the current reference, the relation would appear as $v = -L\,\dot{i}$. Thus no extra minus is added later - the orientation choices at the start encode it.

$$ v_L = L \frac{di_L}{dt} = V_2 - V_3 $$

And for the capacitor:

$$ i_C = C \frac{dv_c}{dt} = i_L - \frac{V_3}{R_2} $$

Since $V_1 = v_g$ and $v_c = V_3$ we get the state-space form

$$
\frac{d}{dt}\begin{bmatrix} i_L \\ v_c \end{bmatrix} =
\begin{bmatrix}
-\frac{R_1}{L} & -\frac{1}{L} \\
\frac{1}{C} & -\frac{1}{C R_2}
\end{bmatrix}
\begin{bmatrix} i_L \\ v_c \end{bmatrix} +
\begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix} v_g.
$$

If outputs are $v_{R_1}$ and $v_L$ then

$$
\begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix} =
\begin{bmatrix}
R_1 & 0 \\
L\,\frac{d}{dt} & 0
\end{bmatrix}
\begin{bmatrix} i_L \\ v_c \end{bmatrix} +
\begin{bmatrix} -1 \\ 0 \end{bmatrix} v_g,
$$

or equivalently using algebraic forms:
$v_{R_1}=R_1 i_L - v_g$, $v_L = L\,\dfrac{di_L}{dt}$.

# State-space

## 4. Solving state-space equations

$$\dot{\vec{x}} = \mathbf{A}\vec{x}$$ 

with initial condition $\vec{x}(0) = \vec{x}_0$ is a linear ODE. The solution can be expressed in terms of the matrix exponential:

### Homogeneous scalar case

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

### Homogeneous vector case

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

### State transition matrix

And because mathematicians don't like writing/typing they decided to shorthand the $e^{\mathbf{A}(t-t_0)}$ to $\Phi(t)$ and call it the state transition matrix. So we can write the solution as:

$$
\vec{X}_H = \Phi(t) \vec{x}_0
$$

State transition matrix has the following properties:

1. $\Phi(0) = \mathbf{I}$ (identity matrix)
2. $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$
3. $\Phi(t_1 - t_2) = \Phi(t_1)\Phi^{-1}(t_2)$
4. $\frac{d}{dt}\Phi(t) = \mathbf{A}\Phi(t)$

### Nonhomogeneous case

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
\begin{example}[frametitle={Example 2 - obtaining $\Phi$ via Taylor series}]
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
\begin{example}[frametitle={Example 3 - obtaining $\Phi$ via Laplace transform}]
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

### $\Phi$ diagonalization

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

- **Algebraic multiplicity** $\alpha_i$ — how many times $\lambda_i$ occurs as a root of the characteristic polynomial. These sum to the matrix dimension: $\sum_i \alpha_i = n$.
- **Geometric multiplicity** $\gamma_i$ — the dimension of the eigenspace $\ker(\mathbf{A} - \lambda_i\mathbf{I})$, i.e. the number of linearly independent eigenvectors belonging to $\lambda_i$. Computed as the nullity $\gamma_i = n - \operatorname{rank}(\mathbf{A} - \lambda_i\mathbf{I})$.

They are always related by $1 \le \gamma_i \le \alpha_i$. The gap $\alpha_i - \gamma_i$ measures how "defective" $\mathbf{A}$ is at $\lambda_i$: if $\gamma_i < \alpha_i$ there are not enough eigenvectors, and diagonalization fails.

In practice:

1. Solve $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ for the eigenvalues — factor the polynomial, use the quadratic formula for $2\times 2$, or numerical methods for larger matrices.
2. For each $\lambda_i$, solve $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v} = 0$; the number of free parameters in the solution is $\gamma_i$.

$\mathbf{A}$ is diagonalizable iff $\gamma_i = \alpha_i$ for every $i$. This is always the case when all eigenvalues are distinct, since then $\gamma_i = \alpha_i = 1$.

```{=latex}
\begin{example}[frametitle={Example 4 - eigenvalues and eigenvectors}]
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

When $\gamma_i = \alpha_i$ for every eigenvalue, there are exactly $n$ linearly independent eigenvectors $\vec{v}_1, \dots, \vec{v}_n$. Stack them as columns:

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
\begin{example}[frametitle={Example 5 - obtaining $\Phi$ via diagonalization}]
```

$\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. The characteristic equation $\det(\mathbf{A} - \lambda\mathbf{I}) = (-2-\lambda)(-1-\lambda) = 0$ gives distinct eigenvalues $\lambda_1 = -2$, $\lambda_2 = -1$, so $\gamma_i = \alpha_i = 1$ and $\mathbf{A}$ is diagonalizable.

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

The diagonalization method is perhaps the most elegant, but it fails for defective matrices. The Laplace method above and Cayley–Hamilton method below both work even for defective matrices.

### $\Phi$ via Cayley–Hamilton

The Cayley–Hamilton theorem states that every matrix satisfies its own characteristic equation. If

$$
\det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_0
$$

substituting the matrix for the scalar gives the zero matrix:

$$
\mathbf{A}^n + c_{n-1}\mathbf{A}^{n-1} + \cdots + c_0\mathbf{I} = \mathbf{0}
$$

So every power $\mathbf{A}^k$ with $k \ge n$ reduces to a combination of $\mathbf{I}, \mathbf{A}, \dots, \mathbf{A}^{n-1}$, and the matrix exponential must have the form

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A} + \cdots + \alpha_{n-1}(t)\mathbf{A}^{n-1}
$$

The coefficients follow from the key observation that $\mathbf{A}$ and its eigenvalues satisfy the same polynomial relation, so the same equation holds at each $\lambda_i$:

$$
e^{\lambda_i t} = \alpha_0(t) + \alpha_1(t)\lambda_i + \cdots + \alpha_{n-1}(t)\lambda_i^{n-1}, \qquad i = 1, \dots, n
$$

Solving this Vandermonde system gives the $\alpha_j(t)$. Unlike diagonalization, this works even for defective matrices (see Example 4).

```{=latex}
\begin{example}[frametitle={Example 6 - obtaining $\Phi$ via Cayley–Hamilton}]
```

Same $\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. Characteristic equation:

$$
\det(\lambda\mathbf{I} - \mathbf{A}) = (\lambda+2)(\lambda+1) = \lambda^2 + 3\lambda + 2 = 0
$$

so $\mathbf{A}^2 + 3\mathbf{A} + 2\mathbf{I} = \mathbf{0}$, and with $n = 2$:

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A}
$$

Evaluate at the eigenvalues:

$$
\lambda_1 = -2: \quad e^{-2t} = \alpha_0 - 2\alpha_1, \qquad
\lambda_2 = -1: \quad e^{-t} = \alpha_0 - \alpha_1
$$

Subtracting gives $\alpha_1 = e^{-t} - e^{-2t}$, and then $\alpha_0 = 2e^{-t} - e^{-2t}$. Substituting back:

$$
\Phi(t) = e^{\mathbf{A}t} = (2e^{-t} - e^{-2t})\mathbf{I} + (e^{-t} - e^{-2t})\mathbf{A}
= \begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}
$$

which (you guessed it) matches all previous methods. 

```{=latex}
\end{example}
```

### Final remarks on obtaining $\Phi$

We have shown four ways to skin a cat, but at the end you still have the same dead cat. The Taylor series is the most general, flows nicely from rudimentary principles, but it is slow and tedious. Diagonalization is elegant, but fails for defective matrices. Laplace transform is a nice trick, but requires some algebraic manipulation. Cayley–Hamilton is a clever method, but requires solving a Vandermonde system. 

Cayley–Hamilton specifically will come in very handy when we'll talk about controllability and observability.

In practice, the choice of method depends on the specific matrix $\mathbf{A}$ and the context of the problem.

# Properties of systems

## Stability

## Controlability

## Observability


# Linearization

TODO

# Discrete systems

TODO





