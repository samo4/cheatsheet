# State-space

## State-space variables and equations

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

## State-space representation

The state-space representation is a geometric view of the dynamics: at every instant the system sits at a point $\vec{x}(t)$ in state space, and the equations $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ push that point along a curve — the *trajectory*. For the example system from the Modeling chapter, $\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x}$ with $\vec{x}(0) = (1, 0)$, the state spirals into the origin (markers at integer times):

```{=latex}
\input{tikz/state-spiral.tex}
```

The decay and the oscillation come straight from the eigenvalues of $\mathbf{A}$ — here $-1 \pm j\sqrt{2}$, the negative real part damping the spiral, the imaginary part driving the rotation.

## Homogeneous Solution

$$\dot{\vec{x}} = \mathbf{A}\vec{x}$$ 

with initial condition $\vec{x}(0) = \vec{x}_0$ is a linear ODE. The solution can be expressed in terms of the matrix exponential:

For the trivial case of homogeneous equations (homogeneous: no input, $\vec{u} = \vec{0}$), let's try solving it with scalars first:

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

By the analogy with the scalar case, we can try the same exponential solution for the vector case $\dot{\vec{x}} = \mathbf{A}\vec{x}$ (still homogeneous, $\vec{u} = \vec{0}$). Try the same exponential:


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

1. $\Phi(0) = \mathbf{I}$
2. $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$
3. $\Phi(t_1 - t_2) = \Phi(t_1)\Phi^{-1}(t_2)$
4. $\frac{d}{dt}\Phi(t) = \mathbf{A}\Phi(t)$

