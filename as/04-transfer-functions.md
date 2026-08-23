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
