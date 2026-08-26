# Appendix B: Selected solved problems

## Modelling

## Problem 1 (2023-11-24 / 1)

We have electric circuit on the schematic below.

```{=latex}
\input{tikz/kolokvij-2023-circuit.tex}
```

a. Find state-space equations of the circuit in the form $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, where $\vec{x} = [i_L, v_C]^T$ and $\vec{u} = [i_g, v_g]^T$.
b. Find the matrix equation for response $\vec{y} = [ v_{R2}, v]^T$.

### Part a. (ground at the bottom rail)

**Step 1 — ground and nodes.** Take the bottom rail as ground and mark the nodes: $V_1$ (top-left, where $i_g$ enters), $V_2$ (top-right, touching $R_1$, $L$, $C$ and $v_g$), $V_3$ (between $L$ and $R_2$), $V_4$ (between $v_g$ and $R_3$). The capacitor sits between $V_2$ and ground, so its state is directly $v_C = V_2$.

**Step 2 — node equations** (currents leaving a node positive, per the modeling recipe):

$$\text{Node } V_1: \quad \frac{V_1 - V_2}{R_1} = i_g$$

$$\text{Node } V_2: \quad \frac{V_2 - V_1}{R_1} + i_L + i_C + i_{v_g} = 0$$

$$\text{Node } V_3: \quad -i_L + \frac{V_3}{R_2} = 0 \;\Longrightarrow\; V_3 = R_2\,i_L$$

$$\text{Node } V_4: \quad \frac{V_4}{R_3} - i_{v_g} = 0 \;\Longrightarrow\; i_{v_g} = \frac{V_4}{R_3}$$

**Step 3 — the C leg.** From node $V_1$, $\frac{V_2 - V_1}{R_1} = -i_g$; substituting into node $V_2$:

$$-i_g + i_L + i_C + i_{v_g} = 0 \;\Longrightarrow\; i_C = i_g - i_L - i_{v_g}$$

With $V_2 - V_4 = v_g$ (and node $V_4$ giving $i_{v_g} = V_4/R_3$), plus $v_C = V_2$:

$$i_{v_g} = \frac{V_2 - v_g}{R_3} = \frac{v_C - v_g}{R_3}$$

so with $i_C = C\dot{v}_C$:

$$\dot{v}_C = -\frac{1}{C}i_L - \frac{1}{CR_3}v_C + \frac{1}{C}i_g + \frac{1}{CR_3}v_g$$

**Step 4 — the L leg.** Faraday's law on the inductor, $V_2 - V_3 = L\dot{i}_L$; node $V_3$ gives $V_3 = R_2 i_L$ and $V_2 = v_C$:

$$L\dot{i}_L = v_C - R_2 i_L \;\Longrightarrow\; \dot{i}_L = -\frac{R_2}{L}i_L + \frac{1}{L}v_C$$

No direct input coupling — $i_g$ and $v_g$ reach the inductor only through $v_C$.

**Step 5 — collect both rows** into the state-space form:

$$\begin{bmatrix} \dot{i}_L \\ \dot{v}_C \end{bmatrix} = \begin{bmatrix} -\frac{R_2}{L} & \frac{1}{L} \\ -\frac{1}{C} & -\frac{1}{CR_3} \end{bmatrix}\begin{bmatrix} i_L \\ v_C \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ \frac{1}{C} & \frac{1}{CR_3} \end{bmatrix}\begin{bmatrix} i_g \\ v_g \end{bmatrix}$$

## Problem 2 (2023-11-24 / 2)

Partially elastic crash of an object to the wall is modeled with a spring and a damper as shown in the figure. Crash starts at $x=0$.

```{=latex}
\input{tikz/kolokvij-2023-crash.tex}
```