PS: Matrix multiplication is associative ($\mathbf{A}\mathbf{B}\mathbf{C} = (\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$) but not commutative ($\mathbf{A}\mathbf{B} \ne \mathbf{B}\mathbf{A}$ in general). Even though it's associative, in many fields the rightmost matrix "acts first", so we usually multiply from right to left.

## Nonhomogeneous Solution

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

```{=latex}
\begin{example}[frametitle={Example - mass on a spring}]
```
Drop a weight on a spring with $v_0$. How will the weight move?

The equation of motion is:

$$m\ddot{x} = -kx - mg$$

Introduce $v = \dot{x}$ and write it in state space:

$$
\begin{bmatrix} \dot{x} \\ \dot{v} \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & 0 \end{bmatrix}\begin{bmatrix} x \\ v \end{bmatrix}
+ \begin{bmatrix} 0 \\ -g \end{bmatrix}
$$

**Step 1 — $\Phi$ by the defining series.** At this point the only tool for a concrete $\Phi$ is Taylor series\footnote{The same $\Phi$ drops out faster through Laplace, $\mathcal{L}^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$ — an identity we derive in Section 5, where the hanging-mass example works exactly that route.} Compute the first powers:

$$
\mathbf{A}^2 = \mathbf{A}\mathbf{A} = \begin{bmatrix} -\frac{k}{m} & 0 \\ 0 & -\frac{k}{m} \end{bmatrix} = -\frac{k}{m}\mathbf{I}
$$

$\mathbf{A}^2$ came out a scalar matrix — a multiple of the identity. For reasons that will be apparent soon, it would be very convenient to introduce a new variable $\omega_0 = \sqrt{k/m}$. Grouping even and odd powers in the series:

$$
\Phi(t) = e^{\mathbf{A}t}
= \mathbf{I}\left(1 - \omega_0^2\frac{t^2}{2!} + \omega_0^4\frac{t^4}{4!} - \cdots\right)
 + \mathbf{A}\left(t - \omega_0^2\frac{t^3}{3!} + \omega_0^4\frac{t^5}{5!} - \cdots\right)
$$

The two brackets are now recognizable: they are the $\cos$ and $\sin$ series with argument $\omega_0 t$. The brackets close:

$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{I}\cos\omega_0 t + \mathbf{A}\,\frac{\sin\omega_0 t}{\omega_0}
= \begin{bmatrix} \cos\omega_0 t & \frac{1}{\omega_0}\sin\omega_0 t \\[2pt] -\omega_0\sin\omega_0 t & \cos\omega_0 t \end{bmatrix}
$$

**Step 2 — the homogeneous part first (the easy one).** The boxed solution is a sum,

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + \int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

and the first term needs no integration — just a matrix multiply. With the drop condition $\vec{x}_0 = \tvec{0,v_0}$:

$$
\Phi(t)\vec{x}_0 = \begin{bmatrix} \cos\omega_0 t & \frac{1}{\omega_0}\sin\omega_0 t \\[2pt] -\omega_0\sin\omega_0 t & \cos\omega_0 t \end{bmatrix}\begin{bmatrix} 0 \\ v_0 \end{bmatrix}
= \begin{bmatrix} \frac{v_0}{\omega_0}\sin\omega_0 t \\[2pt] v_0\cos\omega_0 t \end{bmatrix}
$$

That is the whole homogeneous response: the free ring of the initial kick, starting at $x = 0$ with speed $v_0$ and oscillating forever (no damping yet).

**Step 3 — the forced part: gravity, via the $\tau$ trick.** The homogeneous piece is done; the input term remains. Gravity is a constant input, $\mathbf{B}\vec{u} = \tvec{0,-g}$, so the forced integral is

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

The integrand sees $t$ and $\tau$ only through $t-\tau$, so substitute $u = t-\tau$: as $\tau$ runs $0 \to t$, $u$ runs $t \to 0$, and the minus from $d\tau = -du$ flips the limits back to

$$
\int_0^t \Phi(t-\tau)\,d\tau = \int_0^t \Phi(u)\,du
$$

This is exactly the trick that only works because we start at $0$ — a nonzero lower limit $t_0$ would leave the shifted window $[t-t_0,\, t]$. With $\tau$ gone, what remains is an ordinary integral of $\Phi(u)\mathbf{B}$:

$$
\int_0^t \Phi(u)\mathbf{B}\,du = \int_0^t \begin{bmatrix} -\frac{g}{\omega_0}\sin\omega_0 u \\[2pt] -g\cos\omega_0 u \end{bmatrix}du
= \begin{bmatrix} \frac{g}{\omega_0^2}(\cos\omega_0 t - 1) \\[2pt] -\frac{g}{\omega_0}\sin\omega_0 t \end{bmatrix}
$$

**Putting it together** — the full motion is the sum of the two pieces:

$$
\vec{x}(t) = \begin{bmatrix} \frac{v_0}{\omega_0}\sin\omega_0 t \\[2pt] v_0\cos\omega_0 t \end{bmatrix}
+ \begin{bmatrix} \frac{g}{\omega_0^2}(\cos\omega_0 t - 1) \\[2pt] -\frac{g}{\omega_0}\sin\omega_0 t \end{bmatrix}
$$

Sanity check at $t = 0$: $x(0) = 0$ (both position terms vanish) and $v(0) = v_0$ (only the homogeneous $\cos$ survives), just as dropped. The gravity piece makes the mass ring about the lowered point — its constant part $-\frac{g}{\omega_0^2} = -\frac{mg}{k}$ is the static stretch that balances the weight — while the $\frac{v_0}{\omega_0}\sin\omega_0 t$ term is the free oscillation of the initial kick superimposed on top.

```{=latex}
\end{example}
```

## Obtaining the state-transition matrix

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

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\vec{x}(t) = \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\}\vec{x}_0 + \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)\right\}
$}
\endgroup
\]
```

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

Now let's do something useful with $\Phi$: **the step response**.

Take zero initial state $\vec{x}(0) = \vec{0}$, a step input $u(t) = 5$ (constant for $t \ge 0$), and $\mathbf{B}^{\mathsf{T}} = \left[1\ 0\right]$. The homogeneous term in the boxed solution of Section 4 dies, leaving the forced convolution:

$$
\vec{x}(t) = \int_0^t \underbrace{e^{\mathbf{A}(t-\tau)}}_{\Phi(t-\tau)}\,\mathbf{B}\,u(\tau)\,d\tau = e^{\mathbf{A}t}\int_0^t e^{-\mathbf{A}\tau}\,\mathbf{B}\,u(\tau)\,d\tau = 5\,e^{\mathbf{A}t}\int_0^t e^{-\mathbf{A}\tau}\,\mathbf{B}\,d\tau
$$

Splitting the exponential as $e^{\mathbf{A}(t-\tau)} = e^{\mathbf{A}t}e^{-\mathbf{A}\tau}$, the $\tau$-independent factor $e^{\mathbf{A}t}$ steps out of the integral, and the constant step $u = 5$ follows it out. Writing out the two matrix exponentials — $e^{\mathbf{A}t} = \Phi(t)$ outside, $e^{-\mathbf{A}\tau} = \Phi(-\tau)$ inside — the input vector $\mathbf{B}$ picks out the first column:

$$
\vec{x}(t) = 5 \underbrace{\begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}}_{\Phi(t)} \int_0^t \underbrace{\begin{bmatrix} e^{2\tau} & 0 \\ e^{\tau} - e^{2\tau} & e^{\tau} \end{bmatrix}}_{\Phi(-\tau)} \begin{bmatrix} 1 \\ 0 \end{bmatrix}d\tau
$$

Integrating entry by entry — $\int_0^t e^{a\tau}d\tau = \frac{e^{at}-1}{a}$ — the inner exponential dotted with $\mathbf{B}$ gives

$$
\int_0^t e^{-\mathbf{A}\tau}\,\mathbf{B}\,d\tau = \int_0^t \begin{bmatrix} e^{2\tau} \\[2pt] e^{\tau} - e^{2\tau} \end{bmatrix}d\tau = \begin{bmatrix} \frac{e^{2t}-1}{2} \\[2pt] (e^{t}-1) - \frac{e^{2t}-1}{2} \end{bmatrix}
$$

and multiplying the $5e^{\mathbf{A}t}$ back in front:

$$
\vec{x}(t) = 5 \begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}\begin{bmatrix} \frac{e^{2t}-1}{2} \\[2pt] (e^{t}-1) - \frac{e^{2t}-1}{2} \end{bmatrix}
$$

$$
= \frac{5}{2}\begin{bmatrix} 1 - e^{-2t} \\[2pt] 1 - 2e^{-t} + e^{-2t} \end{bmatrix}
$$

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - hanging mass on a spring with damper, now with time solution}]
```

