# Modeling

A model turns a physical system into a set of equations that predicts how it behaves.

In every domain a system is built from the same three kinds of ideal elements:

- **Sources** deliver energy into the system.
- **Storage** elements hold energy and release it on their own time scale.
- **Dissipation** converts energy into heat.

Storage is what makes a system *dynamic*. A storage element cannot change its energy instantly: it accumulates input over time, so the system keeps reacting after the input is gone. That behaviour is captured by differential equations. Each independent storage element contributes one state, so the number of states equals the number of independent storage elements.

Besides the electrical and mechanical domains, the same structure carries over to hydraulic and thermal systems, and even to non-physical ones such as biological populations or economies. This chapter turns the resulting differential equations into *state-space form*,

$$
\dot{\vec{x}} = \mathbf{A}\vec{x} + \mathbf{B}\vec{u}, \qquad \vec{y} = \mathbf{C}\vec{x} + \mathbf{D}\vec{u},
$$

with $\vec{x}$ the state vector, $\vec{u}$ the input, $\vec{y}$ the output, and $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$ constant matrices. That form is the target of this chapter and the language of the rest of the notes: the State-space chapter develops it in general.

These notes work with LTI, lumped, deterministic systems — the class carved out in the Introduction. Given the state and the input, such a model predicts the behaviour for all future time; outside that class the predictions fall back to local approximations (nonlinear and time-varying systems, via the Linearization chapter) or give out altogether (distributed and stochastic ones).

Building a model is not always a paper exercise — it often needs data. A car suspension model, for instance, needs the spring rate, damping, and mass — not all of these can be easily measured, but given a good model structure, the parameters can be fitted to measurements of the real system. This is *system identification*, the often-forgotten counterpart of modeling.

## Higher-order ODEs as first-order systems

State-space form only contains first derivatives, so a higher-order ODE must first be rewritten as a system. The trick is to promote the lower-order derivatives to state variables: each state is the derivative of the one before, and only the last equation carries the actual dynamics,

$$
\dot{x}_1 = x_2, \qquad
\dot{x}_2 = x_3, \qquad
\dots, \qquad
\dot{x}_{n-1} = x_n, \qquad
\dot{x}_n = f(x_1, x_2, \dots, x_n, u).
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

The number of states equals the order of the ODE.

## Modeling mechanical systems

Modeling does not re-teach physics, it only *upgrades* what you know into the state-space format. Remember the three laws: inertia, $\sum F = ma$, and action–reaction.

Everything genuinely new about mechanical modeling is *directional bookkeeping*: assemble the forces with the correct signs and the equations write themselves.

### Translational systems

The three ideal elements are:

- *Spring* — $F = k(x_2 - x_1)$.
- *Damper* — $F = b(\dot{x}_2 - \dot{x}_1)$: dissipates energy.
- *Mass* — $F = ma$.

Plus, to complete the list at the top, a *source* of energy: a force $F(t)$ or a prescribed motion $x(t)$.

**Recipe.** A spring and a damper are two-terminal elements: each acts only on the difference between its two ends — the spring wants a constant separation, the damper a constant relative velocity. So the force an element exerts on the body you are isolating is always

$$F = k\,(x_{\text{other}} - x_{\text{mass}}), \qquad F = b\,(\dot{x}_{\text{other}} - \dot{x}_{\text{mass}}),$$

and the parentheses already contain every sign:

- the *mass's own coordinate* carries the minus — the element always pushes back on *this* body, whichever way you drew the axis;
- the *other terminal* carries the plus — another moving mass *assists* the motion, while fixed ground contributes nothing ($x_{\text{other}} = 0$) and leaves plain $-kx$ or $-b\dot{x}$.

Because no choice of axis direction can change which terminal is the mass's *own*, the recipe leaves no sign to choose — what remains is reading the picture correctly. So:

1. Use the **same positive direction** for every coordinate and for $ma$.
2. For each element touching the body, write $k(x_{\text{other}} - x_{\text{mass}})$ or $b(\dot{x}_{\text{other}} - \dot{x}_{\text{mass}})$ — never add a sign yourself.
3. Sum with Newton and collect. Then sanity-check at rest: with $\ddot{x} = \dot{x} = 0$ the springs must hold the static load exactly.

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

*Sanity check:* at rest ($\ddot{x} = \dot{x} = 0$) Newton gives $kx = -mg$, i.e. the spring is compressed and pushes up with exactly the weight. A flipped gravity sign would put the equilibrium above the ground; a flipped spring sign would make the body run away from any equilibrium.

**Step 3 — Newton's 2$^\text{nd}$ law.**

