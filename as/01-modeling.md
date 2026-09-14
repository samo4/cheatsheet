# Modeling

A model turns a physical system into a set of equations that predicts how it behaves.

In every domain a system is built from the same three kinds of ideal elements:

- **Sources** deliver energy into the system — a voltage source, a force.
- **Storage** elements hold energy and release it on their own time scale — a capacitor or inductor, a spring or mass.
- **Dissipation** converts energy into heat — a resistor, a damper.

Storage is what makes a system *dynamic*. A storage element cannot change its energy instantly: it accumulates input over time, so the system keeps reacting after the input is gone. That behaviour is captured by differential equations. Each independent storage element contributes one state, so the number of states equals the number of independent storage elements.

The same three elements appear in every domain — electrical, mechanical, hydraulic, thermal — and in non-physical systems such as biological populations or economic ones. This chapter turns the resulting differential equations into *state-space form*,

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}, \qquad \vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u},
$$

with $\vec{x}$ the state vector, $\vec{u}$ the input, $\vec{y}$ the output, and $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$ constant matrices. That form is the target of this chapter and the language of the rest of the notes: the State-space chapter develops it in general.

These notes work with LTI, lumped, deterministic systems — the class carved out in the Introduction. Given the state and the input, such a model predicts the behaviour for all future time; outside that class the predictions fall back to local approximations (nonlinear and time-varying systems, via the Linearization chapter) or give out altogether (distributed and stochastic ones).

Building a model is not always a paper exercise — it often needs data. A car suspension model, for instance, needs the spring rate, damping, and mass. Given a good model structure, the parameters can be fitted to measurements of the real system. This is *system identification*, the often-forgotten counterpart of modeling.

## Higher-order ODEs as first-order systems

State-space form only contains first derivatives, so a higher-order ODE must first be rewritten as a system. The trick is to promote the lower-order derivatives to state variables. Formally we would write something like this:

$$
\dot{x}_n = f_n(x_1, x_2, \dots, x_n, u), \qquad
\dot{x}_{n-1} = x_n, \qquad
\dot{x}_{n-2} = x_{n-1}, \qquad
\dots, \qquad
\dot{x}_1 = x_2
$$

But just looking at the example it's easier: take the second-order ODE

$$
\ddot{y} + 2\dot{y} + 3y = 4u
$$

and define the states $x_1 = y$, $x_2 = \dot{y}$. The system is then just

$$
\dot{x}_1 = x_2, \qquad
\dot{x}_2 = \ddot{y} = -3x_1 - 2x_2 + 4u
$$

which is exactly the state-space shape we are after:

$$
\begin{bmatrix} \dot{x_1} \\ \dot{x_2} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -3 & -2 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 4 \end{bmatrix}u, \qquad
y = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}
$$

In general, an $n$-th order ODE $y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1\dot{y} + a_0 y = u$ becomes $n$ first-order equations by taking $x_1 = y$, $x_2 = \dot{y}$, $\dots$, $x_n = y^{(n-1)}$; the state matrix takes the companion form

$$
\begin{bmatrix}
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & & & \ddots & \vdots \\
-a_0 & -a_1 & -a_2 & \cdots & -a_{n-1}
\end{bmatrix}
$$

The number of states equals the order of the ODE — the same "one state per independent energy-storing element" count as in the electrical circuit below.

## The energy perspective

As already emphasized, the number of state variables corresponds to the number of *independent* energy storage elements. In mechanical systems these are typically the masses (storing kinetic energy) and the springs (storing potential energy); the damper only dissipates.

Comparing to electrical systems, the analogy is obvious: capacitor–spring, inductor–mass, resistor–damper. But the pedant will ask how to reconcile the second derivative in $F = ma$ with the first derivative in the capacitor–current relation. The answer, as in *Higher-order ODEs as first-order systems*, is the choice of state variables: for mechanical systems we take position and velocity, for electrical systems the capacitor voltages and inductor currents. This way, the state-space representation always involves first-order derivatives of the chosen states.

## Modeling mechanical systems

Modeling does not re-teach physics, it only *upgrades* what you know into the state-space format. Remember the three laws: inertia, $\sum F = ma$, and action–reaction.

