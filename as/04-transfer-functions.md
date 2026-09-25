# Transfer functions

To connect components into a system, each one needs a description of its input–output behaviour, independent of how it is built. As we have seen, the impulse response fully characterizes an LTI system. Every input is a superposition of shifted, scaled impulses, so the output is the *convolution*

$$
y(t) = (h * u)(t) = \int_0^t h(t-\tau)\, u(\tau)\, d\tau
$$

But, no matter how beautiful it is (or because of it), convolution is inconvenient to work with: systems in series give nested integrals, and a feedback loop gives an integral equation. We use a mathematical trick to move everything into another space, where finding solutions becomes easier. The Laplace transform is one of those tricks. It turns convolution into multiplication,

$$
Y(s) = G(s)\,U(s), \qquad G(s) = \mathcal{L}\{h(t)\}
$$

and $G(s)$ is what we call the transfer function. Interconnections of systems become algebra on transfer functions. The same property holds for other transforms, most prominently Fourier and Z. 

The Fourier transform gives the frequency response $G(j\omega)$, which has the most direct meaning: a sinusoid of frequency $\omega$ comes out as a sinusoid of the same frequency, scaled by $|G(j\omega)|$ and shifted by $\angle G(j\omega)$. This is how we think about signals as spectra and systems as filters, and it can be measured directly. Its limitation is convergence. As an ordinary integral, Fourier converges only for signals that die out, which rules out steps, ramps and unstable systems. Laplace adds a decaying factor $e^{-\sigma t}$ with $s = \sigma + j\omega$ and so handles all of them. Fourier is the special case $\sigma = 0$: where both converge, $G(j\omega)$ is simply $G(s)$ on the imaginary axis. The Z-transform does the same job for sampled signals and gives $G(z)$ (see Discrete systems). This chapter uses Laplace.

## Scalar transfer function

In practice $G(s)$ is rarely found by transforming $h(t)$; it comes directly from the system's ODE. For a constant-coefficient ODE $a_n y^{(n)} + \cdots + a_0 y = b_m u^{(m)} + \cdots + b_0 u$, Laplace-transform with zero initial conditions. This is the Laplace $\leftrightarrow$ time connection: differentiation in time becomes multiplication by $s$, so the ODE turns into an algebraic equation,

$$
\underbrace{(a_n s^n + \cdots + a_0)}_{D(s)}Y(s) = \underbrace{(b_m s^m + \cdots + b_0)}_{N(s)}U(s)
$$

and the **transfer function** is the ratio of output to input transform:

$$
G(s) = \frac{Y(s)}{U(s)} = \frac{N(s)}{D(s)} = \frac{b_m s^m + \cdots + b_0}{a_n s^n + \cdots + a_0}
$$

## Impulse response

The inverse transform leads back to the time domain. The two test signals have the simplest transforms,

$$
\mathcal{L}\{\delta(t)\} = 1, \qquad \mathcal{L}\{1(t)\} = \frac{1}{s}
$$

so a unit impulse input gives $Y(s) = G(s)$ and

$$
h(t) = \mathcal{L}^{-1}\{G(s)\}
$$

is the impulse response from the introduction. A unit step gives the step response $\mathcal{L}^{-1}\{G(s)/s\}$, which is the integral of $h$.

```{=latex}
\begin{example}[frametitle={Example - impulse response}]
```

For $y'' + 3y' + 2y = u' + 3u$:

$$
G(s) = \frac{s+3}{s^2 + 3s + 2} = \frac{s+3}{(s+1)(s+2)}
= \frac{2}{s+1} - \frac{1}{s+2}
$$

(partial fractions $\frac{A}{s+1} + \frac{B}{s+2}$: covering up at $s=-1$ gives $A = 2$, at $s=-2$ gives $B = -1$), so

$$
h(t) = \mathcal{L}^{-1}\{G(s)\} = 2e^{-t} - e^{-2t}
$$

Sanity check from both ends of $G(s)$: the initial value theorem gives $h(0^+) = \lim_{s\to\infty} sG(s) = 1 = 2 - 1$, and the area under the impulse response is the DC gain, $\int_0^\infty h\,dt = 2 - \frac{1}{2} = \frac{3}{2} = G(0)$.

```{=latex}
\end{example}
```

## Transfer function from state space

The state-space chapter gave the impulse response of $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$ as $h(t) = \mathbf{C}\Phi(t)\mathbf{B} + \mathbf{D}\delta(t)$. By the introduction, its transform is the transfer function, and with $\mathcal{L}\{\Phi(t)\} = (s\mathbf{I} - \mathbf{A})^{-1}$ (see $\Phi$ via the Laplace transform) and $\mathcal{L}\{\delta(t)\} = 1$, $\mathbf{G}(s) = \mathcal{L}\{h(t)\}$ is the boxed formula below. The same result follows from transforming the state equations directly with zero initial conditions:

$$
s\mathbf{X}(s) = \mathbf{A}\mathbf{X}(s) + \mathbf{B}\mathbf{U}(s)
\quad\Longrightarrow\quad
\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)
\quad\Longrightarrow\quad
\mathbf{Y}(s) = \left[\mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}\right]\mathbf{U}(s)
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

