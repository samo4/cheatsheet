# Modeling

A model turns a physical system into a set of equations that predicts how it behaves. This chapter is the first step in the chain **modeling → analysis → control**.

In every domain a system is built from the same three kinds of ideal elements:

- **Sources** deliver energy into the system — a voltage source, a force.
- **Storage** elements hold energy and release it on their own time scale — a capacitor or inductor, a spring or mass.
- **Dissipation** converts energy into heat — a resistor, a damper.

Storage is what makes a system *dynamic*. A storage element cannot change its energy instantly: it accumulates input over time, so the system keeps reacting after the input is gone — sometimes slowly, sometimes violently. That behaviour is captured by differential equations. Each storage element contributes one state, so the number of states equals the number of storage elements.

The same three elements appear in every domain — electrical, mechanical, hydraulic, thermal — and in non-physical systems such as biological populations or economic ones. This chapter turns the resulting differential equations into the common state-space form $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, so that one set of tools works everywhere.

Given the state and the input, such a model predicts the behaviour for all future time — but only under two assumptions that real systems violate:

- **Time invariance** — the parameters must not change with time. A rocket burning fuel loses mass, so its equations change as it flies.
- **Linearity** — the dynamics must be linear, and essentially no real system is. Even the ultimate physical limit — the speed of light — forces nonlinear equations.

This book therefore works with **linear time-invariant (LTI)** systems, not only because the math is elegant, but because LTI theory is the foundation that extends to the harder cases.

Even so, this is an idealization. The framework silently assumes the system is **lumped** — a finite number of states, so no partial differential equations (heat, flexible structures, fluids) and no transport delays — and **deterministic**, so no noise. Linearity itself also erases phenomena that no amount of linearization can recover: multiple equilibria, hysteresis, saturation, chaos. The Linearization chapter pushes back on some of this, and the Discrete chapter on sampled time; distributed, delayed, and stochastic systems remain out of reach — there a linear finite-dimensional model is at best a local approximation.

The correct title of this chapter should then be "LTI lumped deterministic modeling" — but who wants that?

Building a model is not always a paper exercise — it often needs data. A car suspension model, for instance, needs the spring rate, damping, and mass. That is not a dead end: given a good model structure, the parameters can be fitted to measurements of the real system. This is *system identification*, the often-forgotten counterpart of modeling.

## Higher-order ODEs as first-order systems

State-space form only contains first derivatives, so a higher-order ODE must first be rewritten as a system. The trick is to promote the lower-order derivatives to state variables. Formally we would write something like this:

$$
\dot{x}_n = f_n(x_1, x_2, \dots, x_n, u), \qquad
\dot{x}_{n-1} = x_n, \qquad
\dot{x}_{n-2} = x_{n-1}, \qquad
\dots, \qquad
\dot{x}_1 = x_2
$$

But just looking the the example it's easer: take the second-order ODE

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
\begin{bmatrix} \dot{x_1} \\ \dot{x_2} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u, \qquad
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

The number of states equals the order of the ODE — the same "one state per energy-storing element" count as in the electrical circuit below.

## Modeling mechanical systems

You already know Newton's laws — modeling does not re-teach physics, it only *upgrades* what you know into the state-space format. The three laws: 1. Inertia 2. Force and Acceleration 3. Action and Reaction.

Everything genuinely new about mechanical modeling is *directional bookkeeping*: assemble the forces with the correct signs and the equations write themselves.

### Translational systems

The three ideal elements are:

- *Spring* — $F = k(x_2 - x_1)$: stores energy.
- *Damper* — $F = b(\dot{x}_2 - \dot{x}_1)$: dissipates energy.
- *Mass* — $F = ma$: stores kinetic energy.

Plus, to complete the list at the top, a *source* of energy: a force $F(t)$ or a prescribed motion $x(t)$.

**Recipe — getting the directions right.** All the sign trouble lives in the spring and damper formulas, so read them as *"force on point 1 in the positive direction, caused by the relative displacement $x_2 - x_1$."* An element always opposes relative motion: the spring resists being stretched, the damper resists moving apart. Never hand-place a minus — write the difference $(x_2 - x_1)$ and let the formula assign the sign.

1. Pick a positive direction for $x$ once (say up) and keep it for *every* element and for $ma$. Draw the free-body diagram in that frame.
2. For each spring/damper between points 1 and 2, use $F = k(x_2 - x_1)$ or $F = b(\dot{x}_2 - \dot{x}_1)$ — the relative difference carries the sign.
3. Newton: $\sum F = ma$. Add element forces with the sign from their formulas; add external forces with the sign they have in the diagram.
4. Measure $x$ from the static equilibrium (where the spring already holds the weight), so the constant $mg$ never appears.
5. Sanity-check at rest: with $\ddot{x} = 0$ and $\dot{x} = 0$ the spring must hold exactly the static load. If it does not, a sign is flipped.