Everything genuinely new about mechanical modeling is *directional bookkeeping*: assemble the forces with the correct signs and the equations write themselves.

### Translational systems

The three ideal elements are:

- *Spring* — $F = k(x_2 - x_1)$: stores energy.
- *Damper* — $F = b(\dot{x}_2 - \dot{x}_1)$: dissipates energy.
- *Mass* — $F = ma$: stores kinetic energy.

Plus, to complete the list at the top, a *source* of energy: a force $F(t)$ or a prescribed motion $x(t)$.

**Recipe.** A spring and a damper are *two-terminal* elements: each acts only on the difference between its two ends — the spring wants a constant separation, the damper a constant relative velocity. So the force an element exerts on the body you are isolating is always

$$F = k\,(x_{\text{other}} - x_{\text{mass}}), \qquad F = b\,(\dot{x}_{\text{other}} - \dot{x}_{\text{mass}}),$$

and the parentheses already contain every sign:

- the *mass's own coordinate* carries the minus — the element always pushes back on *this* body, whichever way you drew the axis;
- the *other terminal* carries the plus — another moving mass *assists* the motion, while fixed ground adds only a constant, which disappears once $x$ is measured from static equilibrium and leaves plain $-kx$ or $-b\dot{x}$.

Because no choice of axis direction can change which terminal is the mass's *own*, a sign cannot be placed wrongly by reasoning — only the picture can be misread. So:

1. Use the **same positive direction** for every coordinate and for $ma$.
2. For each element touching the body, write $k(x_{\text{other}} - x_{\text{mass}})$ or $b(\dot{x}_{\text{other}} - \dot{x}_{\text{mass}})$ — never add a sign yourself.
3. Sum with Newton and collect. Then sanity-check at rest: with $\ddot{x} = \dot{x} = 0$ the springs must hold the static load exactly — if they don't, the diagram is wrong, not the math.

Measuring $x$ from the static equilibrium makes the constant weight disappear; measuring it from the unstretched position leaves the weight as a constant input. Both are correct; pick one and stick with it.

```{=latex}
\begin{example}[frametitle={Example - car suspension and crash buffer}]
```

```{=latex}
\input{tikz/modeling-wheel.tex}
```

A car body of mass $m$ rests on its suspension — spring $k$ and damper $b$ in parallel — on the ground. Gravity pulls it down with the weight $mg$, our input. We want the body's vertical motion $x(t)$ and its state-space model.

**Step 1 — states.** The natural states are position and velocity:

$$x_1 = x \quad \text{(vertical position)}, \qquad x_2 = \dot{x} \quad \text{(vertical velocity)}.$$

**Step 2 — forces with the correct signs.** Take positive $x$ upward. The suspension connects the body (at $x$) to the ground (at $0$), so the spring stretch and the damper velocity are just $x$ and $\dot{x}$.

- *Spring* opposes stretch. If the body moves up ($x > 0$) the spring is extended and pulls it *down*, hence $F_k = -kx$.
- *Damper* opposes velocity. If the body moves up ($\dot{x} > 0$) the damper pushes it down, hence $F_b = -b\dot{x}$.
- *Gravity* always pulls down, hence $F_g = -mg$.

*Sanity check:* at rest ($\ddot{x} = \dot{x} = 0$) Newton gives $kx = -mg$, i.e. the spring pushes up with exactly the weight — a flipped sign here would make the body float away.

**Step 3 — Newton's 2$^\text{nd}$ law.** $\sum F = ma$:

$$m\ddot{x} = F_k + F_b + F_g = -kx - b\dot{x} - mg,$$

rearranged into the familiar second-order ODE

$$m\ddot{x} + b\dot{x} + kx = -mg.$$

**Step 4 — reduce to first order.** With the states of Step 1:

$$\dot{x}_1 = x_2, \qquad \dot{x}_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2 - g.$$

**Step 5 — matrix form.** With the input $u = mg$ (the weight):

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ -\frac{1}{m} \end{bmatrix} u.
$$

**Physical meaning of the states.** $x_1$ is the body's vertical position, $x_2$ its vertical velocity. The state matrix is the same companion form as in the higher-order ODE example: one state per derivative. The constant input does not change the dynamics — it only sets the equilibrium (the static deflection of Step 2); measure $x$ from that equilibrium and $mg$ drops out entirely.