a. Model the crash with state equations in the form $\dot{\vec{x}} = \mathbf{A}\vec{x}$, where $\vec{x} = [x, v]^T$
b. Write the response equation in the form of $y = \mathbf{C}\vec{x}$, where $y$ is the entire external force acting on the object $y(t) = F(t)$.
c. With Laplace transformation find the solution of the system $\vec{x}(t)$ for parameters m=5kg, k=20N/m, b=25Ns/m and initial speed of v(0) = -10m/s
d. What's the maximum force $F_{\max}$ acting on the object during the crash?

### Part a.

With $x$ positive away from the wall, the buffer pushes back with $F = -kx - bv$, so $m\ddot{x} + b\dot{x} + kx = 0$. With states $x_1 = x$, $x_2 = v = \dot{x}$:

$$\dot{x}_1 = x_2, \qquad \dot{x}_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2$$

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x}, \qquad \vec{x}(0) = \begin{bmatrix} 0 \\ -10 \end{bmatrix}
$$

### Part b.

The external (buffer) force on the object is spring plus damper:

$$y = F(t) = -kx - bv = \begin{bmatrix} -k & -b \end{bmatrix}\vec{x}$$

$$\mathbf{C} = \begin{bmatrix} -k & -b \end{bmatrix}$$

### Part c.

Plug the numbers into the $\mathbf{A}$ from part a ($m=5$, $k=20$, $b=25$: $k/m = 4$, $b/m = 5$):

$$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -4 & -5 \end{bmatrix}, \qquad \vec{x}(0) = \begin{bmatrix} 0 \\ -10 \end{bmatrix}$$

Use the state-space Laplace solution $\vec{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\vec{x}(0)$ (derived in the State-space chapter, § "$\Phi$ via the Laplace transform"):

$$s\mathbf{I} - \mathbf{A} = \begin{bmatrix} s & -1 \\ 4 & s + 5 \end{bmatrix}, \qquad \det(s\mathbf{I} - \mathbf{A}) = s^2 + 5s + 4 = (s+1)(s+4)$$

$$(s\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{(s+1)(s+4)}\begin{bmatrix} s+5 & 1 \\ -4 & s \end{bmatrix}$$

$$\vec{X}(s) = \frac{1}{(s+1)(s+4)}\begin{bmatrix} s+5 & 1 \\ -4 & s \end{bmatrix}\begin{bmatrix} 0 \\ -10 \end{bmatrix} = \begin{bmatrix} \frac{-10}{(s+1)(s+4)} \\ \frac{-10s}{(s+1)(s+4)} \end{bmatrix}$$

Partial fractions on the two entries:

$$X_1(s) = \frac{-10}{(s+1)(s+4)} = \frac{A}{s+1} + \frac{B}{s+4}, \qquad
A = \left.\frac{-10}{s+4}\right|_{s=-1} = -\frac{10}{3}, \quad B = \left.\frac{-10}{s+1}\right|_{s=-4} = \frac{10}{3}$$

$$X_2(s) = \frac{-10s}{(s+1)(s+4)} = \frac{C}{s+1} + \frac{D}{s+4}, \qquad
C = \left.\frac{-10s}{s+4}\right|_{s=-1} = \frac{10}{3}, \quad D = \left.\frac{-10s}{s+1}\right|_{s=-4} = -\frac{40}{3}$$

Inverse Laplace transform, valid for $t \ge 0$:

$$x_1(t) = \frac{10}{3}\left(e^{-4t} - e^{-t}\right), \qquad x_2(t) = \frac{10}{3}\left(e^{-t} - 4e^{-4t}\right)$$

$$
\vec{x}(t) = \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} = \begin{bmatrix} \frac{10}{3}\left(e^{-4t} - e^{-t}\right) \\ \frac{10}{3}\left(e^{-t} - 4e^{-4t}\right) \end{bmatrix}, \qquad t \ge 0
$$

### Part d.

From solution in part b, the force is $F(t) = -kx - bv = -20x - 25v$. At impact $t=0$ the spring is uncompressed $x=0$ and the speed is maximal $v(0) = -10$, so the force is maximal:

$$F(0) = -b\,v(0) = 25 \cdot 10 = 250\ \text{N}$$

**Alternative — the full $F(t)$ route** Plug the solutions from part c into $F(t) = -kx_1 - bx_2 = -20x_1 - 25x_2$:

$$F(t) = -20\cdot\frac{10}{3}\left(e^{-4t} - e^{-t}\right) - 25\cdot\frac{10}{3}\left(e^{-t} - 4e^{-4t}\right) = \frac{800}{3}e^{-4t} - \frac{50}{3}e^{-t}$$

Differentiate and set to zero:

$$F'(t) = -\frac{3200}{3}e^{-4t} + \frac{50}{3}e^{-t} = 0 \quad\Longrightarrow\quad 64e^{-4t} = e^{-t} \quad\Longrightarrow\quad e^{3t} = 64 \quad\Longrightarrow\quad t = \ln 4$$

Evaluate the stationary point against the impact instant:

$$F(0) = 250\ \text{N}, \qquad F(\ln 4) = \frac{800}{3}\cdot\frac{1}{256} - \frac{50}{3}\cdot\frac{1}{4} = -\frac{25}{8}\ \text{N}$$

The impact instant is the maximum (the stationary point is a minimum during the rebound), so $F_{\max} = 250$ N at $t=0$ — same conclusion, more work.

## Problem 1 (2024-11-22 / 1)

For the circuit above we want to write down the state-space equations in the form $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, where the state vector $\vec{x} = [i_L, v_C]^T$ and $\vec{u} = [v_{g1}, i_{g2}]^T$.

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages, american currents]
  \draw (0,6) to[V=$v_{g1}$] (0,0)
        (0,6) to[L=$L$] (4,6)
        to[R=$R_2$] (8,6)
        (8,6) to[I, l_=$i_{g2}$] (8,0)
        (8,0) -- (0,0);
  \draw (4,6) to[R=$R_1$] (4,3);
  \draw (4,3) to[C=$C$] (4,0);
  \node at (3.3,1.5) {$v_C$};
  \node at (3.6,3.2) {$+$};
