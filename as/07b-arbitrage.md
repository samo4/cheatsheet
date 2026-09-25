# Two-exchange arbitrage: the Perron eigenvector

The companion chapter (two crypto exchanges) looked at arbitrage through its *dynamics*: the matrix $\mathbf{A}$ in $\dot{\vec{x}} = \mathbf{A}\vec{x}$, whose eigenvectors split prices into a persistent level and a decaying spread. This chapter looks at a single *snapshot* of the market instead. Here the matrix holds exchange rates, and its eigenvalue answers a yes/no question: **can a round trip make money?**

```{=latex}
\begin{example}[frametitle={Example - arbitrage as an eigenvalue test}]
```

**Setup.** One coin trades on two exchanges at prices $p_1$ (exchange 1) and $p_2$ (exchange 2), in USD per coin. Say $p_1 \ge p_2$. The two assets are USD and the coin, and the best conversion in each direction is:

- **coin → USD:** sell where it is expensive, getting $a = p_1$ USD per coin;
- **USD → coin:** buy where it is cheap, getting $b = 1/p_2$ coin per USD.

Put these into the **trade matrix**. Entry $(i,j)$ is how many units of asset $i$ one unit of asset $j$ buys (order USD, coin):

$$
\mathbf{T} = \begin{bmatrix} 0 & a \\ b & 0 \end{bmatrix}
= \begin{bmatrix} 0 & p_1 \\ 1/p_2 & 0 \end{bmatrix}
$$

Multiplying a holdings vector by $\mathbf{T}$ performs one trade. Start with $\vec{h} = [1\ 0]^{\mathsf T}$ (one dollar): $\mathbf{T}\vec{h} = [0\ \ b]^{\mathsf T}$ is the coin that dollar buys, and a second multiplication turns it back into USD.

**A round trip is $\mathbf{T}^2$.**

$$
\mathbf{T}^2 = \begin{bmatrix} ab & 0 \\ 0 & ab \end{bmatrix} = ab\,\mathbf{I}
$$

Every round trip multiplies wealth by $ab = p_1/p_2$, whichever asset you start in. There is **arbitrage iff $ab > 1$**.

**The eigenvalues say the same thing.** From $\det(\mathbf{T} - \lambda\mathbf{I}) = \lambda^2 - ab = 0$,

$$
\lambda_{1,2} = \pm\sqrt{ab}, \qquad \rho(\mathbf{T}) = \sqrt{ab}
$$

The spectral radius $\rho(\mathbf{T})$ is the **growth factor per trade**, the geometric mean of the rates around the cycle. It squares to the round-trip factor because a round trip is two trades.

| Market                   | $ab$  | $\rho(\mathbf{T})$ | Round trip           |
|:-------------------------|:-----:|:------------------:|:---------------------|
| $p_1 = p_2$ (consistent) | $= 1$ | $= 1$              | break-even           |
| $p_1 > p_2$ (spread)     | $> 1$ | $> 1$              | profit — arbitrage   |
| with fees too high       | $< 1$ | $< 1$              | loss — no trade      |

The stability picture from the discrete chapter carries over with the roles swapped. There, $|\lambda| < 1$ meant the state dies out. Here, $\rho > 1$ means wealth grows without bound on repeated round trips, which is exactly what a market cannot allow for long.

**The Perron eigenvector is the fair price.** $\mathbf{T}$ is nonnegative and irreducible, so by Perron–Frobenius the eigenvalue $\rho = \sqrt{ab}$ has an eigenvector with positive entries. Solving $\mathbf{T}\vec{v} = \rho\vec{v}$, i.e. $a v_2 = \sqrt{ab}\,v_1$:

$$
\vec{v} = \begin{bmatrix} \sqrt{a} \\ \sqrt{b} \end{bmatrix}, \qquad
\frac{v_1}{v_2} = \sqrt{\frac{a}{b}} = \sqrt{p_1 p_2}
$$

Read $\vec{v}$ as values in a common unit: the ratio $v_1/v_2$ is the USD price of one coin that is *most consistent* with both quotes, namely their **geometric mean**. It lies between the two quotes, which is where arbitrage pushes both exchanges.

**The consistent market has rank 1.** Now allow trading on either book in either direction, including doing nothing. With $p_1 = p_2 = p$ the full rate matrix is

$$
\mathbf{R} = \begin{bmatrix} 1 & p \\ 1/p & 1 \end{bmatrix}
= \begin{bmatrix} p \\ 1 \end{bmatrix} \begin{bmatrix} \tfrac{1}{p} & 1 \end{bmatrix}
$$

