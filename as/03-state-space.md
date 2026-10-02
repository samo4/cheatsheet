# State-space

## State-space variables and equations

A system is captured by its state — the smallest set of variables that fully summarizes its past — plus how that state evolves and how it shapes the outputs. State variables are usually chosen as directly measurable or physically meaningful quantities: in electrical circuits the inductor currents and capacitor voltages, in mechanical systems the displacements and velocities. MIMO (multiple-input, multiple-output) systems bundle this into one picture, with the state vector living inside the system:

```{=latex}
\input{tikz/state-space-mimo.tex}
```

$\vec{u}$ collects the inputs, $\vec{y}$ the outputs, and $\vec{x}$ the states. In general (nonlinear, time-varying) systems the state and output equations read:

$$
\dot{\vec{x}} = \mathbf{f}(\vec{x}, \vec{u}, t), \qquad
\vec{y} = \mathbf{g}(\vec{x}, \vec{u}, t)
$$

For LTI systems they collapse to the state-space form:

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}
$$
$$
\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}
$$

with $\mathbf{A}$ the dynamics, $\mathbf{B}$ the input coupling, $\mathbf{C}$ the output coupling, and $\mathbf{D}$ the direct feedthrough, often $\mathbf{D} = \mathbf{0}$. The outputs are generally not the states themselves. $\mathbf{A}$ maps the state vector to its derivative, so it is square, which we will need shortly.

A single second-order ODE is enough to show where the four matrices come from.

```{=latex}
\begin{example}[frametitle={Example - second-order ODE to state space}]
```

Take the second-order ODE

$$
\ddot{y} + 2\dot{y} + 3y = 4u
$$

and define the states $x_1 = y$, $x_2 = \dot{y}$. Then

$$\dot{x}_1 = x_2$$
$$\dot{x}_2 = \ddot{y} = -3x_1 - 2x_2 + 4u$$

or, in matrix form,

$$
\begin{bmatrix} \dot{x_1} \\ \dot{x_2} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u, \qquad
y = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}
$$

Sanity check: with the states chosen as $y$ and $\dot{y}$, the last row of $\mathbf{A}$ is the ODE's own coefficients with flipped sign, $-3$ and $-2$.

```{=latex}
\end{example}
```

The idea is Kalman's: recasting a linear system as matrices acting on a state vector is what he did in 1960 [@kalman1960general], the year usually called the birth of modern system theory [@bernhard2019kalman].

The state variables are not unique. Reordering variables changes nothing but the row order. The interesting case is swapping one physical quantity for another.

```{=latex}
\begin{example}[frametitle={Example - state variables are not unique}]
```

A current source $i_g$ and a capacitor $C$ in parallel drive a series $L$–$R$ branch.

```{=latex}
\input{tikz/state-nonunique-scaling.tex}
```

With $v_C$ the capacitor voltage and $i_L$ the inductor current, KCL at the node and KVL around the branch give

$$
C\dot{v}_C = i_g - i_L, \qquad L\dot{i}_L = v_C - R i_L,
$$

so for the state $\vec{x} = \tvec{v_C, i_L}$,

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & -\frac{1}{C} \\ \frac{1}{L} & -\frac{R}{L} \end{bmatrix}\vec{x} + \begin{bmatrix} \frac{1}{C} \\ 0 \end{bmatrix}i_g.
$$

Now keep the circuit but choose different states: $\tilde{\vec{x}} = \tvec{u_C, u_R}$, the capacitor voltage and the resistor voltage $u_R = R i_L$. The two state vectors are related by the invertible linear map $\tilde{\vec{x}} = \mathbf{T}^{-1}\vec{x}$, $\mathbf{T}^{-1} = \operatorname{diag}(1, R)$, so each determines the other. Differentiating $u_R = R i_L$ and reusing the two equations above,

$$
\dot{u}_C = \frac{1}{C}i_g - \frac{1}{CR}u_R, \qquad \dot{u}_R = \frac{R}{L}\left(u_C - u_R\right),
$$

$$
\dot{\tilde{\vec{x}}} = \begin{bmatrix} 0 & -\frac{1}{CR} \\ \frac{R}{L} & -\frac{R}{L} \end{bmatrix}\tilde{\vec{x}} + \begin{bmatrix} \frac{1}{C} \\ 0 \end{bmatrix}i_g.
$$

Every entry changed, but the circuit did not: the two matrices are _similar_, $\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}$, so they have the same eigenvalues and the same dynamics.

The second choice only makes the bookkeeping easier: both states are voltages, and if the resistor voltage is the output, it is simply a state, $y = \rvec{0, 1}\tilde{\vec{x}}$ instead of $y = \rvec{0, R}\vec{x}$.

```{=latex}
\end{example}
```

## Homogeneous solution

$$
\dot{\vec{x}} = \mathbf{A}\vec{x}, \qquad \vec{x}(t_0) = \vec{x}_0
$$

is a linear ODE with no input ($\vec{u} = \vec{0}$), which is what *homogeneous* means here. The scalar case $\dot{x} = ax$ has the solution $x(t) = e^{a(t-t_0)}x_0$, and the vector case looks the same, with the matrix $\mathbf{A}$ in place of $a$:

$$
\vec{x}(t) = e^{\mathbf{A}(t-t_0)}\,\vec{x}_0,
$$

provided we can make sense of the exponential of a matrix. The scalar exponential is the Taylor series

$$
e^{at} = 1 + at + \frac{(at)^2}{2!} + \frac{(at)^3}{3!} + \dots
$$

and matrices add and multiply like numbers, so we define

$$
e^{\mathbf{A}t} = \mathbf{I} + \mathbf{A}t + \frac{(\mathbf{A}t)^2}{2!} + \frac{(\mathbf{A}t)^3}{3!} + \dots = \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!}.
$$

Differentiating the series term by term brings one power of $\mathbf{A}$ down from every term:

$$
\frac{d}{dt} e^{\mathbf{A}t} = \sum_{k=1}^{\infty} \frac{(\mathbf{A}t)^{k-1}}{(k-1)!}\,\mathbf{A} = e^{\mathbf{A}t}\mathbf{A} = \mathbf{A}e^{\mathbf{A}t},
$$

where both orders agree because a matrix commutes with itself. At $t = 0$ the series gives $\mathbf{I}$. So $e^{\mathbf{A}(t-t_0)}$ differentiates to $\mathbf{A}\,e^{\mathbf{A}(t-t_0)}$ and equals $\mathbf{I}$ at $t = t_0$: it satisfies both the ODE and the initial condition, which is all we needed.

Because nobody likes typing $e^{\mathbf{A}t}$, it is shortened to $\Phi(t)$ and called the state transition matrix. It carries the state from one time to another, $\vec{x}(t) = \Phi(t-t_0)\,\vec{x}_0$.

### Properties of the state-transition matrix

The four properties below say what kind of object $\Phi$ is: a family of matrices that compose, with $\Phi(0)$ doing nothing and every member invertible. All of it is determined by $\mathbf{A}$, so knowing $\mathbf{A}$ means knowing how the state evolves at every later time.

