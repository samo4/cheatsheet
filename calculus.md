---
title: "Calculus and Mathematics Cheatsheet"
author: "Samo F."
date: "2025"
header-includes:
  - |
    \usepackage[leftline,framemethod=TikZ]{mdframed}
    \usepackage{tikz}
    \usetikzlibrary{calc,matrix}
---

# Algebra

## Exponent Properties

$$\frac{a^n}{a^m} = a^{n-m}$$

$$x^a y^a = \left( {xy} \right)^a$$

$$x^{\left( {\frac{a}{b}} \right)} = \sqrt[b]{{x^a }}$$

## Properties of radicals

$$\sqrt[n]{a} = a^{\frac{1}{n}}$$

$$\sqrt[n]{ab} = \sqrt[n]{a}\sqrt[n]{b}$$

$$\sqrt[m]{\sqrt[n]{a}} = \sqrt[nm]{a}$$

$$\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$$

$$\sqrt[n]{a^n} = |a|, \quad \text{if } n \text{ is even}$$

## Complex numbers

$$(a+bi)(c+di) =  ac-bd+(ad+bc)i$$

$$(a+bi)(a-bi) =  a^2 + b^2$$

$$|a + bi| = \sqrt{a^2+b^2} \quad \text{Complex Modulus}$$

$$\overline{(a+bi)}=a-bi$$

$$z_1 \cdot z_2 = r_1 \cdot r_2 e^{i(\theta_1 + \theta_2)}$$

$$z^{\frac{1}{n}} = \sqrt[n] r \cdot e^{i(\frac{\phi}{n} + \frac{2k\pi}{n})}; \quad k = 0,1,..,n-1$$

