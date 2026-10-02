# Discrete systems

Sampled-time systems evolve in discrete steps rather than continuously. The continuous time $t$ is replaced by $kT$ where $T$ is the fixed sampling period and $k$ the integer sample index. Since nobody likes typing, we usually drop the $T$. Discrete signals get square brackets, $x[k]$ in place of the continuous $x(t)$, the same convention most programming languages use. Computers are the main reason to study the discrete case at all: they work in steps, which matches the discrete-time model directly, without numerical integration.

## Difference equations

The discrete analogue of an ODE is a **difference equation**. In matrix form it gives the discrete state-space equations, with the next state on the left; they are the direct counterpart of the continuous $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, $\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}$:

$$
\underbrace{\vec{x}[k+1]}_{\text{next}} = \mathbf{A}\underbrace{\vec{x}[k]}_{\text{current}} + \mathbf{B}\underbrace{\vec{u}[k]}_{\text{current}}
$$
$$
\vec{y}[k] = \mathbf{C}\vec{x}[k] + \mathbf{D}\vec{u}[k]
$$

Given the initial state $\vec{x}[0]$, the first equation steps the state forward one sample at a time.

## Modeling examples

```{=latex}
\begin{example}[frametitle={Example - people moving to the city}]
```

A region holds $x_1$ people in the city and $x_2$ people in the surroundings. Each year a fraction $\alpha$ of the city-dwellers move out to the surroundings, and a fraction $\beta$ of the surrounding dwellers move into the city. Nobody enters or leaves the region:

$$
\begin{bmatrix} x_1[k+1] \\ x_2[k+1] \end{bmatrix}
= \begin{bmatrix} 1-\alpha & \beta \\ \alpha & 1-\beta \end{bmatrix}\begin{bmatrix} x_1[k] \\ x_2[k] \end{bmatrix}
$$

Each entry $A_{ij}$ tells how much of current $x_j$ ends up in next year's $x_i$:

- $A_{11} = 1-\alpha$ — current city people contribute to next year's city, minus the fraction $\alpha$ who moved out to the surroundings.
- $A_{12} = \beta$ — the fraction $\beta$ of current surrounding people who move into the city.
- $A_{21} = \alpha$ — the fraction $\alpha$ of current city people who moved out to the surroundings.
- $A_{22} = 1-\beta$ — current surrounding people contribute to next year's surroundings, minus the fraction $\beta$ who moved into the city.

The columns of $\mathbf{A}$ sum to $1$, so the total population is conserved.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - Samuelson's national income model}]
```

$y$ is the **national income**, the total output the economy produces in a year. It is split between consumption $c$, investment $i$ and government spending $g$:

$$
y[k] = c[k] + i[k] + g[k]
$$

- $\alpha$ — **marginal propensity to consume**: the fraction of last year's income spent on consumption this year, $c[k] = \alpha\,y[k-1]$.
- $\beta$ — **accelerator**: how strongly investment reacts to the *change* in consumption, $i[k] = \beta(c[k] - c[k-1])$.

With $c[k] = \alpha y[k-1]$ and $c[k-1] = \alpha y[k-2]$, so that $i[k] = \alpha\beta(y[k-1] - y[k-2])$, the identity becomes the second-order difference equation

$$
y[k] - \alpha(1+\beta)\,y[k-1] + \alpha\beta\, y[k-2] = g[k]
$$

Stack the two previous incomes into the state $\vec{x}[k] = \tvec{y[k-2], y[k-1]}$, next state on the left:

$$
\begin{bmatrix} y[k-1] \\ y[k] \end{bmatrix}
= \begin{bmatrix} 0 & 1 \\ -\alpha\beta & \alpha(1+\beta) \end{bmatrix}\begin{bmatrix} y[k-2] \\ y[k-1] \end{bmatrix}
+ \begin{bmatrix} 0 \\ 1 \end{bmatrix}g[k]
$$

Each entry tells how much of current $x_j$ ends up in next year's $x_i$:

- $A_{11} = 0$ — the oldest income $y[k-2]$ contributes nothing directly to next year's $y[k-1]$; the two-year window slides forward.
- $A_{12} = 1$ — current $y[k-1]$ *is* next year's $x_1$: last year's income shifts into the oldest slot.
- $A_{21} = -\alpha\beta$ — income from two years ago *lowers* this year's income: a large $y[k-2]$ means consumption was high last year, so the change $c[k] - c[k-1]$, and with it the accelerator investment, is small.
- $A_{22} = \alpha(1+\beta)$ — last year's income feeds this year's through both channels: consumption $\alpha\,y[k-1]$ plus the accelerator's positive leg $\alpha\beta\,y[k-1]$.
- $B_1 = 0,\ B_2 = 1$ — government spending enters the identity one-for-one, and only into the newest slot $y[k]$.

So government spending is the input, and the two previous incomes are the initial conditions.

Sanity check: hold spending constant, $g[k] = g$, and look for a steady income $y^*$. The difference equation gives $y^*\big(1 - \alpha(1+\beta) + \alpha\beta\big) = y^*(1 - \alpha) = g$, so $y^* = \frac{g}{1-\alpha}$. The accelerator drops out at rest (no change in consumption, no induced investment), and what is left is the textbook Keynesian multiplier.

```{=latex}
\end{example}
```

## Z-transform

Same idea as the Laplace transform, but for sequences. Where Laplace turns derivatives into algebra, the $z$-transform does the same for **shifts**: a one-sample delay is a factor of $z^{-1}$. Shifting in time becomes multiplying by a power of $z$, so a difference equation becomes an algebraic equation.

The transform itself tags every sample with the delay it has accumulated and sums:

$$
F(z) = \mathcal{Z}\{f[k]\} = \sum_{k=0}^{\infty} f[k]\, z^{-k}
$$

so $f[k]$ is the coefficient of $z^{-k}$, and $z^{-1}$ is the delay operator. It is a *one-sided* transform: the sum runs over $k \ge 0$, so negative indices never appear. By convention we treat the sequence as *causal*, $f[k] = 0 \ \forall k < 0$, and that convention is what makes the shift rules below asymmetric. Once you know what a shift does to the powers of $z$, the rules follow:\footnote{Equivalently, a causal sequence satisfies $f[k] = f[k]\,u[k]$. We could carry the unit-step factor through every rule below, but that would only clutter the notation.}

- Z-transforms are *linear*, so transform piece by piece and add: $\mathcal{Z}\{a f + b g\} = aF + bG$.
- *Delay* (shift to the right): each sample of delay costs $z^{-1}$, $\mathcal{Z}\{f[k-1]\} = z^{-1}F$.
- *Advance* (shift to the left): pull the sequence one sample earlier and multiply by $z$, but subtract the sample that falls off the front, $\mathcal{Z}\{f[k+1]\} = zF - zf[0]$.
- *Convolution*: multiplying two transforms convolves the sequences in time, $\mathcal{Z}\{f * g\} = FG$. As with Laplace, **convolution in time is multiplication in frequency, and vice versa**.

The most-used pairs (inversion by partial fractions, as with Laplace):

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\delta[k] \leftrightarrow 1, \qquad
u[k] \leftrightarrow \frac{z}{z-1}, \qquad
a^k \leftrightarrow \frac{z}{z-a}, \qquad
k \leftrightarrow \frac{z}{(z-1)^2}
$}
\endgroup
\]
```

