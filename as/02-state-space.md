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

with $\mathbf{A}$ the dynamics, $\mathbf{B}$ the input coupling, $\mathbf{C}$ the output coupling, and $\mathbf{D}$ the direct feedthrough — often, but certainly not always, $\mathbf{D} = \mathbf{0}$. The outputs are generally not the states themselves.

A single second-order ODE is enough to show where the four matrices come from.

```{=latex}
\begin{example}[frametitle={Example - second-order ODE to state space}]
```

Take the second-order ODE

$$
\ddot{y} + 2\dot{y} + 3y = 4u
$$

and define the states $x_1 = y$, $x_2 = \dot{y}$. The system is then just


$$\dot{x}_1 = x_2$$
$$\dot{x}_2 = \ddot{y} = -3x_1 - 2x_2 + 4u$$

which is exactly the state-space shape we are after:

$$
\begin{bmatrix} \dot{x_1} \\ \dot{x_2} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u, \qquad
y = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}
$$

```{=latex}
\end{example}
```

The idea is Kalman's: recasting a linear system as matrices acting on a state vector is what he did in 1960 [@kalman1960general], the year usually called the birth of modern system theory [@bernhard2019kalman].

The state variables are not unique. Relabeling is the dull case — reordering $x_1 = y$, $x_2 = \dot{y}$ changes nothing but the row order. The interesting case is swapping one physical quantity for another, which is a genuine choice rather than a relabeling.

```{=latex}
\begin{example}[frametitle={Example - state variables are not unique}]
```

Two elements give a state, a third gives a choice. A current source $i_g$ and a capacitor $C$ sit in parallel, and that pair drives a series $L$–$R$ branch.

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

Now keep the circuit and change only the description: $\tilde{\vec{x}} = \tvec{u_C, u_R}$ — the capacitor voltage and the resistor voltage $u_R = R i_L$. The two state vectors are related by the invertible linear map $\tilde{\vec{x}} = \mathbf{T}^{-1}\vec{x}$, $\mathbf{T}^{-1} = \operatorname{diag}(1, R)$, so each determines the other and neither is privileged. Differentiating $u_R = R i_L$ and reusing the two equations above,

$$
\dot{u}_C = \frac{1}{C}i_g - \frac{1}{CR}u_R, \qquad \dot{u}_R = \frac{R}{L}\left(u_C - u_R\right),
$$

$$
\dot{\tilde{\vec{x}}} = \begin{bmatrix} 0 & -\frac{1}{CR} \\ \frac{R}{L} & -\frac{R}{L} \end{bmatrix}\tilde{\vec{x}} + \begin{bmatrix} \frac{1}{C} \\ 0 \end{bmatrix}i_g.
$$

Every entry changed, yet the circuit did not, and the two matrices are similar, $\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}$. They therefore share the same eigenvalues — the characteristic equation $\lambda^2 + \frac{R}{L}\lambda + \frac{1}{LC} = 0$ is the same either way — so both descriptions ring at the same frequency and decay at the same rate.

What the second choice buys is bookkeeping. Both components of $\tilde{\vec{x}}$ are voltages, so the state plane carries one unit and one axis scale; and if the resistor voltage is the quantity worth measuring, the output equation collapses to $y = \begin{bmatrix} 0 & 1 \end{bmatrix}\tilde{\vec{x}}$, one of the states, against $y = \begin{bmatrix} 0 & R \end{bmatrix}\vec{x}$ before.

```{=latex}
\end{example}
```

## Homogeneous solution

$$
\dot{\vec{x}} = \mathbf{A}\vec{x}, \qquad \vec{x}(t_0) = \vec{x}_0
$$

is a linear ODE with no input ($\vec{u} = \vec{0}$), which is what *homogeneous* means here. The scalar case is the one you already know: $\dot{x} = ax$ has the solution $x(t) = x_0\,e^{a(t-t_0)}$. The vector case is the same with $a$ replaced by $\mathbf{A}$,

$$
\vec{x}(t) = \vec{x}_0\, e^{\mathbf{A}(t-t_0)},
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