$$e^{ni\theta}=\cos{n\theta} + \sin{n\theta} \quad \text{De Moivre's Formula}$$

## Logarithms

$$\log _b b = 1$$

$$\log _b 1 = 0$$

$$\log _b (x^r) = r \log _b x$$

$$\log _b (xy) = \log _b (x) + \log _b (y)$$

$$\log _b \left( \frac{x}{y} \right) = \log _b (x) - \log _b (y)$$

$$\log _b \left( x \right) = \log _b \left( c \right)\log _c \left( x \right) = \frac{{\log _c \left( x \right)}}{{\log _c \left( b \right)}}$$

## Quadratic Formula

$$x = \frac{{ - b \pm \sqrt {b^2 - 4ac} }}{{2a}} \quad \text{when } ax^2 + bx + c = 0$$

# Linear Algebra

Matrix addition: one by one. (commutative, associative)

Scalar multiplication: all.

Matrix "multiplication of rows into columns". Multiplication is not commutative ($AB\neq BA$).

$$c_{jk} = \sum_{i=1}^{n} a_{ji}b_{ik}$$

Inner or dot product of Vectors
$$\langle a,b \rangle = \mathbf{a} \bullet \mathbf{b} = \textbf{a}^T\mathbf{b}$$

Matrix to the power $A^0=I$

Inverse:

$$
\begin{bmatrix}
    a & b \\ c & d \\
\end{bmatrix}^{-1} =
\frac{1}{\det(\mathbf{A})}
\begin{bmatrix}
    \,\,\,d & \!\!-b \\ -c & \,a \\
\end{bmatrix} =
\frac{1}{ad - bc}
\begin{bmatrix}
    \,\,\,d & \!\!-b \\ -c & \,a \\
\end{bmatrix}
$$

Identities
$$(AB)^T = B^TA^T$$

$$(A+B)^T = A^T+B^T$$

$$(AB)^{-1} = B^{-1}+A^{-1}$$

$$A^kB^l = A^{k+l}$$

Conjugate transpose / adjugate
$$A^* = (\overline{A})^\mathrm{T} = \overline{A^\mathrm{T}}$$

Determinants
$$\det(\mathbf{A}) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n A_{i,\sigma_i}$$

For 3×3 matrices (Sarrus rule):

```{=latex}
\begin{equation}
\begin{tikzpicture}[>=stealth]
\matrix [%
  matrix of math nodes,
  column sep=1em,
  row sep=1em
] (sarrus) {%
  a_{11} & a_{12} & a_{13} & a_{11} & a_{12} \\
  a_{21} & a_{22} & a_{23} & a_{21} & a_{22} \\
  a_{31} & a_{32} & a_{33} & a_{31} & a_{32} \\
};

\path ($(sarrus-1-1.north west)-(0.5em,0)$) edge ($(sarrus-3-1.south west)-(0.5em,0)$)
      ($(sarrus-1-3.north east)+(0.5em,0)$) edge ($(sarrus-3-3.south east)+(0.5em,0)$)
      (sarrus-1-1)                          edge            (sarrus-2-2)
      (sarrus-2-2)                          edge[->]        (sarrus-3-3)
      (sarrus-1-2)                          edge            (sarrus-2-3)
      (sarrus-2-3)                          edge[->]        (sarrus-3-4)
      (sarrus-1-3)                          edge            (sarrus-2-4)
      (sarrus-2-4)                          edge[->]        (sarrus-3-5)
      (sarrus-3-1)                          edge[dashed]    (sarrus-2-2)
      (sarrus-2-2)                          edge[->,dashed] (sarrus-1-3)
      (sarrus-3-2)                          edge[dashed]    (sarrus-2-3)
      (sarrus-2-3)                          edge[->,dashed] (sarrus-1-4)
      (sarrus-3-3)                          edge[dashed]    (sarrus-2-4)
      (sarrus-2-4)                          edge[->,dashed] (sarrus-1-5);

\foreach \c in {1,2,3} {\node[anchor=south] at (sarrus-1-\c.north) {$+$};};
\foreach \c in {1,2,3} {\node[anchor=north] at (sarrus-3-\c.south) {$-$};};
\end{tikzpicture}
\end{equation}
```

$$\det (A \cdot B) = \det (A) \cdot \det (B)$$

$$\det (A^{-1}) = \det (A)^{-1}$$

$$\det\left(rA\right) = r^n\det(A) \quad \text{for all } A^{n\times n} \text{ and scalars } r$$

The determinant of a triangular matrix equals the product of the diagonal entries. Since for any triangular matrix A the matrix $\lambda I-A$, whose determinant is the characteristic polynomial of A, is also triangular, the diagonal entries of A in fact give the multiset of eigenvalues of A (an eigenvalue with multiplicity m occurs exactly m times as diagonal entry)

## Transpose

$$[A^\mathrm{T}]_{ij} = [A]_{ji}$$

$$(A^T)^T = A$$

$$(AB)^T = B^TA^T$$

$$\det(A^T) = \det(A)$$

$$(A^T)^{-1} = (A^{-1})^T$$

# Trigonometry

## Definitions

$$\sin \theta = \frac{{\text{opposite}}}{{\text{hypotenuse}}}$$

$$\tan \theta = \frac{{\text{opposite}}}{{\text{adjacent}}}$$

| $\Theta$      | $0°$ | $30°$                | $45°$                | $60°$                | $90°$ |
| ------------- | ---- | -------------------- | -------------------- | -------------------- | ----- |
| $\sin \Theta$ | $0$  | $\frac{1}{2}$        | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | $1$   |
| $\cos \Theta$ | $1$  | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$        | $0$   |
| $\tan \Theta$ | $0$  | $\frac{1}{\sqrt{3}}$ | $1$                  | $\sqrt{3}$           | /     |

: Trigonometric functions standard values

## Formulas and Identities

$$\tan \theta = \frac{\sin \theta}{\cos \theta}$$

Pythagorean identities
$$\sin^2 \theta + \cos^2 \theta = 1$$

Odd/Even formulas
$$\sin(-\theta) = - \sin \theta$$

$$\cos(-\theta) = \cos \theta$$

Sum and difference formulas
$$\sin \left( {\alpha \pm \beta} \right) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta$$

$$\cos \left( {\alpha \pm \beta } \right) = \cos \alpha \cos \beta \mp \sin \alpha \sin \beta$$

Double angle formulas
$$\sin 2\theta = 2\sin \theta \cos \theta$$

$$\cos 2\theta = \cos ^2 \theta - \sin ^2 \theta = 2\cos ^2 \theta - 1$$

Half angle formulas
$$\tan \frac{\theta}{2} = \pm \sqrt{\frac{1-\cos(\theta)}{1+\cos(\theta)}}$$

Euler's theorem
$$e^{ \pm i\theta } = \cos \theta \pm i\sin \theta$$

$$\cos \theta = \frac{1}{2} (e^{i\theta} + e^{-i\theta})$$

$$\sin \theta = \frac{1}{2i} (e^{i\theta} - e^{-i\theta})$$

Miscellaneous formulas
$$\sin ^2 \theta = \frac{1-\cos(2\theta)}{2}$$

$$\cos ^2 \theta = \frac{1+\sin(2\theta)}{2}$$

# Calculus

## Limits

### Properties

$$\lim_{x \to a} \left[ cf(x) \right] = c\lim_{x \to a} f(x)$$

L'Hopital's Rule
$$\lim_{x \to c} \frac{{f\left( x \right)}}{{g\left( x \right)}} = \lim_{x \to c} \frac{{f'\left( x \right)}}{{g'\left( x \right)}}$$

### Evaluations

$$\lim_{x \to 0} \frac{{\sin x}}{x} = 1$$

$$\lim_{x \to - \infty } e^x = 0$$

## Derivatives

### Definition

$$\frac{d}{{dx}}f\left( x \right) = \lim_{h \to 0} \frac{{f\left( {x + h } \right) - f\left( x \right)}}{h }$$

### Properties

Product rule
$$\left(fg\right)'=f'g+fg'$$

Chain rule
$$\frac{d}{{dx}}\left[ {f\left( u \right)} \right] = \frac{d}{{du}}\left[ {f\left( u \right)} \right]\frac{{du}}{{dx}}$$

or $(f(g(x))'=f'(g(x))g'(x)$ or $(f\circ g)' = (f'\circ g) \cdot g'$

Quotient Rule
$$\left[\frac{f(x)}{g(x)}\right]'=\frac{g(x)f'(x)-f(x)g'(x)}{[g(x)]^2}$$

### Common Derivatives

$$\frac{d}{{dx}}\left(a^x\right)=a^x\ln(a)$$

$$\frac{d}{{dx}}\ln \left( x \right) = \frac{1}{x}, \quad x > 0$$

Power rule
$$\frac{d}{{dx}}x^n = nx^{\left( {n - 1} \right)}$$

$$\frac{d}{{dx}}\cos x = -\sin x$$

$$\frac{d}{{dx}}\sin x = \cos x$$

## Integrals

### Fundamental Theorem of Calculus

$$\int_a^b {\frac{d}{{dx}}F\left( x \right)dx} = F\left( b \right) - F\left( a \right)$$

### Properties

$$\int_{}^{}k dx = kx + C$$

### Common Integrals

$$\int_{}^{}k dx = kx + C$$

$$\int_{}^{}x^n dx = \frac{1}{n+1} x^{n+1} + C, \quad n \neq -1$$

$$\int_{}^{}\frac{1}{x} dx = \ln|x| + C$$

$$\int_{}^{}\ln u du = u\ln(u)-u+C$$

$$\int_{}^{}e^x dx = e^x+C$$

$$\int_{}^{}\sin ax dx = -\frac{1}{a}\cos ax+C$$

$$\int_{}^{}\cos x dx = \sin x+C$$

Per partes (Integration by parts)
$$\int {u\frac{{dv}}{{dx}}} dx = uv - \int {\frac{{du}}{{dx}}} vdx$$

Substitution (or chain) Rule
$$\int {f(u)\frac{du}{dx}} dx = \int f(u)du$$

## Laplace transforms

### Definition

$$X(s) = \int_0^\infty {x(t)e^{ - st} dt}$$

### Properties

$$1 \Leftrightarrow \frac{1}{{s}}$$

Kronecker delta function
$$\delta (t) \Leftrightarrow 1$$

$$Ke^{ - at} u(t) \Leftrightarrow \frac{K}{{s + a}}$$

$$t^n u(t) \Leftrightarrow \frac{{n!}}{{s^{n + 1} }}$$

$$\sin (\alpha t)u(t) \Leftrightarrow \frac{\alpha }{{(s^2 + \alpha ^2 )}}$$

$$\cos (\alpha t)u(t) \Leftrightarrow \frac{s}{{(s^2 + \alpha ^2 )}}$$

$$e^{ - at} \sin (\Omega t)u(t) \Leftrightarrow \frac{\Omega }{{(s + a)^2 + \Omega ^2 }}$$

$$e^{ - at} \cos (\Omega t)u(t) \Leftrightarrow \frac{{s + a}}{{(s + a)^2 + \Omega ^2 }}$$

$$e^{at} x(t) \Leftrightarrow X(s-a)$$

Time domain scaling
$$x(at)u(t) \Leftrightarrow \frac{1}{a}X\left( {\frac{s}{a}} \right)$$

Time domain shifting
$$x(t - a)u(t - a) \Leftrightarrow e^{ - as} X(s + a)$$

Derivative
$$\frac{{d^n x(t)}}{{dt^n }} \Leftrightarrow s^n X(s)$$

or $\mathcal{L}[\dot{x}] = sX(s)-x(0+)$

Integral
$$\int{x(t)dt} \Leftrightarrow \frac{X(s)}{s}$$

Convolution
$$\int_0^\infty {x_1 (\tau )x_2 (t - \tau )d\tau } \Leftrightarrow X_1 (s)X_2 (s)$$

# Greek letters

| Symbol                    | Name    | Symbol              | Name    |
| ------------------------- | ------- | ------------------- | ------- |
| $\alpha A$                | Alpha   | $\nu N$             | Nu      |
| $\beta B$                 | Beta    | $\xi \Xi$           | Xi      |
| $\gamma \Gamma$           | Gamma   | $o O$               | Omicron |
| $\delta \Delta$           | Delta   | $\pi \Pi$           | Pi      |
| $\epsilon \varepsilon$    | Epsilon | $\rho\varrho P$     | Rho     |
| $\zeta Z$                 | Zeta    | $\sigma \Sigma$     | Sigma   |
| $\eta H$                  | Eta     | $\tau T$            | Tau     |
| $\theta \vartheta \Theta$ | Theta   | $\upsilon \Upsilon$ | Upsilon |
| $\iota I$                 | Iota    | $\phi \varphi \Phi$ | Phi     |
| $\kappa K$                | Kappa   | $\chi X$            | Chi     |
| $\lambda \Lambda$         | Lambda  | $\psi \Psi$         | Psi     |
| $\mu M$                   | Mu      | $\omega \Omega$     | Omega   |