A mass $m$ hangs from the ceiling on a spring of constant $k$ with a damper of coefficient $b$. The equation of motion is

$$
m\ddot{x} = -kx - b\dot{x} - mg
$$

Introduce $v = \dot{x}$ and write it as a first-order system:

$$
\begin{bmatrix} \dot{x} \\ \dot{v} \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\begin{bmatrix} x \\ v \end{bmatrix}
+ \begin{bmatrix} 0 \\ -g \end{bmatrix}
$$

The constant gravity term is the input, $\mathbf{B}\vec{u} = \tvec{0,-g}$. This is the boxed solution above in action: build the kernel $\Phi(t) = e^{\mathbf{A}t}$, then run the convolution integral.

**Step 1 — $\Phi$ via Laplace.** $\det(s\mathbf{I} - \mathbf{A}) = s^2 + \frac{b}{m}s + \frac{k}{m}$, which we complete into a sum of squares:

$$
s^2 + \frac{b}{m}s + \frac{k}{m}
= \left(s + \frac{b}{2m}\right)^2 + \frac{k}{m}\left(1 - \frac{b^2}{4km}\right)
$$

Define the natural frequency and damping ratio,

$$
\omega_0 = \sqrt{\frac{k}{m}}, \qquad
\zeta = \frac{b}{2\sqrt{km}} = \frac{b}{2m\omega_0}
$$

so $\frac{b}{m} = 2\zeta\omega_0$ and $\frac{k}{m} = \omega_0^2$, and the determinant takes the classic second-order form, which completes into a sum of squares:

$$
\det(s\mathbf{I} - \mathbf{A}) = s^2 + 2\zeta\omega_0 s + \omega_0^2
= (s + \zeta\omega_0)^2 + \omega_0^2(1-\zeta^2)
$$

Take the **critically damped case $\zeta = 1$** (damper tuned so $b = 2\sqrt{km}$): then $\omega_d = \omega_0\sqrt{1-\zeta^2} = 0$, the two poles collide at $s = -\omega_0$, and the resolvent is

$$
(s\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(s + \omega_0)^2}\begin{bmatrix} s + 2\omega_0 & 1 \\[2pt] -\omega_0^2 & s \end{bmatrix}
$$

Inverting with the double-pole pairs $\frac{1}{(s+\omega_0)^2} \leftrightarrow t e^{-\omega_0 t}$ and $\frac{s}{(s+\omega_0)^2} \leftrightarrow (1 - \omega_0 t)e^{-\omega_0 t}$ leaves only exponentials:

$$
\Phi(t) = e^{\mathbf{A}t} = e^{-\omega_0 t}\begin{bmatrix}
1 + \omega_0 t & t \\[2pt]
-\omega_0^2 t & 1 - \omega_0 t
\end{bmatrix}
$$

**Step 2 — solve the state equation.** Plug $\Phi$ into the boxed nonhomogeneous solution above ($t_0 = 0$, $\vec{u} = 1$, $\mathbf{B} = [0, -g]^T$):

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + \int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

With the critical $\Phi$, the kernel dotted with the input is

$$
\Phi(t-\tau)\mathbf{B} = g\,e^{-\omega_0(t-\tau)}\begin{bmatrix} -(t-\tau) \\[2pt] \omega_0(t-\tau) - 1 \end{bmatrix}
$$

so the gravity term reads

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
= g\,e^{-\omega_0 t}\int_0^t \begin{bmatrix} (-t+\tau)e^{\omega_0\tau} \\[2pt] (\omega_0(t-\tau)-1)e^{\omega_0\tau} \end{bmatrix} d\tau
$$