Because mathematicians don't like writing/typing $e^{\mathbf{A}t}$, they shorthand it to $\Phi(t)$ and call it the state transition matrix — it carries the state from one time to another, $\vec{x}(t) = \Phi(t-t_0)\,\vec{x}_0$.

### Properties of the state-transition matrix

Four properties, and taken together they answer a plain question: what *is* $\Phi$? A family of matrices you can multiply, that has a do-nothing member, and whose members can all be undone — everything built out of the one matrix $\mathbf{A}$. That is the payoff: knowing $\mathbf{A}$ is knowing how the state moves at every later time.

#### The identity

$$
\Phi(0) = \mathbf{I}
$$

The cheapest of the four, and obvious once said: at time zero nothing has happened yet, so the state is the same as the initial state. It's also very usefull as sanity check after every computation of $\Phi$.

#### The semigroup property

$$
\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)
$$

Evolve for $t_1$, then evolve for another $t_2$, and the state lands exactly where a single run of $t_1 + t_2$ would have left it. How the state reached $\vec{x}(t_1)$ is irrelevant to what happens next: **the state is a complete summary of the past**.

#### Inverses

$$
\Phi(t_1 - t_2) = \Phi(t_1)\Phi^{-1}(t_2)
$$

The semigroup property read in reverse. Nothing is assumed here, the inverse is handed to you: take $t_1 = t$ and $t_2 = -t$, and you get $\Phi(t)\Phi(-t) = \Phi(0) = \mathbf{I}$. So every $\Phi$ is invertible, nothing was computed to learn that — no determinant anywhere — and it stays true even when $\mathbf{A}$ itself is singular.

#### The defining ODE

$$
\dot{\Phi}(t) = \mathbf{A}\Phi(t)
$$

The derivative worked out above, with the order free: $\mathbf{A}\Phi(t) = \Phi(t)\mathbf{A}$. *Defining*, because this is $\Phi$ written as an equation.

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

Where the first part is the homogeneous solution (response to initial conditions) and the second part is the particular solution (response to the input signal). The second part is a convolution,

$$
\vec{x}(t) = e^{\mathbf{A}(t-t_0)} \vec{x}(t_0) + \big(\Phi * \mathbf{B}\vec{u}\big)(t),
\qquad
(f * g)(t) = \int_{t_0}^{t} f(t - \tau)\, g(\tau)\, d\tau,
$$

and the shape of that integral is not an accident — the figure below is the whole mechanism in one picture.

Over a short interval $d\tau$ at time $\tau$ the input delivers a scaled, delayed impulse, $\vec{u}(\tau)\,d\tau$. A "kick" at time $\tau$ enters the state through $\mathbf{B}$ and then free-evolves for the remaining time $t - \tau$:

$$
\text{kick at } \tau \;\longmapsto\; \Phi(t-\tau)\,\mathbf{B}\,\vec{u}(\tau)\, d\tau
$$

That kernel $\Phi(t-\tau)\mathbf{B}$ is the *impulse response*: the bare reaction to a unit kick, which is the homogeneous solution re-used with the clock shifted.

Linearity is the *sine qua non*: it is what lets the contributions to add at all, and it is why the response to the whole input is the sum over all past $\tau$. Time invariance supplies the second half: every part is answered by the same function, merely shifted. Together they turn that sum over a continuum into the integral above, and make it a *convolution*: each contribution depends on the present time $t$ and the kick time $\tau$ only through their difference $t - \tau$, so the system cares only about how long ago the input arrived, not about what the clock read.

```{=latex}
\input{tikz/convolution-kicks.tex}
```

The input $u(\tau) = 2^{-\tau}$, sliced into three slices of width $\Delta\tau = 1$, so the slices carry the areas $u(\tau_i)\Delta\tau = 1,\ 0.5,\ 0.25$. Below, each slice draws its own curve $u(\tau_i)\Delta\tau\,\phi(t-\tau_i)$ — the same kick response $\phi(t) = e^{-t}$, scaled by the slice's area and shifted to the slice's time — and the bold curve is their sum: the response to the sliced input. Every kick makes that sum jump, because a kick arrives in no time at all; slice thinner and there are more, smaller kicks, the jumps shrink, and the sum settles onto the integral above.