```{=latex}
\begin{example}[frametitle={Example - partial fraction expansion like we never left Laplace}]
```
$$
y[z] = \frac{z(z-1)}{\left(z+\frac{1}{2}\right)\left(z-\frac{1}{2}\right)(z+1)}
$$

This one is tricky as a first example, because the Laplace way looks perfectly reasonable. Expanding $y[z]$ as it stands gives terms $K/(z-p)$, the same shape as $\frac{K}{s-p}$ in continuous time, and a Laplace-trained eye reads them off at once. But there is no such pair in the table: every pair above has a $z$ in the numerator. Reading those terms off anyway means inventing a transform pair that does not exist, and the answer comes out wrong. Instead, expand $\frac{y[z]}{z}$, which does give clean $K/(z-p)$ terms, and multiply back by $z$ before inverting. That puts the $z$ in the numerator, where the pairs need it:

$$
\frac{y[z]}{z} = \frac{z-1}{\left(z+\frac{1}{2}\right)\left(z-\frac{1}{2}\right)(z+1)} = \frac{A}{z+\frac{1}{2}} + \frac{B}{z-\frac{1}{2}} + \frac{C}{z+1}
$$

Find $A$, $B$, $C$ by equating coefficients of powers of $z$:

$$
z - 1 = (A+B+C)z^2 + \left(\frac{1}{2}A+\frac{3}{2}B\right)z + \left(-\frac{1}{2}A+\frac{1}{2}B-\frac{1}{4}C\right)
$$
$$
A + B + C = 0
$$
$$
\frac{1}{2}A + \frac{3}{2}B = 1
$$
$$
-\frac{1}{2}A + \frac{1}{2}B - \frac{1}{4}C = -1
$$

Solving gives $A = 3$, $B = -\frac{1}{3}$, $C = -\frac{8}{3}$, and multiplying back by $z$ gives

$$
y[z] = \frac{3z}{z+\frac{1}{2}} - \frac{\frac{1}{3}\,z}{z-\frac{1}{2}} - \frac{\frac{8}{3}\,z}{z+1}
$$

**Back to time.** Each term now matches the pair $\frac{Kz}{z-p} \leftrightarrow K p^k$ directly:

$$
y[k] = \mathcal{Z}^{-1}\{y[z]\} = \left[3\left(-\frac{1}{2}\right)^k - \frac{1}{3}\left(\frac{1}{2}\right)^k - \frac{8}{3}(-1)^k\right]u[k]
$$

the two real modes decaying ($|{-}\frac{1}{2}|, |\frac{1}{2}| < 1$) and the alternating mode $(-1)^k$ from the pole on the unit circle, which neither decays nor grows.