\end{circuitikz}
\end{center}
```

**Step 1** Decide on nodes. Take the bottom node (rail) as ground and mark the remaining nodes $V_1$, $V_2$, $V_3$, $V_4$.

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages, american currents]
  \draw (0,6) node[circ,label=above:$V_1$]{} to[V=$v_{g1}$, i>^=$i_{g1}$] (0,0) node[ground]{};
  \draw (0,6) to[L=$L$, i>^=$i_L$] (4,6) node[circ,label=above:$V_2$]{}
              to[R=$R_2$] (8,6) node[circ,label=above:$V_4$]{}
              (8,6) to[I, l_=$i_{g2}$] (8,0);
  \draw (8,0) -- (0,0);
  \draw (4,6) to[R=$R_1$] (4,3) node[circ,label=right:$V_3$]{};
  \draw (4,3) to[C=$C$, i>^=$i_C$] (4,0);
  \node at (3.3,1.5) {$v_C$};
  \node at (3.6,3.2) {$+$};
\end{circuitikz}
\end{center}
```

**Step 2** Node and element equations. From the annotated circuit above we write the equations.

Node $V_1$: $\; i_{g1} + i_L = 0$

Node $V_2$: $\; -i_L + \dfrac{V_2 - V_3}{R_1} + \dfrac{V_2 - V_4}{R_2} = 0$

Node $V_3$: $\; \dfrac{V_3 - V_2}{R_1} + i_C = 0$

Node $V_4$: $\; \dfrac{V_4 - V_2}{R_2} + i_{g2} = 0$

Capacitor: $\; i_C = C\dot{v}_C, \quad v_C = V_3$

Inductor: $\; v_L = L\dot{i}_L, \quad v_L = V_1 - V_2$

And we note that $V_1 = v_{g1}$.

Instead of trying to rearrange the node equations from the start, start with the equations that already contain the derivatives — the constitutive relations of the two energy-storing elements, $i_C = C\dot{v}_C$ and $v_L = L\dot{i}_L$. They give the state derivatives directly; the node equations are only used to fill in whatever current or voltage they still need.