Every entry is a ratio of values, $r_{ij} = w_i / w_j$. That makes $\mathbf{R}$ an outer product, so it has rank 1. Its eigenvalues are $\operatorname{tr}\mathbf{R} = 2$ and $0$, and its eigenvector is the value vector $[p\ 1]^{\mathsf T}$. A spread breaks the factorization. In general $\mathbf{R} = \mathbf{I} + \mathbf{T}$ has eigenvalues $1 \pm \sqrt{ab}$ and $\det\mathbf{R} = 1 - ab$. The determinant is zero (rank 1) exactly when $ab = 1$ and negative (rank 2) when there is arbitrage. This is Saaty's consistency test: $\lambda_{\max}(\mathbf{R}) \ge n$, with equality iff the matrix is consistent, and

$$
\text{CI} = \frac{\lambda_{\max} - n}{n - 1} = \sqrt{ab} - 1
$$

measures how far the market is from consistency.

**Worked gap.** Take the same quotes as the dynamics chapter: $p_1 = 100$, $p_2 = 96$.

$$
a = 100, \quad b = \tfrac{1}{96}, \quad ab = \tfrac{100}{96} \approx 1.0417, \quad \rho(\mathbf{T}) = \sqrt{1.0417} \approx 1.0206
$$

- **Round trip:** \$96 buys 1 coin on exchange 2, which sells for \$100 on exchange 1. That is a factor of $1.0417$, a 4.17 % gain per loop.
- **Per trade:** $\rho \approx 1.0206$, a 2.06 % gain on each of the two legs (geometric mean).
- **Fair price:** $\sqrt{100 \cdot 96} \approx 97.98$, practically the mid-price 98 of the dynamics chapter. For a small spread the geometric and arithmetic means agree to first order.
- **Consistency index:** $\text{CI} = \lambda_{\max}(\mathbf{R}) - 2 = 0.0206$.

**Fees shrink the eigenvalue.** A proportional fee $f$ on each leg scales both rates by $(1-f)$:

$$
a = p_1(1-f), \quad b = \frac{1-f}{p_2}, \qquad \rho(\mathbf{T}) = (1-f)\sqrt{\frac{p_1}{p_2}}
$$

Arbitrage survives only while $\rho > 1$, i.e. $f < 1 - \sqrt{p_2/p_1}$. For $100$ vs $96$ that is $f < 1 - \sqrt{0.96} \approx 2.02\,\%$ per leg. Withdrawal and network fees enter the same way, as extra factors on $a$ or $b$. The fee band $\rho \le 1$ is the **no-arbitrage region**: prices may disagree by up to the fees and no trader can profit.

**Link to the dynamics.** In the companion chapter's eigen-coordinates, with level $\xi_1 = \frac{p_1+p_2}{2}$ and spread $\xi_2 = \frac{p_1-p_2}{2}$,

$$
ab = \frac{p_1}{p_2} = \frac{\xi_1 + \xi_2}{\xi_1 - \xi_2}
$$

As the spread mode decays ($\xi_2 \propto e^{-2kt}$), $ab \to 1$ and $\rho(\mathbf{T}) \to 1$. The dynamic eigenvalue $-2k$ is the rate at which the snapshot eigenvalue $\rho$ is driven down to its no-arbitrage value 1. In the presence of fees it is driven only to the edge of the fee band, which is why real spreads never fully close.

**More than two assets — a caveat.** With $n$ assets there are many cycles, and ordinary matrix multiplication *sums* over paths. So $(\mathbf{T}^k)_{ii}$ adds up the proceeds of all $k$-step routes, as if one dollar could travel every route at once. The ordinary $\rho(\mathbf{T})$ can then exceed 1 even when no single cycle is profitable. The algebra that matches trading is **max-times**: replace $\sum$ by $\max$ in the product. Its eigenvalue is the best cycle's geometric-mean rate, and arbitrage exists iff that eigenvalue exceeds 1. After taking $-\log$ of the rates, this becomes a *negative-cycle* search (Bellman–Ford). With two assets there is only one cycle, so the ordinary and max-times eigenvalues coincide, and the simple picture above is exact.

```{=latex}
\end{example}
```

## Further reading

- Saaty, T. L. (1977). *A Scaling Method for Priorities in Hierarchical Structures*, Journal of Mathematical Psychology. Reciprocal matrices, $\lambda_{\max} \ge n$ with equality iff consistent, and the consistency index.
- Baccelli, F., Cohen, G., Olsder, G. J. and Quadrat, J.-P. (1992). *Synchronization and Linearity*, Wiley. Max-plus / max-times algebra, where the eigenvalue is the maximum cycle mean.
- Makarov, D. and Schoar, A. (2020). *Trading and Arbitrage in Cryptocurrency Markets*, Journal of Financial Economics. How large, and how persistent, cross-exchange spreads are in practice.
