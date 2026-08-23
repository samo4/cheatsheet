# Linearization

Most real systems are nonlinear. Linearization replaces them by a linear system near an operating point, so that all the state-space machinery applies.

## Single-variable Taylor expansion

For a smooth $f(x)$, expand around a point $x_0$:

$$
f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2}f''(x_0)(x - x_0)^2 + \cdots
$$

Dropping the higher-order terms leaves the tangent-line approximation

$$
f(x) \approx f(x_0) + f'(x_0)(x - x_0)
$$

which is good as long as the deviation $|x - x_0|$ is small.

```{=latex}
\begin{example}[frametitle={Example - linearizing the diode}]
```

The Shockley diode law $i = I_s(e^{v/V_T} - 1)$ is strongly nonlinear. Around an operating point $v_0$,

$$
i \approx i_0 + \left.\frac{di}{dv}\right|_{v_0}(v - v_0), \qquad
g_d = \left.\frac{di}{dv}\right|_{v_0} = \frac{I_s}{V_T}e^{v_0/V_T} = \frac{i_0 + I_s}{V_T} \approx \frac{i_0}{V_T}
$$

so near the bias point the diode behaves like a small-signal resistor $r_d = 1/g_d = V_T/i_0$ (about $25\,\text{mV}/i_0$ at room temperature).

```{=latex}
\end{example}
```

## Multivariable functions

In several variables the same expansion uses the gradient:

$$
f(\vec{x}) \approx f(\vec{x}_0) + \nabla f(\vec{x}_0)^T(\vec{x} - \vec{x}_0), \qquad
\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}
$$

```{=latex}
\begin{example}[frametitle={Example - linearizing $f(x_1, x_2) = x_1^2 + x_2^2$}]
```

Around $\vec{x}_0 = (1, 2)$: $f(1, 2) = 5$ and $\nabla f(1, 2) = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$, so

$$
f(x_1, x_2) \approx 5 + 2(x_1 - 1) + 4(x_2 - 2) = 2x_1 + 4x_2 - 5
$$

— the plane tangent to the paraboloid at $(1, 2)$.

```{=latex}
\end{example}
```

## Linearizing state-space systems

For $\dot{\vec{x}} = \mathbf{f}(\vec{x}, \vec{u})$ and $\vec{y} = \mathbf{g}(\vec{x}, \vec{u})$, take an equilibrium $(\vec{x}_e, \vec{u}_e)$ with $\mathbf{f}(\vec{x}_e, \vec{u}_e) = \vec{0}$. A first-order Taylor expansion around it gives, in the deviations $\delta\vec{x} = \vec{x} - \vec{x}_e$, $\delta\vec{u} = \vec{u} - \vec{u}_e$:

$$
\delta\dot{\vec{x}} = \mathbf{A}\,\delta\vec{x} + \mathbf{B}\,\delta\vec{u}, \qquad
\delta\vec{y} = \mathbf{C}\,\delta\vec{x} + \mathbf{D}\,\delta\vec{u}
$$

where the matrices are the Jacobians evaluated at the equilibrium:

$$
\mathbf{A} = \left.\frac{\partial \vec{f}}{\partial \vec{x}}\right|_e, \qquad
\mathbf{B} = \left.\frac{\partial \vec{f}}{\partial \vec{u}}\right|_e, \qquad
\mathbf{C} = \left.\frac{\partial \vec{g}}{\partial \vec{x}}\right|_e, \qquad
\mathbf{D} = \left.\frac{\partial \vec{g}}{\partial \vec{u}}\right|_e
$$

The linearization captures the local behaviour: for small deviations the nonlinear and linear trajectories stay close (Hartman–Grobman), so the eigenvalues of $\mathbf{A}$ decide local stability — see Stability. It breaks down at bifurcations, where the linearization is marginally stable.

```{=latex}
\begin{example}[frametitle={Example - linearizing a car leaf spring}]
```

A mass $m$ on a leaf spring has a cubic restoring force:

$$
\dot{x} = v, \qquad \dot{v} = g - \frac{k_1}{m}x - \frac{k_2}{m}x^3
$$

At rest the spring sags to the equilibrium $x_e$ with $k_1 x_e + k_2 x_e^3 = mg$, $v_e = 0$. With $\vec{f}(x, v) = \begin{bmatrix} v \\ g - \frac{k_1}{m}x - \frac{k_2}{m}x^3 \end{bmatrix}$, the Jacobian at the equilibrium is

$$
\mathbf{A} = \begin{bmatrix} \frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial v} \\ \frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial v} \end{bmatrix}_e
= \begin{bmatrix} 0 & 1 \\ -\frac{k_1 + 3k_2 x_e^2}{m} & 0 \end{bmatrix}
$$

so $\delta\ddot{x} + \dfrac{k_1 + 3k_2 x_e^2}{m}\,\delta x = 0$: the cubic term simply adds a linear stiffness $3k_2 x_e^2$ at the operating point.

```{=latex}
\end{example}
```