Evaluating entry by entry — this is the alternative to the $\tau$ trick of the spring example: no substitution, we integrate in $\tau$ directly and watch each $\tau$ vanish. The $t$ inside the integrand is a *constant* as far as the $\tau$-integration is concerned, and a $\tau$ disappears only when its antiderivative is evaluated at the limits. First entry — using $\int \tau e^{\omega_0\tau}d\tau = \left(\frac{\tau}{\omega_0}-\frac{1}{\omega_0^2}\right)e^{\omega_0\tau}$:

$$
\int_0^t (-t+\tau)e^{\omega_0\tau}\,d\tau
= \left[-\frac{t}{\omega_0}e^{\omega_0\tau} + \left(\frac{\tau}{\omega_0}-\frac{1}{\omega_0^2}\right)e^{\omega_0\tau}\right]_{0}^{t}
= \frac{t}{\omega_0} - \frac{e^{\omega_0 t}-1}{\omega_0^2}
$$

Second entry — here the antiderivative is simply $(t-\tau)e^{\omega_0\tau}$, because its $\tau$-derivative is $(\omega_0(t-\tau)-1)e^{\omega_0\tau}$:

$$
\int_0^t \big(\omega_0(t-\tau)-1\big)e^{\omega_0\tau}\,d\tau
= \Big[(t-\tau)e^{\omega_0\tau}\Big]_{0}^{t}
= -t
$$

Assembling both rows under the common factor $g\,e^{-\omega_0 t}$:

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
= e^{-\omega_0 t}\begin{bmatrix} \frac{g}{\omega_0}t - \frac{g}{\omega_0^2}\left(e^{\omega_0 t}-1\right) \\[2pt] -g\,t \end{bmatrix}
$$

so the full motion is

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + e^{-\omega_0 t}\begin{bmatrix} \frac{g}{\omega_0}t - \frac{g}{\omega_0^2}\left(e^{\omega_0 t}-1\right) \\[2pt] -g\,t \end{bmatrix}
$$

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

If diagonal matrices are so nice, how do we make one? Let's make a detour through eigenvalues and eigenvectors.

#### Eigenvalues and eigenvectors

The eigenvalues\footnote{D.Hilbert gave us the nice german name "Eigenwert" for eigenvalue} of $\mathbf{A}$ are the scalars $\lambda$ for which

$$
\mathbf{A}\vec{v} = \lambda\vec{v}
$$

has a nonzero solution $\vec{v} \ne 0$ — the eigenvector. Geometrically, $\mathbf{A}$ just stretches $\vec{v}$ by $\lambda$ without rotating it. Rearranging gives $(\mathbf{A} - \lambda\mathbf{I})\vec{v} = \vec{0}$, which has a nontrivial solution iff the matrix is singular, i.e.

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

Eigenvalues are the roots of the characteristic polynomial $\det(\mathbf{A} - \lambda\mathbf{I})$. For an $n \times n$ matrix this is a polynomial of degree $n$, so by the fundamental theorem of algebra there are $n$ eigenvalues counting multiplicity. Each eigenvalue carries two numbers:

- **Algebraic** multiplicity $m_{a,i}$ — how many times $\lambda_i$ occurs as a root of the characteristic polynomial. These sum to the matrix dimension: $\sum_i m_{a,i} = n$.
- **Geometric** multiplicity $m_{g,i}$ — the dimension of the eigenspace $\ker(\mathbf{A} - \lambda_i\mathbf{I})$, i.e. the number of linearly independent eigenvectors belonging to $\lambda_i$. Computed as the nullity $m_{g,i} = n - \operatorname{rank}(\mathbf{A} - \lambda_i\mathbf{I})$.

They are always related by $1 \le m_{g,i} \le m_{a,i}$. The gap $m_{a,i} - m_{g,i}$ measures how "defective" $\mathbf{A}$ is at $\lambda_i$: if $m_{g,i} < m_{a,i}$ there are not enough eigenvectors, and diagonalization fails.

In practice:

1. Solve $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ for the eigenvalues.
2. For each $\lambda_i$, solve $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v} = \vec{0}$; the number of free parameters in the solution is $m_{g,i}$.

**Watch out for linear dependence.** Since $\lambda_i$ *is* an eigenvalue, the matrix $(\mathbf{A} - \lambda_i\mathbf{I})$ is singular by construction — its rows are linearly dependent. So when you solve $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v} = \vec{0}$, don't be alarmed that one row turns out to be a multiple of another, or that a row is all zeros: that's exactly what should happen. Only the independent equations carry information — their number is the rank, and the leftover free variables are precisely the geometric multiplicity $m_{g,i}$.

$\mathbf{A}$ is diagonalizable iff $m_{g,i} = m_{a,i}$ for every $i$. This is always the case when all eigenvalues are distinct, since then $m_{g,i} = m_{a,i} = 1$.

```{=latex}
\begin{example}[frametitle={Example - eigenvalues and eigenvectors}]
```

Find the eigenvalues and eigenvectors of $\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$.