$$m\ddot{x} = F_k + F_b + F_g = -kx - b\dot{x} - mg,$$

rearranged into

$$m\ddot{x} + b\dot{x} + kx = -mg.$$

**Step 4 — reduce to first order.** Introduce $\dot{x}_1 = x_2$ as a new state and divide by $m$.

$$\dot{x}_2 = -\frac{k}{m}x_1 - \frac{b}{m}x_2 - g.$$

**Step 5 — matrix form.** With the input $u = mg$:

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ -\frac{1}{m} \end{bmatrix} u.
$$

**Physical meaning of the states.** $x_1$ is the body's vertical position, $x_2$ its vertical velocity. The state matrix is the same companion form as in *Higher-order ODEs as first-order systems*: one state per derivative. The constant input does not change the dynamics — it only sets the equilibrium (the static deflection of Step 2); measure $x$ from that equilibrium and $mg$ drops out entirely.

**Variant — the same system with no input.** Replace the weight by a crash: a car of mass $m$ entering a rigid barrier at speed $v_0$, cushioned by the same spring $k$ and damper $b$ in parallel. Take $x$ as the *compression* of the buffer, positive into the barrier. The motion now resists itself — the spring pushes back ($F_k = -kx$) and the damper pushes back harder the faster the car is still moving ($F_b = -b\dot{x}$):

$$m\ddot{x} + b\dot{x} + kx = 0, \qquad \dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix}\vec{x}:$$

the same state matrix, with the input removed. Here $x_1$ is how deep the car has penetrated and $x_2$ how fast it is still going, with the initial state $\vec{x}(0) = \tvec{0, v_0}$. The spring only stores the kinetic energy $\tfrac{1}{2}mv_0^2$; the damper turns it into heat — that is what makes the crash cushioned. The model holds only while the car touches the buffer: once $x$ returns to $0$ the car rebounds free, which our model cannot express.

```{=latex}
\end{example}
```

### Real forces you will meet

#### Static friction

At rest, friction is a *reaction* force: it takes whatever value holds the body still, up to a limit ($N$ the normal force),

$$|F_s| \le \mu_s N .$$

So it is not a function of the state at all — it is fixed by the other forces, and the bound only decides *whether* the body moves. That switch between sticking and sliding is what makes friction nonlinear. In practice static friction is a breakaway test: compute the force needed to keep the body at rest; if it stays below $\mu_s N$ nothing moves, otherwise the body slides and kinetic friction takes over.

#### Kinetic friction

Once the body slides, the force is constant in size and opposes the motion,

$$F_k = -\mu_k N \operatorname{sign}(\dot{x}), \qquad \mu_k < \mu_s .$$

The $\operatorname{sign}$ is nonlinear, so this is never a $b\dot{x}$ term. If the direction of travel is known, it is just a constant force entering through $\mathbf{B}$, like the weight $mg$. The drop from $\mu_s$ to $\mu_k$ causes stick–slip: squealing brakes, the violin bow.

#### Rolling resistance

Same form, smaller coefficient, and no static jump, hence no stick–slip:

$$F_r = -c_r N \operatorname{sign}(\dot{x}), \qquad c_r \approx 0.01 \ \text{(tyre on asphalt)}, \quad 0.001 \ \text{(steel on rail)}.$$

#### Air drag

Which law applies depends on the Reynolds number $Re = vL/\nu$ ($L$ the size of the body, $\nu$ the kinematic viscosity):

$$
F_d \approx
\begin{cases}
-c_v\,\dot{x}, & Re \lesssim 1 \quad \text{(viscous: dust, MEMS)}\\[2pt]
-\tfrac{1}{2}\rho C_d A\,\dot{x}\,|\dot{x}|, & Re \gtrsim 10^3 \quad \text{(inertial: anything everyday)}
\end{cases}
$$

The viscous law is linear and keeps the model LTI. The quadratic one is written with $|\dot{x}|$ so that drag still opposes the motion; it is nonlinear, but linearizing about the terminal velocity $v_t$ gives an exponential approach with $\tau = v_t/(2g)$. $C_d$ depends on shape: about $1.1$ for a flat plate or disc facing the flow, $0.3$ for a dome.

### Rotational systems

The translational equations carry over one to one, with angle for position, torque for force and moment of inertia for mass: inertia $\tau = J\alpha$, torsional spring $\tau = k(\theta_2 - \theta_1)$, rotational damper $\tau = b(\omega_2 - \omega_1)$. A gear ratio $n$ scales torque and speed linearly, but inertia, stiffness and damping seen through the gear scale with $n^2$.

