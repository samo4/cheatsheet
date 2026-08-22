---
title: "Kolokvij AS, 22.11.2024"
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

# 1

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