The characteristic polynomial (upper-triangular, so the eigenvalues sit on the diagonal):

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 1-\lambda & 0 & 0 \\ 0 & 2-\lambda & 1 \\ 0 & 0 & 2-\lambda \end{vmatrix} = (1-\lambda)(2-\lambda)^2 = 0
$$

so $\lambda_1 = 1$ with $m_{a,1} = 1$, and $\lambda_2 = 2$ with $m_{a,2} = 2$.

For $\lambda_1 = 1$, solve $(\mathbf{A} - \mathbf{I})\vec{v} = \vec{0}$:

$$
(\mathbf{A} - \mathbf{I}) = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}
$$

The first row vanished entirely — the eigenvalue knocked out the $(1,1)$ diagonal entry and there's nothing else in that row, so it contributes no equation. The other two rows are independent (each has a pivot), so the rank is $2$ and exactly one variable is free: $m_{g,1} = 3 - 2 = 1 = m_{a,1}$.

The surviving equations are $v_2 + v_3 = 0$ and $v_3 = 0$, which force $v_3 = 0$ and $v_2 = 0$ while leaving $v_1$ free:

$$
v_2 + v_3 = 0,\ v_3 = 0
\quad\Longrightarrow\quad
v_3 = 0,\ v_2 = 0,\ v_1 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
$$

As always, any scalar multiple of $\vec{v}_1$ is also an eigenvector — the eigenspace is the whole line through $\vec{v_1}$.

For $\lambda_2 = 2$, solve $(\mathbf{A} - 2\mathbf{I})\vec{v} = \vec{0}$:

$$
\begin{bmatrix} -1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}\vec{v} = \vec{0}
\quad\Longrightarrow\quad
v_1 = 0,\ v_3 = 0,\ v_2 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

Here $m_{g,2} = 1 < m_{a,2} = 2$: only two linearly independent eigenvectors exist, so $\mathbf{A}$ is defective and **not** diagonalizable.

```{=latex}
\end{example}
```

#### Diagonalization

And now back where we're really going: how to reorganize our matrix into a diagonal form. When $m_{g,i} = m_{a,i}$ for every eigenvalue, there are exactly $n$ linearly independent eigenvectors $\vec{v}_1, \dots, \vec{v}_n$. Stack them as columns:

$$
\mathbf{V} = \begin{bmatrix} \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \end{bmatrix}
$$

Each eigenpair satisfies $\mathbf{A}\vec{v}_i = \lambda_i \vec{v}_i$, so stacking the $n$ equations side by side lets $\mathbf{A}$ act on every column at once:

$$
\mathbf{A} \begin{bmatrix} \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \end{bmatrix} = \begin{bmatrix} \lambda_1\vec{v}_1 & \lambda_2\vec{v}_2 & \cdots & \lambda_n\vec{v}_n \end{bmatrix}
$$

The scaled columns on the right are just the original ones times the diagonal eigenvalue matrix $\boldsymbol{\Lambda} = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$:

$$
= \begin{bmatrix} \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \end{bmatrix}\begin{bmatrix}
\lambda_1 & & \\
& \ddots & \\
& & \lambda_n
\end{bmatrix}
$$

So, writing $\mathbf{V}$ for the stacked matrix, this is exactly

$$
\mathbf{A}\mathbf{V} = \mathbf{V}\boldsymbol{\Lambda}
$$

Independence makes $\mathbf{V}$ invertible, so multiplying by $\mathbf{V}^{-1}$ from the right gives the factorization

$$
\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}
$$

The order of the columns is your choice — each eigenvalue on the diagonal of $\boldsymbol{\Lambda}$ just has to follow its own eigenvector. Swapping two columns of $\mathbf{V}$ (and the matching eigenvalues) flips the sign of $\det\mathbf{V}$ but leaves $\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$, and hence $\Phi(t)$, identical. Only $\det\mathbf{V} \ne 0$ really matters.

This is the whole trick: $\mathbf{A}$ is just a diagonal matrix in a different basis. Powers pass through the same similarity — the inner $\mathbf{V}^{-1}\mathbf{V}$ pairs cancel, like a telescope:

$$
\mathbf{A}^2 = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}\,\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}
= \mathbf{V}\boldsymbol{\Lambda}\,(\mathbf{V}^{-1}\mathbf{V})\,\boldsymbol{\Lambda}\mathbf{V}^{-1}
= \mathbf{V}\boldsymbol{\Lambda}^2\mathbf{V}^{-1}
$$

$$
\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}
$$

so the Taylor series telescopes into

$$
e^{\mathbf{A}t} = \mathbf{I} + \mathbf{A}t + \frac{(\mathbf{A}t)^2}{2!} + \frac{(\mathbf{A}t)^3}{3!} + \dots
$$

