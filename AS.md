---
title: "Modeling and analysis of linear systems"
author: "Samo F."
header-includes:
  - |
    \usepackage[leftline,framemethod=TikZ]{mdframed}
    \usepackage{circuitikz}
    \usepackage{pgfplots}
    \pgfplotsset{compat=1.17}
    \pgfplotsset{
      spane/.style={
        width=0.30\linewidth, height=0.30\linewidth,
        xlabel={$\operatorname{Re}\lambda$}, ylabel={$j\operatorname{Im}\lambda$},
        axis lines=center,
        axis line style={gray},
        xmin=-3, xmax=3, ymin=-3, ymax=3,
        xtick={-2,-1,0,1,2}, ytick={-2,-1,0,1,2},
      }
    }
    \renewcommand{\arraystretch}{1.4}
    \usepackage{titlesec}
    \newcommand{\sectionbreak}{\clearpage}
    \widowpenalty=10000
    \clubpenalty=10000
    \displaywidowpenalty=10000
    \newmdenv[
      linecolor=gray!55, linewidth=0.7pt,
      backgroundcolor=gray!6,
      innertopmargin=0.6em, innerbottommargin=0.6em,
      innerleftmargin=1em, innerrightmargin=1em,
      skipabove=0.8em, skipbelow=0.8em,
      frametitlefont=\bfseries\small,
      frametitlerule=true, frametitlerulewidth=0.3pt,
      frametitlebackgroundcolor=gray!15,
      frametitleaboveskip=0.3em, frametitlebelowskip=0.3em
    ]{example}
    \usepackage{xcolor}
    \usepackage{pifont}
    \makeatletter
    \renewcommand{\paragraph}{\@startsection{paragraph}{4}{\z@}{1.0em \@plus 0.3em \@minus 0.2em}{0.5em}{\normalfont\normalsize\bfseries\color{black!70}}}
    \renewcommand{\subparagraph}{\@startsection{subparagraph}{5}{\z@}{1.0em \@plus 0.3em \@minus 0.2em}{0.5em}{\normalfont\normalsize\bfseries\color{black!70}}}
    \makeatother
---

# About this

> **Draft.** This is a personal document, clobbered together from notes on lectures by prof. Brumen. Edited and extended by me and LLM's (large lying models). Use at your own risk.

# Modeling

## Higher-order ODEs as first-order systems

State-space form only contains first derivatives, so a higher-order ODE must first be rewritten as a system. The trick is to promote the lower-order derivatives to state variables.

Take the second-order ODE

$$
\ddot{y} + 2\dot{y} + 3y = 4u
$$

and define the states $x_1 = y$, $x_2 = \dot{y}$. The system is then just

$$
\dot{x}_1 = x_2, \qquad
\dot{x}_2 = \ddot{y} = -3x_1 - 2x_2 + 4u
$$

which is exactly the state-space shape from the circuit example:

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u, \qquad
y = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}
$$

In general, an $n$-th order ODE $y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1\dot{y} + a_0 y = u$ becomes $n$ first-order equations by taking $x_1 = y$, $x_2 = \dot{y}$, $\dots$, $x_n = y^{(n-1)}$; the $\mathbf{A}$ matrix takes the companion form

$$
\mathbf{A} = \begin{bmatrix}
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & & & \ddots & \vdots \\
-a_0 & -a_1 & -a_2 & \cdots & -a_{n-1}
\end{bmatrix}
$$

The number of states equals the order of the ODE — the same "one state per energy-storing element" count as in the circuit below.

## State-space modeling of electrical circuits

For this example we want to write down the state-space equations of the circuit in matrix form
$\dot{\vec{x}} = \mathbf{A} \vec{x} + \mathbf{B} \vec{u}$ and $\vec{y} = \mathbf{C} \vec{x} + \mathbf{D} \vec{u}$,
where $\vec{x} = \begin{bmatrix} i_L \\ v_c \end{bmatrix}$ and $\vec{u} = \begin{bmatrix} v_g \end{bmatrix}$ and $\vec{y} = \begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix}$.

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages]
  \draw (0,3) to[V=$v_g$] (0,0)
              (0,3) to[R=$R_1$, v>=$v_{R_1}$] (3,3)
              to[L=$L$, i>^=$i_L$] (6,3)
              (6,3) to[C] (6,0)
              (6,3) -- (8,3)
              to[R=$R_2$] (8,0)
              to[short] (0,0);
  \node[left=14pt] at (6,1.5) {$C$};
  \node at (6.25,1.9) {$+$};
  \node[right=14pt] at (6,1.5) {$v_c$};
\end{circuitikz}
\end{center}
```

Let's select one node as ground. Although any node can be ground, we try to choose it in a way that will make the resulting equation as easy as possible. Generally, pick the node with the most element connections to reduce the number of unknown node voltages. In our case, we can select the bottom node as ground.\footnote{In simulation software (e.g., SPICE), the ground node choice can influence numerical stability, but picking the one with most connections is a still good rule of thumb.}

Then we proceed to mark the remaining nodes.

Passive sign convention (PSC) defines an element’s voltage positive at the terminal where the reference current enters; then power is positive when the element absorbs energy. For voltage source, according to PSC, we must mark the reference current in such a way that current entering the element will absorb power and when leaving (minus sign) give power to the rest of the circuit. That means that arrow should point into the + of voltage source. For capacitor we have defined polarity: we apply the PSC convention to $i_c$ (arrow into +). And for the inductor we have defined the current $i_L$. Although $v_L$ is not required here, we could define its polarity according to PSC as well ($V_2$ is positive in relation to $V_3$).

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages]
  \draw (0,3) node[circ,label=above:$V_1$]{} to[V=$v_g$, i>^=$i_g$] (0,0) node[ground]{};
  \draw (0,3) to[R=$R_1$, v>=$v_{R_1}$] (3,3) node[circ,label=above:$V_2$]{}
              to[L=$L$, i>^=$i_L$] (6,3) node[circ,label=above:$V_3$]{}
              -- (8,3) to[R=$R_2$] (8,0) to[short] (0,0);
  \draw (6,3) to[C, i>^=$i_C$ ] (6,0);
  \node[left=14pt] at (6,1.5) {$C$};
  \node at (6.25,1.9) {$+$};
  \node[right=14pt] at (6,1.5) {$v_c$};
\end{circuitikz}
\end{center}
```

Common approaches for deriving state-space equations include node-voltage and mesh-current methods. Here we apply a combination of both. It might be described as node-voltage formulation with selected element state variables.

First we observe the $V_1 = v_g$ and $v_c = V_3$.

We write down the equations for each node using Kirchhoff's current law. When expressing currents through resistors, we start with the current node voltage (so currents are taken as leaving the node: plus sign in our equations).

$$\frac{V_1 - V_2}{R_1} + i_g = 0$$

When node is connected to an inductor, we express the current through the inductor as a state variable. Note that the direction of current for $i_L$ is defined as flowing out of $V_2$. For $V_2$ we get:

$$\frac{V_2 - V_1}{R_1} + i_L = 0$$

And the same for capacitors: we express the current through the capacitor as a state variable. For the capacitor we take its voltage $v_c$ as the state variable (more standard); current follows $i_C = C\,\dot{v}_c$ under PSC.

Next, we write down the equations for the energy-storing elements using their constitutive relations. Note that $i_L$ is chosen from $V_2$ to $V_3$. Lenz’s law is not ignored; its effect was already built into the sign of the inductor’s voltage when we adopted PSC. Faraday’s law gives $v = L\,\dot{i}$ for the chosen polarity (voltage drop in the direction of the reference current). If you had defined the voltage polarity opposite to the current reference, the relation would appear as $v = -L\,\dot{i}$. Thus no extra minus is added later - the orientation choices at the start encode it.

$$ v_L = L \frac{di_L}{dt} = V_2 - V_3 $$

And for the capacitor:

$$ i_C = C \frac{dv_c}{dt} = i_L - \frac{V_3}{R_2} $$

Since $V_1 = v_g$ and $v_c = V_3$ we get the state-space form

$$
\frac{d}{dt}\begin{bmatrix} i_L \\ v_c \end{bmatrix} =
\begin{bmatrix}
-\frac{R_1}{L} & -\frac{1}{L} \\
\frac{1}{C} & -\frac{1}{C R_2}
\end{bmatrix}
\begin{bmatrix} i_L \\ v_c \end{bmatrix} +
\begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix} v_g.
$$

If outputs are $v_{R_1}$ and $v_L$ then

$$
\begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix} =
\begin{bmatrix}
R_1 & 0 \\
L\,\frac{d}{dt} & 0
\end{bmatrix}
\begin{bmatrix} i_L \\ v_c \end{bmatrix} +
\begin{bmatrix} -1 \\ 0 \end{bmatrix} v_g,
$$