**Variant — the same system with no input.** Replace the weight by a crash: a car of mass $m$ entering a rigid barrier at speed $v_0$, cushioned by the same spring $k$ and damper $b$ in parallel. Take $x$ as the *compression* of the buffer, positive into the barrier. The motion now resists itself — the spring pushes back ($F_k = -kx$) and the damper pushes back harder the faster the car is still moving ($F_b = -b\dot{x}$) — so

$$m\ddot{x} + b\dot{x} + kx = 0, \qquad \dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x}:$$

the same state matrix, with the input removed. Here $x_1$ is how deep the car has penetrated and $x_2$ how fast it is still going, and the damper turns the kinetic energy $\tfrac{1}{2}mv_0^2$ into heat — that is what makes the crash *cushioned*.

```{=latex}
\end{example}
```

**Real forces you will meet.** Friction comes as a stick–slip pair: static (stiction) while at rest, $F \le \mu_s N$, kinetic once moving, $F = \mu_k N$; both oppose motion, so their sign is $-\operatorname{sign}(\dot{x})$. Rolling resistance is roughly constant, $F = c_r N$. Air drag is viscous at low speed, $F = c_v \dot{x}$, and quadratic at high speed, $F = \tfrac{1}{2}\rho C_d A \dot{x}^2$ — the Reynolds number decides which regime applies.

### Rotational systems

The same equations with $x \to \theta$, $v \to \omega$, $F \to \tau$, $m \to J$: torque $\tau = J\alpha$, torsional spring $\tau = k(\theta_2 - \theta_1)$, rotational damper $\tau = b(\omega_2 - \omega_1)$. Gears and transmissions just scale torque and angular speed by the gear ratio.

The inertia term is also what picks the states, exactly as for a mass:

$$
\dot{\theta} = \omega, \qquad
\tau = J\ddot{\theta} = J\dot{\omega} = J\alpha
$$

so angle and angular velocity play the role of position and velocity, and a rotational model again reduces to two first-order equations.

## Modeling of electrical circuits

Let's skip how resistors, capacitors and inductors are modeled. Electrical modeling rests on Kirchhoff's laws, and since there are two of them — both able to generate independent equations — two methods were taught: node-voltage and mesh-current. In principle either one suffices; in practice you use whichever leaves fewer unknowns, and in the examples below we mix them where it is convenient.

```{=latex}
\begin{example}[frametitle={Example - state-space equations of a circuit}]
```

We want to write down the state-space equations of the circuit in matrix form, with state vector $\vec{x} = \begin{bmatrix} i_L \\ v_C \end{bmatrix}$, input $\vec{u} = \begin{bmatrix} v_g \end{bmatrix}$, and output $\vec{y} = \begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix}$.

```{=latex}
\input{tikz/modeling-circuit.tex}
```

Let's select one node as ground. Although any node can be ground, we try to choose it in a way that will make the resulting equation as easy as possible. Generally, pick the node with the most element connections to reduce the number of unknown node voltages. Prefer to ground a terminal of a voltage source: then the other terminal is fixed by the source ($V_1 = v_g$), so we never write the KCL equation at that node and the source current $i_{v_g}$ never enters the equations as an unknown. If a voltage source instead floats between two non-grounded nodes, its current appears in both node equations with opposite signs — eliminate it by adding the two node equations (the *supernode*) and closing the pair with the source constraint $V_2 - V_1 = v_g$. In our case, we can select the bottom node as ground.\footnote{In simulation software (e.g., SPICE), the ground node choice can influence numerical stability, but picking the one with the most connections is still a good rule of thumb.}