$$
= \mathbf{V}\mathbf{I}\mathbf{V}^{-1} + \mathbf{V}\boldsymbol{\Lambda}t\,\mathbf{V}^{-1} + \mathbf{V}\frac{(\boldsymbol{\Lambda}t)^2}{2!}\mathbf{V}^{-1} + \mathbf{V}\frac{(\boldsymbol{\Lambda}t)^3}{3!}\mathbf{V}^{-1} + \dots
$$

$$
= \mathbf{V} \left( \mathbf{I} + \boldsymbol{\Lambda}t + \frac{(\boldsymbol{\Lambda}t)^2}{2!} + \frac{(\boldsymbol{\Lambda}t)^3}{3!} + \dots \right) \mathbf{V}^{-1}
$$

$$
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

$\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. 

The characteristic equation $\det(\mathbf{A} - \lambda\mathbf{I}) = (-2-\lambda)(-1-\lambda) = 0$ gives distinct eigenvalues $\lambda_1 = -2$, $\lambda_2 = -1$, so $m_{g,i} = m_{a,i} = 1$ and $\mathbf{A}$ is diagonalizable.

We hunt for the eigenvectors from the condition

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
(\mathbf{A} - \lambda\mathbf{I})\vec{v} = \vec{0}
$}
\endgroup
\]
```

one eigenvalue at a time.

For $\lambda_1 = -2$: $(\mathbf{A} - (-2)\mathbf{I}) = \mathbf{A} + 2\mathbf{I}$, so

$$
(\mathbf{A} + 2\mathbf{I}) = \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}
$$

The first row vanished — $\lambda = -2$ zeroed the $(1,1)$ diagonal entry and the $(1,2)$ entry was already $0$ — so the rank is $1$ and one variable is free. The one surviving equation, $v_1 + v_2 = 0$, forces $v_2 = -v_1$:

$$
\begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}\vec{v}_1 = \vec{0}
\quad\Longrightarrow\quad
v_2 = -v_1,\ v_1 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

For $\lambda_2 = -1$: $(\mathbf{A} - (-1)\mathbf{I}) = \mathbf{A} + \mathbf{I}$, so

$$
(\mathbf{A} + \mathbf{I}) = \begin{bmatrix} -1 & 0 \\ 1 & 0 \end{bmatrix}
$$

The bottom row is $-1\times$ the top row, so the rank is $1$ again: the surviving equation $v_1 = 0$ pins down $v_1$ and leaves $v_2$ free:

$$
\begin{bmatrix} -1 & 0 \\ 1 & 0 \end{bmatrix}\vec{v}_2 = \vec{0}
\quad\Longrightarrow\quad
v_1 = 0,\ v_2 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

**Assemble the pieces.** The eigenvectors become the *columns* of $\mathbf{V}$, and the eigenvalues sit on the diagonal of $\boldsymbol{\Lambda}$ in the same order:

$$
\mathbf{V} = \begin{bmatrix} \vec{v}_1 & \vec{v}_2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}, \qquad
\boldsymbol{\Lambda} = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} = \begin{bmatrix} -2 & 0 \\ 0 & -1 \end{bmatrix}
$$

Last, $\mathbf{V}^{-1}$ by the $2\times2$ inverse formula:

$$
\mathbf{V}^{-1} = \frac{1}{\det\mathbf{V}}\begin{bmatrix} v_{22} & -v_{12} \\ -v_{21} & v_{11} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}
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
```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via diagonalization, 3×3}]
```

Let's do a bigger one, and keep our eyes on the prize: we're after $\Phi(t) = e^{\mathbf{A}t}$, with

$$
\mathbf{A} = \begin{bmatrix} 2 & 2 & 2 \\ 0 & 2 & 0 \\ 0 & 1 & 3 \end{bmatrix}
$$

**Step 1 — eigenvalues.** Expand the determinant along the first column:

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 2-\lambda & 2 & 2 \\ 0 & 2-\lambda & 0 \\ 0 & 1 & 3-\lambda \end{vmatrix} = (2-\lambda)\begin{vmatrix} 2-\lambda & 0 \\ 1 & 3-\lambda \end{vmatrix} = (2-\lambda)^2(3-\lambda) = 0
$$

so $\lambda_1 = 2$ with $m_{a,1} = 2$, and $\lambda_2 = 3$ with $m_{a,2} = 1$.

**Step 2 — eigenvectors for $\lambda_1 = 2$.** Solve $(\mathbf{A} - 2\mathbf{I})\vec{v} = \vec{0}$:

$$
(\mathbf{A} - 2\mathbf{I}) = \begin{bmatrix} 0 & 2 & 2 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \end{bmatrix}
$$

The first and last rows are proportional — the first is $2\times$ the last — and the middle row is all zeros. So every row is a multiple of $(0,1,1)$, the rank is $1$, and two parameters ($v_1$ and $v_3$) stay free:

$$
v_2 = -v_3,\ v_1 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix},\qquad
\vec{v}_2 = \begin{bmatrix} 0 \\ -1 \\ 1 \end{bmatrix}
$$

Since $m_{g,1} = 2 = m_{a,1}$, the repeated eigenvalue still contributes two independent eigenvectors.

**Step 3 — eigenvector for $\lambda_2 = 3$.** Solve $(\mathbf{A} - 3\mathbf{I})\vec{v} = \vec{0}$:

$$
(\mathbf{A} - 3\mathbf{I}) = \begin{bmatrix} -1 & 2 & 2 \\ 0 & -1 & 0 \\ 0 & 1 & 0 \end{bmatrix}
$$

Rows 2 and 3 are again dependent (each is the negative of the other), so the rank is $2$ and only $v_3$ is free:

$$
v_2 = 0,\ v_1 = 2v_3,\ v_3 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_3 = \begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix}
$$

Every eigenvalue has $m_{g,i} = m_{a,i}$, so $\mathbf{A}$ is diagonalizable.

**Step 4 — assemble $\Phi(t)$.** Stack the eigenvectors as columns and read off $\boldsymbol{\Lambda}$:

$$
\mathbf{V} = \begin{bmatrix} 1 & 0 & 2 \\ 0 & -1 & 0 \\ 0 & 1 & 1 \end{bmatrix}, \qquad
\boldsymbol{\Lambda} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}
$$

$\det\mathbf{V} = -1$ (invertible), and the inverse is

$$
\mathbf{V}^{-1} = \begin{bmatrix} 1 & -2 & -2 \\ 0 & -1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
$$

so

$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{V} e^{\boldsymbol{\Lambda}t} \mathbf{V}^{-1}
= \begin{bmatrix} 1 & 0 & 2 \\ 0 & -1 & 0 \\ 0 & 1 & 1 \end{bmatrix}\begin{bmatrix} e^{2t} & 0 & 0 \\ 0 & e^{2t} & 0 \\ 0 & 0 & e^{3t} \end{bmatrix}\begin{bmatrix} 1 & -2 & -2 \\ 0 & -1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
$$

$$
= \begin{bmatrix} e^{2t} & 2(e^{3t}-e^{2t}) & 2(e^{3t}-e^{2t}) \\ 0 & e^{2t} & 0 \\ 0 & e^{3t}-e^{2t} & e^{3t} \end{bmatrix}
$$

Sanity check: $\Phi(0) = \mathbf{I}$, as it must.

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
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A}, \qquad
e^{\lambda t} = \alpha_0(t) + \alpha_1(t)\lambda
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
so the only eigenvalue is $\lambda = 1$ with algebraic multiplicity $m_a = 3$, and geometric multiplicity $m_g = n - \operatorname{rank}(\mathbf{A} - \mathbf{I}) = 3 - 1 = 2 < 3 = m_a$ — defective, so diagonalization is out. We could use Laplace, but we're in the mood for Cayley–Hamilton. Algebraic multiplicity greater than one introduces another complication: we'll need to differentiate to get enough equations.

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

```{=latex}
\begin{example}[frametitle={Example - diagonalization and Cayley–Hamilton on the same matrix}]
```

A quick one to watch both routes land on the same $\Phi(t)$:

$$
\mathbf{A} = \begin{bmatrix} -3 & 4 \\ 0 & -2 \end{bmatrix}
$$

Upper-triangular, so the eigenvalues sit right on the diagonal: $\lambda_1 = -3$, $\lambda_2 = -2$ — distinct, hence diagonalizable.

**Diagonalization.** Eigenvectors from $(\mathbf{A} - \lambda\mathbf{I})\vec{v} = \vec{0}$, one eigenvalue at a time.

For $\lambda_1 = -3$: $(\mathbf{A} + 3\mathbf{I})$ the surviving equation is $4v_2 = 0$ (row two says $v_2 = 0$, the same constraint), forcing $v_2 = 0$ with $v_1$ free $\vec{v}_1 = \tvec{1,0}$

For $\lambda_2 = -2$: $(\mathbf{A} + 2\mathbf{I})$ leaves the single equation $-v_1 + 4v_2 = 0$, i.e. $v_1 = 4v_2$; picking $v_2 = 1$ gives $\vec{v}_2 = \tvec{4,1}$

Then we assemble the vector matrix $\mathbf{V}$ and the diagonal eigenvalue matrix $\boldsymbol{\Lambda}$:

$$
\Phi(t) = \mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}
= \begin{bmatrix} 1 & 4 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} e^{-3t} & 0 \\ 0 & e^{-2t} \end{bmatrix}\begin{bmatrix} 1 & -4 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} e^{-3t} & 4(e^{-2t}-e^{-3t}) \\ 0 & e^{-2t} \end{bmatrix}
$$

**Cayley–Hamilton.** Same $\mathbf{A}$. The characteristic polynomial $\det(\lambda\mathbf{I}-\mathbf{A}) = (\lambda+3)(\lambda+2) = \lambda^2 + 5\lambda + 6$ gives the degree-1 ansatz

$$e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A}$$
$$e^{\lambda t} = \alpha_0 + \alpha_1\lambda$$
$$\lambda_1 = -3: \quad e^{-3t} = \alpha_0 - 3\alpha_1$$
$$\lambda_2 = -2: \quad e^{-2t} = \alpha_0 - 2\alpha_1$$

Subtracting the two equations gives $\alpha_1 = e^{-2t} - e^{-3t}$, and back-substitution yields $\alpha_0 = e^{-3t} + 3\alpha_1 = 3e^{-2t} - 2e^{-3t}$. Putting these back into the matrix form:

$$
\Phi(t) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}
= \left(3e^{-2t} - 2e^{-3t}\right)\mathbf{I}
+ \left(e^{-2t}-e^{-3t}\right)\begin{bmatrix} -3 & 4 \\ 0 & -2 \end{bmatrix}
= \begin{bmatrix} e^{-3t} & 4(e^{-2t}-e^{-3t}) \\ 0 & e^{-2t} \end{bmatrix}
$$

Identical to the diagonalization result — two routes, same $\Phi(t)$, and indeed $\Phi(0) = \mathbf{I}$.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - complex eigenvalues: $\Phi$ via Cayley–Hamilton and an impulse response}]
```