or equivalently using algebraic forms:
$v_{R_1}=R_1 i_L - v_g$, $v_L = L\,\dfrac{di_L}{dt}$.


```{=latex}
\begin{example}[frametitle={Fully worked out example - getting state-space equations from a circuit }]
```

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages, american currents]
  \draw (0,3) to[V=$v_g$] (0,0)
        (0,3) to[R=$R_1$] (3,3) -- (8,3);
  \draw (4,3) to[C=$C$] (4,0);        % vertical C  at 4
  \draw (6,3) to[R=$R_2$] (6,0);      % vertical R at 6
  \draw (8,0) to[I, l_=$i_g$] (8,3);  % vertical i_g at 8
  \draw (0,0) to[L=$L$] (3,0);
  \draw (3,0) -- (4,0);
  \draw (3,0) to[open, i>^=$i_L$] (4,0);
  \draw (4,0) -- (8,0);
  \node at (3.3,1.5) {$v_c$};
\end{circuitikz}
\end{center}
```

For the circuit above, we want to write down the state-space equations  in the form $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, where the state vector $\vec{x} = [i_L, v_c]^T$ and $\vec{u} = [v_g, i_g]^T$.

**Step 1** Decide on nodes.

```{=latex}
\begin{center}
\begin{circuitikz}[scale=1.2, european resistors, american voltages, american currents]
  \draw (0,3) node[circ,label=above:$V_1$]{} to[V=$v_g$, i>^=$i_{g'}$] (0,0) node[ground]{};
  \draw (0,3) to[R=$R_1$] (3,3) -- (8,3);
  \draw (4,3) to[C=$C$, i>^=$i_C$] (4,0);
  \draw (6,3) to[R=$R_2$] (6,0);
  \draw (8,0) to[I, l_=$i_g$] (8,3);
  \draw (0,0) to[L=$L$] (3,0);
  \draw (3,0) -- (4,0);
  \draw (3,0) to[open, i>^=$i_L$] (4,0);
  \draw (4,0) node[circ,label=below:$V_3$]{} -- (8,0);
  \node at (3.3,1.5) {$v_c$};
  \node at (3.75,1.85) {$+$};
  \node at (4,3) [circ,label=above:$V_2$]{};
\end{circuitikz}
\end{center}
```

**Step 2** Node and element equations. From the annotated circuit above we write the equations.

Node $V_1$: $\; i_{g'} + \dfrac{V_1 - V_2}{R_1} = 0$

Node $V_2$: $\; i_c + \dfrac{V_2 - V_1}{R_1} - i_g + \dfrac{V_2 - V_3}{R_2} = 0$

Node $V_3$: $\; -i_c + \dfrac{V_3 - V_2}{R_2} + i_g - i_L = 0$

Capacitor: $\; i_c = C\dot{v}_c, \quad v_c = V_2 - V_3$

Inductor: $\; v_L = L\dot{i}_L, \quad v_L = -V_3$

And we note that $V_1 = v_g$ and $i_{g'} = i_L$ (the current through the source $v_g$ equals the inductor current). 
Substituting into $\dot{v}_c = i_c/C$ and $\dot{i}_L = v_L/L$:


**Step 3** 


**Step 4** collect the equations into matrix form.

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}, \qquad
\mathbf{A} = \begin{bmatrix}
-\frac{R_1}{L} & \frac{1}{L} \\[2pt]
-\frac{1}{C} & -\frac{1}{CR_2}
\end{bmatrix}, \quad
\mathbf{B} = \begin{bmatrix}
-\frac{1}{L} & 0 \\[2pt]
0 & \frac{1}{C}
\end{bmatrix}
$$




```{=latex}
\end{example}
```

## Modeling mechanical systems

Mechanical models rest on Newton's laws; the three ideal elements are direct analogues of the electrical ones.

### Translational systems

- Newton's second law: $F = ma$.
- **Spring** — $F = k(x_2 - x_1)$: stores energy, like a capacitor.
- **Damper** — $F = b(\dot{x}_2 - \dot{x}_1)$: dissipates energy, like a resistor.
- **Mass** — stores kinetic energy, like an inductor.

```{=latex}
\begin{example}[frametitle={Example - mass–spring–damper}]
```

For $m\ddot{x} + b\dot{x} + kx = F$ with states $x_1 = x$, $x_2 = \dot{x}$:

$$
\dot{x}_1 = x_2, \qquad
\dot{x}_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2 + \frac{1}{m}F
$$

the same state-space shape as the electrical circuit, with $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}$, $\mathbf{B} = \begin{bmatrix} 0 \\ \frac{1}{m} \end{bmatrix}$ and output $y = x = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}$.

```{=latex}
\end{example}
```

### Rotational systems

The same equations with $x \to \theta$, $v \to \omega$, $F \to \tau$, $m \to J$: torque $\tau = J\alpha$, torsional spring $\tau = k(\theta_2 - \theta_1)$, rotational damper $\tau = b(\omega_2 - \omega_1)$. Gears and transmissions just scale torque and angular speed by the gear ratio.

## Modeling biological systems

Nonlinear population models — the linearization machinery of the Linearization chapter applies around their equilibria.

### Lotka–Volterra (predator–prey)

Prey $x$, predators $y$:

$$
\dot{x} = \alpha x - \beta xy, \qquad \dot{y} = \delta xy - \gamma y
$$

the prey grows exponentially ($\alpha x$) and is eaten proportionally to encounters ($\beta xy$); the predators grow with the available food ($\delta xy$) and die off ($\gamma y$). Equilibria: the trivial $(0, 0)$ and the coexistence point $(x_e, y_e) = (\gamma/\delta,\ \alpha/\beta)$.

### SIR epidemic

Susceptible $S$, infectious $I$, recovered $R$, with $N = S + I + R$ constant:

$$
\dot{S} = -\beta SI, \qquad \dot{I} = \beta SI - \gamma I, \qquad \dot{R} = \gamma I
$$

With $N$ fixed, only two of the three equations are independent. The epidemic takes off iff the basic reproduction number $R_0 = \beta S_0/\gamma > 1$.

# State-space

## 1. State-space variables and equations

A system is captured by its state — the smallest set of variables that fully summarizes its past — plus how that state evolves and how it shapes the outputs. State variables are usually chosen as directly measurable or physically meaningful quantities: in electrical circuits the inductor currents and capacitor voltages, in mechanical systems the displacements and velocities. MIMO (multiple-input, multiple-output) systems bundle this into one picture, with the state vector living inside the system:

```{=latex}
\begin{center}
\begin{tikzpicture}[>=stealth]
  \node[draw, thick, minimum width=3cm, minimum height=2.6cm, align=center] (sys) {$\vec{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$};
  \draw[->] (-2.8,0.8) -- node[above]{$u_1$} (-1.5,0.8);
  \draw[->] (-2.8,-0.8) -- node[above]{$u_2$} (-1.5,-0.8);
  \draw[->] (1.5,0.8) -- node[above]{$y_1$} (2.8,0.8);
  \draw[->] (1.5,-0.8) -- node[above]{$y_2$} (2.8,-0.8);
\end{tikzpicture}
\end{center}
```

$\vec{u}$ collects the inputs, $\vec{y}$ the outputs, and $\vec{x}$ the states. In general (nonlinear, time-varying) systems the state and output equations read

$$
\dot{\vec{x}} = \mathbf{f}(\vec{x}, \vec{u}, t), \qquad
\vec{y} = \mathbf{g}(\vec{x}, \vec{u}, t)
$$

For linear time-invariant (LTI) systems they collapse to Kalman's matrix form:

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}
$$
$$
\vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u}
$$

with $\mathbf{A}$ ($n\times n$) the dynamics, $\mathbf{B}$ ($n\times p$) the input coupling, $\mathbf{C}$ ($q\times n$) the output coupling, and $\mathbf{D}$ ($q\times p$) the direct feedthrough — typically $\mathbf{D} = \mathbf{0}$. The outputs are generally not the states themselves — that is exactly what $\mathbf{C}$ and $\mathbf{D}$ capture.

The state variables are not unique. For the second-order ODE $\ddot{y} + 2\dot{y} + 3y = 4u$, the Modeling chapter chose $x_1 = y$, $x_2 = \dot{y}$:

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u, \qquad y = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}
$$

but swapping the order, $z_1 = \dot{y}$, $z_2 = y$, gives an equally valid triple with the same input–output behaviour:

$$
\dot{\vec{z}} = \begin{bmatrix} -2 & -3 \\ 1 & 0 \end{bmatrix}\vec{z} + \begin{bmatrix} 4 \\ 0 \end{bmatrix}u, \qquad y = \begin{bmatrix} 0 & 1 \end{bmatrix}\vec{z}
$$

In general, any invertible $\mathbf{T}$ defines new states $\tilde{\vec{x}} = \mathbf{T}^{-1}\vec{x}$ and yields the equivalent representation $\tilde{\mathbf{A}} = \mathbf{T}^{-1}\mathbf{A}\mathbf{T}$, $\tilde{\mathbf{B}} = \mathbf{T}^{-1}\mathbf{B}$, $\tilde{\mathbf{C}} = \mathbf{C}\mathbf{T}$, $\tilde{\mathbf{D}} = \mathbf{D}$.

## 2. State-space representation

The state-space representation is a geometric view of the dynamics: at every instant the system sits at a point $\vec{x}(t)$ in state space, and the equations $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ push that point along a curve — the *trajectory*. For the example system from the Modeling chapter, $\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x}$ with $\vec{x}(0) = (1, 0)$, the state spirals into the origin (markers at integer times):

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[
  width=0.6\linewidth, height=0.6\linewidth,
  xlabel={$x_1$}, ylabel={$x_2$},
  axis lines=center,
  axis line style={gray},
  label style={font=\small},
  xmin=-1.3, xmax=1.3, ymin=-1.3, ymax=1.3,
  xtick={-1,0,1}, ytick={-1,0,1},
  grid=major, grid style={gray!25},
]
\addplot[domain=0:8, samples=200, thick, blue]
  ({exp(-x)*(cos(deg(sqrt(2)*x)) + (1/sqrt(2))*sin(deg(sqrt(2)*x)))},
   {-(3/sqrt(2))*exp(-x)*sin(deg(sqrt(2)*x))});
\addplot[only marks, mark=*, mark size=1.5pt, black]
  coordinates {(1,0) (0.314,-0.771) (-0.099,-0.089) (-0.054,0.094)};
\node[below left, font=\scriptsize] at (axis cs:1,0) {$t=0$};
\node[below, font=\scriptsize] at (axis cs:0.314,-0.771) {$t=1$};
\node[above right, font=\scriptsize] at (axis cs:-0.099,-0.089) {$t=2$};
\node[above, font=\scriptsize] at (axis cs:-0.054,0.094) {$t=3$};
\end{axis}
\end{tikzpicture}
\end{center}
```

The decay and the oscillation come straight from the eigenvalues of $\mathbf{A}$ — here $-1 \pm j\sqrt{2}$, the negative real part damping the spiral, the imaginary part driving the rotation.

## 3. Homogeneous Solution

$$\dot{\vec{x}} = \mathbf{A}\vec{x}$$ 

with initial condition $\vec{x}(0) = \vec{x}_0$ is a linear ODE. The solution can be expressed in terms of the matrix exponential:

For the trivial case of homogeneous equations (homogeneous: no input, $\vec{u} = 0$), let's try solving it with scalars first:

$$
\dot{x} = a x
$$
$$
\dot{x} - a x = 0
$$

Then we insert $x = e^{\lambda t}$ (which per chain rule gives $\dot{x} = \lambda e^{\lambda t}$) and get:

$$
\lambda e^{\lambda t} - a e^{\lambda t} = 0
$$
$$
\lambda - a = 0
$$
$$
\lambda = a
$$

So $\lambda = a$ is the only root and the general solution is $x(t) = C e^{at}$, with $C$ fixed by the initial condition $x(0) = x_0$:

$$
x(t_0) = C e^{a{t_0}} \quad\Longrightarrow\quad C = x_0 e^{-a{t_0}} \quad\Longrightarrow\quad x(t) = x_0 e^{a(t-t_0)}.
$$

Where the last part is the solution of scalar homogeneous ODE. The solution of the vector case is a straightforward generalization.

By the analogy with the scalar case, we can try the same exponential solution for the vector case $\dot{\vec{x}} = \mathbf{A}\vec{x}$ (still homogeneous, $\vec{u} = 0$). Try the same exponential:


$$
\vec{X}_H = \vec{x}_0\, e^{\mathbf{A}(t-t_0)}
$$

which indeed satisfies $\vec{X}_H(t_0) = \vec{x}_0\, e^{\mathbf{A}(t_0-t_0)} = \vec{x}_0\, \mathbf{I} = \vec{x}_0$.

Solutions for the scalar case can be expressed as a Taylor series:

$$
e^{at} = 1 + at + \frac{(at)^2}{2!} + \frac{(at)^3}{3!} + \dots
$$

And since matrices are happily multipliable:

$$
e^{\mathbf{A}t} = \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!}
$$

And because mathematicians don't like writing/typing they decided to shorthand the $e^{\mathbf{A}(t-t_0)}$ to $\Phi(t)$ and call it the state transition matrix. So we can write the solution as:

$$
\vec{X}_H = \Phi(t) \vec{x}_0
$$

State transition matrix has the following properties:

1. $\Phi(0) = \mathbf{I}$ (identity matrix)
2. $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$
3. $\Phi(t_1 - t_2) = \Phi(t_1)\Phi^{-1}(t_2)$
4. $\frac{d}{dt}\Phi(t) = \mathbf{A}\Phi(t)$

## 4. Nonhomogeneous Solution

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

Where the first part is the homogeneous solution (response to initial conditions) and the second part is the particular solution (response to the input signal) in the form of a convolution integral:

$$
\int f(t-\tau) g(\tau) d\tau = f * g
$$

## 5. Obtaining the state-transition matrix

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

$$
\vec{x}(t) = \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\}\vec{x}_0 + \mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)\right\}
$$

