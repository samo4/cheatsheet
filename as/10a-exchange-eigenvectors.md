# Two crypto exchanges: eigenvectors in the wild

```{=latex}
\begin{example}[frametitle={Example - two crypto exchanges, or: eigenvectors in the wild}]
```

**Setup.** Two exchanges quote the same coin, at prices $p_1$ (exchange 1) and $p_2$ (exchange 2), collected into the state vector

$$
\vec{x} = \begin{bmatrix} p_1 \\ p_2 \end{bmatrix}
$$

Two forces act on the prices:

- **The market.** News that moves the coin pushes both exchanges jointly, i.e. the state moves along $\begin{bmatrix}1\\1\end{bmatrix}$: the price *level* changes while the exchanges stay in agreement.
- **Arbitrage.** If $p_1 > p_2$, traders buy on the cheap exchange and sell on the expensive one; buying raises $p_2$, selling lowers $p_1$, so the *spread* $p_1 - p_2$ shrinks, i.e. the state moves along $\begin{bmatrix}1\\-1\end{bmatrix}$: the *disagreement* changes while the average price stays put.

Arbitrage is what couples the two coordinates: $p_1$ reacts to $p_2$ through the gap between them.

**Linear model.** Let arbitrage close a fixed fraction of the gap per unit time, at rate $k > 0$:

$$
\dot{p}_1 = -k(p_1 - p_2), \qquad \dot{p}_2 = -k(p_2 - p_1)
$$

If $p_1 > p_2$ then $\dot{p}_1 < 0$ (the expensive book is sold down) and $\dot{p}_2 > 0$ (the cheap book is bought up). In matrix form,

$$
\dot{\vec{x}} = \mathbf{A}\vec{x}, \qquad \mathbf{A} = \begin{bmatrix} -k & k \\ k & -k \end{bmatrix}
$$

**The eigenvectors are exactly those two directions.**

$$
\mathbf{A}\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}0\\0\end{bmatrix} = 0 \cdot \begin{bmatrix}1\\1\end{bmatrix}, \qquad
\mathbf{A}\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}-2k\\2k\end{bmatrix} = (-2k)\begin{bmatrix}1\\-1\end{bmatrix}
$$

So $\vec{v}_1 = [1\ 1]^{\mathsf T}$ has eigenvalue $\lambda_1 = 0$ and $\vec{v}_2 = [1\ -1]^{\mathsf T}$ has $\lambda_2 = -2k$.

- **Equilibrium direction, $\lambda_1 = 0$.** On the line $p_1 = p_2$ the spread is zero, arbitrage has nothing to do and $\mathbf{A}\vec{x} = \vec{0}$: every point of the line is an equilibrium. Strictly the line is not one vector but the **span** of $\vec{v}_1$, the eigenspace of $\lambda = 0$.
- **Convergence direction, $\lambda_2 = -2k < 0$.** Any spread is a multiple of $\vec{v}_2$ and decays like $e^{-2kt}$: prices snap back to the equilibrium line.

The two eigenspaces span the whole plane, so every price pair decomposes uniquely into one piece along the equilibrium direction and one along the convergence direction:

```{=latex}
\input{tikz/two-exchange-phase-portrait.tex}
```

**Worked gap.** Exchange 1 quotes $p_1 = 100$, exchange 2 quotes $p_2 = 96$ — a \$4 spread:

$$
\vec{x} = \begin{bmatrix}100\\96\end{bmatrix} = 98\begin{bmatrix}1\\1\end{bmatrix} + 2\begin{bmatrix}1\\-1\end{bmatrix}
$$

Check: $98 + 2 = 100$, $98 - 2 = 96$. The two pieces have direct meaning:

- $98[1\ 1]^{\mathsf T}$ — the **common part**: the mid-price $\frac{p_1+p_2}{2} = 98$;
- $2[1\ -1]^{\mathsf T}$ — the **spread part**: half the gap $\frac{p_1-p_2}{2} = 2$, the arbitrage profit per coin.

Each part evolves with its own eigenvalue, independently:

$$
\vec{x}(t) = 98\begin{bmatrix}1\\1\end{bmatrix} e^{0\cdot t} + 2\begin{bmatrix}1\\-1\end{bmatrix} e^{-2kt}
= \begin{bmatrix}98 + 2e^{-2kt} \\ 98 - 2e^{-2kt}\end{bmatrix}
$$

The common part ($\lambda = 0$) persists; the spread part ($\lambda = -2k$) decays, so both prices slide toward the mid-price 98. With $k = 1$ the gap halves in $\frac{\ln 2}{2} \approx 0.35$ time units. Sampled discretely, the gap is multiplied by $e^{-2k}$ per step — a stable eigenvalue in the sense of the discrete chapter.

**Diagonalization.** In the eigen-basis the coupled system becomes two independent scalar ODEs:

$$
\dot{\xi}_1 = 0\cdot\xi_1, \qquad \dot{\xi}_2 = -2k\,\xi_2, \qquad
\xi_1 = \frac{p_1 + p_2}{2}, \quad \xi_2 = \frac{p_1 - p_2}{2}
$$

This is $\mathbf{A} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1}$ with $\boldsymbol{\Lambda} = \operatorname{diag}(0, -2k)$: the eigenvalues are the **modes** of the system (Properties chapter) — the *level* mode persists, the *spread* mode dies out.