A two-parter that leans on complex eigenvalues (so the state spirals) and an impulse input:

$$
\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix}
= \begin{bmatrix} -1 & -1 \\ 1 & -1 \end{bmatrix}\vec{x}
+ \begin{bmatrix} 1 \\ 0 \end{bmatrix}u
$$

**(a) $\Phi$ via Cayley–Hamilton.** The characteristic polynomial,

$$
\det(\lambda\mathbf{I} - \mathbf{A})
= \begin{vmatrix} \lambda+1 & 1 \\ -1 & \lambda+1 \end{vmatrix}
= (\lambda+1)^2 + 1 = \lambda^2 + 2\lambda + 2
$$

after you apply quadratic formula you get conjugate pair solution $\lambda = -1 \pm i$ — the $\pm i$. Cayley–Hamilton doesn't care: $\mathbf{A}^2 + 2\mathbf{A} + 2\mathbf{I} = \mathbf{0}$, so with $n = 2$

$$e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A}$$
$$e^{\lambda t} = \alpha_0 + \alpha_1\lambda$$

Evaluate at $\lambda = -1 + i$ (the conjugate root merely conjugates the same equations). By Euler, $e^{(-1+i)t} = e^{-t}(\cos t + i\sin t)$, so splitting $\alpha_0 + \alpha_1(-1+i)$ into real and imaginary parts:

$$e^{-t}\cos t = \alpha_0 - \alpha_1$$
$$e^{-t}\sin t = \alpha_1$$

hence $\alpha_1 = e^{-t}\sin t$ and $\alpha_0 = e^{-t}(\cos t + \sin t)$. Reassembling entrywise:

$$
\Phi(t) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}
= e^{-t}\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}
$$

the state transition matrix is $e^{-t}$ times a rotation: it spins the state while pulling it toward the origin — a decaying spiral. Sanity check: $\Phi(0) = \mathbf{I}$.

**(b) Impulse response.** Take $\vec{x}(0) = \tvec{1,1}$ and $u(t) = \delta(t)$. The nonhomogeneous solution

$$
\vec{x}(t) = \Phi(t)\vec{x}(0) + \int_0^t \Phi(t-\tau)\mathbf{B}\,u(\tau)\,d\tau
$$

collapses under the sifting property: the $\delta$ at $\tau = 0$ pulls $\Phi(t)\mathbf{B}$ out of the integral — physically, the impulse at $t = 0$ jumps the state by $\mathbf{B}$, so the motion is free from $\vec{x}(0) + \mathbf{B}$:

$$
\vec{x}(t) = \Phi(t)\big(\vec{x}(0) + \mathbf{B}\big)
= e^{-t}\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}\left(\begin{bmatrix} 1 \\ 1 \end{bmatrix} + \begin{bmatrix} 1 \\ 0 \end{bmatrix}\right)
$$

$$
= e^{-t}\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix}
= e^{-t}\begin{bmatrix} 2\cos t - \sin t \\ 2\sin t + \cos t \end{bmatrix}
$$

```{=latex}
\end{example}
```