The first term is the homogeneous response, the second is the convolution with $\vec{u}$, so comparing with the boxed solution of Section 4 identifies

$$
\mathcal{L}^{-1}\left\{(s\mathbf{I} - \mathbf{A})^{-1}\right\} = e^{\mathbf{A}t} = \Phi(t)
$$

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

which (shockingly, I know!) matches the Taylor result.

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

i.e. entrywise $\Phi_{nn}(t) = \sum_{k=0}^{\infty} \frac{(d_n t)^k}{k!} = e^{d_n t}$.

#### Eigenvalues

Let's go on a little tangent and see how to diagonalize a matrix. The eigenvalues of $\mathbf{A}$ are the scalars $\lambda$ for which

$$
\mathbf{A}\vec{v} = \lambda\vec{v}
$$

has a nonzero solution $\vec{v} \ne 0$ — the eigenvector. Geometrically, $\mathbf{A}$ just stretches $\vec{v}$ by $\lambda$ without rotating it. Rearranging gives $(\mathbf{A} - \lambda\mathbf{I})\vec{v} = 0$, which has a nontrivial solution iff the matrix is singular, i.e.

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

So eigenvalues are the roots of the characteristic polynomial $\det(\mathbf{A} - \lambda\mathbf{I})$. For an $n \times n$ matrix this is a polynomial of degree $n$, so by the fundamental theorem of algebra there are $n$ eigenvalues counting multiplicity. Each eigenvalue carries two numbers:

- **Algebraic multiplicity** $\alpha_i$ — how many times $\lambda_i$ occurs as a root of the characteristic polynomial. These sum to the matrix dimension: $\sum_i \alpha_i = n$.
- **Geometric multiplicity** $\gamma_i$ — the dimension of the eigenspace $\ker(\mathbf{A} - \lambda_i\mathbf{I})$, i.e. the number of linearly independent eigenvectors belonging to $\lambda_i$. Computed as the nullity $\gamma_i = n - \operatorname{rank}(\mathbf{A} - \lambda_i\mathbf{I})$.

They are always related by $1 \le \gamma_i \le \alpha_i$. The gap $\alpha_i - \gamma_i$ measures how "defective" $\mathbf{A}$ is at $\lambda_i$: if $\gamma_i < \alpha_i$ there are not enough eigenvectors, and diagonalization fails.

In practice:

1. Solve $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ for the eigenvalues — factor the polynomial, use the quadratic formula for $2\times 2$, or numerical methods for larger matrices.
2. For each $\lambda_i$, solve $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v} = 0$; the number of free parameters in the solution is $\gamma_i$.

$\mathbf{A}$ is diagonalizable iff $\gamma_i = \alpha_i$ for every $i$. This is always the case when all eigenvalues are distinct, since then $\gamma_i = \alpha_i = 1$.

```{=latex}
\begin{example}[frametitle={Example - eigenvalues and eigenvectors}]
```

Find the eigenvalues and eigenvectors of $\mathbf{A} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{bmatrix}$.

The characteristic polynomial (upper-triangular, so the eigenvalues sit on the diagonal):

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 1-\lambda & 0 & 0 \\ 0 & 2-\lambda & 1 \\ 0 & 0 & 2-\lambda \end{vmatrix} = (1-\lambda)(2-\lambda)^2 = 0
$$

so $\lambda_1 = 1$ with $\alpha_1 = 1$, and $\lambda_2 = 2$ with $\alpha_2 = 2$.

For $\lambda_1 = 1$, solve $(\mathbf{A} - \mathbf{I})\vec{v} = 0$:

$$
\begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}\vec{v} = 0
\quad\Longrightarrow\quad
v_3 = 0,\ v_2 = 0,\ v_1 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
$$