**Step 3 — Capacitor** What we need is: **$\dot{v}_C$** expressed as a function of the states and the inputs.

Substitute into $\dot{v}_C = i_C/C$ to get the state derivative.

From $i_C = C\dot{v}_C$ we need the capacitor current $i_C$.

Where to get it: $i_C$ appears only in the node-$V_3$ equation (the capacitor sits between $V_3$ and ground). Solve it for $i_C$:

$$i_C = \frac{V_2 - V_3}{R_1}$$

That still leaves $V_2$. The node-$V_2$ equation ties everything together, once we express the current through $R_2$ via the node-$V_4$ equation:

$$\frac{V_4 - V_2}{R_2} + i_{g2} = 0
\quad\Longrightarrow\quad
\frac{V_2 - V_4}{R_2} = i_{g2}$$

Insert both into the node-$V_2$ equation:

$$-i_L + \frac{V_2 - V_3}{R_1} + \frac{V_2 - V_4}{R_2} = 0
\quad\Longrightarrow\quad
-i_L + i_C + i_{g2} = 0$$

so $i_C = i_L - i_{g2}$ — only states and inputs. Insert the capacitor equation $i_C = C\dot{v}_C$:

$$C\,\dot{v}_C = i_L - i_{g2}
\quad\Longrightarrow\quad
\dot{v}_C = \frac{1}{C}\,i_L - \frac{1}{C}\,i_{g2}$$

**Step 4 — Inductor** What we need is: **$\dot{i}_L$**.

Substitute into $\dot{i}_L = v_L/L$ to get the state derivative.

From $v_L = L\dot{i}_L$ we need $v_L = V_1 - V_2$, and $V_1 = v_{g1}$ is already known — so we need $V_2$.

Where to get $V_2$? The node-$V_2$ equation is the best bet — with $\frac{V_2 - V_4}{R_2} = i_{g2}$ (from the node-$V_4$ equation), it contains $V_2$ together with only known quantities: $V_3 = v_C$ (a state), $i_L$ (a state) and $i_{g2}$ (an input). Solve it for $V_2$:

$$-i_L + \frac{V_2 - V_3}{R_1} + \frac{V_2 - V_4}{R_2} = 0
\quad\Longrightarrow\quad
\frac{V_2 - V_3}{R_1} = i_L - i_{g2}$$

$$V_2 = V_3 + R_1(i_L - i_{g2}) = v_C + R_1 i_L - R_1 i_{g2}$$

Then with $v_L = L\dot{i}_L = V_1 - V_2$:

$$L\,\dot{i}_L = v_{g1} - v_C - R_1 i_L + R_1 i_{g2}
\quad\Longrightarrow\quad
\dot{i}_L = -\frac{R_1}{L}\,i_L - \frac{1}{L}\,v_C + \frac{1}{L}\,v_{g1} + \frac{R_1}{L}\,i_{g2}$$

**Step 5** Collect the equations into matrix form.

The two scalar equations from Steps 3 and 4 are exactly the two rows of $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$:

$$
\frac{d}{dt}\begin{bmatrix} i_L \\ v_C \end{bmatrix} =
\begin{bmatrix}
-\frac{R_1}{L} & -\frac{1}{L} \\[2pt]
\frac{1}{C} & 0
\end{bmatrix}
\begin{bmatrix} i_L \\ v_C \end{bmatrix} +
\begin{bmatrix}
\frac{1}{L} & \frac{R_1}{L} \\[2pt]
0 & -\frac{1}{C}
\end{bmatrix}
\begin{bmatrix} v_{g1} \\ i_{g2} \end{bmatrix}
$$

with $\mathbf{A} = \begin{bmatrix} -\frac{R_1}{L} & -\frac{1}{L} \\ \frac{1}{C} & 0 \end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix} \frac{1}{L} & \frac{R_1}{L} \\ 0 & -\frac{1}{C} \end{bmatrix}$. The top row is $\dot{i}_L$ (from Step 4), the bottom row is $\dot{v}_C$ (from Step 3).