#### The identity

$$
\Phi(0) = \mathbf{I}
$$

At time zero nothing has happened yet, so the state is still the initial state. This is also a useful sanity check after every computation of $\Phi$.

#### The semigroup property

$$
\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)
$$

Evolving for $t_1$ and then for $t_2$ gives the same state as evolving for $t_1 + t_2$ at once. How the state reached $\vec{x}(t_1)$ is irrelevant to what happens next: **the state is a complete summary of the past**.

#### Inverses

$$
\Phi(t_1 - t_2) = \Phi(t_1)\Phi^{-1}(t_2)
$$

This follows from the semigroup property with $t_1 = t$, $t_2 = -t$: $\Phi(t)\Phi(-t) = \Phi(0) = \mathbf{I}$. So $\Phi(t)$ is always invertible, with inverse $\Phi(-t)$, even when $\mathbf{A}$ is singular.

#### The defining ODE

$$
\dot{\Phi}(t) = \mathbf{A}\Phi(t)
$$

This is the derivative computed above, and the order does not matter: $\mathbf{A}\Phi(t) = \Phi(t)\mathbf{A}$. It is called *defining* because $\Phi$ is the only solution of this ODE with $\Phi(0) = \mathbf{I}$.

## Nonhomogeneous solution

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

The first term is the homogeneous solution (the response to the initial state), the second the particular solution (the response to the input). The second term is a convolution,

$$
\vec{x}(t) = e^{\mathbf{A}(t-t_0)} \vec{x}(t_0) + \big(\Phi * \mathbf{B}\vec{u}\big)(t),
\qquad
(f * g)(t) = \int_{t_0}^{t} f(t - \tau)\, g(\tau)\, d\tau,
$$

and the figure below shows why.

Over a short interval $d\tau$ at time $\tau$ the input delivers a scaled, delayed impulse, $\vec{u}(\tau)\,d\tau$. A "kick" at time $\tau$ enters the state through $\mathbf{B}$ and then free-evolves for the remaining time $t - \tau$:

$$
\text{kick at } \tau \;\longmapsto\; \Phi(t-\tau)\,\mathbf{B}\,\vec{u}(\tau)\, d\tau
$$

The kernel $\Phi(t-\tau)\mathbf{B}$ is the *impulse response*: the response to a unit kick, which is the homogeneous solution shifted in time.

Linearity lets the responses to all past kicks add up, so the response to the whole input is their sum over $\tau$. Time invariance makes every kick produce the same response, only shifted. Together they turn the sum into the integral above and make it a *convolution*: each contribution depends on $t$ and $\tau$ only through $t - \tau$, that is, on how long ago the kick arrived.

```{=latex}
\input{tikz/convolution-kicks.tex}
```

The figure cuts the input $u(\tau) = 2^{-\tau}$ into three slices of width $\Delta\tau = 1$, with areas $u(\tau_i)\Delta\tau = 1,\ 0.5,\ 0.25$. Each slice produces its own curve $u(\tau_i)\Delta\tau\,\phi(t-\tau_i)$: the kick response $\phi(t) = e^{-t}$, scaled by the slice's area and shifted to the slice's time. The bold curve is their sum, the response to the sliced input. It jumps at every kick, because a kick arrives instantaneously. With thinner slices there are more and smaller kicks, and the sum approaches the integral above.

*Why the lower limit matters.* The integral starts at $t_0$ because that is where our knowledge of the input starts; everything earlier must already be contained in $\vec{x}(t_0)$. Starting it at $0$ when the experiment began at another time assigns part of the system's history to the wrong place, a common source of missing terms.

With $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$ the state is seen through $\mathbf{C}$ and the direct path $\mathbf{D}\vec{u}$ is added on top, so a single input/output pair gives

$$
y(t) = \underbrace{(\mathbf{C}\Phi * \mathbf{B}u)(t)}_{\text{through the state}} + \underbrace{\mathbf{D}\,u(t)}_{\text{direct path}} = (h * u)(t),
\qquad
h(t) = \mathbf{C}\Phi(t)\mathbf{B} + \mathbf{D}\delta(t),
$$

which is the same $h(t)$ the Transfer functions chapter defines as $\mathcal{L}^{-1}\{G(s)\}$. A system with no memory at all has $h(t) = \mathbf{D}\delta(t)$ and the convolution reduces to $y = \mathbf{D}u$, the static case.

*From here on, the clock starts with the experiment.* The examples below all take $t_0 = 0$, with $\vec{x}(0)$ the state at that instant and the input applied from then on. For an LTI system this loses no generality, since the general form is the same with the time origin moved, $t \mapsto t - t_0$. For a time-varying system it does: $\Phi(t, t_0)$ is not a function of $t - t_0$ alone, and the integral is no longer a convolution.

```{=latex}
\begin{example}[frametitle={Example - mass on a spring}]
```
A weight is dropped onto a spring, moving downward with speed $v_0$. Take $x$ as the downward displacement from the unstretched position, so at $t = 0$ we have $x = 0$ and $v = v_0$. How will the weight move?

The equation of motion is:

$$m\ddot{x} = -kx + mg$$

Introduce $v = \dot{x}$ and write it in state space:

$$
\begin{bmatrix} \dot{x} \\ \dot{v} \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & 0 \end{bmatrix}\begin{bmatrix} x \\ v \end{bmatrix}
+ \begin{bmatrix} 0 \\ g \end{bmatrix}
$$

**Step 1 — $\Phi$ by the defining series.** At this point our only tool for computing $\Phi$ is the Taylor series. Compute the first powers:

$$
\mathbf{A}^2 = \mathbf{A}\mathbf{A} = \begin{bmatrix} -\frac{k}{m} & 0 \\ 0 & -\frac{k}{m} \end{bmatrix} = -\frac{k}{m}\mathbf{I}
$$

$\mathbf{A}^2$ is a multiple of the identity, so every even power is too, and every odd power is a multiple of $\mathbf{A}$. With $\omega_0 = \sqrt{k/m}$, so that $\mathbf{A}^2 = -\omega_0^2\mathbf{I}$, group the even and odd powers in the series:

$$
\Phi(t) = e^{\mathbf{A}t}
= \mathbf{I}\left(1 - \omega_0^2\frac{t^2}{2!} + \omega_0^4\frac{t^4}{4!} - \cdots\right)
 + \mathbf{A}\left(t - \omega_0^2\frac{t^3}{3!} + \omega_0^4\frac{t^5}{5!} - \cdots\right)
$$

The brackets are the series of $\cos\omega_0 t$ and $\frac{1}{\omega_0}\sin\omega_0 t$:

$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{I}\cos\omega_0 t + \mathbf{A}\,\frac{\sin\omega_0 t}{\omega_0}
= \begin{bmatrix} \cos\omega_0 t & \frac{1}{\omega_0}\sin\omega_0 t \\[2pt] -\omega_0\sin\omega_0 t & \cos\omega_0 t \end{bmatrix}
$$