```{=latex}
\begin{example}[frametitle={Example - car wheel on its suspension}]
```

```{=latex}
\input{tikz/modeling-wheel.tex}
```

A car body of mass $m$ rests on its suspension — spring $k$ and damper $b$ in parallel — on the ground. Gravity pulls it down with the weight $mg$, our input. We want the body's vertical motion $x(t)$ and its state-space model.

**Step 1 — states.** The natural states are position and velocity:

$$x_1 = x \quad \text{(vertical position)}, \qquad x_2 = \dot{x} \quad \text{(vertical velocity)}.$$

**Step 2 — forces with the correct signs.** Take positive $x$ upward. The suspension connects the body (at $x$) to the ground (at $0$), so the spring stretch and the damper velocity are just $x$ and $\dot{x}$.

- **Spring** opposes stretch. If the body moves up ($x > 0$) the spring is extended and pulls it *down*, hence $F_k = -kx$.
- **Damper** opposes velocity. If the body moves up ($\dot{x} > 0$) the damper pushes it down, hence $F_b = -b\dot{x}$.
- **Gravity** always pulls down, hence $F_g = -mg$.

*Sanity check:* at rest ($\ddot{x} = \dot{x} = 0$) Newton gives $kx = -mg$, i.e. the spring pushes up with exactly the weight — a flipped sign here would make the body float away.

**Step 3 — Newton's 2$^\text{nd}$ law.** $\sum F = ma$:

$$m\ddot{x} = F_k + F_b + F_g = -kx - b\dot{x} - mg,$$

rearranged into the familiar second-order ODE

$$m\ddot{x} + b\dot{x} + kx = -mg.$$

**Step 4 — reduce to first order** With the states of Step 1:

$$\dot{x}_1 = x_2, \qquad \dot{x}_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2 - g.$$

**Step 5 — matrix form.** With the input $u = mg$ (the weight):

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ -\frac{1}{m} \end{bmatrix} u.
$$

**Physical meaning of the states.** $x_1$ is the body's vertical position, $x_2$ its vertical velocity. The $\mathbf{A}$ matrix is the same companion form as the higher-order ODE example: one state per derivative. The constant input does not change the dynamics — it only sets the equilibrium (the static deflection of Step 2); measure $x$ from that equilibrium and $mg$ drops out entirely.

```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Example - crash buffer (no input)}]
```

A car of mass $m$ moving at speed $v_0$ hits a rigid barrier cushioned by a spring $k$ and damper $b$ in parallel. Take $x$ as the *compression* of the buffer, positive into the barrier. The motion now resists itself: the spring pushes back ($F_k = -kx$), the damper pushes back harder the faster the car is still moving ($F_b = -b\dot{x}$):

$$m\ddot{x} = -kx - b\dot{x}, \qquad m\ddot{x} + b\dot{x} + kx = 0.$$

With states $x_1 = x$, $x_2 = \dot{x}$ this is the same $\mathbf{A}$ with no input:

$$\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x}.$$

**Physical meaning.** $x_1$ = how deep the car has penetrated the buffer, $x_2$ = how fast it is still going. The damper turns the kinetic energy $\tfrac{1}{2}mv_0^2$ into heat — that is what makes the crash *cushioned*; without the damper the car would bounce back at nearly full speed.

```{=latex}
\end{example}
```

**Real forces you will meet.** Friction comes as a stick–slip pair: static (stiction) while at rest, $F \le \mu_s N$, kinetic once moving, $F = \mu_k N$; both oppose motion, so their sign is $-\operatorname{sign}(\dot{x})$. Rolling resistance is roughly constant, $F = c_r N$. Air drag is viscous at low speed, $F = c_v \dot{x}$, and quadratic at high speed, $F = \tfrac{1}{2}\rho C_d A \dot{x}^2$ — the Reynolds number decides which regime applies.

### Rotational systems

The same equations with $x \to \theta$, $v \to \omega$, $F \to \tau$, $m \to J$: torque $\tau = J\alpha$, torsional spring $\tau = k(\theta_2 - \theta_1)$, rotational damper $\tau = b(\omega_2 - \omega_1)$. Gears and transmissions just scale torque and angular speed by the gear ratio.

## State-space modeling of electrical circuits