As with a mass, the inertia is what picks the states:

$$\dot{\theta} = \omega$$
$$\tau = J\ddot{\theta} = J\dot{\omega}$$

so angle and angular velocity play the role of position and velocity, and a rotational model again reduces to two first-order equations.

```{=latex}
\begin{example}[frametitle={Example - motor rotor}]
```

A motor shaft carries a rotor of moment of inertia $J$. The bearings resist rotation with a viscous torque $b\omega$, and the motor drives the shaft with a torque $\tau_m(t)$ — the input. We want the rotor's motion.

**Step 1 — states.** Exactly as translation used position and velocity:

$$x_1 = \theta \quad \text{(shaft angle)}, \qquad x_2 = \omega = \dot{\theta} \quad \text{(angular velocity)}.$$

**Step 2 — torques with the correct signs.** Take positive $\omega$ in the motor's direction of rotation, so the same directional bookkeeping applies with $\dot{x} \to \omega$ and $m \to J$.

- *Viscous bearing torque* — opposes rotation, so $\tau_b = -b\omega$.
- *Motor torque* — external, and we define it positive in the chosen direction: $\tau_m$, the input.
- *Load torque* — add $-\tau_L$ if a fan or pump hangs on the shaft; it is a second input, not a new state.

**Step 3 — rotational form of Newton's law.** $\sum \tau = J\alpha$:

$$J\dot{\omega} = \tau_m - b\omega \qquad\Longrightarrow\qquad J\ddot{\theta} + b\dot{\theta} = \tau_m .$$

No spring appears — nothing stores torsional potential energy — so the equation is first order in $\omega$ and second order only because $\theta$ integrates it.

**Step 4 — matrix form.** With $\vec{x} = \tvec{\theta, \omega}$ and input $\tau_m$,

$$
\dot{\vec{x}} = \begin{bmatrix} 0 & 1 \\ 0 & -\frac{b}{J} \end{bmatrix}\vec{x} + \begin{bmatrix} 0 \\ \frac{1}{J} \end{bmatrix}\tau_m, \qquad y = \begin{bmatrix} 1 & 0 \end{bmatrix}\vec{x}
$$

if the output of interest is the angle.