**Step 2 — the homogeneous part first.** The boxed solution is a sum,

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + \int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

and the first term needs no integration, only a matrix product. With the initial state $\vec{x}_0 = \tvec{0,v_0}$:

$$
\Phi(t)\vec{x}_0 = \begin{bmatrix} \cos\omega_0 t & \frac{1}{\omega_0}\sin\omega_0 t \\[2pt] -\omega_0\sin\omega_0 t & \cos\omega_0 t \end{bmatrix}\begin{bmatrix} 0 \\ v_0 \end{bmatrix}
= \begin{bmatrix} \frac{v_0}{\omega_0}\sin\omega_0 t \\[2pt] v_0\cos\omega_0 t \end{bmatrix}
$$

This is the homogeneous response: starting at $x = 0$ with speed $v_0$, the mass oscillates forever, since there is no damping.

**Step 3 — the forced part: gravity.** Gravity is a constant input, $\mathbf{B}\vec{u} = \tvec{0,g}$, so the forced integral is

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

The integrand sees $t$ and $\tau$ only through $t-\tau$, so substitute $u = t-\tau$: as $\tau$ runs $0 \to t$, $u$ runs $t \to 0$, and the minus from $d\tau = -du$ flips the limits back to

$$
\int_0^t \Phi(t-\tau)\,d\tau = \int_0^t \Phi(u)\,du
$$

What remains is an ordinary integral of $\Phi(u)\mathbf{B}$:

$$
\int_0^t \Phi(u)\mathbf{B}\,du = \int_0^t \begin{bmatrix} \frac{g}{\omega_0}\sin\omega_0 u \\[2pt] g\cos\omega_0 u \end{bmatrix}du
= \begin{bmatrix} \frac{g}{\omega_0^2}(1-\cos\omega_0 t) \\[2pt] \frac{g}{\omega_0}\sin\omega_0 t \end{bmatrix}
$$

**Putting it together.** The full motion is the sum of the two parts:

$$
\vec{x}(t) = \begin{bmatrix} \frac{v_0}{\omega_0}\sin\omega_0 t \\[2pt] v_0\cos\omega_0 t \end{bmatrix}
+ \begin{bmatrix} \frac{g}{\omega_0^2}(1-\cos\omega_0 t) \\[2pt] \frac{g}{\omega_0}\sin\omega_0 t \end{bmatrix}
$$

Sanity check at $t = 0$: $x(0) = 0$ (both position terms vanish) and $v(0) = v_0$ (only the homogeneous $\cos$ survives), as required. The gravity term makes the mass oscillate about a lowered point: its constant part $\frac{g}{\omega_0^2} = \frac{mg}{k}$ is the static stretch that balances the weight. The $\frac{v_0}{\omega_0}\sin\omega_0 t$ term is the free oscillation caused by the initial speed.

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

Adding entry by entry:

$$
e^{\mathbf{A}t} = \begin{bmatrix}
1 - 2t + \frac{4t^2}{2} - \frac{8t^3}{6} + \dots & 0 \\
t - \frac{3t^2}{2} + \frac{7t^3}{6} + \dots & 1 - t + \frac{t^2}{2} - \frac{t^3}{6} + \dots
\end{bmatrix}
$$

Each entry is the series $\sum x^k/k! = e^x$ of an exponential, or a difference of two:

$$
\Phi(t) = e^{\mathbf{A}t} = \begin{bmatrix}
e^{-2t} & 0 \\
e^{-t} - e^{-2t} & e^{-t}
\end{bmatrix}
$$

Sanity check: $\Phi(0) = \mathbf{I}$ and $\dot{\Phi}(0) = \begin{bmatrix} -2 & 0 \\ -1+2 & -1 \end{bmatrix} = \mathbf{A}$.

```{=latex}
\end{example}
```

### $\Phi$ via the Laplace transform

Instead of recognizing series, transform the whole ODE. Apply $\mathcal{L}$ to both sides of

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

The first term is the homogeneous response, the second is the convolution with $\vec{u}$, so comparing with the boxed nonhomogeneous solution above identifies

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
e^{\mathbf{A}t} = \Phi(t) = \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\}
$}
\endgroup
\]
```

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

which matches the Taylor result.

Next, use $\Phi$ to compute **the step response**.

Take zero initial state $\vec{x}(0) = \vec{0}$, a step input $u(t) = 5$ (constant for $t \ge 0$), and $\mathbf{B} = \tvec{1, 0}$. The homogeneous term in the boxed solution vanishes, leaving only the convolution:

$$
\vec{x}(t) = \int_0^t \underbrace{e^{\mathbf{A}(t-\tau)}}_{\Phi(t-\tau)}\,\mathbf{B}\,u(\tau)\,d\tau = e^{\mathbf{A}t}\int_0^t e^{-\mathbf{A}\tau}\,\mathbf{B}\,u(\tau)\,d\tau = 5\,e^{\mathbf{A}t}\int_0^t e^{-\mathbf{A}\tau}\,\mathbf{B}\,d\tau
$$

After splitting $e^{\mathbf{A}(t-\tau)} = e^{\mathbf{A}t}e^{-\mathbf{A}\tau}$, the factor $e^{\mathbf{A}t}$ does not depend on $\tau$ and moves out of the integral, together with the constant $u = 5$. With $e^{\mathbf{A}t} = \Phi(t)$ outside and $e^{-\mathbf{A}\tau} = \Phi(-\tau)$ inside, $\mathbf{B}$ picks out the first column:

$$
\vec{x}(t) = 5 \underbrace{\begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}}_{\Phi(t)} \int_0^t \underbrace{\begin{bmatrix} e^{2\tau} & 0 \\ e^{\tau} - e^{2\tau} & e^{\tau} \end{bmatrix}}_{\Phi(-\tau)} \begin{bmatrix} 1 \\ 0 \end{bmatrix}d\tau
$$

Integrating entry by entry, with $\int_0^t e^{a\tau}d\tau = \frac{e^{at}-1}{a}$:

$$
\int_0^t e^{-\mathbf{A}\tau}\,\mathbf{B}\,d\tau = \int_0^t \begin{bmatrix} e^{2\tau} \\[2pt] e^{\tau} - e^{2\tau} \end{bmatrix}d\tau = \begin{bmatrix} \frac{e^{2t}-1}{2} \\[2pt] (e^{t}-1) - \frac{e^{2t}-1}{2} \end{bmatrix}
$$

and multiplying by $5e^{\mathbf{A}t}$:

$$
\vec{x}(t) = 5 \begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}\begin{bmatrix} \frac{e^{2t}-1}{2} \\[2pt] (e^{t}-1) - \frac{e^{2t}-1}{2} \end{bmatrix}
$$

$$
= \frac{5}{2}\begin{bmatrix} 1 - e^{-2t} \\[2pt] 1 - 2e^{-t} + e^{-2t} \end{bmatrix}
$$

Sanity check: $\vec{x}(0) = \vec{0}$, as started. The final value also follows without any integral: at rest $\dot{\vec{x}} = \vec{0}$, so $\vec{x}(\infty) = -\mathbf{A}^{-1}\mathbf{B}\cdot 5 = -\frac{1}{2}\begin{bmatrix} -1 & 0 \\ -1 & -2 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix}\cdot 5 = \frac{5}{2}\tvec{1, 1}$, where both entries above settle.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - hanging mass on a spring with damper, now with time solution}]
```

