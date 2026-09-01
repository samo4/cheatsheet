# Transfer functions

A transfer function is the input–output description of a system in the $s$-domain: it keeps only how inputs map to outputs, hiding the internal state.

## Heaviside and Dirac

The two building blocks of signal analysis are the **unit step** (Heaviside) and the **unit impulse** (Dirac delta):

$$
u(t) = \begin{cases} 1 & t \ge 0 \\ 0 & t < 0 \end{cases}, \qquad
\delta(t): \quad \int_{-\infty}^{\infty} \delta(t)\, dt = 1, \; \delta(t) = 0 \text{ for } t \ne 0
$$

with the sifting property $\int f(t)\delta(t)\, dt = f(0)$ and Laplace transforms

$$
\mathcal{L}\{u(t)\} = \frac{1}{s}, \qquad \mathcal{L}\{\delta(t)\} = 1
$$

## Scalar transfer function

For a constant-coefficient ODE $a_n y^{(n)} + \cdots + a_0 y = b_m u^{(m)} + \cdots + b_0 u$, Laplace-transform with zero initial conditions. This is the Laplace $\leftrightarrow$ time connection: differentiation in time becomes multiplication by $s$, so the ODE turns into an algebraic equation,

$$
\underbrace{(a_n s^n + \cdots + a_0)}_{D(s)}Y(s) = \underbrace{(b_m s^m + \cdots + b_0)}_{N(s)}U(s)
$$

and the **transfer function** is the ratio of output to input transform:

$$
G(s) = \frac{Y(s)}{U(s)} = \frac{N(s)}{D(s)} = \frac{b_m s^m + \cdots + b_0}{a_n s^n + \cdots + a_0}
$$

## Impulse response and convolution

Feed in a unit impulse, $u(t) = \delta(t)$: since $\mathcal{L}\{\delta(t)\} = 1$, the output transform is just $G(s)$, so

$$
h(t) = \mathcal{L}^{-1}\{G(s)\}
$$

is the **impulse response** — the output to a single kick, and the complete fingerprint of the system. By linearity and time invariance, the response to any input is a superposition of time-shifted, scaled kicks, i.e. the convolution

$$
y(t) = (h * u)(t) = \int_0^t h(t-\tau)\, u(\tau)\, d\tau
$$

```{=latex}
\begin{example}[frametitle={Example - impulse response}]
```

For $y'' + 3y' + 2y = u' + 3u$:

$$
G(s) = \frac{s+3}{s^2 + 3s + 2} = \frac{s+3}{(s+1)(s+2)}
= \frac{2}{s+1} - \frac{1}{s+2}
$$

(partial fractions: $s=-1$ gives $A = 2$, $s=-2$ gives $B = -1$), so

$$
h(t) = \mathcal{L}^{-1}\{G(s)\} = 2e^{-t} - e^{-2t}
$$

```{=latex}
\end{example}
```

## Transfer function from state space

Laplace-transform the state equations $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$ with zero initial conditions:

$$
s\mathbf{X}(s) = \mathbf{A}\mathbf{X}(s) + \mathbf{B}\mathbf{U}(s)
\quad\Longrightarrow\quad
\mathbf{Y}(s) = \underbrace{\left[\mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}\right]}_{\mathbf{G}(s)}\mathbf{U}(s)
$$

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\mathbf{G}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$}
\endgroup
\]
```

```{=latex}
\begin{example}[frametitle={Example - transfer function from state space}]
```

Same $\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$ as in the controllability and observability examples, with $\mathbf{B} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, $\mathbf{C} = \begin{bmatrix} 6 & -6 & 1 \end{bmatrix}$, $\mathbf{D} = 0$. Since $\mathbf{A}$ is diagonal,

$$
(s\mathbf{I} - \mathbf{A})^{-1} = \begin{bmatrix} \frac{1}{s+1} & 0 & 0 \\ 0 & \frac{1}{s+2} & 0 \\ 0 & 0 & \frac{1}{s+3} \end{bmatrix}
$$

and

$$
G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}
= \frac{6}{s+1} - \frac{6}{s+2} + \frac{1}{s+3}
= \frac{s^2 + 9s + 20}{(s+1)(s+2)(s+3)}
= \frac{(s+4)(s+5)}{(s+1)(s+2)(s+3)}
$$

The poles are the eigenvalues of $\mathbf{A}$ ($-1, -2, -3$ — see Modes of an LTI system) and the zeros are $-4, -5$.

```{=latex}
\end{example}
```

## Block diagrams

Block diagrams exist, and they are boring. Boxes and arrows just redraw the same transfer functions — series $G_1G_2$, parallel $G_1 + G_2$, feedback $G_1/(1 + G_1H)$ — without saying anything the transfer functions don't already.

Commonly used in causal control design, they are a convenient shorthand for the algebra of transfer functions, but they are not a fundamental representation of the system.

Their real use is *communication*. But in order to understand block diagrams, some exercises involving  *manipulation* will help you read what a block diagram is trying to communicate to you.

## Feedback

The one interconnection that genuinely creates something new is **feedback** — a signal derived from the output is fed back to the input and subtracted before the system acts:

```{=latex}
\input{tikz/feedback-loop.tex}
```

The summing junction forms the error $e = u - Hy$, so

$$
y = G(u - Hy) \quad\Longrightarrow\quad \frac{Y(s)}{U(s)} = \frac{G(s)}{1 + G(s)H(s)}
$$

## Movement of summing junctions and pickoff points

Summing junctions and pickoff points slide through a diagram, but only if the branches they move past are compensated. Moving a summing junction past a block $G$,

```{=latex}
\input{tikz/block-diagram-summing-move.tex}
```

puts a copy of $G$ on *every* branch through the junction, because $G(u_1 + u_2) = Gu_1 + Gu_2$. Moving it the other way — from after the block back to before — divides the bypassed branches by $G$ instead.

A pickoff point moves the other way. Tapping the signal before $G$ instead of after it,

```{=latex}
\input{tikz/block-diagram-pickoff-move.tex}
```

forces the tapped branch through $1/G$ so the tapped signal is unchanged.

## Conversion to and from state space

Block diagrams are basically encoding equations, and by reading the block diagram you can build them back. Step one in both cases is to identify your variables, especially the state variables. 

The single most important block for state space conversions is the integrator, here represented as a block with $1/s$. If you place $\dot{x}$ on the input of this block, you get $x$ on the output. This already takes care of the A part of the state equation.

Initial state can be packed into the integrator as an initial condition, or you can add it in as a separate input.

```{=latex}
\input{tikz/integrator-block.tex}
```

If you wrap it into a feedback loop, you get a first-order system, $G(s) = \frac{1}{s + a}$:

```{=latex}
\input{tikz/first-order-loop.tex}
```
 
Working backwards from the transfer function shows where the loop comes from: for $G(s) = \frac{1}{s+4}$,

$$
(s+4)Y = U \;\Rightarrow\; sY = U - 4Y \;\Rightarrow\; Y = \frac{1}{s}(U - 4Y)
$$

The last line says $Y$ is the integral of $U - 4Y$: feed $U$ into an integrator, subtract the feedback $4Y$, and out comes the loop above (with $a = 4$).

Reading the diagram: the summing junction subtracts the feedback $a x$ from $u$, so the integrator input — the state derivative — is

$$
\dot{x} = u - a x
$$

and the output taps the state, $y = x$. Compared with $\dot{x} = \mathbf{A}x + \mathbf{B}u$, $y = \mathbf{C}x + \mathbf{D}u$: $\mathbf{A} = -a$, $\mathbf{B} = 1$, $\mathbf{C} = 1$, $\mathbf{D} = 0$.

Higher order is the same story with more integrators: one state per integrator, feedback wrapping in the denominator coefficients, feedforward summing the numerator ones. Read the equations off the diagram, integrator by integrator.

```{=latex}
\begin{example}[frametitle={Example - converting a two-core block diagram to state space}]
```

Two first-order cores: core 1 is an integrator $\frac{1}{s}$ with negative feedback $3$ (net $\frac{1}{s+3}$), core 2 is a $\frac{1}{s+4}$ block driven by $u_1$ plus the coupling $3x_1$ from core 1. The outputs mix the states and feed $u_2$ straight through:

```{=latex}
\input{tikz/two-core-ss.tex}
```

Reading the diagram core by core,

$$
X_1 = \frac{1}{s}(U_2 - 3X_1) \;\Rightarrow\; (s+3)X_1 = U_2 \;\Rightarrow\; \dot{x}_1 = -3x_1 + u_2
$$

$$
X_2 = \frac{1}{s+4}(U_1 + 3X_1) \;\Rightarrow\; (s+4)X_2 = U_1 + 3X_1 \;\Rightarrow\; \dot{x}_2 = 3x_1 - 4x_2 + u_1
$$

and from the output mixing, $y_1 = x_1 + x_2 + u_2$, $y_2 = x_1$. In matrix form:

$$
\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix}
= \begin{bmatrix} -3 & 0 \\ 3 & -4 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
+ \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} u_1 \\ u_2 \end{bmatrix}
$$

$$
\begin{bmatrix} y_1 \\ y_2 \end{bmatrix}
= \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
+ \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} u_1 \\ u_2 \end{bmatrix}
$$ 

```{=latex}
\end{example}
```