Then we proceed to mark the remaining nodes.\footnote{Passive sign convention (PSC) defines an element's voltage positive at the terminal where the reference current enters; power is then positive when the element absorbs energy. For a voltage source, PSC requires the reference current to be marked so that current entering absorbs power and current leaving (minus sign) delivers power to the rest of the circuit — the arrow points into the + terminal. For the capacitor we have defined the polarity and applied PSC to $i_C$ (arrow into +); for the inductor we have defined the current $i_L$. Although $v_L$ is not needed here, we could define its polarity according to PSC as well ($V_2$ positive with respect to $V_3$).}

```{=latex}
\input{tikz/modeling-circuit-nodes.tex}
```

Here we mix the two: a node-voltage formulation, with the state variables of the energy-storing elements chosen up front.

First we observe that $V_1 = v_g$ and $v_C = V_3$.

We write down the equations for each node using Kirchhoff's current law. When expressing currents through resistors, we start with the current node voltage (so currents are taken as leaving the node: plus sign in our equations).

$$\frac{V_1 - V_2}{R_1} + i_g = 0$$

When a node is connected to an inductor, we express the current through the inductor as a state variable. Note that the direction of current for $i_L$ is defined as flowing out of $V_2$. For $V_2$ we get:

$$\frac{V_2 - V_1}{R_1} + i_L = 0$$

For capacitors we do the same, but take the voltage rather than the current as the state variable (more standard); the current then follows from $i_C = C\,\dot{v}_C$ under PSC.

Next, we write down the equations for the energy-storing elements using their constitutive relations. Note that $i_L$ is chosen from $V_2$ to $V_3$. Lenz’s law is not ignored; its effect was already built into the sign of the inductor’s voltage when we adopted PSC. Faraday’s law gives $v = L\,\dot{i}$ for the chosen polarity (voltage drop in the direction of the reference current). If you had defined the voltage polarity opposite to the current reference, the relation would appear as $v = -L\,\dot{i}$. Thus no extra minus is added later — the orientation choices at the start encode it.

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

If the outputs are $v_{R_1}$ and $v_L$, both are algebraic combinations of the states and the input — with $V_2 = v_g - R_1 i_L$ and $V_3 = v_C$,

$$v_{R_1} = R_1 i_L - v_g, \qquad v_L = V_2 - V_3 = v_g - R_1 i_L - v_C,$$

so

$$
\begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix} =
\begin{bmatrix} R_1 & 0 \\ -R_1 & -1 \end{bmatrix}
\begin{bmatrix} i_L \\ v_C \end{bmatrix} +
\begin{bmatrix} -1 \\ 1 \end{bmatrix} v_g.
$$

Note what the output equation may *not* contain: $\mathbf{C}$ and $\mathbf{D}$ are constant matrices, so no derivative can appear in them. $v_L = L\,\dot{i}_L$ is the state equation in disguise, not an output relation.


```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Fully worked out example - getting state-space equations from a circuit}]
```

```{=latex}
\input{tikz/example-circuit.tex}
```

For the circuit above, we want to write the state-space equations in matrix form, with state vector $\vec{x} = [i_L, v_C]^T$ and input $\vec{u} = [v_g, i_g]^T$.

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

**Step 3 — Capacitor.** What we need is **$\dot{v}_C$**, expressed as a function of the states and the inputs.

To get it from $i_C = C\dot{v}_C$ we need the capacitor current $i_C$:

$i_C$ appears in both the node-$V_2$ and node-$V_3$ equations — the capacitor sits between $V_2$ and $V_3$, so its current shows up in both. Either one works; the node-$V_3$ equation is the quicker pick because all its other terms are already known: $V_3 - V_2 = -v_C$ (a state), $i_g$ (an input) and $i_L$ (a state). (The node-$V_2$ equation also contains $\frac{V_2 - V_1}{R_1} = i_{g'}$, which we'd have to swap for $i_L$ first.) Solve it for $i_C$:

$$i_C = \frac{V_3 - V_2}{R_2} + i_g - i_L = -\frac{v_C}{R_2} + i_g - i_L$$

Insert the capacitor equation $i_C = C\dot{v}_C$:

$$C\,\dot{v}_C = - \frac{v_C}{R_2} + i_g - i_L
\quad\Longrightarrow\quad
\dot{v}_C = -\frac{1}{C}\,i_L - \frac{1}{CR_2}\,v_C + \frac{1}{C}\,i_g$$

**Step 4 — Inductor.** What we need is **$\dot{i}_L$**.

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

**Step 5** Collect the equations into matrix form.

The two scalar equations from Steps 3 and 4 are exactly the two rows of the state equation. Written out in full, the left-hand side is the derivative of the state vector, so both state derivatives appear explicitly:

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