A mass $m$ hangs from the ceiling on a spring of constant $k$ with a damper of coefficient $b$; $x$ is the downward displacement from the unstretched length. The equation of motion is

$$
m\ddot{x} = -kx - b\dot{x} + mg
$$

Introduce $v = \dot{x}$ and write it as a first-order system:

$$
\begin{bmatrix} \dot{x} \\ \dot{v} \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\begin{bmatrix} x \\ v \end{bmatrix}
+ \begin{bmatrix} 0 \\ g \end{bmatrix}
$$

The constant gravity term is the input, $\mathbf{B}\vec{u} = \tvec{0,g}$. We use the boxed solution: first compute $\Phi(t) = e^{\mathbf{A}t}$, then evaluate the convolution integral.

**Step 1 — $\Phi$ via Laplace.** $\det(s\mathbf{I} - \mathbf{A}) = s^2 + \frac{b}{m}s + \frac{k}{m}$. Define the natural frequency and damping ratio,

$$
\omega_0 = \sqrt{\frac{k}{m}}, \qquad
\zeta = \frac{b}{2\sqrt{km}} = \frac{b}{2m\omega_0}
$$

so $\frac{b}{m} = 2\zeta\omega_0$ and $\frac{k}{m} = \omega_0^2$, and completing the square gives

$$
\det(s\mathbf{I} - \mathbf{A}) = s^2 + 2\zeta\omega_0 s + \omega_0^2
= (s + \zeta\omega_0)^2 + \omega_0^2(1-\zeta^2)
$$

Take the **critically damped case $\zeta = 1$** (damper tuned so $b = 2\sqrt{km}$): then the damped frequency $\omega_d = \omega_0\sqrt{1-\zeta^2}$ vanishes, the two poles coincide at $s = -\omega_0$, and the resolvent is

$$
(s\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(s + \omega_0)^2}\begin{bmatrix} s + 2\omega_0 & 1 \\[2pt] -\omega_0^2 & s \end{bmatrix}
$$

Inverting with the double-pole pairs $\frac{1}{(s+\omega_0)^2} \leftrightarrow t e^{-\omega_0 t}$ and $\frac{s}{(s+\omega_0)^2} \leftrightarrow (1 - \omega_0 t)e^{-\omega_0 t}$ gives

$$
\Phi(t) = e^{\mathbf{A}t} = e^{-\omega_0 t}\begin{bmatrix}
1 + \omega_0 t & t \\[2pt]
-\omega_0^2 t & 1 - \omega_0 t
\end{bmatrix}
$$

**Step 2 — solve the state equation.** Plug $\Phi$ into the boxed nonhomogeneous solution above ($t_0 = 0$, $\vec{u} = 1$, $\mathbf{B} = \tvec{0, g}$):

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + \int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

With the critically damped $\Phi$, the kernel times $\mathbf{B}$ is

$$
\Phi(t-\tau)\mathbf{B} = g\,e^{-\omega_0(t-\tau)}\begin{bmatrix} t-\tau \\[2pt] 1 - \omega_0(t-\tau) \end{bmatrix}
$$

so the gravity term reads

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
= g\,e^{-\omega_0 t}\int_0^t \begin{bmatrix} (t-\tau)e^{\omega_0\tau} \\[2pt] (1-\omega_0(t-\tau))e^{\omega_0\tau} \end{bmatrix} d\tau
$$

Integrate entry by entry. Unlike in the spring example, we do not substitute but integrate in $\tau$ directly; inside the integral, $t$ is a constant. First entry, using $\int (t-\tau)e^{\omega_0\tau}\,d\tau = \left(\frac{1}{\omega_0^2}+\frac{t-\tau}{\omega_0}\right)e^{\omega_0\tau}$:

$$
\int_0^t (t-\tau)e^{\omega_0\tau}\,d\tau
= \left[\left(\frac{1}{\omega_0^2}+\frac{t-\tau}{\omega_0}\right)e^{\omega_0\tau}\right]_{0}^{t}
= \frac{e^{\omega_0 t}-1}{\omega_0^2} - \frac{t}{\omega_0}
$$

Second entry: the antiderivative is $(\tau-t)e^{\omega_0\tau}$, since its $\tau$-derivative is $(1-\omega_0(t-\tau))e^{\omega_0\tau}$:

$$
\int_0^t \big(1-\omega_0(t-\tau)\big)e^{\omega_0\tau}\,d\tau
= \Big[(\tau-t)e^{\omega_0\tau}\Big]_{0}^{t}
= t
$$

Assembling both rows under the common factor $g\,e^{-\omega_0 t}$:

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
= e^{-\omega_0 t}\begin{bmatrix} \frac{g}{\omega_0^2}\left(e^{\omega_0 t}-1\right) - \frac{g}{\omega_0}t \\[2pt] g\,t \end{bmatrix}
$$

so the full motion is

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + e^{-\omega_0 t}\begin{bmatrix} \frac{g}{\omega_0^2}\left(e^{\omega_0 t}-1\right) - \frac{g}{\omega_0}t \\[2pt] g\,t \end{bmatrix}
$$

Sanity check: at $t = 0$ the gravity term vanishes, leaving $\vec{x}(0) = \vec{x}_0$. As $t \to \infty$, $\Phi(t) \to \mathbf{0}$ and every $e^{-\omega_0 t}$ and $t e^{-\omega_0 t}$ decays.

```{=latex}
\end{example}
```

### $\Phi$ via diagonalization

Powers of a diagonal matrix are easy: each diagonal entry is raised to the power, and the off-diagonal entries stay zero,

$$
\boldsymbol{\Lambda}^k = \begin{bmatrix}
d_1^k & & \\
& \ddots & \\
& & d_n^k
\end{bmatrix}
$$

So, by the Taylor series, the exponential of a diagonal matrix is the diagonal of scalar exponentials,

$$
e^{\mathbf{A}t} = \mathbf{I} + t\mathbf{A} + \frac{t^2}{2!}\mathbf{A}^2 + \frac{t^3}{3!}\mathbf{A}^3 + \dots = \begin{bmatrix} e^{d_1 t} & & \\ & \ddots & \\ & & e^{d_n t} \end{bmatrix} = \begin{bmatrix} \Phi_{11} & & \\ & \ddots & \\ & & \Phi_{nn} \end{bmatrix}
$$

*If $\mathbf{A}$ is already diagonal*, $\Phi(t)$ can be read off directly:

$$
\Phi(t) = e^{\mathbf{A}t} = \operatorname{diag}\!\big(e^{d_1 t},\, e^{d_2 t},\, \dots,\, e^{d_n t}\big)
$$

Most matrices are not diagonal, but many can be made diagonal by a change of basis. The ingredients are the eigenvalues and eigenvectors of $\mathbf{A}$, with their algebraic and geometric multiplicities $m_{a,i}$ and $m_{g,i}$.

*Triangular shortcut.* If $\mathbf{A}$ is upper or lower triangular, the eigenvalues are its diagonal entries, because the determinant is already factored. $\Phi$ itself still has to be computed by one of the methods in this section.

#### Diagonalization

When $m_{g,i} = m_{a,i}$ for every eigenvalue, the $n$ independent eigenvectors stacked as the columns of $\mathbf{V}$ give the factorization (derived in the Linear algebra chapter)

$$
\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}, \qquad \boldsymbol{\Lambda} = \operatorname{diag}(\lambda_1, \dots, \lambda_n)
$$

with each eigenvalue on the diagonal of $\boldsymbol{\Lambda}$ in the same position as its eigenvector in $\mathbf{V}$.

So $\mathbf{A}$ is a diagonal matrix in a different basis. Powers keep this form, because the inner $\mathbf{V}^{-1}\mathbf{V}$ pairs cancel:

$$
\mathbf{A}^2 = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}\,\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}
= \mathbf{V}\boldsymbol{\Lambda}\,(\mathbf{V}^{-1}\mathbf{V})\,\boldsymbol{\Lambda}\mathbf{V}^{-1}
= \mathbf{V}\boldsymbol{\Lambda}^2\mathbf{V}^{-1}
$$

$$
\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}
$$

so the Taylor series becomes

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

Note that $\boldsymbol{\Lambda}$ is diagonal, but $\Phi$ generally is not. The examples below give a triangular $\Phi$ only because their $\mathbf{A}$ is triangular.

```{=latex}
\begin{example}[frametitle={Example - modes of a coupled RC pair}]
```

Diagonalization is worth the effort because a good choice of states splits a coupled system into independent parts. Take two identical RC sections, each with capacitance $C$ and leakage $R$ to ground, joined by a coupling resistor $R_c$.

```{=latex}
\input{tikz/state-nonunique-modes.tex}
```

Writing $v_1, v_2$ for the capacitor voltages and $\alpha = \frac{1}{RC}$, $\beta = \frac{1}{R_cC}$, KCL at the two nodes gives

$$
\dot{\vec{v}} = \begin{bmatrix} -(\alpha+\beta) & \beta \\ \beta & -(\alpha+\beta) \end{bmatrix}\vec{v}.
$$

The coupling ties the two equations together, and no rescaling of the states can break it: scaling multiplies one off-diagonal entry and divides the other by the same factor, leaving their product unchanged. Only a change that *mixes* the two states can separate them. Adding and subtracting the two equations does this, which means choosing the *common* and *differential* combinations $w_1 = v_1 + v_2$ and $w_2 = v_1 - v_2$:

$$
\dot{\vec{w}} = \begin{bmatrix} -\alpha & 0 \\ 0 & -(\alpha+2\beta) \end{bmatrix}\vec{w},
$$

two independent first-order systems. The physics agrees: in common mode, $v_1 = v_2$, no current flows through $R_c$, and each capacitor discharges through its own $R$ with time constant $RC$. In differential mode, $v_1 = -v_2$, the coupling resistor sees the full $2v_1$, which shortens the time constant to $\frac{1}{\alpha+2\beta}$, as if $\frac{R_c}{2}$ were in parallel with $R$.

The new states are coordinates along the eigenvectors of $\mathbf{A}$, the *modes* of the system. Here they were found by inspection; in general they are $\mathbf{V}^{-1}\vec{x}$, the same state expressed in the eigenvector basis.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via diagonalization}]
```

$\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. 

$\mathbf{A}$ is lower triangular, so its eigenvalues are the diagonal entries, $\lambda_1 = -2$ and $\lambda_2 = -1$; $\det(\mathbf{A} - \lambda\mathbf{I}) = (-2-\lambda)(-1-\lambda) = 0$ confirms this. They are distinct, so $m_{g,i} = m_{a,i} = 1$ and $\mathbf{A}$ is diagonalizable.

The eigenvectors follow from the condition

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

The first row is zero, so the rank is $1$ and one variable is free. The remaining equation, $v_1 + v_2 = 0$, gives $v_2 = -v_1$:

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

The bottom row is $-1\times$ the top row, so the rank is $1$ again: the remaining equation $v_1 = 0$ fixes $v_1$ and leaves $v_2$ free:

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

which matches the Taylor and Laplace results. 

```{=latex}
\end{example}
```
```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via diagonalization, 3×3}]
```

A larger example: find $\Phi(t) = e^{\mathbf{A}t}$ for

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

The first row is twice the last, and the middle row is zero. So every row is a multiple of $(0,1,1)$, the rank is $1$, and two parameters ($v_1$ and $v_3$) stay free:

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

Diagonalization is elegant, but it needs a full set of eigenvectors, and a defective matrix does not have one. The next section handles that case.

### $\Phi$ via the Jordan form

$$\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$$

A defective matrix, such as $\mathbf{A}$ above, cannot be diagonalized by any choice of basis. Defective matrices are common: every repeated root of a scalar ODE produces one, from the double integrator $\ddot{x} = 0$ to the critically damped oscillator in the Laplace section.

Instead we use the Jordan form $\mathbf{T}^{-1}\mathbf{A}\mathbf{T} = \mathbf{J}$, the basis in which $\mathbf{A}$ is *as diagonal as possible*. It is less a new method than the general version of diagonalization: it works for every $\mathbf{A}$, and for a diagonalizable one it *is* diagonalization.

#### The exponential of a Jordan block

The similarity passes through the Taylor series as before, since the argument used only $\mathbf{T}\mathbf{T}^{-1} = \mathbf{I}$, never the diagonal shape. So $e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{J}t}\mathbf{T}^{-1}$. Powers of a block-diagonal matrix stay block-diagonal, so $e^{\mathbf{J}t}$ has the exponentials of the individual blocks on its diagonal. It remains to exponentiate one block.

The Linear algebra chapter did this in The exponential of a Jordan block: split $\mathbf{J}_k(\lambda) = \lambda\mathbf{I} + \mathbf{N}_k$, factor out $e^{\lambda t}$, and the series for $e^{\mathbf{N}_k t}$ stops after $k$ terms because $\mathbf{N}_k$ is nilpotent:

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
e^{\mathbf{J}_k(\lambda)t} = e^{\lambda t}\left(\mathbf{I} + \mathbf{N}_k t + \frac{\mathbf{N}_k^2 t^2}{2!} + \cdots + \frac{\mathbf{N}_k^{k-1} t^{k-1}}{(k-1)!}\right)
$}
\endgroup
\]
```

Written out, the powers of $t$ climb the superdiagonals:

$$
e^{\mathbf{J}_k(\lambda)t} = e^{\lambda t}\begin{bmatrix} 1 & t & \frac{t^2}{2!} & \cdots & \frac{t^{k-1}}{(k-1)!} \\ & 1 & t & \ddots & \vdots \\ & & \ddots & \ddots & \frac{t^2}{2!} \\ & & & 1 & t \\ & & & & 1 \end{bmatrix}
$$

and with it, for every $\mathbf{A}$,

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\Phi(t) = e^{\mathbf{A}t} = \mathbf{T} e^{\mathbf{J}t} \mathbf{T}^{-1} = \mathbf{T} \begin{bmatrix}
e^{\mathbf{J}_{k_1}(\lambda_1) t} & & \\
& \ddots & \\
& & e^{\mathbf{J}_{k_p}(\lambda_p) t}
\end{bmatrix} \mathbf{T}^{-1}
$}
\endgroup
\]
```

This is where the $t e^{\lambda t}, t^2 e^{\lambda t}, \dots$ of a defective system come from: a $k\times k$ block produces powers of $t$ up to $t^{k-1}$, and nothing else does.

*Shortcut for a single eigenvalue.* If $\mathbf{A}$ has only one eigenvalue $\lambda$ (with $m_a = n$), then $\mathbf{N} = \mathbf{A} - \lambda\mathbf{I}$ is nilpotent itself, because its only eigenvalue is $0$. The splitting trick then works on $\mathbf{A}$ directly, with no $\mathbf{T}$ at all:

$$
e^{\mathbf{A}t} = e^{\lambda t}\left(\mathbf{I} + \mathbf{N}t + \frac{\mathbf{N}^2t^2}{2!} + \cdots\right)
$$

The series stops as soon as a power of $\mathbf{N}$ vanishes, at the latest after $\mathbf{N}^{n-1}$.

```{=latex}
\begin{example}[frametitle={Example - a matrix already in Jordan form}]
```

The defective matrix from the Linear algebra chapter,

$$
\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}
$$

is already a Jordan matrix: a $1\times1$ block $\mathbf{J}_1(1)$ and a $2\times2$ block $\mathbf{J}_2(2)$. That fits the counting rules, $m_{g,2} = 1$ block of total size $m_{a,2} = 2$. With $\mathbf{T} = \mathbf{I}$, $\Phi$ follows by inspection, block by block:

$$
\Phi(t) = e^{\mathbf{A}t} = \begin{bmatrix} e^{t} & 0 & 0 \\ 0 & e^{2t} & t e^{2t} \\ 0 & 0 & e^{2t} \end{bmatrix}
$$

*Where the $t$ comes from.* Write the $2\times2$ block out as equations: $\dot{x}_3 = 2x_3$ and $\dot{x}_2 = 2x_2 + x_3$. So $x_3 = e^{2t}x_3(0)$ drives $x_2$ like an input, at $x_2$'s own rate. This is resonance, and resonance produces the factor $t$. In the coupled RC pair a change of state decoupled the modes completely. Here no change of state can separate $x_2$ from $x_3$, and the superdiagonal $1$ is that coupling.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - the critically damped oscillator via Jordan form}]
```

Back to the hanging mass from the Laplace section, with $\zeta = 1$:

$$
\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -\omega_0^2 & -2\omega_0 \end{bmatrix}
$$

**Step 1 — eigenvalues and block structure.** $\det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^2 + 2\omega_0\lambda + \omega_0^2 = (\lambda + \omega_0)^2$, so $\lambda = -\omega_0$ with $m_a = 2$. Then

$$
\mathbf{N} = \mathbf{A} + \omega_0\mathbf{I} = \begin{bmatrix} \omega_0 & 1 \\ -\omega_0^2 & -\omega_0 \end{bmatrix}
$$

has rank $1$ (the second row is $-\omega_0\times$ the first), so $m_g = 2 - 1 = 1$. That is one $2\times2$ block:

$$
\mathbf{J} = \begin{bmatrix} -\omega_0 & 1 \\ 0 & -\omega_0 \end{bmatrix}
$$

For a matrix built from a scalar ODE like this one (companion form), $\mathbf{A} - \lambda\mathbf{I}$ always has rank at least $n - 1$, so $m_g = 1$ for every eigenvalue, and a repeated root of an ODE *always* gives a single Jordan block. That is why the textbook recipe for repeated characteristic roots adds $t e^{\lambda t}$.

**Step 2 — the chain.** Pick $\vec{v}_2$ with $\mathbf{N}\vec{v}_2 \ne \vec{0}$, e.g. $\vec{v}_2 = \tvec{0, 1}$, and go down:

$$
\vec{v}_1 = \mathbf{N}\vec{v}_2 = \begin{bmatrix} 1 \\ -\omega_0 \end{bmatrix}
$$

It is an eigenvector, and also the only straight-line trajectory of the system: start with $v(0) = -\omega_0 x(0)$ and the mass returns as a pure $e^{-\omega_0 t}$. Every other start picks up a $t e^{-\omega_0 t}$ as well.

**Step 3 — assemble $\Phi(t)$.**

$$
\mathbf{T} = \begin{bmatrix} \vec{v}_1 & \vec{v}_2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ -\omega_0 & 1 \end{bmatrix}, \qquad
\mathbf{T}^{-1} = \begin{bmatrix} 1 & 0 \\ \omega_0 & 1 \end{bmatrix}
$$

$$
\Phi(t) = \mathbf{T}e^{\mathbf{J}t}\mathbf{T}^{-1}
= e^{-\omega_0 t}\begin{bmatrix} 1 & 0 \\ -\omega_0 & 1 \end{bmatrix}\begin{bmatrix} 1 & t \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ \omega_0 & 1 \end{bmatrix}
= e^{-\omega_0 t}\begin{bmatrix} 1 + \omega_0 t & t \\[2pt] -\omega_0^2 t & 1 - \omega_0 t \end{bmatrix}
$$