**Sanity check.** With a constant torque the speed settles at $\omega_\infty = \tau_m/b$, while the angle grows without bound — a steady torque pins the *speed*, never the *position*, because the rotor has no torsional spring to define one. The eigenvalues say the same: $-b/J$, minus the reciprocal of the mechanical time constant $J/b$ (the rotor's version of an RC circuit), and $0$, the free integrator in $\dot{\theta} = \omega$.

**What attaches to the shaft.** Modeling the motor's electrical side as well ($\tau_m = K_t i$) would add the armature current as a third state. A gearbox adds none: referred to one shaft, the two inertias collapse into a single $J = J_1 + n^2 J_2$.

```{=latex}
\end{example}
```

## Modeling of electrical circuits

Let's skip how resistors, capacitors and inductors are modeled — you know that. Electrical modeling rests on Kirchhoff's laws, and since there are two of them — both able to generate independent equations — two methods were taught: node-voltage and mesh-current. In principle either one suffices; in practice you use whichever leaves fewer unknowns. Both examples below use node voltages.

```{=latex}
\begin{example}[frametitle={Example - state-space equations of a circuit}]
```

We want to write down the state-space equations of the circuit in matrix form, with state vector $\vec{x} = \tvec{i_L,  v_C}$, input $\vec{u} = \tvec{v_g}$, and output $\vec{y} = \tvec{v_{R_1}, v_L}$.

```{=latex}
\input{tikz/modeling-circuit.tex}
```

Let's select one node as ground. Although any node can be ground, we try to choose it in a way that will make the resulting equation as easy as possible. The number of unknown node voltages is always one less than the number of nodes, whichever you pick; what the choice changes is how many terms each equation carries, so pick the node with the most element connections. Prefer to ground a terminal of a voltage source: then the other terminal is fixed by the source ($V_1 = v_g$), so we never write the KCL equation at that node and the source current $i_{v_g}$ never enters the equations as an unknown. If a voltage source instead floats between two non-grounded nodes, its current appears in both node equations with opposite signs — eliminate it by adding the two node equations (the *supernode*) and closing the pair with the source constraint $V_2 - V_1 = v_g$. In our case, we can select the bottom node as ground.

Then we proceed to mark the remaining nodes.\footnote{Passive sign convention (PSC) defines an element's voltage positive at the terminal where the reference current enters; power is then positive when the element absorbs energy. For the voltage source we marked $i_g$ entering the + terminal, so under PSC a positive $v_g i_g$ means the source absorbs power, and a negative one that it delivers power to the rest of the circuit. For the capacitor we have defined the polarity and applied PSC to $i_C$ (arrow into +); for the inductor we have defined the current $i_L$. The output $v_L$ takes its polarity from PSC as well ($V_2$ positive with respect to $V_3$).}

```{=latex}
\input{tikz/modeling-circuit-nodes.tex}
```

This is a node-voltage formulation, with the state variables of the energy-storing elements chosen up front.

First we observe that $V_1 = v_g$ and $v_C = V_3$.

We write down the equations for each node using Kirchhoff's current law. When expressing currents through resistors, we start with the voltage of the node being written (so currents are taken as leaving the node: plus sign in our equations).

$$\frac{V_1 - V_2}{R_1} + i_g = 0$$

This one only determines the source current $i_g$; the state equations will not need it.

When a node is connected to an inductor, we express the current through the inductor as a state variable. Note that the direction of current for $i_L$ is defined as flowing out of $V_2$, towards $V_3$. For $V_2$ we get:

$$\frac{V_2 - V_1}{R_1} + i_L = 0$$

For capacitors we do the same, but take the voltage rather than the current as the state variable (more standard); the current then follows from $i_C = C\,\dot{v}_C$ under PSC. For $V_3$, with $i_L$ entering and $i_C$ leaving through the capacitor:

$$-i_L + i_C + \frac{V_3}{R_2} = 0$$

Next, we write down the equations for the energy-storing elements using their constitutive relations.\footnote{Lenz's law is not ignored; its effect was already built into the sign of the inductor's voltage when we adopted PSC. Faraday's law gives $v = L\,\dot{i}$ for the chosen polarity (voltage drop in the direction of the reference current). Had the voltage polarity been defined opposite to the current reference, the relation would read $v = -L\,\dot{i}$. No extra minus is added later — the orientation choices at the start encode it.} For the inductor:

$$ v_L = L \frac{di_L}{dt} = V_2 - V_3 $$

And for the capacitor, solving the node-$V_3$ equation for $i_C$:

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

$$v_{R_1} = V_1 - V_2 = R_1 i_L, \qquad v_L = V_2 - V_3 = v_g - R_1 i_L - v_C,$$

so

$$
\begin{bmatrix} v_{R_1} \\ v_L \end{bmatrix} =
\begin{bmatrix} R_1 & 0 \\ -R_1 & -1 \end{bmatrix}
\begin{bmatrix} i_L \\ v_C \end{bmatrix} +
\begin{bmatrix} 0 \\ 1 \end{bmatrix} v_g.
$$

Note what the output equation may *not* contain: $\mathbf{C}$ and $\mathbf{D}$ are constant matrices, so no derivative can appear in them. $v_L = L\,\dot{i}_L$ is the state equation in disguise, not an output relation.

Sanity check: the voltages around the loop add up to the source, $R_1 i_L + (v_g - R_1 i_L - v_C) + v_C = v_g$, as KVL demands.


```{=latex}
\end{example}
```

```{=latex}
\begin{example}[frametitle={Fully worked out example - getting state-space equations from a circuit}]
```

```{=latex}
\input{tikz/example-circuit.tex}
```

For the circuit above, we want to write the state-space equations in matrix form, with state vector $\vec{x} = [i_L, v_C]^T$ and input $\vec{u} = [v_g, i_g]^T$. No output is specified, so only the state equation is wanted.

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

Sanity check: the diagonal of $\mathbf{A}$ is negative (each storage element drains through its resistor), and the off-diagonal entries have opposite signs (the inductor and capacitor pass energy back and forth). A sign slip in Step 3 or 4 breaks one of these.

```{=latex}
\end{example}
```

## The energy perspective

In mechanical systems the independent storage elements are typically the masses (storing kinetic energy) and the springs (storing potential energy); the damper only dissipates.

Comparing to electrical systems, the usual *force–voltage* analogy pairs inductor–mass, capacitor–spring, resistor–damper (the *force–current* analogy pairs them differently, mass–capacitor and spring–inductor; both are consistent). The pedant will ask how to reconcile the second derivative in $F = ma$ with the first derivative in $v = L\,\dot{i}$. There is nothing to reconcile: $F = m\dot{v}$ is already first order in the velocity, just as $v = L\,\dot{i}$ is in the current. As in *Higher-order ODEs as first-order systems*, it is the choice of state variables that does the work: position and velocity for mechanical systems, capacitor voltages and inductor currents for electrical ones. This way, the state-space representation always involves first-order derivatives of the chosen states.