For $\lambda_2 = 2$, solve $(\mathbf{A} - 2\mathbf{I})\vec{v} = 0$:

$$
\begin{bmatrix} -1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}\vec{v} = 0
\quad\Longrightarrow\quad
v_1 = 0,\ v_3 = 0,\ v_2 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

Here $\gamma_2 = 1 < \alpha_2 = 2$: only two linearly independent eigenvectors exist, so $\mathbf{A}$ is defective and **not** diagonalizable.

```{=latex}
\end{example}
```

#### Diagonalization

When $\gamma_i = \alpha_i$ for every eigenvalue, there are exactly $n$ linearly independent eigenvectors $\vec{v}_1, \dots, \vec{v}_n$. Stack them as columns:

$$
\mathbf{V} = \begin{bmatrix} \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \end{bmatrix}
$$

Each eigenpair satisfies $\mathbf{A}\vec{v}_i = \lambda_i \vec{v}_i$, so all of them at once read

$$
\mathbf{A}\mathbf{V} = \mathbf{V}\boldsymbol{\Lambda}, \qquad
\boldsymbol{\Lambda} = \begin{bmatrix}
\lambda_1 & & \\
& \ddots & \\
& & \lambda_n
\end{bmatrix}
$$

Independence makes $\mathbf{V}$ invertible, so multiplying by $\mathbf{V}^{-1}$ from the right gives the factorization

$$
\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}
$$

This is the whole trick: $\mathbf{A}$ is just a diagonal matrix in a different basis. Powers pass through the same similarity ($\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}$), so the Taylor series telescopes into

$$
e^{\mathbf{A}t} = \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!}
= \mathbf{V} \left( \sum_{k=0}^{\infty} \frac{(\boldsymbol{\Lambda}t)^k}{k!} \right) \mathbf{V}^{-1}
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

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via diagonalization}]
```

$\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. The characteristic equation $\det(\mathbf{A} - \lambda\mathbf{I}) = (-2-\lambda)(-1-\lambda) = 0$ gives distinct eigenvalues $\lambda_1 = -2$, $\lambda_2 = -1$, so $\gamma_i = \alpha_i = 1$ and $\mathbf{A}$ is diagonalizable.

Eigenvectors from $(\mathbf{A} - \lambda_i\mathbf{I})\vec{v}_i = 0$, one eigenvalue at a time.

For $\lambda_1 = -2$: $(\mathbf{A} - (-2)\mathbf{I}) = \mathbf{A} + 2\mathbf{I}$, so

$$
(\mathbf{A} + 2\mathbf{I}) = \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}, \qquad
\begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix}\vec{v}_1 = 0
\quad\Longrightarrow\quad
v_1 + v_2 = 0,\ v_1 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

For $\lambda_2 = -1$: $(\mathbf{A} - (-1)\mathbf{I}) = \mathbf{A} + \mathbf{I}$, so

$$
(\mathbf{A} + \mathbf{I}) = \begin{bmatrix} -1 & 0 \\ 1 & 0 \end{bmatrix}, \qquad
\begin{bmatrix} -1 & 0 \\ 1 & 0 \end{bmatrix}\vec{v}_2 = 0
\quad\Longrightarrow\quad
v_1 = 0,\ v_2 \text{ free}
\quad\Longrightarrow\quad
\vec{v}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

Assemble the pieces ($\det\mathbf{V} = 1$, so inversion is trivial):

$$
\mathbf{V} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}, \qquad
\mathbf{V}^{-1} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \qquad
\boldsymbol{\Lambda} = \begin{bmatrix} -2 & 0 \\ 0 & -1 \end{bmatrix}
$$

Putting it together,

$$
\Phi(t) = e^{\mathbf{A}t} = \mathbf{V} e^{\boldsymbol{\Lambda}t} \mathbf{V}^{-1}
= \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}\begin{bmatrix} e^{-2t} & 0 \\ 0 & e^{-t} \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}
= \begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}
$$

which (surprise, surprise) matches the Taylor and Laplace results. 

```{=latex}
\end{example}
```

The diagonalization method is perhaps the most elegant, but it fails for defective matrices. The Laplace method above and Cayley–Hamilton method below both work even for defective matrices.

### $\Phi$ via Cayley–Hamilton

The Cayley–Hamilton theorem states that every matrix satisfies its own characteristic equation. If

$$
\det(\lambda\mathbf{I} - \mathbf{A}) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_0
$$

substituting the matrix for the scalar gives the zero matrix:

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

For an analytic function (e.g. $e^{\mathbf{A}t}$ or $\sin\mathbf{A}$) the same holds after expanding it in a Taylor series and reducing term by term.

The coefficients follow from the key observation that $\mathbf{A}$ and its eigenvalues satisfy the same polynomial relation, so the same equation holds at each $\lambda_i$:

$$
e^{\lambda_i t} = \alpha_0(t) + \alpha_1(t)\lambda_i + \cdots + \alpha_{n-1}(t)\lambda_i^{n-1}, \qquad i = 1, \dots, n
$$

Solving this Vandermonde system gives the $\alpha_j(t)$. If an eigenvalue $\lambda_i$ has algebraic multiplicity $k$, evaluating at $\lambda_i$ yields only one equation; the missing $k-1$ come from differentiating $f(\lambda) = r(\lambda)$ with respect to $\lambda$, $k-1$ times — each eigenvalue contributes exactly as many equations as its multiplicity. Unlike diagonalization, this works even for defective matrices (see the eigenvalues example).

```{=latex}
\begin{example}[frametitle={Example - obtaining $\Phi$ via Cayley–Hamilton}]
```

Same $\mathbf{A} = \begin{bmatrix} -2 & 0 \\ 1 & -1 \end{bmatrix}$. Characteristic equation:

$$
\det(\lambda\mathbf{I} - \mathbf{A}) = (\lambda+2)(\lambda+1) = \lambda^2 + 3\lambda + 2 = 0
$$

so $\mathbf{A}^2 + 3\mathbf{A} + 2\mathbf{I} = \mathbf{0}$, and with $n = 2$:

$$
e^{\mathbf{A}t} = \alpha_0(t)\mathbf{I} + \alpha_1(t)\mathbf{A}
$$

Evaluate at the eigenvalues:

$$
\lambda_1 = -2: \quad e^{-2t} = \alpha_0 - 2\alpha_1, \qquad
\lambda_2 = -1: \quad e^{-t} = \alpha_0 - \alpha_1
$$

Subtracting gives $\alpha_1 = e^{-t} - e^{-2t}$, and then $\alpha_0 = 2e^{-t} - e^{-2t}$. Substituting back:

$$
\Phi(t) = e^{\mathbf{A}t} = (2e^{-t} - e^{-2t})\mathbf{I} + (e^{-t} - e^{-2t})\mathbf{A}
= \begin{bmatrix} e^{-2t} & 0 \\ e^{-t} - e^{-2t} & e^{-t} \end{bmatrix}
$$

which (you guessed it) matches all previous methods. 

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - computing $\sin\mathbf{A}$ via Cayley–Hamilton}]
```

The theorem is not limited to the exponential. $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$ has characteristic polynomial $g(\lambda) = \lambda^2 + 1$ (eigenvalues $\pm j$), so $\sin\mathbf{A} = \alpha_0\mathbf{I} + \alpha_1\mathbf{A}$ with

$$
\sin\lambda = \alpha_0 + \alpha_1\lambda \quad \text{at } \lambda = \pm j:
\qquad
\alpha_0 + \alpha_1 j = \sin(j) = j\sinh 1, \qquad
\alpha_0 - \alpha_1 j = -j\sinh 1
$$

giving $\alpha_0 = 0$, $\alpha_1 = \sinh 1$, hence

$$
\sin\mathbf{A} = \sinh(1)\,\mathbf{A} = \begin{bmatrix} 0 & \sinh 1 \\ -\sinh 1 & 0 \end{bmatrix}
$$

(consistent with the Taylor series: $\mathbf{A}^2 = -\mathbf{I}$, $\mathbf{A}^3 = -\mathbf{A}$, $\dots$, so $\sin\mathbf{A} = (1 + \frac{1}{3!} + \frac{1}{5!} + \cdots)\mathbf{A} = \sinh(1)\,\mathbf{A}$).

```{=latex}
\end{example}
```

### Final remarks on obtaining $\Phi$

We have shown four ways to skin a cat, but at the end you still have the same dead cat. The Taylor series is the most general, flows nicely from rudimentary principles, but it is slow and tedious. Diagonalization is elegant, but fails for defective matrices. Laplace transform is a nice trick, but requires some algebraic manipulation. Cayley–Hamilton is a clever method, but requires solving a Vandermonde system. 

Cayley–Hamilton specifically will come in very handy when we'll talk about controllability and observability.

In practice, the choice of method depends on the specific matrix $\mathbf{A}$ and the context of the problem.