This matches the Laplace result, without partial fractions. The single-eigenvalue shortcut is even quicker: $\mathbf{N}^2 = \mathbf{0}$, so $e^{\mathbf{A}t} = e^{-\omega_0 t}(\mathbf{I} + \mathbf{N}t)$, which is the same matrix.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - Jordan form of a defective 3×3 matrix}]
```

$$
\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix}
$$

The same matrix comes back in the Cayley–Hamilton section below, so we can compare the two routes.

**Step 1 — eigenvalues and block structure.** $\det(\mathbf{A} - \lambda\mathbf{I}) = (1-\lambda)^3$ (expand along the first row), so $\lambda = 1$ with $m_a = 3$. With

$$
\mathbf{N} = \mathbf{A} - \mathbf{I} = \begin{bmatrix} 0 & 0 & 0 \\ 1 & 0 & -3 \\ 0 & 0 & 0 \end{bmatrix}, \qquad \mathbf{N}^2 = \mathbf{0}
$$

the ranks are $3, 1, 0$ for $\mathbf{N}^0, \mathbf{N}^1, \mathbf{N}^2$. That gives $3 - 1 = 2$ blocks of size $\ge 1$ (this is $m_g = 2$) and $1 - 0 = 1$ block of size $\ge 2$, so one $2\times2$ and one $1\times1$ block:

$$
\mathbf{J} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

**Step 2 — the chain for the $2\times2$ block.** Take $\vec{v}_2$ with $\mathbf{N}\vec{v}_2 \ne \vec{0}$. The first column of $\mathbf{N}$ is nonzero, so $\vec{v}_2 = \tvec{1, 0, 0}$ works, and

$$
\vec{v}_1 = \mathbf{N}\vec{v}_2 = \tvec{0, 1, 0}
$$

is automatically an eigenvector, because $\mathbf{N}\vec{v}_1 = \mathbf{N}^2\vec{v}_2 = \vec{0}$.

**Step 3 — the eigenvector for the $1\times1$ block.** The eigenspace is $\ker\mathbf{N}$: $x_1 - 3x_3 = 0$, which is two-dimensional. We need a second eigenvector independent of $\vec{v}_1$, e.g. $\vec{v}_3 = \tvec{3, 0, 1}$.

**Step 4 — assemble $\mathbf{T}$ and check.** Order the columns chain-first, bottom up:

$$
\mathbf{T} = [\vec{v}_1\ \vec{v}_2\ \vec{v}_3] = \begin{bmatrix} 0 & 1 & 3 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \qquad
\mathbf{T}^{-1} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & -3 \\ 0 & 0 & 1 \end{bmatrix}
$$

Column by column, $\mathbf{A}\vec{v}_1 = \vec{v}_1$, $\mathbf{A}\vec{v}_2 = \tvec{1, 1, 0} = \vec{v}_1 + \vec{v}_2$ and $\mathbf{A}\vec{v}_3 = \vec{v}_3$. That is $\mathbf{A}\mathbf{T} = \mathbf{T}\mathbf{J}$.

**Step 5 — the exponential.** The $2\times2$ block contributes $e^{t}\begin{bmatrix} 1 & t \\ 0 & 1 \end{bmatrix}$ and the $1\times1$ block $e^{t}$, so

$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{T}e^{\mathbf{J}t}\mathbf{T}^{-1}
= e^{t}\begin{bmatrix} 0 & 1 & 3 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 1 & t & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & -3 \\ 0 & 0 & 1 \end{bmatrix}
= \begin{bmatrix} e^t & 0 & 0 \\ t e^t & e^t & -3t e^t \\ 0 & 0 & e^t \end{bmatrix}
$$

The largest block is $2\times2$, so the highest power of $t$ is $t^1$, even though $m_a = 3$. Shortcut: a single eigenvalue again, and $\mathbf{N}^2 = \mathbf{0}$, so $e^{\mathbf{A}t} = e^{t}(\mathbf{I} + \mathbf{N}t)$ in one line.

```{=latex}
\end{example}
```

The Jordan blocks matter beyond $\Phi$. In LTI analysis you rarely need $\mathbf{T}$ itself, but the block sizes answer questions that the eigenvalues alone leave open; the later chapters point these out where they come up.

By hand, finding the chains is the laborious part. The Laplace method above and the Cayley–Hamilton method below both handle defective matrices with no eigenvectors at all.

### $\Phi$ via Cayley–Hamilton

Cayley–Hamilton turns any analytic function of $\mathbf{A}$ into a polynomial of degree at most $n-1$ in $\mathbf{A}$. Here the function is $f(\lambda) = e^{\lambda t}$, so the matrix exponential must have the form

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A} + \cdots + \alpha_{n-1}(t)\mathbf{A}^{n-1}
$$

The difference is that the coefficients now depend on $t$. Otherwise the recipe is unchanged: match the scalar twin $e^{\lambda t} = \alpha_0(t) + \alpha_1(t)\lambda + \cdots + \alpha_{n-1}(t)\lambda^{n-1}$ at every eigenvalue,

$$
e^{\lambda_i t} = \alpha_0(t) + \alpha_1(t)\lambda_i + \cdots + \alpha_{n-1}(t)\lambda_i^{n-1}, \qquad i = 1, \dots, n
$$

and solve the resulting system for the $\alpha_j(t)$; $t$ lives only in the known right-hand sides. A repeated eigenvalue again needs derivatives with respect to $\lambda$ (not $t$). They give $\frac{d^j}{d\lambda^j}e^{\lambda t} = t^j e^{\lambda t}$, the terms a Jordan block needs. In Jordan coordinates every method for $f(\mathbf{A})$ (Taylor, Laplace, Cayley–Hamilton) reduces to applying $f$ to the individual blocks, which is why they all agree. Unlike diagonalization, this works even for defective matrices (see the defective-matrix example below).

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

Evaluating at the eigenvalues gives a $2\times2$ linear system in $\alpha_0, \alpha_1$, with $t$ only on the right-hand side:

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

which matches all previous methods, as it must: $\dot{\Phi} = \mathbf{A}\Phi$ with $\Phi(0) = \mathbf{I}$ has only one solution, so every method returns the same $\Phi$.

```{=latex}
\end{example}
```
```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ for non-diagonalizable A via Cayley–Hamilton}]
```
Take
$$
\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix}
$$
Its characteristic polynomial is
$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \det\begin{bmatrix} 1-\lambda & 0 & 0 \\ 1 & 1-\lambda & -3 \\ 0 & 0 & 1-\lambda \end{bmatrix} = (1-\lambda)^3
$$
so the only eigenvalue is $\lambda = 1$ with algebraic multiplicity $m_a = 3$, and geometric multiplicity $m_g = n - \operatorname{rank}(\mathbf{A} - \mathbf{I}) = 3 - 1 = 2 < 3 = m_a$. The matrix is defective, so diagonalization fails. The Jordan section above found its $\Phi$ through a chain of generalized eigenvectors; Cayley–Hamilton needs no eigenvectors at all. Because the eigenvalue is repeated, we will need derivatives to get enough equations.

**Step 1: set up the ansatz.** With $n = 3$ the exponential reduces to a degree-2 polynomial in $\mathbf{A}$:

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A} + \alpha_2(t)\mathbf{A}^2, \qquad
e^{\lambda t} = \alpha_0(t) + \alpha_1(t)\lambda + \alpha_2(t)\lambda^2
$$

**Step 2: handle the repeated eigenvalue by differentiating.** Evaluating the scalar equation at $\lambda = 1$ gives only one equation for three unknowns. The missing two come from differentiating with respect to $\lambda$ (the $\alpha_j$ depend on $t$, not on $\lambda$, so their $\lambda$-derivatives vanish):

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

Substituting into $\Phi(t) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A} + \alpha_2\mathbf{A}^2$ and adding entry by entry: every diagonal entry is $\alpha_0 + \alpha_1 + \alpha_2 = e^t$, while the only nonzero off-diagonals are $(2,1) = \alpha_1 + 2\alpha_2 = t e^t$ and $(2,3) = -3\alpha_1 - 6\alpha_2 = -3t e^t$. Hence

$$
\Phi(t) = e^{\mathbf{A}t} = \begin{bmatrix} e^t & 0 & 0 \\ t e^t & e^t & -3t e^t \\ 0 & 0 & e^t \end{bmatrix}
$$

Sanity check: $\Phi(0) = \mathbf{I}$, and differentiating at $t = 0$ ($\frac{d}{dt}te^t = 1$ there) gives back $\dot{\Phi}(0) = \mathbf{A}$ entry by entry. It is the same $\Phi$ as in the Jordan-form example: no eigenvectors here, but no insight into the block structure either.

```{=latex}
\end{example}
```

### Choosing between the four methods

We have shown four ways to skin a cat, but at the end you still have the same dead cat. The Taylor series is the most general and follows from first principles, but it is tedious. Diagonalization is elegant, and with its Jordan extension it shows how the system works: independent modes along the eigenvectors. Defective matrices make it laborious, though. The Laplace transform is a neat trick, but it needs symbolic algebra, which makes it hard to implement on a computer. Cayley–Hamilton is clever, but it is a black box: it gives $\Phi$, but no insight into the structure.

In practice the choice depends on $\mathbf{A}$ and on the problem. Cayley–Hamilton (CH) comes back later as the basis of controllability and observability, and it is the best choice when:

- The matrix is *defective*: diagonalization fails, and the Jordan chains are laborious. CH, with derivatives for the repeated eigenvalue, needs no eigenvectors.
- The matrix has *repeated eigenvalues* but is still diagonalizable: CH avoids computing eigenvectors.
- You want a closed form without computing $\mathbf{V}^{-1}$: CH never inverts a matrix, it only multiplies powers of $\mathbf{A}$.
- You work with *symbolic parameters*: eigenvectors become rational expressions in the parameters, while CH's coefficients stay simpler.

In short: **Cayley–Hamilton to compute, diagonalization (and its Jordan extension) to understand.**^[In the spirit of Hamming's motto, "The purpose of computing is insight, not numbers" [@hamming1962numerical]. For many more ways to compute $e^{\mathbf{A}t}$, and why most of them are numerically dubious, see @moler2003nineteen.]

```{=latex}
\begin{example}[frametitle={Example - diagonalization and Cayley–Hamilton on the same matrix}]
```

Both methods applied to one matrix:

$$
\mathbf{A} = \begin{bmatrix} -3 & 4 \\ 0 & -2 \end{bmatrix}
$$

It is upper triangular, so the eigenvalues are the diagonal entries, $\lambda_1 = -3$ and $\lambda_2 = -2$. They are distinct, so $\mathbf{A}$ is diagonalizable.

**Diagonalization.** Eigenvectors from $(\mathbf{A} - \lambda\mathbf{I})\vec{v} = \vec{0}$, one eigenvalue at a time.

For $\lambda_1 = -3$: $\mathbf{A} + 3\mathbf{I} = \begin{bmatrix} 0 & 4 \\ 0 & 1 \end{bmatrix}$, so $v_2 = 0$ and $v_1$ is free: $\vec{v}_1 = \tvec{1, 0}$.

For $\lambda_2 = -2$: $\mathbf{A} + 2\mathbf{I} = \begin{bmatrix} -1 & 4 \\ 0 & 0 \end{bmatrix}$ leaves $-v_1 + 4v_2 = 0$, so $v_1 = 4v_2$; with $v_2 = 1$, $\vec{v}_2 = \tvec{4, 1}$.

With the eigenvectors as the columns of $\mathbf{V}$ and the eigenvalues on the diagonal of $\boldsymbol{\Lambda}$:

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

This is the diagonalization result again, and $\Phi(0) = \mathbf{I}$.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - complex eigenvalues: $\Phi$ via Cayley–Hamilton and an impulse response}]
```

