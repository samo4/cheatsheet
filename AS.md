---
title: "AS notes"
author: "Samo F."
header-includes:
  - |
    \usepackage[leftline,framemethod=TikZ]{mdframed}
    \usepackage{circuitikz}
---

# Example of state-space modeling

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

Next, we write down the equations for the energy-storing elements using their constitutive relations. Note that $i_L$ is chosen from $V_2$ to $V_3$ (arbitrary but fixed). Lenz’s law is not ignored; its effect was already built into the sign of the inductor’s voltage when we adopted PSC. Faraday’s law gives $v = L\,\dot{i}$ for the chosen polarity (voltage drop in the direction of the reference current). If you had defined the voltage polarity opposite to the current reference, the relation would appear as $v = -L\,\dot{i}$. Thus no extra minus is added later - the orientation choices at the start encode it.

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