# Properties of systems

## Modes of an LTI system

The (free) response of an LTI system is set entirely by the eigenvalues of $\mathbf{A}$. From the homogeneous solution, $\vec{x}(t) = e^{\mathbf{A}t}\vec{x}_0$, and diagonalizing gives $e^{\mathbf{A}t} = \mathbf{V}e^{\boldsymbol{\Lambda}t}\mathbf{V}^{-1}$, so the response is a linear combination of the exponentials

$$
e^{\lambda_1 t},\; e^{\lambda_2 t},\; \dots,\; e^{\lambda_n t}
$$

each a **mode** of the system. The spectrum of $\mathbf{A}$ — its eigenvalues $\lambda_i$ — therefore maps one-to-one onto the modes of the response: to the $n$ eigenvalues of $\mathbf{A}$ belong $n$ modes of the system. A real $\lambda$ gives a growing or decaying exponential; a conjugate pair $\sigma \pm j\omega$ gives an oscillation with envelope $e^{\sigma t}$.

These eigenvalues are also the **poles** of the transfer function $G(s) = \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$: its denominator is $\det(s\mathbf{I}-\mathbf{A})$, so the poles are exactly the eigenvalues of $\mathbf{A}$ — at least for a minimal (controllable and observable) realization. An eigenvalue belonging to an uncontrollable or unobservable mode cancels out of $G(s)$ and is not a pole.

Everything that follows — stability, controllability, observability — is decided by these modes.

## Controllability

A system $(\mathbf{A}, \mathbf{B})$ is **controllable** if, for any initial state $\vec{x}_0$ and any target state $\vec{x}_1$, there exists an input $\vec{u}(t)$ that drives the state from $\vec{x}_0$ to $\vec{x}_1$ in finite time — the input can steer the state anywhere in state space.

The **controllability matrix** collects the columns that matter:

$$
\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}
$$

and the system is controllable iff $\operatorname{rank}\mathcal{C} = n$.

Why exactly those columns? Take the state response with $\vec{x}(0) = \vec{0}$; reaching $\vec{x}$ at time $t$ requires

$$
\vec{x}(t) = \int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\vec{u}(\tau)\, d\tau
$$

(for LTI, reachability from the origin is the same as controllability, since $e^{\mathbf{A}t}$ is always invertible). By Cayley–Hamilton, $e^{\mathbf{A}s}$ is a polynomial in $\mathbf{A}$ of degree at most $n-1$:

$$
e^{\mathbf{A}s} = \sum_{k=0}^{n-1}\alpha_k(s)\mathbf{A}^k
$$

Substituting and pulling $\mathbf{A}^k\mathbf{B}$ out of the integral,

$$
\vec{x}(t) = \sum_{k=0}^{n-1} \mathbf{A}^k\mathbf{B} \underbrace{\int_0^t \alpha_k(t-\tau)\vec{u}(\tau)\, d\tau}_{\vec{w}_k}
= \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}\vec{w}
$$

A state is reachable exactly when it lies in the column space of $\mathcal{C}$, so every state is reachable iff $\operatorname{rank}\mathcal{C} = n$. Powers $\mathbf{A}^k$ with $k \ge n$ contribute nothing new — Cayley–Hamilton folds them back into $\mathbf{A}^0, \dots, \mathbf{A}^{n-1}$.

```{=latex}
\begin{example}[frametitle={Example - controllability of a diagonal system}]
```

$\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$, $\mathbf{B} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$.

$$
\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} \end{bmatrix}
= \begin{bmatrix} 1 & -1 & 1 \\ 1 & -2 & 4 \\ 1 & -3 & 9 \end{bmatrix}, \qquad
\det\mathcal{C} = -2 \ne 0
$$

so $\operatorname{rank}\mathcal{C} = 3 = n$ and the system is controllable — every mode is driven by the input. With $\mathbf{B} = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$ the second mode is decoupled from the input and

$$
\mathcal{C} = \begin{bmatrix} 1 & -1 & 1 \\ 0 & 0 & 0 \\ 1 & -3 & 9 \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{C} = 2 < 3
$$

so the system is **not** controllable.

```{=latex}
\end{example}
```

## Observability

A system $(\mathbf{A}, \mathbf{C})$ is **observable** if the initial state $\vec{x}_0$ can be reconstructed from the output $\vec{y}(t)$ (and the known input $\vec{u}(t)$) over a finite time interval — every mode eventually shows up in the output.

The **observability matrix** collects the rows that matter:

$$
\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}
$$

and the system is observable iff $\operatorname{rank}\mathcal{O} = n$.

Why exactly those rows? With $\vec{u} = \vec{0}$, the output is

$$
\vec{y}(t) = \mathbf{C}e^{\mathbf{A}t}\vec{x}_0
$$

and by Cayley–Hamilton, $e^{\mathbf{A}t}$ is a polynomial in $\mathbf{A}$ of degree at most $n-1$:

$$
e^{\mathbf{A}t} = \sum_{k=0}^{n-1}\alpha_k(t)\mathbf{A}^k
$$

so the output becomes

$$
\vec{y}(t) = \sum_{k=0}^{n-1}\alpha_k(t)\,\mathbf{C}\mathbf{A}^k\vec{x}_0
$$

The known functions $\alpha_k(t)$ let the output pin down each $\mathbf{C}\mathbf{A}^k\vec{x}_0$; stacking them,

$$
\begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix}\vec{x}_0 = \vec{z}
$$

is a linear system for $\vec{x}_0$ with a unique solution iff $\mathcal{O}$ has full column rank $n$. Powers $\mathbf{A}^k$ with $k \ge n$ add nothing new — Cayley–Hamilton folds them back into $\mathbf{A}^0, \dots, \mathbf{A}^{n-1}$.

Note the duality: observability of $(\mathbf{A}, \mathbf{C})$ is controllability of $(\mathbf{A}^T, \mathbf{C}^T)$ — here, with $\mathbf{C} = \mathbf{B}^T$, the observability matrix is exactly $\mathcal{O} = \mathcal{C}^T$.

```{=latex}
\begin{example}[frametitle={Example - observability of a diagonal system}]
```

Same $\mathbf{A} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}$, $\mathbf{C} = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$.

$$
\mathcal{O} = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \end{bmatrix}
= \begin{bmatrix} 1 & 1 & 1 \\ -1 & -2 & -3 \\ 1 & 4 & 9 \end{bmatrix}, \qquad
\det\mathcal{O} = -2 \ne 0
$$

so $\operatorname{rank}\mathcal{O} = 3 = n$ and the system is observable — every mode shows up in the output. With $\mathbf{C} = \begin{bmatrix} 1 & 0 & 1 \end{bmatrix}$ the second mode is invisible in the output:

$$
\mathcal{O} = \begin{bmatrix} 1 & 0 & 1 \\ -1 & 0 & -3 \\ 1 & 0 & 9 \end{bmatrix}, \qquad
\operatorname{rank}\mathcal{O} = 2 < 3
$$

so the system is **not** observable.

```{=latex}
\end{example}
```

## Equilibrium states and phase portraits

An **equilibrium state** $\vec{x}_e$ is where the system stays put, $\dot{\vec{x}} = \vec{0}$ at $\vec{x} = \vec{x}_e$. For the linear system $\dot{\vec{x}} = \mathbf{A}\vec{x}$ the equilibria solve $\mathbf{A}\vec{x}_e = \vec{0}$: the origin $\vec{x}_e = \vec{0}$ when $\mathbf{A}$ is nonsingular, or a whole subspace of equilibria when $\mathbf{A}$ is singular. (With a constant input, $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ has equilibria where $\mathbf{A}\vec{x}_e + \mathbf{B}\vec{u} = \vec{0}$.)

The **phase portrait** — trajectories plotted together in state space — shows how the state moves and whether it reaches the equilibrium. Near an equilibrium the behaviour is set by the eigenvalues of $\mathbf{A}$, i.e. the modes from the beginning of this chapter:

- **Node** — real eigenvalues of the same sign: the state moves straight along the eigenvectors, into (both negative) or away from (both positive) the equilibrium.
- **Saddle** — real eigenvalues of opposite signs: it approaches along one eigenvector and escapes along the other — always unstable.
- **Focus** (spiral) — complex pair $\sigma \pm j\omega$: it spirals into the equilibrium for $\sigma < 0$, away for $\sigma > 0$.
- **Center** — purely imaginary $\pm j\omega$: closed elliptical orbits; it neither settles nor escapes.

