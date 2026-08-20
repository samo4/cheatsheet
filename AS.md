---
title: "AS notes"
author: "Samo F."
header-includes:
  - |
    \usepackage[leftline,framemethod=TikZ]{mdframed}
    \usepackage{circuitikz}
---

# Example of state-space modeling

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

Example: $\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. First compute the powers of $\mathbf{A}$:

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

Example: same $\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$:

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

### $\Phi$ via eigenvalues and diagonalization

Powers of a diagonal matrix are trivial, because for a diagonal matrix

$$
\mathbf{D}^k = \begin{bmatrix}
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





### $\Phi$ via Cayley–Hamilton







