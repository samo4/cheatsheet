# 1. exercise

We have electric circuit on the schematic below.

```{=latex}
\input{tikz/kolokvij-2023-circuit.tex}
```

a. Find state-space equations of the circuit in the form $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, where $\vec{x} = [i_L, v_C]^T$ and $\vec{u} = [i_g, v_g]^T$.
b. Find the matrix equation for response $\vec{y} = [ v_{R2}, v]^T$.

## Part a. (ground at the bottom rail)

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

# 2. exercise

Partially elastic crash of an object to the wall is modeled with a spring and a damper as shown in the figure. Crash starts at $x=0$.

```{=latex}
\input{tikz/kolokvij-2023-crash.tex}
```

a. Model the crash with state equations in the form $\dot{\vec{x}} = \mathbf{A}\vec{x}$, where $\vec{x} = [x, v]^T$
b. Write the response equation in the form of $y = \mathbf{C}\vec{x}$, where $y$ is the entire external force acting on the object $y(t) = F(t)$.
c. With Laplace transformation find the solution of the system $\vec{x}(t)$ for parameters m=5kg, k=20N/m, b=25Ns/m and initial speed of v(0) = -10m/s
d. What's the maximum force $F_{\max}$ acting on the object during the crash?

## Part a.

With $x$ positive away from the wall, the buffer pushes back with $F = -kx - bv$, so $m\ddot{x} + b\dot{x} + kx = 0$. With states $x_1 = x$, $x_2 = v = \dot{x}$:

$$\dot{x}_1 = x_2, \qquad \dot{x}_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2$$

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x}, \qquad \vec{x}(0) = \begin{bmatrix} 0 \\ -10 \end{bmatrix}
$$

## Part b.

The external (buffer) force on the object is spring plus damper:

$$y = F(t) = -kx - bv = \begin{bmatrix} -k & -b \end{bmatrix}\vec{x}$$

$$\mathbf{C} = \begin{bmatrix} -k & -b \end{bmatrix}$$

## Part c.

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

## Part d.

From solution in part b, the force is $F(t) = -kx - bv = -20x - 25v$. At impact $t=0$ the spring is uncompressed $x=0$ and the speed is maximal $v(0) = -10$, so the force is maximal:

$$F(0) = -b\,v(0) = 25 \cdot 10 = 250\ \text{N}$$

**Alternative — the full $F(t)$ route** Plug the solutions from part c into $F(t) = -kx_1 - bx_2 = -20x_1 - 25x_2$:

$$F(t) = -20\cdot\frac{10}{3}\left(e^{-4t} - e^{-t}\right) - 25\cdot\frac{10}{3}\left(e^{-t} - 4e^{-4t}\right) = \frac{800}{3}e^{-4t} - \frac{50}{3}e^{-t}$$

Differentiate and set to zero:

$$F'(t) = -\frac{3200}{3}e^{-4t} + \frac{50}{3}e^{-t} = 0 \quad\Longrightarrow\quad 64e^{-4t} = e^{-t} \quad\Longrightarrow\quad e^{3t} = 64 \quad\Longrightarrow\quad t = \ln 4$$

Evaluate the stationary point against the impact instant:

$$F(0) = 250\ \text{N}, \qquad F(\ln 4) = \frac{800}{3}\cdot\frac{1}{256} - \frac{50}{3}\cdot\frac{1}{4} = -\frac{25}{8}\ \text{N}$$

The impact instant is the maximum (the stationary point is a minimum during the rebound), so $F_{\max} = 250$ N at $t=0$ — same conclusion, more work.