*Why the lower limit matters?* The integral starts at $t_0$ because that is where our knowledge of the input starts; anything earlier must already be accounted for in $\vec{x}(t_0)$. Starting it at $0$ when the experiment did not begin at $0$ silently charges the whole pre-history of the system to the initial state — the usual home of missing-term errors.

With $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$ the state is seen through $\mathbf{C}$ and the direct path $\mathbf{D}\vec{u}$ is added on top, so a single input/output pair gives

$$
y(t) = \underbrace{(\mathbf{C}\Phi * \mathbf{B}u)(t)}_{\text{through the state}} + \underbrace{\mathbf{D}\,u(t)}_{\text{direct path}} = (h * u)(t),
\qquad
h(t) = \mathbf{C}\Phi(t)\mathbf{B} + \mathbf{D}\delta(t),
$$

which is the same $h(t)$ the Transfer functions chapter defines as $\mathcal{L}^{-1}\{G(s)\}$. A system with no memory at all has $h(t) = \mathbf{D}\delta(t)$ and the convolution collapses to $y = \mathbf{D}u$ — the static case, with no integral in sight.

*From here on, the clock starts with the experiment.* The examples below all take $t_0 = 0$, with $\vec{x}(0)$ the state at that instant and the input applied from then on. For an LTI system this costs no generality — the general form above is this one with the origin moved, $t \mapsto t - t_0$ — but it is not free for a time-varying system, where $\Phi(t, t_0)$ cannot be written as a function of $t - t_0$ alone and the integral stops being a convolution.

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

**Step 1 — $\Phi$ by the defining series.** At this point the only tool for a concrete $\Phi$ is Taylor series\footnote{The same $\Phi$ drops out faster through Laplace, $\mathcal{L}^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$ — an identity we derive in the Laplace transform subsection below, where the hanging-mass example works exactly that route.} Compute the first powers:

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

**Step 2 — the homogeneous part first.** The boxed solution is a sum,

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + \int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

and the first term needs no integration — just a matrix multiply. With the drop condition $\vec{x}_0 = \tvec{0,v_0}$:

$$
\Phi(t)\vec{x}_0 = \begin{bmatrix} \cos\omega_0 t & \frac{1}{\omega_0}\sin\omega_0 t \\[2pt] -\omega_0\sin\omega_0 t & \cos\omega_0 t \end{bmatrix}\begin{bmatrix} 0 \\ v_0 \end{bmatrix}
= \begin{bmatrix} \frac{v_0}{\omega_0}\sin\omega_0 t \\[2pt] v_0\cos\omega_0 t \end{bmatrix}
$$

That is the whole homogeneous response: the free ring of the initial kick, starting at $x = 0$ with speed $v_0$ and oscillating forever (no damping yet).

**Step 3 — the forced part: gravity, via the $\tau$ trick.** The homogeneous piece is done; the input term remains. Gravity is a constant input, $\mathbf{B}\vec{u} = \tvec{0,g}$, so the forced integral is

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

The integrand sees $t$ and $\tau$ only through $t-\tau$, so substitute $u = t-\tau$: as $\tau$ runs $0 \to t$, $u$ runs $t \to 0$, and the minus from $d\tau = -du$ flips the limits back to

$$
\int_0^t \Phi(t-\tau)\,d\tau = \int_0^t \Phi(u)\,du
$$

This is exactly the trick that only works because we start at $0$ — a nonzero lower limit $t_0$ would leave the shifted window $[t-t_0,\, t]$. With $\tau$ gone, what remains is an ordinary integral of $\Phi(u)\mathbf{B}$:

$$
\int_0^t \Phi(u)\mathbf{B}\,du = \int_0^t \begin{bmatrix} \frac{g}{\omega_0}\sin\omega_0 u \\[2pt] g\cos\omega_0 u \end{bmatrix}du
= \begin{bmatrix} \frac{g}{\omega_0^2}(1-\cos\omega_0 t) \\[2pt] \frac{g}{\omega_0}\sin\omega_0 t \end{bmatrix}
$$

**Putting it together** — the full motion is the sum of the two pieces:

$$
\vec{x}(t) = \begin{bmatrix} \frac{v_0}{\omega_0}\sin\omega_0 t \\[2pt] v_0\cos\omega_0 t \end{bmatrix}
+ \begin{bmatrix} \frac{g}{\omega_0^2}(1-\cos\omega_0 t) \\[2pt] \frac{g}{\omega_0}\sin\omega_0 t \end{bmatrix}
$$

Sanity check at $t = 0$: $x(0) = 0$ (both position terms vanish) and $v(0) = v_0$ (only the homogeneous $\cos$ survives), just as dropped. The gravity piece makes the mass ring about the lowered point — its constant part $\frac{g}{\omega_0^2} = \frac{mg}{k}$ is the static stretch that balances the weight — while the $\frac{v_0}{\omega_0}\sin\omega_0 t$ term is the free oscillation of the initial kick superimposed on top.

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

Now let's do something useful with $\Phi$: **the step response**.

Take zero initial state $\vec{x}(0) = \vec{0}$, a step input $u(t) = 5$ (constant for $t \ge 0$), and $\mathbf{B}^{\mathsf{T}} = \left[1\ 0\right]$. The homogeneous term in the boxed solution above dies, leaving the forced convolution:

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

The constant gravity term is the input, $\mathbf{B}\vec{u} = \tvec{0,g}$. This is the boxed solution above in action: build the kernel $\Phi(t) = e^{\mathbf{A}t}$, then run the convolution integral.

**Step 1 — $\Phi$ via Laplace.** $\det(s\mathbf{I} - \mathbf{A}) = s^2 + \frac{b}{m}s + \frac{k}{m}$. Define the natural frequency and damping ratio,

$$
\omega_0 = \sqrt{\frac{k}{m}}, \qquad
\zeta = \frac{b}{2\sqrt{km}} = \frac{b}{2m\omega_0}
$$

so $\frac{b}{m} = 2\zeta\omega_0$ and $\frac{k}{m} = \omega_0^2$, and the determinant takes the classic second-order form, which completes into a sum of squares:

$$
\det(s\mathbf{I} - \mathbf{A}) = s^2 + 2\zeta\omega_0 s + \omega_0^2
= (s + \zeta\omega_0)^2 + \omega_0^2(1-\zeta^2)
$$

Take the **critically damped case $\zeta = 1$** (damper tuned so $b = 2\sqrt{km}$): then the damped frequency $\omega_d = \omega_0\sqrt{1-\zeta^2}$ vanishes, the two poles collide at $s = -\omega_0$, and the resolvent is

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

**Step 2 — solve the state equation.** Plug $\Phi$ into the boxed nonhomogeneous solution above ($t_0 = 0$, $\vec{u} = 1$, $\mathbf{B} = [0, g]^T$):

$$
\vec{x}(t) = \Phi(t)\vec{x}_0 + \int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
$$

With the critical $\Phi$, the kernel dotted with the input is

$$
\Phi(t-\tau)\mathbf{B} = g\,e^{-\omega_0(t-\tau)}\begin{bmatrix} t-\tau \\[2pt] 1 - \omega_0(t-\tau) \end{bmatrix}
$$

so the gravity term reads

$$
\int_0^t \Phi(t-\tau)\mathbf{B}\,d\tau
= g\,e^{-\omega_0 t}\int_0^t \begin{bmatrix} (t-\tau)e^{\omega_0\tau} \\[2pt] (1-\omega_0(t-\tau))e^{\omega_0\tau} \end{bmatrix} d\tau
$$

Evaluating entry by entry — this is the alternative to the $\tau$ trick of the spring example: no substitution, we integrate in $\tau$ directly and watch each $\tau$ vanish. The $t$ inside the integrand is a *constant* as far as the $\tau$-integration is concerned, and a $\tau$ disappears only when its antiderivative is evaluated at the limits. First entry — using $\int (t-\tau)e^{\omega_0\tau}\,d\tau = \left(\frac{1}{\omega_0^2}+\frac{t-\tau}{\omega_0}\right)e^{\omega_0\tau}$:

$$
\int_0^t (t-\tau)e^{\omega_0\tau}\,d\tau
= \left[\left(\frac{1}{\omega_0^2}+\frac{t-\tau}{\omega_0}\right)e^{\omega_0\tau}\right]_{0}^{t}
= \frac{e^{\omega_0 t}-1}{\omega_0^2} - \frac{t}{\omega_0}
$$

Second entry — here the antiderivative is simply $(\tau-t)e^{\omega_0\tau}$, because its $\tau$-derivative is $(1-\omega_0(t-\tau))e^{\omega_0\tau}$:

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

*If $\mathbf{A}$ is already diagonal, you hit the jackpot.* When only the main diagonal is nonzero, nothing needs to be done: $\Phi(t)$ reads off by inspection,

$$
\Phi(t) = e^{\mathbf{A}t} = \operatorname{diag}\!\big(e^{d_1 t},\, e^{d_2 t},\, \dots,\, e^{d_n t}\big)
$$

Most $\mathbf{A}$'s are not diagonal, but with a little elbow grease we can still get there — the ingredients are eigenvalues and eigenvectors, so let's detour.

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

**In practice**:

1. Solve $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ for the eigenvalues.
2. For each $\lambda_i$, solve $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v} = \vec{0}$; the number of free parameters in the solution is $m_{g,i}$.

*Triangular shortcut.* If $\mathbf{A}$ is upper or lower triangular, step 1 needs no work: the determinant is already factored, and the eigenvalues are just the diagonal entries. Diagonal was the whole jackpot; triangular is the half-jackpot — eigenvalues free, but the full $\Phi$ still needs a method.

*Watch out for linear dependence.* Since $\lambda_i$ *is* an eigenvalue, the matrix $(\mathbf{A} - \lambda_i\mathbf{I})$ is singular by construction — its rows are linearly dependent. So when you solve $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v} = \vec{0}$, don't be alarmed that one row turns out to be a multiple of another, or that a row is all zeros: that's exactly what should happen. Only the independent equations carry information — their number is the rank, and the leftover free variables are precisely the geometric multiplicity $m_{g,i}$.

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

As always, any scalar multiple of $\vec{v}_1$ is also an eigenvector — the eigenspace is the whole line through $\vec{v}_1$.

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

*$\boldsymbol{\Lambda}$ is fully diagonal; $\Phi$ generally is not.* Diagonalization, when it works, lands on a genuinely diagonal $\boldsymbol{\Lambda}$ — that's the whole deal. The triangular-looking $\Phi$'s below are an accident of the triangular example $\mathbf{A}$'s — triangular in, triangular out.

```{=latex}
\begin{example}[frametitle={Example - modes of a coupled RC pair}]
```

Diagonalization is worth this much machinery because a good choice of state splits a coupled system into independent pieces. Two identical RC sections — capacitance $C$ and leakage $R$ to ground each — joined by a coupling resistor $R_c$ show it.

```{=latex}
\input{tikz/state-nonunique-modes.tex}
```

Writing $v_1, v_2$ for the capacitor voltages and $\alpha = \frac{1}{RC}$, $\beta = \frac{1}{R_cC}$, KCL at the two nodes gives

$$
\dot{\vec{v}} = \begin{bmatrix} -(\alpha+\beta) & \beta \\ \beta & -(\alpha+\beta) \end{bmatrix}\vec{v}.
$$

The coupling ties the two equations together, and no rescaling of the states can break it: scaling multiplies one off-diagonal entry up and the other down by the same factor, leaving their product — and the coupling it represents — untouched. Only a change that *mixes* the two states can separate them. So add and subtract the two equations — that is, choose the *common* and *differential* combinations $w_1 = v_1 + v_2$ and $w_2 = v_1 - v_2$:

$$
\dot{\vec{w}} = \begin{bmatrix} -\alpha & 0 \\ 0 & -(\alpha+2\beta) \end{bmatrix}\vec{w},
$$

two independent first-order systems. The physics explains why: in common mode $v_1 = v_2$, no current flows through $R_c$, and each capacitor discharges through its own $R$ with time constant $RC$; in differential mode $v_1 = -v_2$, the coupling resistor sees the full $2v_1$ and shortens the time constant to $\frac{1}{\alpha+2\beta}$ — exactly as if $\frac{R_c}{2}$ sat in parallel with $R$.