An example with complex eigenvalues, so the state spirals, and an impulse input:

$$
\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix}
= \begin{bmatrix} -1 & -1 \\ 1 & -1 \end{bmatrix}\vec{x}
+ \begin{bmatrix} 1 \\ 0 \end{bmatrix}u
$$

**(a) $\Phi$ via Cayley–Hamilton.** The characteristic polynomial is

$$
\det(\lambda\mathbf{I} - \mathbf{A})
= \begin{vmatrix} \lambda+1 & 1 \\ -1 & \lambda+1 \end{vmatrix}
= (\lambda+1)^2 + 1 = \lambda^2 + 2\lambda + 2
$$

with the conjugate roots $\lambda = -1 \pm i$. Cayley–Hamilton works the same for complex eigenvalues: $\mathbf{A}^2 + 2\mathbf{A} + 2\mathbf{I} = \mathbf{0}$, so with $n = 2$

$$e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A}$$
$$e^{\lambda t} = \alpha_0 + \alpha_1\lambda$$

Evaluate at $\lambda = -1 + i$ (the conjugate root gives the conjugate equation, nothing new). By Euler, $e^{(-1+i)t} = e^{-t}(\cos t + i\sin t)$, so splitting $\alpha_0 + \alpha_1(-1+i)$ into real and imaginary parts:

$$e^{-t}\cos t = \alpha_0 - \alpha_1$$
$$e^{-t}\sin t = \alpha_1$$

hence $\alpha_1 = e^{-t}\sin t$ and $\alpha_0 = e^{-t}(\cos t + \sin t)$. Then

$$
\Phi(t) = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}
= e^{-t}\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}
$$

So $\Phi$ is $e^{-t}$ times a rotation: it rotates the state while shrinking it toward the origin, a decaying spiral. Sanity check: $\Phi(0) = \mathbf{I}$.

**(b) Impulse response.** Take $\vec{x}(0) = \tvec{1,1}$ and $u(t) = \delta(t)$. The nonhomogeneous solution

$$
\vec{x}(t) = \Phi(t)\vec{x}(0) + \int_0^t \Phi(t-\tau)\mathbf{B}\,u(\tau)\,d\tau
$$

simplifies by the sifting property: the $\delta$ at $\tau = 0$ turns the integral into $\Phi(t)\mathbf{B}$. Physically, the impulse at $t = 0$ makes the state jump by $\mathbf{B}$, and from $\vec{x}(0) + \mathbf{B}$ the system evolves freely:

$$
\vec{x}(t) = \Phi(t)\big(\vec{x}(0) + \mathbf{B}\big)
= e^{-t}\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}\left(\begin{bmatrix} 1 \\ 1 \end{bmatrix} + \begin{bmatrix} 1 \\ 0 \end{bmatrix}\right)
$$

$$
= e^{-t}\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix}
= e^{-t}\begin{bmatrix} 2\cos t - \sin t \\ 2\sin t + \cos t \end{bmatrix}
$$

Sanity check: at $t = 0^+$ this gives $\tvec{2,1} = \vec{x}(0) + \mathbf{B}$, the state right after the kick, which then spirals into the origin as in part (a).

```{=latex}
\end{example}
```