For this example we want to write down the state-space equations of the circuit in matrix form
$\dot{\vec{x}} = \mathbf{A} \vec{x} + \mathbf{B} \vec{u}$ and $\vec{y} = \mathbf{C} \vec{x} + \mathbf{D} \vec{u}$,
where $\vec{x} = \begin{bmatrix} i_L \\ v_C \end{bmatrix}$ and $\vec{u} = \begin{bmatrix} v_g \end{bmatrix}$ and $\vec{y} = \begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix}$.

```{=latex}
\input{tikz/modeling-circuit.tex}
```

Let's select one node as ground. Although any node can be ground, we try to choose it in a way that will make the resulting equation as easy as possible. Generally, pick the node with the most element connections to reduce the number of unknown node voltages. In our case, we can select the bottom node as ground.\footnote{In simulation software (e.g., SPICE), the ground node choice can influence numerical stability, but picking the one with most connections is a still good rule of thumb.}

Then we proceed to mark the remaining nodes.

Passive sign convention (PSC) defines an element’s voltage positive at the terminal where the reference current enters; then power is positive when the element absorbs energy. For voltage source, according to PSC, we must mark the reference current in such a way that current entering the element will absorb power and when leaving (minus sign) give power to the rest of the circuit. That means that arrow should point into the + of voltage source. For capacitor we have defined polarity: we apply the PSC convention to $i_C$ (arrow into +). And for the inductor we have defined the current $i_L$. Although $v_L$ is not required here, we could define its polarity according to PSC as well ($V_2$ is positive in relation to $V_3$).

```{=latex}
\input{tikz/modeling-circuit-nodes.tex}
```

Common approaches for deriving state-space equations include node-voltage and mesh-current methods. Here we apply a combination of both. It might be described as node-voltage formulation with selected element state variables.

First we observe the $V_1 = v_g$ and $v_C = V_3$.

We write down the equations for each node using Kirchhoff's current law. When expressing currents through resistors, we start with the current node voltage (so currents are taken as leaving the node: plus sign in our equations).

$$\frac{V_1 - V_2}{R_1} + i_g = 0$$

When node is connected to an inductor, we express the current through the inductor as a state variable. Note that the direction of current for $i_L$ is defined as flowing out of $V_2$. For $V_2$ we get:

$$\frac{V_2 - V_1}{R_1} + i_L = 0$$

And the same for capacitors: we express the current through the capacitor as a state variable. For the capacitor we take its voltage $v_C$ as the state variable (more standard); current follows $i_C = C\,\dot{v}_C$ under PSC.

Next, we write down the equations for the energy-storing elements using their constitutive relations. Note that $i_L$ is chosen from $V_2$ to $V_3$. Lenz’s law is not ignored; its effect was already built into the sign of the inductor’s voltage when we adopted PSC. Faraday’s law gives $v = L\,\dot{i}$ for the chosen polarity (voltage drop in the direction of the reference current). If you had defined the voltage polarity opposite to the current reference, the relation would appear as $v = -L\,\dot{i}$. Thus no extra minus is added later - the orientation choices at the start encode it.

$$ v_L = L \frac{di_L}{dt} = V_2 - V_3 $$

And for the capacitor:

$$ i_C = C \frac{dv_C}{dt} = i_L - \frac{V_3}{R_2} $$

Since $V_1 = v_g$ and $v_C = V_3$ we get the state-space form

$$
\frac{d}{dt}\begin{bmatrix} i_L \\ v_C \end{bmatrix} =
\begin{bmatrix}
-\frac{R_1}{L} & -\frac{1}{L} \\
\frac{1}{C} & -\frac{1}{C R_2}
\end{bmatrix}
\begin{bmatrix} i_L \\ v_C \end{bmatrix} +
\begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix} v_g.
$$

If outputs are $v_{R_1}$ and $v_L$ then

$$
\begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix} =
\begin{bmatrix}
R_1 & 0 \\
L\,\frac{d}{dt} & 0
\end{bmatrix}
\begin{bmatrix} i_L \\ v_C \end{bmatrix} +
\begin{bmatrix} -1 \\ 0 \end{bmatrix} v_g,
$$

or equivalently using algebraic forms:
$v_{R_1}=R_1 i_L - v_g$, $v_L = L\,\dfrac{di_L}{dt}$.


```{=latex}
\begin{example}[frametitle={Fully worked out example - getting state-space equations from a circuit }]
```

```{=latex}
\input{tikz/example-circuit.tex}
```

For the circuit above, we want to write down the state-space equations  in the form $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$, where the state vector $\vec{x} = [i_L, v_C]^T$ and $\vec{u} = [v_g, i_g]^T$.

**Step 1** Decide on nodes.

```{=latex}
\input{tikz/example-circuit-nodes.tex}
```