Sanity check against the initial value theorem: the numerator of $y[z]$ is one degree short of the denominator, so $y[0] = \lim_{z\to\infty} y[z] = 0$ and $y[1] = \lim_{z\to\infty} z\,y[z] = 1$. The formula agrees: $y[0] = 3 - \frac{1}{3} - \frac{8}{3} = 0$ and $y[1] = -\frac{3}{2} - \frac{1}{6} + \frac{8}{3} = 1$.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - when PFE hands you lemons}]
```

The example above had a factor $z$ in the numerator, so dividing by $z$ cost nothing. This one has none:

$$Y(z) = \frac{6z+6}{6z^2 - 7z + 2} = \frac{z+1}{\left(z-\frac{2}{3}\right)\left(z-\frac{1}{2}\right)}$$

**The Laplace habit.** Expand $Y(z)$ as it stands, as we would $F(s)$:

$$\frac{z+1}{\left(z-\frac{2}{3}\right)\left(z-\frac{1}{2}\right)} = \frac{A}{z-\frac{2}{3}} + \frac{B}{z-\frac{1}{2}}$$

Clear denominators and equate coefficients of powers of $z$:

$$z+1 = A\left(z-\frac{1}{2}\right) + B\left(z-\frac{2}{3}\right) = (A+B)z - \frac{1}{2}A - \frac{2}{3}B$$

Reading off the coefficient of $z$ and of the constant separately gives two equations in $A$ and $B$:

$$A + B = 1, \qquad -\frac{1}{2}A - \frac{2}{3}B = 1$$

From the first, $A = 1 - B$; substituting into the second gives $-\frac{1}{2}(1-B) - \frac{2}{3}B = 1$, i.e. $-\frac{1}{2} - \frac{1}{6}B = 1$, so $B = -9$ and then $A = 10$:

$$Y(z) = \frac{10}{z-\frac{2}{3}} - \frac{9}{z-\frac{1}{2}}$$

Algebraically this decomposition is correct, but it cannot be inverted with the table, the same trap as in the previous example: there is no $\frac{K}{z-a}$ pair.

**The fix: a delay supplies the missing $z$.** Write each term with an explicit factor $\frac{1}{z}$:

$$\frac{K}{z-a} = \frac{K}{z}\cdot\frac{z}{z-a}$$

The right-hand factor is a table pair, and the leftover $\frac{1}{z}$ is the delay operator $z^{-1}$ ($\mathcal{Z}\{f[k-1]\} = z^{-1}F$), which delays the whole mode by one sample:

$$Y(z) = \frac{10}{z}\cdot\frac{z}{z-\frac{2}{3}} - \frac{9}{z}\cdot\frac{z}{z-\frac{1}{2}}$$

Inverting, each clean pair $\frac{Kz}{z-a} \leftrightarrow K a^k$ arrives one sample late: the step becomes $u[k-1]$ and the exponent drops to $k-1$,

$$y[k] = \left[10\left(\frac{2}{3}\right)^{k-1} - 9\left(\frac{1}{2}\right)^{k-1}\right]u[k-1]$$

The $u[k-1]$ instead of $u[k]$ comes from the delay: **the response starts at $k=1$, not $k=0$**, so $y[0] = 0$. Sanity check: $Y(z) \to 0$ as $z \to \infty$, so $y[0] = 0$. A naive inversion that ignores the missing $z$, $\frac{10}{z-\frac{2}{3}} \to 10\left(\frac{2}{3}\right)^k$, would give $y[0] = 10 - 9 = 1$, wrong because the delay is missing.

**Cross-check with the divide-by-$z$ recipe.** Run the same recipe as in the example above on this $Y(z)$. Dividing by $z$ now adds a pole at $z=0$, since there is no $z$ in the numerator to cancel it, so the expansion gets a *third* term:

$$\frac{Y(z)}{z} = \frac{z+1}{z\left(z-\frac{2}{3}\right)\left(z-\frac{1}{2}\right)} = \frac{3}{z} + \frac{15}{z-\frac{2}{3}} - \frac{18}{z-\frac{1}{2}}$$

(cover-up, one coefficient at a time: the one in front of $\frac{1}{z}$ is $Y(0) = \frac{6}{2} = 3$; the others are $\left.\frac{z+1}{z\left(z-\frac{1}{2}\right)}\right|_{z=\frac{2}{3}} = 15$ and $\left.\frac{z+1}{z\left(z-\frac{2}{3}\right)}\right|_{z=\frac{1}{2}} = -18$.) Multiplying back by $z$ turns that $\frac{3}{z}$ into the constant $3$, a term a Laplace-trained eye would not expect:

$$Y(z) = 3 + \frac{15z}{z-\frac{2}{3}} - \frac{18z}{z-\frac{1}{2}}
\quad\Longrightarrow\quad
y[k] = 3\delta[k] + \left[15\left(\frac{2}{3}\right)^k - 18\left(\frac{1}{2}\right)^k\right]u[k]$$

The $3\delta[k]$ is needed: without it the two modes alone would give $y[0] = 15 - 18 = -3$, contradicting $Y(z) \to 0$.

```{=latex}
\end{example}
```

## Higher-order difference equations as first-order systems

Take a third-order equation (the $n$-th order case works the same way):

$$
y[k+3] + a_2 y[k+2] + a_1 y[k+1] + a_0 y[k] = b_0 u[k], \quad y[0] = y_0, \quad y[1] = y_1, \quad y[2] = y_2
$$

To get everything on the left in terms of $k+1$, we introduce new state variables that shift the output along:

$$x_1[k] = y[k]$$
$$x_2[k] = y[k+1]$$
$$x_3[k] = y[k+2]$$

The form we want has $k+1$ on the left, so we shift the index by one: each state steps into the next, and the last row comes straight from the starting difference equation, the same companion form as in the continuous case:

$$x_1[k+1] = x_2[k] = y[k+1]$$
$$x_2[k+1] = x_3[k] = y[k+2]$$
$$x_3[k+1] = -a_0 x_1[k] - a_1 x_2[k] - a_2 x_3[k] + b_0 u[k]$$

Or in matrix form (and extending to $n$-th order):

$$
\begin{bmatrix} x_1[k+1] \\ x_2[k+1] \\ \vdots \\ x_n[k+1] \end{bmatrix}
=
\begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -a_0 & -a_1 & -a_2 & \cdots & -a_{n-1} \end{bmatrix}
\begin{bmatrix} x_1[k] \\ x_2[k] \\ \vdots \\ x_n[k] \end{bmatrix}
+
\begin{bmatrix} 0 \\ 0 \\ \vdots \\ b_0 \end{bmatrix} u[k]
$$

The state-space form is the same as in continuous time; only the indexing changes, from the derivative $\dot{\vec{x}}$ to the shift $\vec{x}[k+1]$:

$$\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$$
$$\vec{y}[k] = \mathbf{C}\vec{x}[k] + \mathbf{D}\vec{u}[k]$$

But the *matrices* are not the same as in the continuous case. If you mix continuous and discrete systems, be careful to use the right ones. In the following section we add subscripts to distinguish the two: $A_D$ and $A_c$, $B_D$ and $B_c$, etc.


## Discretizing continuous systems

### Euler method

Start from the continuous state equation

$$\dot{\vec{x}} = \mathbf{A}_c\vec{x} + \mathbf{B}_c\vec{u}$$

and approximate the derivative with a finite difference (Euler's method):

$$\dot{\vec{x}} \approx \frac{\vec{x}[k+1] - \vec{x}[k]}{T}$$

which gives the Euler discretization:

$$\vec{x}[(k+1)T] \approx \underbrace{(\mathbf{I} + T\mathbf{A}_c)}_{\mathbf{A}_D}\vec{x}[kT] + \underbrace{T\mathbf{B}_c}_{\mathbf{B}_D}\vec{u}[kT]$$

This gives a simple set of conversions:

$$ \mathbf{A}_D = \mathbf{I} + T\mathbf{A}_c, \quad  \mathbf{B}_D = T\mathbf{B}_c, \quad \mathbf{C}_D = \mathbf{C}_c, \quad \mathbf{D}_D = \mathbf{D}_c$$

Euler's method is simple, but we need a small $T$ to get a good approximation.

### Integral approximation

We want the step from $t_1 = kT$ to $t_2 = (k+1)T$, but the system is time-invariant: the step over *any* sample period is the same as the step over the first one. So we derive it once for the first period, $t \in [0, T]$ (i.e. $k = 0$), and put the general $k$ back at the end.

Start from the exact solution of the continuous system:

$$\vec{x}(t) = e^{\mathbf{A}_c t}\vec{x}(0) + \int_0^t e^{\mathbf{A}_c (t-\tau)}\mathbf{B}_c\vec{u}(\tau)\, d\tau$$

At $t = T$, with a zero-order hold\footnote{Strictly, what the plant sees is not the sequence but the *held* staircase: the output of a D/A converter that holds $\vec{u}[k]$ for a whole period, $\vec{u}_h(t) = \vec{u}[k]$ for $kT \le t < (k+1)T$.} keeping $\vec{u}(\tau) = \vec{u}[0]$ constant over the whole period:

$$\vec{x}(T) = e^{\mathbf{A}_c T}\vec{x}(0) + \int_0^T e^{\mathbf{A}_c (T-\tau)}\, d\tau\, \mathbf{B}_c\, \vec{u}[0]$$

The substitution $\tau' = T - \tau$ ($d\tau = -d\tau'$, limits flip) turns the integral into the familiar form,

$$\int_0^T e^{\mathbf{A}_c (T-\tau)}\, d\tau = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau$$

so the first period reads

$$\vec{x}(T) = \underbrace{e^{\mathbf{A}_c T}}_{\mathbf{A}_D}\vec{x}(0) + \underbrace{\left(\int_0^T e^{\mathbf{A}_c \tau}\, d\tau\right)\mathbf{B}_c}_{\mathbf{B}_D}\, \vec{u}[0]$$

By time invariance every period looks the same; shift $0 \to kT$ and $T \to (k+1)T$:

$$\vec{x}((k+1)T) = \mathbf{A}_D \vec{x}(kT) + \mathbf{B}_D\, \vec{u}[k]$$

Where:

$$
\mathbf{A}_D = e^{\mathbf{A}_c T}, \qquad
\mathbf{B}_D = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau\, \mathbf{B}_c  = (\mathbf{A}_D - \mathbf{I})\mathbf{A}_c^{-1}\mathbf{B}_c \qquad
\mathbf{C}_D = \mathbf{C}_c, \quad \mathbf{D}_D = \mathbf{D}_c$$

We state without proof that the continuous poles map as $z_i = e^{s_i T}$.

```{=latex}
\begin{example}[frametitle={Example - discretizing for $T = 0.1$ s}]
```

Discretize $\dot{\vec{x}} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ 1 \end{bmatrix}u$ with $T = 0.1$ s.

We need the matrix exponential. Both discrete matrices are built from it, so the example is mostly about computing $e^{\mathbf{A}_c T}$.

**The general way.** The cleanest route is diagonalization: if $\mathbf{A}_c = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$ (eigenvectors in the columns of $\mathbf{V}$, eigenvalues on the diagonal of $\boldsymbol{\Lambda}$), then

$$e^{\mathbf{A}_c T} = \mathbf{V}\,e^{\boldsymbol{\Lambda} T}\,\mathbf{V}^{-1}, \qquad e^{\boldsymbol{\Lambda}T} = \operatorname{diag}\left(e^{\lambda_1 T}, \dots, e^{\lambda_n T}\right)$$

so exponentiating the matrix reduces to exponentiating its eigenvalues. (If the matrix cannot be diagonalized, Cayley–Hamilton does the same job without eigenvectors.) So the plan is: find the eigenvalues, then exponentiate.

**Step 1 — eigenvalues.** $\det(\lambda\mathbf{I} - \mathbf{A}_c) = (\lambda + 2)(\lambda + 1)$, so the eigenvalues are real: $\lambda_1 = -2$ and $\lambda_2 = -1$.

**Step 2 — the discrete $\mathbf{A}_D$.** The eigenvalues are distinct, so $\mathbf{A}_c$ is diagonalizable and we run the recipe above. Eigenvectors: for $\lambda_1 = -2$ take $\vec{v}_1 = \tvec{1, -1}$, for $\lambda_2 = -1$ take $\vec{v}_2 = \tvec{0, 1}$. Hence

$$\mathbf{V} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}, \qquad \mathbf{V}^{-1} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \qquad \boldsymbol{\Lambda} = \begin{bmatrix} -2 & 0 \\ 0 & -1 \end{bmatrix}$$

With $e^{-0.2} = 0.8187$ and $e^{-0.1} = 0.9048$,

$$\mathbf{A}_D = e^{\mathbf{A}_c T} = \mathbf{V}e^{\boldsymbol{\Lambda}T}\mathbf{V}^{-1} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} e^{-0.2} & 0 \\ 0 & e^{-0.1} \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} e^{-0.2} & 0 \\ e^{-0.1}-e^{-0.2} & e^{-0.1} \end{bmatrix} \approx \begin{bmatrix} 0.819 & 0 \\ 0.086 & 0.905 \end{bmatrix}$$

**Step 3 — the discrete $\mathbf{B}_D$.** Use the formula from above, which requires $\mathbf{A}_c$ to be invertible; it is ($\det\mathbf{A}_c = 2$).

$$\mathbf{A}_c^{-1} = \begin{bmatrix} -\frac{1}{2} & 0 \\ -\frac{1}{2} & -1 \end{bmatrix}$$

$$\mathbf{B}_D = (\mathbf{A}_D - \mathbf{I})\mathbf{A}_c^{-1}\mathbf{B}_c \approx \begin{bmatrix} 0 \\ 0.095 \end{bmatrix}$$

Sanity check: for a short $T$ both matrices must be close to their first-order (Euler) versions, $\mathbf{A}_D \approx \mathbf{I} + \mathbf{A}_c T = \begin{bmatrix} 0.8 & 0 \\ 0.1 & 0.9 \end{bmatrix}$ and $\mathbf{B}_D \approx \mathbf{B}_c T = \tvec{0, 0.1}$, and they are. The exact $\mathbf{B}_D = \tvec{0, 1 - e^{-0.1}}$ keeps the $0$ in the first entry: $u$ never reaches $x_1$ in continuous time, so sampling cannot make it.

```{=latex}
\end{example}
```

Finally, at the start of this chapter we dropped the sampling period $T$ from the notation. It is still there: the discrete system is a sampled version of the continuous one, and $\mathbf{A}_D = e^{\mathbf{A}_c T}$ holds only for that particular $T$. If you change $T$, you have to recompute $\mathbf{A}_D$ and $\mathbf{B}_D$.

## Solving the discrete state equations

### Homogeneous state equations

With an initial state $\vec{x}[0]$ and no input, $\vec{u}[k] = 0$, the state equation gives

$$\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$$
$$\vec{x}[1] = \mathbf{A}\vec{x}[0]$$
$$\vec{x}[2] = \mathbf{A}\vec{x}[1] = \mathbf{A}^2\vec{x}[0]$$
$$\vec{x}[3] = \mathbf{A}\vec{x}[2] = \mathbf{A}^3\vec{x}[0]$$
$$\vdots$$
$$\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$$
and since $\vec{u}[k] = 0$:
$$\vec{y}[k] = \mathbf{C}\mathbf{A}^k\vec{x}[0]$$

$\mathbf{A}^k$ is the **discrete state-transition matrix**, mapping the initial state to the state at step $k$.

One place where the discrete case is *not* a copy of the continuous one: **$\mathbf{A}^k$ need not be invertible.**

```{=latex}
\begin{example}[frametitle={Note - how to solve the response to an initial state}]
```

All the work is in computing $\mathbf{A}^k$; the three methods are below (diagonalization is usually quickest). Once you have it, the response to a given initial state $\vec{x}[0]$ is a single matrix-vector product:

$$
\vec{x}[k] = \mathbf{A}^k\vec{x}[0]
$$

With the diagonalization form $\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}$ this reads as a combination of the modes $\lambda_i^k$:

$$
\vec{x}[k] = c_1\lambda_1^k\vec{v}_1 + \cdots + c_n\lambda_n^k\vec{v}_n, \qquad
\vec{c} = \mathbf{V}^{-1}\vec{x}[0]
$$

The coefficients $c_i$ are the coordinates of $\vec{x}[0]$ in the eigenbasis, so the initial state only decides *how much* of each mode appears; the modes themselves are properties of $\mathbf{A}$ alone.

```{=latex}
\end{example}
```

### Nonhomogeneous state equations

As in the homogeneous case, but now with the input $\vec{u}[k]$:

$$\vec{x}[1] = \mathbf{A}\vec{x}[0] + \mathbf{B}\vec{u}[0]$$
$$\vec{x}[2] = \mathbf{A}\vec{x}[1] + \mathbf{B}\vec{u}[1] = \mathbf{A}^2\vec{x}[0] + \mathbf{A}\mathbf{B}\vec{u}[0] + \mathbf{B}\vec{u}[1]$$
$$\vec{x}[3] = \mathbf{A}\vec{x}[2] + \mathbf{B}\vec{u}[2] = \mathbf{A}^3\vec{x}[0] + \mathbf{A}^2\mathbf{B}\vec{u}[0] + \mathbf{A}\mathbf{B}\vec{u}[1] + \mathbf{B}\vec{u}[2]$$
$$\vdots$$

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\vec{x}[k] = \mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1} \mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i]
$}
\endgroup
\]
```