**More than two exchanges.** The same picture holds for $n$ exchanges, with state $\vec{p} = [p_1\ \cdots\ p_n]^{\mathsf T} \in \mathbb{R}^n$:

- The **state space** is $n$-dimensional, one coordinate per exchange.
- The **equilibrium manifold** is still 1-dimensional: "no arbitrage" means $p_1 = \cdots = p_n$, the diagonal line $\operatorname{span}\{(1,\dots,1)\}$ with eigenvalue $0$.
- The **spread space** is the $(n-1)$-dimensional hyperplane of zero-sum deviations $\{\vec{s} : \sum_i s_i = 0\}$, orthogonal to the diagonal. Every direction in it has a negative eigenvalue, so it collapses onto the equilibrium line.

With all pairs coupled at rate $k$, the dynamics matrix is the graph Laplacian of the complete graph,

$$
\mathbf{A} = k(\mathbf{J} - n\mathbf{I}), \qquad \mathbf{J} = \text{all-ones matrix}
$$

which reduces to the $2\times2$ $\mathbf{A}$ above for $n = 2$. Its spectrum: $\lambda_1 = 0$ (once, the all-ones direction) and $\lambda_2 = \cdots = \lambda_n = -kn$ (multiplicity $n-1$, the zero-sum eigenspace). More exchanges mean more arbitrage channels, so the spread decays faster.

The equilibrium manifold is 1-dimensional per *independent common price level*. It becomes a genuine higher-dimensional surface only when several such factors exist — e.g. $m$ distinct coins across the $n$ exchanges give an $m$-dimensional manifold, since arbitrage cannot force BTC's level to equal ETH's. This is the essence of **cointegration** (VECM): the dimension of the $\lambda = 0$ eigenspace counts the common factors, and everything else must mean-revert. Arbitrage does not create dimensions; it removes them.

The model is deliberately linear and input-free. Real fees, depth and latency make the arbitrage force nonlinear (linearization chapter), and external news acts as an input $\mathbf{B}\vec{u}$ that pushes the common level around, so the equilibrium line becomes a moving target the spread mode keeps chasing.

```{=latex}
\end{example}
```

## Further reading

The eigen-structure above is the mathematical skeleton of a few established fields: the 2-exchange case is *bivariate cointegration*, the $n$-exchange generalization is *Johansen's vector error-correction model* (VECM), and the market-mode / spread-modes split is the eigenvalue spectrum of return-correlation matrices.

**Cointegration and common trends** — how many $\lambda = 0$ directions (independent common price levels) a panel of prices has:

- Engle, R. and Granger, C. (1987). *Co-integration and Error Correction: Representation, Estimation, and Testing*, Econometrica — the 2-exchange (bivariate) case.
- Johansen, S. (1988; 1991). *Statistical Analysis of Cointegration Vectors* — the $n$-exchange case: the number of common trends equals $n - \operatorname{rank}\boldsymbol{\Pi}$, i.e. the dimension of the $\lambda = 0$ eigenspace.
- Stock, J. and Watson, M. (1988). *Testing for Common Trends*; Gonzalo, J. and Granger, C. (1995). *Estimation of Common Long-Memory Components in Cointegrated Systems* — the permanent (level) / transitory (spread) decomposition.

**Eigenvalue spectra of correlation matrices** — the "market mode" as the dominant eigenvalue:

- Laloux, L., Cizeau, P., Bouchaud, J.-P. and Potters, M. (2000). *Random Matrix Theory and Financial Correlations*, Int. J. Theor. Appl. Finance.
- Plerou, V., Gopikrishnan, P., Rosenow, B., Amaral, L. A. N. and Stanley, H. E. (1999). *Universal and Nonuniversal Properties of Cross-Correlations in Financial Time Series*, Phys. Rev. Lett.
- Grassi, R., Pastorino, C. and Uberti, P. (2026). *Lower Spectrum of Financial Correlation Matrices: A New Perspective on Market Synchronization*, arXiv:2608.09641 — the small eigenvalues (the spread side) carry structure too.

**Statistical arbitrage and pairs trading** — betting on the spread modes closing:

- Avellaneda, M. and Lee, J.-H. (2010). *Statistical Arbitrage in the US Equities Market*, Quantitative Finance — PCA factors plus Ornstein–Uhlenbeck residuals.
- Gatev, E., Goetzmann, W. and Rouwenhorst, K. (2006). *Pairs Trading: Performance of a Relative-Value Arbitrage Rule*, Review of Financial Studies.

**Crypto exchange arbitrage** — the specific setting:

- Makarov, D. and Schoar, A. (2020). *Trading and Arbitrage in Cryptocurrency Markets*, Journal of Financial Economics.
- Plazuelo Pascual, J., Tardón Rubio, C., Toro Cebada, J. and Hernando Veciana, A. (2025). *Price Discovery in Cryptocurrency Markets*, arXiv:2506.08718 — cointegration / Gonzalo–Granger applied to Binance vs. Uniswap and spot vs. futures.
- Zhang, D. (2025). *Efficient Triangular Arbitrage Detection via Graph Neural Networks*, arXiv:2502.03194 — the graph/network view of arbitrage.