**Step 2** Node and element equations. From the annotated circuit above we write the equations.

Node–$V_1$: $\; i_{g'} + \dfrac{V_1 - V_2}{R_1} = 0$

Node–$V_2$: $\; i_C + \dfrac{V_2 - V_1}{R_1} - i_g + \dfrac{V_2 - V_3}{R_2} = 0$

Node–$V_3$: $\; -i_C + \dfrac{V_3 - V_2}{R_2} + i_g - i_L = 0$

Capacitor: $\; i_C = C\dot{v}_C, \quad v_C = V_2 - V_3$

Inductor: $\; v_L = L\dot{i}_L, \quad v_L = -V_3$

And we note that $V_1 = v_g$ and $i_{g'} = i_L$ (the current through the source $v_g$ equals the inductor current). 

Instead of trying to rearrange the node equations from the start, start with the equations that already contain the derivatives — the constitutive relations of the two energy-storing elements, $i_C = C\dot{v}_C$ and $v_L = L\dot{i}_L$. They give the state derivatives directly; the node equations are only used to fill in whatever current or voltage they still need.

**Step 4 — Capacitor** What we need is: **$\dot{v}_C$** expressed as a function of the states and the inputs.

To get it from $i_C = C\dot{v}_C$ we need the capacitor current $i_C$:

$i_C$ appears in both the node-$V_2$ and node-$V_3$ equations — the capacitor sits between $V_2$ and $V_3$, so its current shows up in both. Either one works; the node-$V_3$ equation is the quicker pick because all its other terms are already known: $V_3 - V_2 = -v_C$ (a state), $i_g$ (an input) and $i_L$ (a state). (The node-$V_2$ equation also contains $\frac{V_2 - V_1}{R_1} = i_{g'}$, which we'd have to swap for $i_L$ first.) Solve it for $i_C$:

$$i_C = \frac{V_3 - V_2}{R_2} + i_g - i_L = -\frac{v_C}{R_2} + i_g - i_L$$

Insert the capacitor equation $i_C = C\dot{v}_C$:

$$C\,\dot{v}_C = - \frac{v_C}{R_2} + i_g - i_L
\quad\Longrightarrow\quad
\dot{v}_C = -\frac{1}{C}\,i_L - \frac{1}{CR_2}\,v_C + \frac{1}{C}\,i_g$$

**Step 5 — Inductor** What we need is: **$\dot{i}_L$**.

From $v_L = L\dot{i}_L$ we need $v_L$, and the inductor relation already tells us $v_L = -V_3$ — so we need the node voltage $V_3$.

How to get $V_3$? The capacitor relation $v_C = V_2 - V_3$ gives $V_3 = V_2 - v_C$, and $v_C$ is a state we already have. So it remains to find $V_2$:

The node-$V_1$ equation is the best bet — it contains $V_2$ together with only known quantities: $V_1 = v_g$ (an input) and $i_{g'}$ (which we showed equals the state $i_L$). (The node-$V_2$ equation could work too, but it also drags in $i_C$ — and hence $\dot{v}_C$ — so it is messier.) With $i_{g'} = i_L$ and $V_1 = v_g$:

$$\frac{V_2 - V_1}{R_1} = i_{g'} = i_L
\quad\Longrightarrow\quad
V_2 = v_g + R_1 i_L$$

Then back to $V_3$ via $v_C = V_2 - V_3$:

$$V_3 = V_2 - v_C = v_g + R_1 i_L - v_C$$

Finally use $v_L = L\dot{i}_L = -V_3$:

$$L\,\dot{i}_L = -v_g - R_1 i_L + v_C
\quad\Longrightarrow\quad
\dot{i}_L = -\frac{R_1}{L}\,i_L + \frac{1}{L}\,v_C - \frac{1}{L}\,v_g$$

**Step 6** Collect the equations into matrix form.

The two scalar equations from Steps 4 and 5 are exactly the two rows of $\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}$. Written out in full, the left-hand side is the derivative of the state vector, so both state derivatives appear explicitly:

$$
\frac{d}{dt}\begin{bmatrix} i_L \\ v_C \end{bmatrix} =
\begin{bmatrix}
-\frac{R_1}{L} & \frac{1}{L} \\[2pt]
-\frac{1}{C} & -\frac{1}{CR_2}
\end{bmatrix}
\begin{bmatrix} i_L \\ v_C \end{bmatrix} +
\begin{bmatrix}
-\frac{1}{L} & 0 \\[2pt]
0 & \frac{1}{C}
\end{bmatrix}
\begin{bmatrix} v_g \\ i_g \end{bmatrix}
$$

```{=latex}
\end{example}
```

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
