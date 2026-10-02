# Appendix B: Formulas

## Laplace and Z-transforms

Definitions, rules and pairs. The Z rules assume a causal sequence, $f[k] = 0$ for $k < 0$.

$$
\begin{array}{c@{\hspace{4em}}c}
\begin{array}[t]{c@{\qquad}c}
f(t) & F(s) \\[4pt] \hline
\rule{0pt}{4ex}f(t) & \displaystyle\int_0^\infty f(t)\, e^{-st}\, dt \\[12pt]
a f(t) + b g(t) & aF(s) + bG(s) \\[6pt]
\dot{f}(t) & sF(s) - f(0) \\[6pt]
\ddot{f}(t) & s^2F(s) - sf(0) - \dot{f}(0) \\[6pt] \hline
\rule{0pt}{3ex}\delta(t) & 1 \\[10pt]
1(t) & \dfrac{1}{s} \\[10pt]
t & \dfrac{1}{s^2} \\[10pt]
e^{at} & \dfrac{1}{s-a} \\[10pt]
t e^{at} & \dfrac{1}{(s-a)^2} \\[10pt]
\sin\omega t & \dfrac{\omega}{s^2+\omega^2} \\[10pt]
\cos\omega t & \dfrac{s}{s^2+\omega^2}
\end{array}
&
\begin{array}[t]{c@{\qquad}c}
f[k] & F(z) \\[4pt] \hline
\rule{0pt}{4ex}f[k] & \displaystyle\sum_{k=0}^{\infty} f[k]\, z^{-k} \\[14pt]
a f[k] + b g[k] & aF(z) + bG(z) \\[6pt]
f[k-1] & z^{-1}F(z) \\[6pt]
f[k+1] & zF(z) - zf[0] \\[6pt]
(f * g)[k] & F(z)\,G(z) \\[6pt] \hline
\rule{0pt}{3ex}\delta[k] & 1 \\[10pt]
u[k] & \dfrac{z}{z-1} \\[10pt]
a^k & \dfrac{z}{z-a} \\[10pt]
k & \dfrac{z}{(z-1)^2}
\end{array}
\end{array}
$$

## Linear algebra

Exponential of a Jordan block:

$$
e^{\mathbf{J}_4(\lambda)t} = e^{\lambda t}\begin{bmatrix}
1 & t & \frac{t^2}{2!} & \frac{t^3}{3!} \\[2pt]
0 & 1 & t & \frac{t^2}{2!} \\[2pt]
0 & 0 & 1 & t \\[2pt]
0 & 0 & 0 & 1
\end{bmatrix}
$$

## State space

Nonhomogeneous solution:

$$
\vec{x}(t) = e^{\mathbf{A}(t-t_0)} \vec{x}(t_0) + \int_{t_0}^{t} e^{\mathbf{A}(t-\tau)} \mathbf{B}\vec{u}(\tau)\, d\tau
$$

Solution via Laplace and $\Phi$ from the resolvent:

$$
\vec{x}(t) = \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\}\vec{x}_0 + \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)\right\}
$$
$$
e^{\mathbf{A}t} = \Phi(t) = \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\}
$$

Diagonalization:

$$
(\mathbf{A} - \lambda\mathbf{I})\vec{v} = \vec{0}
$$
$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{V} e^{\boldsymbol{\Lambda}t} \mathbf{V}^{-1} = \mathbf{V} \begin{bmatrix}
e^{\lambda_1 t} & & \\
& \ddots & \\
& & e^{\lambda_n t}
\end{bmatrix} \mathbf{V}^{-1}
$$

Jordan form:

$$
e^{\mathbf{J}_k(\lambda)t} = e^{\lambda t}\left(\mathbf{I} + \mathbf{N}_k t + \frac{\mathbf{N}_k^2 t^2}{2!} + \cdots + \frac{\mathbf{N}_k^{k-1} t^{k-1}}{(k-1)!}\right)
$$
$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{T} e^{\mathbf{J}t} \mathbf{T}^{-1} = \mathbf{T} \begin{bmatrix}
e^{\mathbf{J}_{k_1}(\lambda_1) t} & & \\
& \ddots & \\
& & e^{\mathbf{J}_{k_p}(\lambda_p) t}
\end{bmatrix} \mathbf{T}^{-1}
$$

## Properties

Stability:

$$
\operatorname{Re}\lambda_i < 0 \ \ \forall i \iff \text{asymptotically stable}
$$

Controllability:

$$
\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{C} = n \iff \text{controllable}
$$

Observability:

$$
\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{O} = n \iff \text{observable}
$$

## Transfer functions

Transfer function from state space:

$$
\mathbf{G}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$$

## Discrete systems

Nonhomogeneous solution:

$$
\vec{x}[k] = \mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1} \mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i]
$$

$\mathbf{A}^k$ and the solution via the Z-transform:

$$
\mathbf{A}^k = \mathcal{Z}^{-1}\left\{z\left(z\mathbf{I} - \mathbf{A}\right)^{-1}\right\}
$$
$$
\vec{X}(z) = z(z\mathbf{I}-\mathbf{A})^{-1}\vec{x}[0] + (z\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}\,U(z)
$$

$\mathbf{A}^k$ via diagonalization:

$$
\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}, \qquad
\boldsymbol{\Lambda}^k = \operatorname{diag}\left(\lambda_1^k, \dots, \lambda_n^k\right)
$$

Stability:

$$
|\lambda_i| < 1 \ \ \forall i \iff \text{asymptotically stable}
$$