$$\vec{y}[k] = \mathbf{C}\mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1} \mathbf{C}\mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i] + \mathbf{D}\vec{u}[k]$$

## Obtaining the discrete state-transition matrix $\mathbf{A}^k$

All three methods are the continuous-time ones from the State-space chapter with the notation swapped: $\lambda_i^k$ in place of $e^{\lambda_i t}$, and the $z$-transform in place of the Laplace transform. The same caveats apply.

### $\mathbf{A}^k$ via the Z-transform

Invert the resolvent, almost as the Laplace transform did in the continuous case:\footnote{Watch for the additional $z$.}

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\mathbf{A}^k = \mathcal{Z}^{-1}\left\{z\left(z\mathbf{I} - \mathbf{A}\right)^{-1}\right\}
$}
\endgroup
\]
```

How did we get here? Start from the homogeneous state equations, take the Z-transform, and solve for $\vec{X}(z)$. The advance rule $\mathcal{Z}\{\vec{x}[k+1]\} = z\vec{X}(z) - z\vec{x}[0]$ handles the left-hand side:

$$\vec{X}(z) = \mathcal{Z}\{\vec{x}[k]\} = \sum_{k=0}^{\infty} \vec{x}[k]\, z^{-k}$$
$$z\vec{X}(z) - z\vec{x}[0] = \mathbf{A}\vec{X}(z)$$
$$(z\mathbf{I} - \mathbf{A})\vec{X}(z) = z\vec{x}[0]$$
$$\vec{X}(z) = (z\mathbf{I} - \mathbf{A})^{-1} z\,\vec{x}[0]$$

Inverting and comparing with the homogeneous solution $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$ gives

$$\vec{x}[k] = \mathcal{Z}^{-1}\left\{(z\mathbf{I} - \mathbf{A})^{-1} z\right\}\vec{x}[0] = \mathbf{A}^k\vec{x}[0]
\quad\Longrightarrow\quad
\mathbf{A}^k = \mathcal{Z}^{-1}\left\{z\left(z\mathbf{I} - \mathbf{A}\right)^{-1}\right\}$$

With an input, transform $\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$:

$$z\vec{X}(z) - z\vec{x}[0] = \mathbf{A}\vec{X}(z) + \mathbf{B}U(z)$$

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\vec{X}(z) = z(z\mathbf{I}-\mathbf{A})^{-1}\vec{x}[0] + (z\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}\,U(z)
$}
\endgroup
\]
```