## Discrete

### Problem 1 (2021-01-19 / 4)

On battlefield we have two tank units, tank unit *a* starts with 100 tanks and tank unit *b* starts with 75 tanks. Step is 1minute. Probability of unit *a* destroying a tank of unit *b* in one step is $\alpha$, and probability of unit *b* destroying a tank of unit *a* in one step is $\beta$. Unit *a* has better shields, so they have $\gamma$ probability of surviving a hit.

a. Model the number of operational tanks over time. Write the result into diference equation $x[k+1] = Ax[k] + Bu[k]$.
b. How long does the battle last with $\alpha = 0.2$, $\beta = 0.45$, and $\gamma = 0.19$?
c. How many tanks does each unit have at the end of the battle?
d. Is given model valid for all times $k > 0$?

#### 1.a

State $x_1[k]$ = operational tanks of unit $a$, $x_2[k]$ = operational tanks of unit $b$ at minute $k$.

Each of the $x_1[k]$ tanks of unit $a$ destroys one tank of unit $b$ with probability $\alpha$, so unit $b$ loses on average $\alpha x_1[k]$ tanks per step. Each of the $x_2[k]$ tanks of unit $b$ destroys a tank of unit $a$ with probability $\beta$, but the shields of unit $a$ save it with probability $\gamma$ — it is destroyed only with probability $1 - \gamma$. Hence unit $a$ loses on average $\beta(1-\gamma)x_2[k]$ tanks per step:

$$
x_1[k+1] = x_1[k] - \beta(1-\gamma)\,x_2[k]
$$
$$
x_2[k+1] = x_2[k] - \alpha\,x_1[k]
$$

In matrix form this is the discrete state equation (no input, $\mathbf{B} = \mathbf{0}$, $u[k] = 0$):

$$
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}[k+1] = \begin{bmatrix} 1 & -\beta(1-\gamma) \\ -\alpha & 1 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}[k] 
$$

#### 1.b

Solve the homogeneous state equation with the $z$-transform. 

Taking $\mathcal{Z}$ of $\vec{x}[k+1] = \mathbf{A}\vec{x}[k]$:

$$
zX(z) - z\vec{x}[0] = \mathbf{A}X(z)
\quad\Longrightarrow\quad
X(z) = z(z\mathbf{I} - \mathbf{A})^{-1}\vec{x}[0]
$$

In other words, $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$ with the discrete state-transition matrix $\mathbf{A}^k = \mathcal{Z}^{-1}\{z(z\mathbf{I}-\mathbf{A})^{-1}\}$. 

Plug in the greeks:

$$
\mathbf{A} = \begin{bmatrix} 1 & -0.3645 \\ -0.2 & 1 \end{bmatrix},
\qquad
\det(\lambda\mathbf{I}-\mathbf{A}) = (\lambda-1)^2 - 0.2\cdot 0.3645 = (\lambda-1)^2 - 0.0729
$$

Using the quadratic formula we get eigenvalues $\lambda_1 = 1.27$ and $\lambda_2 = 0.73$. Invert $X(z) = z(z\mathbf{I}-\mathbf{A})^{-1}\vec{x}[0]$ directly. With

$$
(z\mathbf{I}-\mathbf{A})^{-1} = \frac{1}{(z-1.27)(z-0.73)}\begin{bmatrix} z-1 & -0.3645 \\ -0.2 & z-1 \end{bmatrix}
$$

the two components are

$$
X_1(z) = \frac{z(100z - 127.3375)}{(z-1.27)(z-0.73)}, \qquad
X_2(z) = \frac{z(75z - 95)}{(z-1.27)(z-0.73)}
$$

Split $X_i(z)/z$ into partial fractions (cover-up method) and use the pair $\dfrac{z}{z-a} \leftrightarrow a^k$:

$$
\frac{X_1(z)}{z} = \frac{100z - 127.3375}{(z-1.27)(z-0.73)} = \frac{-0.625}{z-1.27} + \frac{100.625}{z-0.73}
$$

