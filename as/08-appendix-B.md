# Appendix B: Calculus and transforms review

## Calculus

### Taylor series

Near a point $x_0$ a smooth function is its polynomial expansion — value, slope, curvature and all higher derivatives matched there:

$$
f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
= f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \cdots
$$

The $k!$ is the leftover from differentiating $x^k$ $k$ times, and the coefficients are read off the derivatives at $x_0$. Expanding at $x_0 = 0$ is the Maclaurin series, and three of those do all the work in these notes:

$$
e^{x} = \underbrace{1}_{\cos} + \underbrace{x}_{\sin} + \underbrace{\frac{x^{2}}{2!}}_{\cos} + \underbrace{\frac{x^{3}}{3!}}_{\sin} + \underbrace{\frac{x^{4}}{4!}}_{\cos} + \underbrace{\frac{x^{5}}{5!}}_{\sin} + \cdots
$$

The underbraces sort the terms by parity — the even powers build $\cos$, the odd powers build $\sin$.

Cutting after the linear term leaves the tangent line $f(x) \approx f(x_0) + f'(x_0)(x-x_0)$, good while the deviation $|x - x_0|$ is small and off by the size of the first discarded term — see the Linearization chapter.

## Continuous-time math

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

- Distinct linear factors $(s-a)(s-b)$: $\ \dfrac{A}{s-a} + \dfrac{B}{s-b}$
- Repeated factors $(s-a)^2$: $\ \dfrac{A}{s-a} + \dfrac{B}{(s-a)^2}$
- Irreducible quadratic $s^2 + \omega^2$: $\ \dfrac{As + B}{s^2 + \omega^2}$ ($\to$ sines and cosines)

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

Sanity check: at a convenient point, $s = 0$, both sides give $\frac{1}{2} = -1 + 1 + \frac{1}{2}$. In time, the denominator is three degrees above the numerator, so the response must start flat, $f(0) = \dot{f}(0) = 0$ — and it does: $f(0) = -1 + 0 + 1 = 0$, $\dot{f}(0) = 1 + 1 - 2 = 0$.

```{=latex}
\end{example}
```