A block diagram is the drawn form of the transfer-function algebra from the introduction. Each block is a transfer function, arrows are signals, summing junctions add or subtract signals, and pickoff points copy a signal. It is how engineers communicate a system without anyone's internal equations.

The basic connections each reduce to a single transfer function:

$$
\text{series: } G_1 G_2, \qquad \text{parallel: } G_1 + G_2, \qquad \text{feedback: } \frac{G}{1 + GH}
$$

Repeating these reductions, together with moving summing junctions and pickoff points, collapses any diagram into one transfer function. Reading a diagram runs the other way, from boxes and arrows back to equations.

## Feedback

In **feedback**, a signal derived from the output is fed back and subtracted from the input:

```{=latex}
\input{tikz/feedback-loop.tex}
```

The summing junction forms the error $E = U - HY$, so

$$
Y = G(U - HY) \quad\Longrightarrow\quad \frac{Y(s)}{U(s)} = \frac{G(s)}{1 + G(s)H(s)}
$$

Unlike series and parallel connections, feedback changes the poles. The closed-loop poles are the roots of $1 + G(s)H(s) = 0$, not the poles of $G$, so choosing $H$ moves them. This is how feedback stabilizes an unstable system or speeds up a slow one.

## Movement of summing junctions and pickoff points

Summing junctions and pickoff points slide through a diagram, but only if the branches they move past are compensated. Moving a summing junction past a block $G$,

```{=latex}
\input{tikz/block-diagram-summing-move.tex}
```

puts a copy of $G$ on *every* branch through the junction, because $G(u_1 + u_2) = Gu_1 + Gu_2$. Moving it the other way — from after the block back to before — divides the bypassed branches by $G$ instead.

Pickoff points compensate the opposite way. Moving the tap from after $G$ to before it,

```{=latex}
\input{tikz/block-diagram-pickoff-move.tex}
```

leaves the tapped branch carrying $u$ instead of $y = Gu$, so a copy of $G$ goes on that branch to keep the tapped signal unchanged. Moving the tap from before $G$ to after it divides the tapped branch by $G$ instead.

## Conversion to and from state space

A block diagram encodes equations, so the equations can be read back off it, and a set of equations can be drawn as a diagram. In both directions the first step is to choose the variables, in particular the state variables.

The key block is the integrator $\frac{1}{s}$: with $\dot{x}$ at its input, its output is $x$. Each integrator therefore holds one state, and the state equations are whatever the rest of the diagram feeds into the integrator inputs. An initial state can be kept as the integrator's initial condition or added as a separate input.

```{=latex}
\input{tikz/integrator-block.tex}
```

Wrapping an integrator in a feedback loop with gain $a$ gives a first-order system:

```{=latex}
\input{tikz/first-order-loop.tex}
```

The summing junction subtracts the feedback $ax$ from $u$, so the integrator input, the state derivative, is

$$
\dot{x} = u - a x
$$

and the output taps the state, $y = x$. Compared with $\dot{x} = \mathbf{A}x + \mathbf{B}u$, $y = \mathbf{C}x + \mathbf{D}u$: $\mathbf{A} = -a$, $\mathbf{B} = 1$, $\mathbf{C} = 1$, $\mathbf{D} = 0$. In the $s$-domain this is the feedback formula with $G = \frac{1}{s}$ and $H = a$, which gives $\frac{1/s}{1 + a/s} = \frac{1}{s + a}$.

Going the other way, start from a transfer function such as $G(s) = \frac{1}{s+4}$ and rearrange until $sY$ stands alone:

$$
(s+4)Y = U \;\Rightarrow\; sY = U - 4Y \;\Rightarrow\; Y = \frac{1}{s}(U - 4Y)
$$

The last form says $Y$ is the integral of $U - 4Y$, which is the loop above with $a = 4$.

Higher orders work the same way with more integrators, one state per integrator. The feedback gains carry the denominator coefficients and the feedforward paths carry the numerator coefficients. Read the equations off the diagram one integrator at a time.

```{=latex}
\begin{example}[frametitle={Example - converting a two-core block diagram to state space}]
```

Two first-order cores: core 1 is an integrator $\frac{1}{s}$ driven by $u_2$ with negative feedback $3$ (net $\frac{1}{s+3}$), core 2 is a $\frac{1}{s+4}$ block driven by $u_1$ plus the coupling $3x_1$ from core 1. The outputs mix the states and feed $u_2$ straight through:

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

Sanity check: $\mathbf{A}$ is triangular, so its eigenvalues $-3$ and $-4$ are read off the diagonal — exactly the poles of the two cores. And one channel end to end: $u_2 \to y_2$ is core 1 alone, $\frac{1}{s+3}$, while the matrices give $\begin{bmatrix} 1 & 0 \end{bmatrix}(s\mathbf{I} - \mathbf{A})^{-1}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \frac{1}{s+3}$.

```{=latex}
\end{example}
```