So the new states are not the old ones relabeled; they are coordinates along the eigenvectors of $\mathbf{A}$ — the *modes* of the system. Here they were read off by inspection; in general they are $\mathbf{V}^{-1}\vec{x}$, the same state expressed in the eigenvector basis.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via diagonalization}]
```

$\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. 

$\mathbf{A}$ is lower triangular, so the shortcut applies: the eigenvalues sit on the diagonal, $\lambda_1 = -2$, $\lambda_2 = -1$, and $\det(\mathbf{A} - \lambda\mathbf{I}) = (-2-\lambda)(-1-\lambda) = 0$ just confirms it. They are distinct, so $m_{g,i} = m_{a,i} = 1$ and $\mathbf{A}$ is diagonalizable.

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

which matches the Taylor and Laplace results. 

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

The diagonalization method is perhaps the most elegant, but plain diagonalization fails for defective matrices. With generalized eigenvectors in $\mathbf{T}$, $\boldsymbol{\Lambda}$ becomes the Jordan matrix $\mathbf{J}$ ($1$s on the superdiagonal) and $\Phi(t) = \mathbf{T} e^{\mathbf{J}t} \mathbf{T}^{-1}$ works for every $\mathbf{A}$ — but the eigenvector hunt gets harder.\footnote{See Appendix A for a few words on the Jordan form, including the defective example below worked this way.} The Laplace method above and Cayley–Hamilton\footnote{A. Cayley coined the name \emph{matrix}; W. R. Hamilton invented the quaternions, which, like matrices, refuse to commute.} method below both work even for defective matrices, with no eigenvectors at all.

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

Solving this Vandermonde system gives the $\alpha_j(t)$. If an eigenvalue $\lambda_i$ has algebraic multiplicity $m_{a,i}$, evaluating at $\lambda_i$ yields only one equation; the missing $m_{a,i}-1$ come from differentiating $f(\lambda) = r(\lambda)$ with respect to $\lambda$, $m_{a,i}-1$ times — each eigenvalue contributes exactly as many equations as its multiplicity. Unlike diagonalization, this works even for defective matrices (see the defective-matrix example below).

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

which (you guessed it) matches all previous methods — as it must. $\Phi$ is pinned down by $\dot{\Phi} = \mathbf{A}\Phi$ and $\Phi(0) = \mathbf{I}$, so a given $\mathbf{A}$ has exactly one state transition matrix, and every method has to return it.

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

### Choosing between the four methods

We have shown four ways to skin a cat, but at the end you still have the same dead cat. The Taylor series is the most general, flows nicely from rudimentary principles, but it is tedious. Diagonalization is elegant, and with its Jordan extension it shows how the system works: independent modes along the eigenvectors. Defective matrices make it laborious, though. Laplace transform is a nice trick, but requires some algebraic manipulation (in other words: much harder to implement in computers). Cayley–Hamilton is a clever method, but requires solving a Vandermonde system, and it is a black box: $\Phi$ comes out, insight into the structure doesn't.

In practice the choice depends on $\mathbf{A}$ and on the problem. Cayley–Hamilton (CH) is the one that keeps coming back — it is the method behind controllability and observability later in these notes — and it wins when:

- The matrix is *defective* — plain diagonalization is out, and CH, with the derivative trick for the repeated eigenvalue, picks up where it fails.
- The matrix has *repeated eigenvalues* but is still diagonalizable — CH avoids eigenvector hunting.
- You want a closed form without computing $\mathbf{V}^{-1}$ — CH never inverts a matrix, only multiplies out powers of $\mathbf{A}$.
- You're working with *symbolic parameters*, where eigenvectors get messy — they come out as rational expressions in the parameters, while CH's coefficients stay clean.

In short: **Cayley–Hamilton to compute, eigenvectors to understand.**

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

the quadratic formula gives the conjugate pair $\lambda = -1 \pm i$. Cayley–Hamilton doesn't care: $\mathbf{A}^2 + 2\mathbf{A} + 2\mathbf{I} = \mathbf{0}$, so with $n = 2$

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