For the example system of the State-space chapter, $\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x}$ (eigenvalues $-1 \pm j\sqrt{2}$), the origin is the only equilibrium and a stable focus — every trajectory spirals into it:

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[
  width=0.62\linewidth, height=0.62\linewidth,
  xlabel={$x_1$}, ylabel={$x_2$},
  axis lines=center,
  axis line style={gray},
  label style={font=\small},
  xmin=-1.6, xmax=1.6, ymin=-1.6, ymax=1.6,
  xtick={-1,0,1}, ytick={-1,0,1},
  grid=major, grid style={gray!25},
]
\addplot[domain=0:8, samples=120, thick, blue]
  ({exp(-x)*(cos(deg(sqrt(2)*x)) + (1/sqrt(2))*sin(deg(sqrt(2)*x)))},
   {-(3/sqrt(2))*exp(-x)*sin(deg(sqrt(2)*x))});
\addplot[domain=0:8, samples=120, thick, blue]
  ({(1/sqrt(2))*exp(-x)*sin(deg(sqrt(2)*x))},
   {exp(-x)*(cos(deg(sqrt(2)*x)) - (1/sqrt(2))*sin(deg(sqrt(2)*x)))});
\addplot[domain=0:8, samples=120, thick, blue]
  ({-exp(-x)*(cos(deg(sqrt(2)*x)) + (1/sqrt(2))*sin(deg(sqrt(2)*x)))},
   {(3/sqrt(2))*exp(-x)*sin(deg(sqrt(2)*x))});
\addplot[domain=0:8, samples=120, thick, blue]
  ({-(1/sqrt(2))*exp(-x)*sin(deg(sqrt(2)*x))},
   {-exp(-x)*(cos(deg(sqrt(2)*x)) - (1/sqrt(2))*sin(deg(sqrt(2)*x)))});
\addplot[only marks, mark=*, mark size=2.5pt, red] coordinates {(0,0)};
\node[above right, font=\small] at (axis cs:0,0) {$\vec{x}_e$};
\end{axis}
\end{tikzpicture}
\end{center}
```

Whether trajectories actually end up at the equilibrium is exactly what the next section, Stability, formalizes.

## Stability

For $\dot{\vec{x}} = \mathbf{A}\vec{x}$ stability is decided by the eigenvalues of $\mathbf{A}$ — the poles — i.e. by where they sit relative to the imaginary axis. All plots below use the family $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -3 & a \end{bmatrix}$, whose poles are $\lambda = \frac{a \pm j\sqrt{12-a^2}}{2}$; the grey half-plane is the stable region, the dashed line its boundary.

### Asymptotically stable

$\operatorname{Re}\lambda_i < 0$ for all $i$: every mode decays, so from any initial condition the trajectory converges to the equilibrium $\vec{x}_e = \vec{0}$. All poles lie strictly inside the shaded left half-plane:

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[spane, width=0.42\linewidth, height=0.42\linewidth, title={asymptotically stable ($a=-2$)}]
\fill[gray!15] (axis cs:-3,-3) rectangle (axis cs:0,3);
\draw[dashed, thick] (axis cs:0,-3) -- (axis cs:0,3);
\addplot[only marks, mark=x, mark size=3pt, thick, red] coordinates {(-1,1.414) (-1,-1.414)};
\end{axis}
\end{tikzpicture}
\end{center}
```

### Stable (marginal / Lyapunov)

No eigenvalue with $\operatorname{Re}\lambda_i > 0$, and the eigenvalues on the imaginary axis are simple. Trajectories stay bounded (e.g. the center of the previous section — closed orbits) but need not converge. The poles sit exactly on the dashed boundary:

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[spane, width=0.42\linewidth, height=0.42\linewidth, title={stable, marginal ($a=0$)}]
\fill[gray!15] (axis cs:-3,-3) rectangle (axis cs:0,3);
\draw[dashed, thick] (axis cs:0,-3) -- (axis cs:0,3);
\addplot[only marks, mark=x, mark size=3pt, thick, red] coordinates {(0,1.732) (0,-1.732)};
\end{axis}
\end{tikzpicture}
\end{center}
```

### Unstable

Some eigenvalue with $\operatorname{Re}\lambda_i > 0$, or a repeated eigenvalue on the imaginary axis (which brings a factor $t$ and grows). Trajectories diverge; the poles lie in the right half-plane, outside the stable region:

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[spane, width=0.42\linewidth, height=0.42\linewidth, title={unstable ($a=+2$)}]
\fill[gray!15] (axis cs:-3,-3) rectangle (axis cs:0,3);
\draw[dashed, thick] (axis cs:0,-3) -- (axis cs:0,3);
\addplot[only marks, mark=x, mark size=3pt, thick, red] coordinates {(1,1.414) (1,-1.414)};
\end{axis}
\end{tikzpicture}
\end{center}
```

### What if the parameters change just a little?

The eigenvalues depend continuously on the entries of $\mathbf{A}$, so a small change moves each pole a little. The red circles below are the regions the poles can wander into under a small perturbation — a circle that stays inside the shaded half-plane means the stability is robust, one that straddles the dashed boundary means it is not:

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{axis}[spane, title={$a=-2$}]
\fill[gray!15] (axis cs:-3,-3) rectangle (axis cs:0,3);
\draw[dashed, thick] (axis cs:0,-3) -- (axis cs:0,3);
\addplot[domain=0:360, samples=60, red, thick] ({-1 + 0.5*cos(x)}, {1.414 + 0.5*sin(x)});
\addplot[domain=0:360, samples=60, red, thick] ({-1 + 0.5*cos(x)}, {-1.414 + 0.5*sin(x)});
\addplot[only marks, mark=x, mark size=3pt, red] coordinates {(-1,1.414) (-1,-1.414)};
\end{axis}
\end{tikzpicture}
\hspace{0.8em}
\begin{tikzpicture}
\begin{axis}[spane, title={$a=0$}]
\fill[gray!15] (axis cs:-3,-3) rectangle (axis cs:0,3);
\draw[dashed, thick] (axis cs:0,-3) -- (axis cs:0,3);
\addplot[domain=0:360, samples=60, red, thick] ({0.5*cos(x)}, {1.732 + 0.5*sin(x)});
\addplot[domain=0:360, samples=60, red, thick] ({0.5*cos(x)}, {-1.732 + 0.5*sin(x)});
\addplot[only marks, mark=x, mark size=3pt, red] coordinates {(0,1.732) (0,-1.732)};
\end{axis}
\end{tikzpicture}
\hspace{0.8em}
\begin{tikzpicture}
\begin{axis}[spane, title={$a=+2$}]
\fill[gray!15] (axis cs:-3,-3) rectangle (axis cs:0,3);
\draw[dashed, thick] (axis cs:0,-3) -- (axis cs:0,3);
\addplot[domain=0:360, samples=60, red, thick] ({1 + 0.5*cos(x)}, {1.414 + 0.5*sin(x)});
\addplot[domain=0:360, samples=60, red, thick] ({1 + 0.5*cos(x)}, {-1.414 + 0.5*sin(x)});
\addplot[only marks, mark=x, mark size=3pt, red] coordinates {(1,1.414) (1,-1.414)};
\end{axis}
\end{tikzpicture}
\end{center}
```

- **Asymptotic stability is robust**: the circles stay entirely inside the shaded left half-plane, so small perturbations keep the poles there (the margin is the distance from the boundary).
- **Marginal stability is not**: the circles straddle the dashed boundary, so a tiny change (here, $a$ crossing $0$) pushes the poles into one half-plane or the other — the system becomes asymptotically stable or unstable.
- **Instability is robust**: the circles stay in the right half-plane — pushing a pole back across the axis takes a finite change.

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

# Discrete systems

Sampled-time systems evolve in discrete steps rather than continuously. The continuous time $t$ is replaced by $kT$ — $T$ the fixed sampling period, $k$ the integer sample index — and the $T$ is usually dropped, writing $x[k] = x(kT)$.

## Difference equations

The discrete analogue of an ODE is a **difference equation**. It has two equivalent notations, using forward or backward shifts:

$$
y[k+1] + a_0 y[k] = b_0 u[k+1] + b_1 u[k], \qquad
y[k] + a_0 y[k-1] = b_0 u[k] + b_1 u[k-1]
$$

In general an $n$-th order difference equation reads

$$
y[k+n] + a_{n-1}y[k+n-1] + \cdots + a_0 y[k] = b_m u[k+m] + \cdots + b_0 u[k]
$$

and needs $n$ initial conditions (e.g. $y[0], \dots, y[n-1]$).

## Modeling examples

```{=latex}
\begin{example}[frametitle={Example - population migration}]
```

Each year, $a$ of the townspeople move to the suburbs and $b$ of the suburbanites move into the city:

$$
x_1[k+1] = (1-a)x_1[k] + b\,x_2[k], \qquad
x_2[k+1] = a\,x_1[k] + (1-b)x_2[k]
$$

In matrix form this is exactly the discrete state equation $\vec{x}[k+1] = \mathbf{A}\vec{x}[k]$ with

$$
\mathbf{A} = \begin{bmatrix} 1-a & b \\ a & 1-b \end{bmatrix}
$$

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - Samuelson's national income model}]
```