The first term is the homogeneous (zero-input) response from above; the second is the forced response.

```{=latex}
\begin{example}[frametitle={Example - $\mathbf{A}^k$ via the Z-transform}]
```

Take $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -0.1 & 0.7 \end{bmatrix}$. Since $\det(z\mathbf{I}-\mathbf{A}) = z^2 - 0.7z + 0.1 = (z-0.5)(z-0.2)$, the resolvent is

$$(z\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(z-0.5)(z-0.2)}\begin{bmatrix} z-0.7 & 1 \\ -0.1 & z \end{bmatrix}$$

Expanding it into pole/projection form,

$$(z\mathbf{I} - \mathbf{A})^{-1} = \frac{\mathbf{P}_1}{z-0.5} + \frac{\mathbf{P}_2}{z-0.2}, \qquad
\mathbf{P}_1 = \frac{10}{3}\begin{bmatrix} -0.2 & 1 \\ -0.1 & 0.5 \end{bmatrix}, \qquad
\mathbf{P}_2 = -\frac{10}{3}\begin{bmatrix} -0.5 & 1 \\ -0.1 & 0.2 \end{bmatrix}$$

(check: $\mathbf{P}_1 + \mathbf{P}_2 = \mathbf{I}$). The extra $z$ in the inversion formula turns each term into the pair $\frac{z}{z-p} \leftrightarrow p^k$:

$$\mathbf{A}^k = \mathcal{Z}^{-1}\left\{\frac{z\mathbf{P}_1}{z-0.5} + \frac{z\mathbf{P}_2}{z-0.2}\right\} = 0.5^k\mathbf{P}_1 + 0.2^k\mathbf{P}_2 = \begin{bmatrix} -\frac{2}{3}0.5^k + \frac{5}{3}0.2^k & \frac{10}{3}(0.5^k - 0.2^k) \\[2pt] -\frac{1}{3}(0.5^k - 0.2^k) & \frac{5}{3}0.5^k - \frac{2}{3}0.2^k \end{bmatrix}$$

and at $k = 0$ this reduces to $\mathbf{A}^0 = \mathbf{P}_1 + \mathbf{P}_2 = \mathbf{I}$, as it must.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - the $z$-domain route, double pole}]
```

The previous example had distinct poles; this one has a repeated pole. Take $\mathbf{A} = \begin{bmatrix} 1 & 0 \\ -\frac{1}{100} & 1 \end{bmatrix}$ and $\mathbf{B} = \tvec{100, 40}$, with zero initial conditions and a unit step input $u[k] = 1$. All we need is the forced term of the $z$-domain solution just derived:

$$\vec{X}(z) = (z\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\,U(z)$$

**Step 1 — the resolvent.** $\det(z\mathbf{I} - \mathbf{A}) = (z-1)^2$, so

$$(z\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(z-1)^2}\begin{bmatrix} z-1 & 0 \\[2pt] -\frac{1}{100} & z-1 \end{bmatrix}$$

Keep the determinant factor outside; each row of the resolvent then feeds one entry of $\vec{X}(z)$.

**Step 2 — $X_1$.** Row 1 of the resolvent times $\mathbf{B}$, times $U(z) = \frac{z}{z-1}$ (unit step):

$$X_1(z) = \underbrace{\frac{1}{(z-1)^2}}_{\det\text{ factor}}\left[\underbrace{(z-1)\cdot 100}_{\text{row 1 }\cdot\, \mathbf{B}}\right]\underbrace{\frac{z}{z-1}}_{U(z)} = \frac{100z}{(z-1)^2}$$

The pair $\frac{z}{(z-1)^2} \leftrightarrow k$ reads off immediately: $x_1[k] = 100k$.

**Step 3 — $X_2$ via partial fractions.** Row 2 of the resolvent times $\mathbf{B}$, times $U(z)$:

$$X_2(z) = \frac{1}{(z-1)^2}\left[-\frac{1}{100}\cdot 100 + (z-1)\cdot 40\right]\frac{z}{z-1} = \frac{z(40z-41)}{(z-1)^3}$$

Same trick as in the Z-transform section: expand $\frac{X_2}{z}$, which has a triple pole at $z=1$:

$$\frac{X_2(z)}{z} = \frac{40z-41}{(z-1)^3} = \frac{A}{z-1} + \frac{B}{(z-1)^2} + \frac{C}{(z-1)^3}$$

Clear denominators: $40z - 41 = A(z-1)^2 + B(z-1) + C$. At $z = 1$ we get $C = -1$; matching powers of $z$ gives $A = 0$ and $B = 40$. So

$$\frac{X_2(z)}{z} = \frac{40}{(z-1)^2} - \frac{1}{(z-1)^3}$$

multiply back by $z$ and read off the pairs $\frac{z}{(z-1)^2} \leftrightarrow k$ and $\frac{z}{(z-1)^3} \leftrightarrow \frac{k(k-1)}{2}$:

$$X_2(z) = \frac{40z}{(z-1)^2} - \frac{z}{(z-1)^3}
\quad\Longrightarrow\quad
x_2[k] = 40k - \frac{k(k-1)}{2} = \frac{k(81-k)}{2}$$

so

$$\vec{x}[k] = \begin{bmatrix} 100k \\[2pt] \frac{k(81-k)}{2} \end{bmatrix}$$

At which step does a state return to zero? $x_2[k] = \frac{k(81-k)}{2}$ vanishes at $k = 0$ and again at $k = 81$, so the second state returns to zero after 81 steps. The first state, $x_1[k] = 100k$, is zero only at $k = 0$.

Sanity check: $\vec{x}[1] = \tvec{100, 40} = \mathbf{B}$, as it must from $\vec{x}[1] = \mathbf{B}u[0]$. The same resolvent also gives $\mathbf{A}^k$, as in the section header: $\mathbf{A}^k = \mathcal{Z}^{-1}\{z(z\mathbf{I}-\mathbf{A})^{-1}\} = \begin{bmatrix} 1 & 0 \\[2pt] -\frac{k}{100} & 1 \end{bmatrix}$.

```{=latex}
\end{example}
```

### $\mathbf{A}^k$ via diagonalization

Powers of a diagonal matrix are entrywise powers, so with $\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$,

```{=latex}
\[
\begingroup
\setlength{\fboxsep}{1.2em}
\fbox{$\displaystyle
\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}, \qquad
\boldsymbol{\Lambda}^k = \operatorname{diag}\left(\lambda_1^k, \dots, \lambda_n^k\right)
$}
\endgroup
\]
```

This requires $\mathbf{A}$ to be diagonalizable. Otherwise the Jordan form takes over, $\mathbf{A}^k = \mathbf{T}\mathbf{J}^k\mathbf{T}^{-1}$, and the same blocks govern $\mathbf{A}^k$ as $e^{\mathbf{A}t}$. Splitting a block as $\mathbf{J}_q(\lambda) = \lambda\mathbf{I} + \mathbf{N}_q$ and using $\binom{k}{i} = 0$ for $i > k$, the binomial expansion gives $\mathbf{J}_q(\lambda)^k = \sum_{i=0}^{q-1}\binom{k}{i}\lambda^{k-i}\mathbf{N}_q^i$, so a $q\times q$ block contributes the modes $\lambda^k, k\lambda^{k-1}, \dots$ in place of $e^{\lambda t}, t e^{\lambda t}, \dots$.


```{=latex}
\begin{example}[frametitle={Example - $\mathbf{A}^k$ via diagonalization}]
```

Again take $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -0.1 & 0.7 \end{bmatrix}$.

**Step 1 — eigenvalues:** $\det(\mathbf{A}-\lambda\mathbf{I}) = \lambda^2 - 0.7\lambda + 0.1 = (\lambda-0.5)(\lambda-0.2)$, so $\lambda_1 = 0.2$ and $\lambda_2 = 0.5$.

**Step 2 — eigenvectors $\mathbf{V}$ and $\mathbf{V}^{-1}$:** for $\lambda_1 = 0.2$ take $\vec{v}_1 = \tvec{1, 0.2}$, for $\lambda_2 = 0.5$ take $\vec{v}_2 = \tvec{1, 0.5}$, so

$$\mathbf{V} = \begin{bmatrix} 1 & 1 \\ 0.2 & 0.5 \end{bmatrix}, \qquad
\mathbf{V}^{-1} = \begin{bmatrix} \frac{5}{3} & -\frac{10}{3} \\ -\frac{2}{3} & \frac{10}{3} \end{bmatrix}$$

**Step 3 — $\mathbf{A}^k$:** with $\boldsymbol{\Lambda}^k = \operatorname{diag}(0.2^k, 0.5^k)$,

$$\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1} = \begin{bmatrix} 1 & 1 \\ 0.2 & 0.5 \end{bmatrix} \begin{bmatrix} 0.2^k & 0 \\ 0 & 0.5^k \end{bmatrix} \begin{bmatrix} \frac{5}{3} & -\frac{10}{3} \\ -\frac{2}{3} & \frac{10}{3} \end{bmatrix} = \begin{bmatrix} \frac{5}{3}0.2^k - \frac{2}{3}0.5^k & \frac{10}{3}(0.5^k - 0.2^k) \\[2pt] -\frac{1}{3}(0.5^k - 0.2^k) & \frac{5}{3}0.5^k - \frac{2}{3}0.2^k \end{bmatrix}$$

This is the same $\mathbf{A}^k$ as the resolvent method gave.

```{=latex}
\end{example}
```

### $\mathbf{A}^k$ via Cayley–Hamilton

Cayley–Hamilton reduces every power $\mathbf{A}^k$ ($k \ge n$) to a polynomial of degree at most $n-1$:

$$
\mathbf{A}^k = \alpha_0(k)\mathbf{I} + \alpha_1(k)\mathbf{A} + \cdots + \alpha_{n-1}(k)\mathbf{A}^{n-1}
$$

The coefficients follow from the scalar identities $\lambda_i^k = \alpha_0 + \alpha_1\lambda_i + \cdots + \alpha_{n-1}\lambda_i^{n-1}$ (differentiate for repeated eigenvalues), and the method works even for defective matrices.

```{=latex}
\begin{example}[frametitle={Example - obtaining $\mathbf{A}^k$ via Cayley–Hamilton}]
```

Same $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -0.1 & 0.7 \end{bmatrix}$. Characteristic equation:

$$\det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^2 - 0.7\lambda + 0.1 = 0$$

so $\mathbf{A}^2 - 0.7\mathbf{A} + 0.1\mathbf{I} = \mathbf{0}$, and with $n = 2$:

$$\mathbf{A}^k = \alpha_0(k)\mathbf{I} + \alpha_1(k)\mathbf{A}, \qquad
\lambda^k = \alpha_0(k) + \alpha_1(k)\lambda$$

We already have the eigenvalues from the two examples above, $\lambda_1 = 0.2$ and $\lambda_2 = 0.5$. Evaluating there gives a $2\times2$ linear system in $\alpha_0, \alpha_1$, with $k$ only on the right-hand side:

$$\lambda_1 = 0.2: \quad 0.2^k = \alpha_0 + 0.2\alpha_1$$
$$\lambda_2 = 0.5: \quad 0.5^k = \alpha_0 + 0.5\alpha_1$$

Subtract the two equations to eliminate $\alpha_0$:

$$0.5^k - 0.2^k = 0.3\alpha_1 \quad\Longrightarrow\quad \alpha_1 = \frac{10}{3}(0.5^k - 0.2^k)$$

Back-substitute: $\alpha_0 = 0.2^k - 0.2\alpha_1 = \frac{5}{3}0.2^k - \frac{2}{3}0.5^k$. Put the coefficients back into $\mathbf{A}^k = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}$ and multiply out:

$$\mathbf{A}^k = \left(\frac{5}{3}0.2^k - \frac{2}{3}0.5^k\right)\mathbf{I} + \frac{10}{3}(0.5^k - 0.2^k)\mathbf{A}
= \begin{bmatrix} \frac{5}{3}0.2^k - \frac{2}{3}0.5^k & \frac{10}{3}(0.5^k - 0.2^k) \\[2pt] -\frac{1}{3}(0.5^k - 0.2^k) & \frac{5}{3}0.5^k - \frac{2}{3}0.2^k \end{bmatrix}$$

which matches both previous methods.

```{=latex}
\end{example}
```

### Final remarks

As in the continuous case, Cayley–Hamilton is the best default unless the problem calls for another method.

## Transfer function

From the discrete state equations with zero initial conditions,

$$
\mathbf{H}(z) = \mathbf{C}(z\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$$

the same rational-function picture as in the Transfer functions chapter, with the unit circle as the stability boundary. Block algebra (series, parallel, feedback) is identical.

## Equilibrium, stability, controllability, observability

Everything mirrors the continuous case:

- **Equilibrium** — with $u[k] = 0$, a linear discrete system has the single equilibrium at the origin $\vec{x}_e = \vec{0}$; the equilibrium types are the same as for continuous systems.
- **Stability** — the modes are $\lambda_i^k$, so the boundary is the **unit circle** in place of the imaginary axis.\footnote{For the exact (zero-order hold) discretization this verdict does not depend on the sampling period: the poles map as $z_i = e^{s_i T}$, so $|z_i| = e^{\operatorname{Re}(s_i)T} < 1$ iff $\operatorname{Re}(s_i) < 0$, for any $T > 0$; $T$ moves the poles but cannot flip them across the unit circle. Under Euler ($z_i = 1 + T s_i$) it is the opposite: a too-large $T$ can push even a stable pole outside the unit circle, which is why Euler needs a small $T$.} The three cases are the same, with $|\lambda_i|$ in place of $\operatorname{Re}\lambda_i$:

  ```{=latex}
  \[
  \begingroup
  \setlength{\fboxsep}{1.2em}
  \fbox{$\displaystyle
  \begin{array}{lcl}
  |\lambda_i| < 1 \ \ \forall i & \iff & \text{asymptotically stable}
  \end{array}
  $}
  \endgroup
  \]
  ```
- **Controllability** — the same controllability matrix $\mathcal{C} = [\mathbf{B}\ \mathbf{A}\mathbf{B}\ \cdots\ \mathbf{A}^{n-1}\mathbf{B}]$ and rank test as for continuous systems.
- **Observability** — the same observability matrix $\mathcal{O}$ and rank test as for continuous systems.