$$
\frac{X_2(z)}{z} = \frac{75z - 95}{(z-1.27)(z-0.73)} = \frac{0.463}{z-1.27} + \frac{74.537}{z-0.73}
$$

For the first one, cover-up gives $-0.625 = \frac{100\cdot1.27 - 127.3375}{0.54}$ and $100.625 = \frac{100\cdot0.73 - 127.3375}{-0.54}$. Multiplying through by $z$ and inverting term by term gives the closed form

$$
x_1[k] = -0.625\cdot 1.27^k + 100.625\cdot 0.73^k, \qquad
x_2[k] = 0.463\cdot 1.27^k + 74.537\cdot 0.73^k
$$

```{=latex}
\begin{example}[frametitle={Remark - why split $X_i(z)/z$, not $X_i(z)$?}]
```

Your table also carries $\frac{1}{z-a} \leftrightarrow a^{k-1}u[k-1]$, so $X_i(z)$ *could* be split into such terms directly. We still split $X_i(z)/z$ for two reasons: (1) our $X_1(z) = \frac{z(100z - 127.3375)}{(z-1.27)(z-0.73)}$ is not strictly proper (numerator degree = denominator degree = 2), so a direct split would need polynomial division first; (2) the standard pair $\mathcal{Z}\{a^k\} = \frac{z}{z-a}$ has no one-sample delay, so splitting $X(z)/z$ and multiplying back by $z$ turns every term into exactly that unshifted form:

$$
\frac{X(z)}{z} = \frac{A_1}{z-\lambda_1} + \frac{A_2}{z-\lambda_2}
\quad\Longrightarrow\quad
X(z) = A_1\frac{z}{z-\lambda_1} + A_2\frac{z}{z-\lambda_2}
\quad\Longrightarrow\quad
x[k] = A_1\lambda_1^k + A_2\lambda_2^k
$$

It is the $z$-domain analogue of partial-fractioning a Laplace transform into $\frac{A}{s-a}$ terms (where $\mathcal{L}^{-1}\{\frac{1}{s-a}\} = e^{at}$), except that in the $z$-domain the natural building block has a $z$ on top.

```{=latex}
\end{example}
```

Since $|\lambda_1| = 1.27 > 1$ the system is unstable — the growing mode $1.27^k$ dominates, so one side must be wiped out. Unit $a$ is the first to go: set $x_1[k] = 0$ and solve for $k$ with the natural log:

$$
-0.625\cdot 1.27^k + 100.625\cdot 0.73^k = 0
\quad\Longrightarrow\quad
\left(\frac{0.73}{1.27}\right)^k = \frac{0.625}{100.625}
$$

$$
k = \frac{\ln(0.625/100.625)}{\ln(0.73/1.27)} = \frac{-5.081}{-0.554} \approx 9.18
$$

Unit $a$'s expected count crosses zero after $\approx 9.18$ minutes, i.e. during the 10th step. **The battle lasts 10 minutes.**

#### 1.c

At the end of the battle unit $a$ is wiped out ($x_1 = 0$) and unit $b$ has **about 8 tanks**. Evaluating the closed form at the last step $k = 10$:

$$
x_2[10] = 0.463\cdot 1.27^{10} + 74.537\cdot 0.73^{10} \approx 8.3
$$

(rounding to whole tanks, and with no further losses once $a$ is gone, unit $b$ keeps $\approx 8$).

#### 1.d

**No.** The model is only an expected-value (mean) model and is valid only while both counts stay positive:

- it returns fractional values, and once a unit is wiped out it keeps producing *negative* tank counts, which are meaningless;
- the recurrence never stops the defeated unit from firing — the term $\alpha x_1[k]$ keeps subtracting even when $x_1[k] \le 0$.

So here it holds only for $0 \le k < 10$, not for all $k > 0$. (The real battle is also stochastic: the linear model tracks only the average over many realizations and ignores the boundary at zero.)