National income $y$, consumption $c$, investment $i$ and government spending $g$ satisfy $y[k] = c[k] + i[k] + g[k]$ with $c[k] = \alpha\,y[k-1]$ and $i[k] = \beta(c[k] - c[k-1])$. Substituting gives the second-order difference equation

$$
y[k] - \alpha(1+\beta)\,y[k-1] + \alpha\beta\, y[k-2] = g[k]
$$

with the government spending as input, and the income of the two previous periods as initial conditions.

```{=latex}
\end{example}
```

## Z-transform

The $z$-transform maps a sequence into a function of $z$:

$$
X(z) = \mathcal{Z}\{x[k]\} = \sum_{k=0}^{\infty} x[k]\, z^{-k}
$$

It turns shifts into algebra, exactly as the Laplace transform turns derivatives into algebra:

- **Linearity** — $\mathcal{Z}\{a x[k] + b y[k]\} = aX(z) + bY(z)$
- **Right shift (delay)** — $\mathcal{Z}\{x[k-1]\} = z^{-1}X(z)$
- **Left shift (advance)** — $\mathcal{Z}\{x[k+1]\} = z(X(z) - x[0])$
- **Convolution** — $\mathcal{Z}\{(x * y)[k]\} = X(z)Y(z)$, with $(x*y)[k] = \sum_i x[i]\,y[k-i]$

A few common pairs (inverse transform works by partial fractions, as with Laplace):

$$
\delta[k] \leftrightarrow 1, \qquad
u[k] \leftrightarrow \frac{z}{z-1}, \qquad
a^k \leftrightarrow \frac{z}{z-a}, \qquad
k \leftrightarrow \frac{z}{(z-1)^2}
$$

## From a difference equation to state space

As for ODEs, an $n$-th order difference equation becomes a first-order vector equation — the discrete state space $\vec{x}[k+1] = \mathbf{A}\vec{x}[k] + \mathbf{B}\vec{u}[k]$, $\vec{y}[k] = \mathbf{C}\vec{x}[k] + \mathbf{D}\vec{u}[k]$ — by stacking the delayed outputs. For $y[k+2] + a_1 y[k+1] + a_0 y[k] = b_0 u[k]$ take $x_1[k] = y[k]$, $x_2[k] = y[k+1]$:

$$
\vec{x}[k+1] = \begin{bmatrix} 0 & 1 \\ -a_0 & -a_1 \end{bmatrix}\vec{x}[k] + \begin{bmatrix} 0 \\ b_0 \end{bmatrix}u[k]
$$

the discrete companion form, the exact analogue of the continuous one.

## Discretizing continuous systems

Given $\dot{\vec{x}} = \mathbf{A}_c\vec{x} + \mathbf{B}_c\vec{u}$ and the sampling period $T$:

- **Exact (zero-order hold)** — keep $u$ constant between samples and integrate the continuous solution from $kT$ to $(k+1)T$:

$$
\mathbf{A} = e^{\mathbf{A}_c T}, \qquad
\mathbf{B} = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau\, \mathbf{B}_c
$$

  the continuous poles map as $z_i = e^{s_i T}$, and the approximation improves as $T$ shrinks.

- **Euler** — first-order approximation $\mathbf{A} \approx \mathbf{I} + \mathbf{A}_c T$, $\mathbf{B} \approx \mathbf{B}_c T$: simpler, but less accurate for the same $T$.

```{=latex}
\begin{example}[frametitle={Example - discretizing for $T = 0.1$ s}]
```

$\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u$ with $T = 0.1$ (eigenvalues $-1 \pm j\sqrt{2}$, so $z = e^{(-1\pm j\sqrt2)\cdot 0.1} = 0.9048\, e^{\pm j\,0.1414}$):

$$
\mathbf{A} = e^{\mathbf{A}_c T} \approx \begin{bmatrix} 0.986 & 0.090 \\ -0.271 & 0.806 \end{bmatrix}, \qquad
\mathbf{B} = \int_0^T e^{\mathbf{A}_c \tau}\, d\tau\, \mathbf{B}_c \approx \begin{bmatrix} 0.019 \\ 0.361 \end{bmatrix}
$$

```{=latex}
\end{example}
```

## Solving the state equations

- **Homogeneous** — $\vec{x}[k] = \mathbf{A}^k\vec{x}[0]$; $\mathbf{A}^k$ is the **discrete state-transition matrix**, mapping the initial state to the state at step $k$.
- **Nonhomogeneous** —

$$
\vec{x}[k] = \mathbf{A}^k\vec{x}[0] + \sum_{i=0}^{k-1} \mathbf{A}^{k-1-i}\mathbf{B}\vec{u}[i]
$$

  the sum being a discrete convolution.

## Obtaining the discrete state-transition matrix $\mathbf{A}^k$

Exactly the same four ways as for $e^{\mathbf{A}t}$, with $\lambda_i^k$ in place of $e^{\lambda_i t}$:

- **Z-transform** — $\mathbf{A}^k = \mathcal{Z}^{-1}\{z(z\mathbf{I}-\mathbf{A})^{-1}\}$.
- **Diagonalization** — $\mathbf{A}^k = \mathbf{V}\boldsymbol{\Lambda}^k\mathbf{V}^{-1}$, with $\boldsymbol{\Lambda}^k$ diagonal (entries $\lambda_i^k$); only if $\mathbf{A}$ is diagonalizable.
- **Cayley–Hamilton** — $\mathbf{A}^k = \alpha_0(k)\mathbf{I} + \cdots + \alpha_{n-1}(k)\mathbf{A}^{n-1}$, the $\alpha_i$ following from $\lambda_i^k = \alpha_0 + \alpha_1\lambda_i + \cdots$ (differentiate for repeated eigenvalues); works even for defective matrices.

## Transfer function

From the discrete state equations with zero initial conditions,

$$
\mathbf{H}(z) = \mathbf{C}(z\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$$

the same rational-function picture as in the Transfer functions chapter, with the unit circle as the stability boundary. Block algebra (series, parallel, feedback) is identical.

## Equilibrium, stability, controllability, observability

Everything mirrors the continuous case:

- **Equilibrium** — with $u[k] = 0$, a linear discrete system has the single equilibrium at the origin $\vec{x}_e = \vec{0}$; the equilibrium types are the same as for continuous systems.
- **Stability** — the modes are $\lambda_i^k$, so the boundary is the **unit circle**: asymptotically stable if $|\lambda_i| < 1$ for all $i$; marginal if $|\lambda_i| \le 1$ with unit-circle eigenvalues simple; unstable if some $|\lambda_i| > 1$ or a repeated unit-circle eigenvalue.
- **Controllability** — the same controllability matrix $\mathcal{C} = [\mathbf{B}\ \mathbf{A}\mathbf{B}\ \cdots\ \mathbf{A}^{n-1}\mathbf{B}]$ and rank test as for continuous systems.
- **Observability** — the same observability matrix $\mathcal{O}$ and rank test as for continuous systems.

# Appendix A: Math review

## Linear algebra

### Matrix multiplication

Two matrices can be multiplied only when the number of columns of the left one equals the number of rows of the right one. If $\mathbf{A}$ is $m \times n$ and $\mathbf{B}$ is $n \times p$, then $\mathbf{C} = \mathbf{A}\mathbf{B}$ is $m \times p$ with entries

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj},
$$

i.e. entry $(i,j)$ is the dot product of row $i$ of $\mathbf{A}$ with column $j$ of $\mathbf{B}$.

```{=latex}
\begin{example}[frametitle={Example - 2×3 times 3×2}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}$. Since $\mathbf{A}$ is $2\times3$ and $\mathbf{B}$ is $3\times2$, the product is $2\times2$:

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}
$$

Entry by entry (just one to illustrate):

$$
c_{11} = 1\cdot7 + 2\cdot9 + 3\cdot11 = 58
$$

hence

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 58 & 64 \\ 139 & 154 \end{bmatrix}.
$$

Note the order matters: $\mathbf{B}\mathbf{A}$ is $3\times3$, so it cannot equal the $2\times2$ $\mathbf{A}\mathbf{B}$. Matrix multiplication is **not** commutative.

```{=latex}
\end{example}
```

### Matrix determinant

The determinant is a single number attached to a square matrix. It decides invertibility ($\det\mathbf{A} \ne 0$) and, geometrically, how much the matrix scales volumes.

For a $2\times2$ matrix:

$$
\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc
$$

For $n\times n$, expand along a row or column (Laplace expansion); signs alternate $+,-,+,\dots$. For $3\times3$ along the first row:

$$
\det\begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}
= a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix}
- a_{12}\begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix}
+ a_{13}\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}
$$

$\det\mathbf{A} = 0$ means the rows (or columns) are linearly dependent — the matrix crushes a volume to zero.

Also useful later: $\det(\mathbf{A}\mathbf{B}) = \det\mathbf{A}\,\det\mathbf{B}$ and $\det(\mathbf{A}^{-1}) = 1/\det\mathbf{A}$.

### Inverse of a matrix

The inverse $\mathbf{A}^{-1}$ is the matrix with $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. Two standard ways to compute it.

#### Existence of inverse

A square matrix is invertible (nonsingular) iff $\det\mathbf{A} \ne 0$.

```{=latex}
\begin{example}[frametitle={Example - for which $a$ is the matrix invertible?}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 4 & a \end{bmatrix}$.

$$
\det\mathbf{A} = 1\cdot(3a - 16) - 2\cdot(2a - 12) + 3\cdot(8 - 9) = 5 - a
$$

so $\mathbf{A}$ is invertible exactly for $a \ne 5$. At $a = 5$ the third row is a linear combination of the first two: $[3\ 4\ 5] = -[1\ 2\ 3] + 2[2\ 3\ 4]$.

```{=latex}
\end{example}
```

#### Gauss elimination

Row-reduce the augmented matrix $[\mathbf{A} \mid \mathbf{I}]$ until the left block is $\mathbf{I}$; the right block is then $\mathbf{A}^{-1}$.

```{=latex}
\begin{example}[frametitle={Example - inverse via Gauss elimination}]
```

$\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix}$. Augment and reduce:

$$
\left[\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 5 & 3 & 0 & 1 \end{array}\right]
\xrightarrow{R_1/2}
\left[\begin{array}{cc|cc} 1 & \frac12 & \frac12 & 0 \\ 5 & 3 & 0 & 1 \end{array}\right]
$$

$$
\xrightarrow{R_2 - 5R_1}
\left[\begin{array}{cc|cc} 1 & \frac12 & \frac12 & 0 \\ 0 & \frac12 & -\frac52 & 1 \end{array}\right]
\xrightarrow{2R_2}
\left[\begin{array}{cc|cc} 1 & \frac12 & \frac12 & 0 \\ 0 & 1 & -5 & 2 \end{array}\right]
$$

$$
\xrightarrow{R_1 - \frac12 R_2}
\left[\begin{array}{cc|cc} 1 & 0 & 3 & -1 \\ 0 & 1 & -5 & 2 \end{array}\right]
\quad\Longrightarrow\quad
\mathbf{A}^{-1} = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}
$$

```{=latex}
\end{example}
```

#### With cofactors

The adjugate formula

$$
\mathbf{A}^{-1} = \frac{1}{\det\mathbf{A}}\operatorname{adj}\mathbf{A},
$$

where $\operatorname{adj}\mathbf{A}$ is the transpose of the matrix of cofactors. For $2\times2$ this collapses to the famous formula

$$
\mathbf{A}^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}.
$$

Applying it to the same $\mathbf{A}$ above ($ad - bc = 1$):

$$
\mathbf{A}^{-1} = \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix},
$$

which matches the Gauss result.

### System of equations and rank

The rank $r = \operatorname{rank}\mathbf{A}$ is the number of linearly independent rows (or columns). Vectors are linearly independent when none of them is a linear combination of the others. For a system $\mathbf{A}\vec{x} = \vec{b}$ with $n$ unknowns:

- **No solution** if $\operatorname{rank}[\mathbf{A}\mid\vec{b}] > \operatorname{rank}\mathbf{A}$ (inconsistent).
- **Exactly one solution** if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] = n$.
- **Infinitely many solutions** if $\operatorname{rank}\mathbf{A} = \operatorname{rank}[\mathbf{A}\mid\vec{b}] < n$; then there are $n - r$ free variables.

The homogeneous system $\mathbf{A}\vec{x} = \vec{0}$ always has the trivial solution $\vec{x} = \vec{0}$, and has nontrivial ones exactly when $\operatorname{rank}\mathbf{A} < n$, i.e. when $\mathbf{A}$ is singular ($\det\mathbf{A} = 0$). That is the exact condition behind the eigenvalue problem below.

### Eigenvalues and eigenvectors

A common use for matrices is to describe linear transformations. A transformation $\vec{x}  \mapsto \mathbf{A}\vec{x}$ can stretch, shrink, rotate, or reflect vectors. Eigenvectors are the special directions that are only stretched or shrunk, not rotated.

A nonzero vector $\vec{x}$ is an eigenvector of $\mathbf{A}$ if multiplying by $\mathbf{A}$ just scales it:

$$
\mathbf{A}\vec{x} = \lambda\vec{x}
$$

The scalar $\lambda$ is the eigenvalue. Rearranging gives $(\mathbf{A} - \lambda\mathbf{I})\vec{x} = \vec{0}$, which has a nontrivial solution iff $\mathbf{A} - \lambda\mathbf{I}$ is singular (square, not invertable). Hence the eigenvalues are the roots of the characteristic polynomial

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

```{=latex}
\begin{example}[frametitle={Example - eigenvalues and eigenvectors}]
```

$\mathbf{A} = \begin{bmatrix} 1 & 0 & -1 \\ 1 & 2 & 1 \\ 2 & 2 & 3 \end{bmatrix}$. The characteristic polynomial:

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 1-\lambda & 0 & -1 \\ 1 & 2-\lambda & 1 \\ 2 & 2 & 3-\lambda \end{vmatrix} = (1-\lambda)(\lambda-2)(\lambda-3)
$$

so $\lambda_1 = 1$, $\lambda_2 = 2$, $\lambda_3 = 3$ — all distinct, hence $\mathbf{A}$ is diagonalizable.

For $\lambda = 1$, solve $(\mathbf{A} - \mathbf{I})\vec{x} = \vec{0}$:

$$
\begin{bmatrix} 0 & 0 & -1 \\ 1 & 1 & 1 \\ 2 & 2 & 2 \end{bmatrix}\vec{x} = \vec{0}
\quad\Longrightarrow\quad
x_3 = 0,\ x_1 + x_2 = 0
\quad\Longrightarrow\quad
\vec{x}_1 = \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}
$$

For $\lambda = 2$: $(\mathbf{A} - 2\mathbf{I})\vec{x} = \vec{0}$:

$$
\begin{bmatrix} -1 & 0 & -1 \\ 1 & 0 & 1 \\ 2 & 2 & 1 \end{bmatrix}\vec{x} = \vec{0}
\quad\Longrightarrow\quad
x_3 = -x_1,\ x_1 = -2x_2
\quad\Longrightarrow\quad
\vec{x}_2 = \begin{bmatrix} -2 \\ 1 \\ 2 \end{bmatrix}
$$

For $\lambda = 3$: $(\mathbf{A} - 3\mathbf{I})\vec{x} = \vec{0}$:

$$
\begin{bmatrix} -2 & 0 & -1 \\ 1 & -1 & 1 \\ 2 & 2 & 0 \end{bmatrix}\vec{x} = \vec{0}
\quad\Longrightarrow\quad
x_3 = -2x_1,\ x_2 = -x_1
\quad\Longrightarrow\quad
\vec{x}_3 = \begin{bmatrix} 1 \\ -1 \\ -2 \end{bmatrix}
$$

Sanity check: $\mathbf{A}\vec{x}_1 = \vec{x}_1$, $\mathbf{A}\vec{x}_2 = 2\vec{x}_2$, $\mathbf{A}\vec{x}_3 = 3\vec{x}_3$.

```{=latex}
\end{example}
```

This is the exact machinery used later to obtain the state-transition matrix $\Phi(t) = e^{\mathbf{A}t}$ via diagonalization.

## Continuous-time math

### ODE

A linear ODE is one whose left-hand side is a linear operator $L$. Linearity is two properties bundled together:

- **Additivity**: $L[y_1 + y_2] = L[y_1] + L[y_2]$
- **Homogeneity**: $L[cy] = c\,L[y]$

Together, $L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2]$. The key consequence is **superposition**: if $y_1, y_2$ solve the homogeneous equation $L[y] = 0$, so does any linear combination $c_1 y_1 + c_2 y_2$. For example, $L[y] = \ddot{y} + 2\dot{y} + y$ is linear, whereas $L[y] = \dot{y}^2$ is not.

**Time invariance** means the system does not care when we start the clock: if $x(t)$ is the response to input $u(t)$, then $x(t - \tau)$ is the response to $u(t - \tau)$.

The state-space equation $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$ is a linear, time-invariant (LTI) system — these two properties are exactly what let us use the Laplace transform and the matrix exponential below.

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

- **Distinct linear factors** $(s-a)(s-b)$: $\ \dfrac{A}{s-a} + \dfrac{B}{s-b}$
- **Repeated factors** $(s-a)^2$: $\ \dfrac{A}{s-a} + \dfrac{B}{(s-a)^2}$
- **Irreducible quadratic** $s^2 + \omega^2$: $\ \dfrac{As + B}{s^2 + \omega^2}$ ($\to$ sines and cosines)

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

```{=latex}
\end{example}
```



