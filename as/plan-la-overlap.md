# Plan: remove the overlap between 02-linear-algebra and 03-state-space

Rule: 02 owns pure matrix theory; 03 keeps only what is Φ-specific and cites 02. One step per commit.

1. [x] **Eigenvalues and eigenvectors.** Merge 03's extras into 02 (Hilbert footnote, Σm_a = n, m_g = n − rank, "In practice" recipe, linear-dependence warning, defective 3×3 example). Drop the subsection from 03; keep its triangular half-jackpot line.
2. [x] **Diagonalization.** AV = VΛ derivation and column-order remark move to 02 (replacing its short version; add "always true for distinct eigenvalues"). 03 keeps the diagonal motivation, the telescoped series to the boxed Φ = Ve^{Λt}V⁻¹, RC-modes and Φ examples.
3. [x] **"Defective cannot be diagonalized"** (the [[2,1],[0,2]] argument). Keep in 02; 03 points back and keeps the "not exotic" motivation.
4. [x] **Similarity.** Delete "Similarity in one breath" from 03.
5. [x] **Jordan form.** New 02 section between Similarity and Functions: Jordan matrix, counting blocks, generalized eigenvectors + chain recipe, Schur caveat. 03 keeps Φ via Jordan: block exponential, the three examples (whole), "What the blocks tell you".
6. [x] **Cayley–Hamilton.** Theorem, Cayley/Hamilton footnote, remainder argument, interpolation view, derivative rule move into 02's "Functions of a square matrix". 03 shrinks to "apply the recipe with f(λ) = e^{λt}, α_j depend on t" + examples.
7. [x] **Forward references in 02.** Point to 03's worked examples, not to 03 as the explainer.

Untouched: Taylor, Laplace, "Choosing between the four methods", chapters 04 and 07.
