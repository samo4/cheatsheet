Mostly yes. For understanding the dynamics, Jordan gives more insight. I wouldn't cut Laplace completely, though; I'd shrink it.

**What Jordan gives you that nothing else in this chapter does:**
- **The structure of the modes.** It tells you not just which λ appear but how they appear: how many independent modes share a λ, and how long each t-chain is.
- **Stability on the imaginary axis.** This is the one case where the eigenvalues alone can't decide. Jordan is the only clean explanation of why the double integrator is unstable while 0₂ₓ₂ is not.
- **Controllability and observability.** Blocks that share a λ can't all be steered by one input (Gilbert's criterion). This leads straight into the Properties chapter.
- **Why the methods agree.** Cayley–Hamilton's derivative trick, repeated poles in partial fractions, and the factor k in discrete time all come from the same block exponential.
- **Discrete time.** A nilpotent A (a single Jordan block at λ = 0) is the deadbeat response, which settles in finite time. That's worth having later in the course.

**What Laplace gives you, and why it's cheap to keep:**
- Students already know the mechanics. What's new is a single identity, e^{At} = ℒ⁻¹{(sI − A)⁻¹}.
- That resolvent is exactly the object the transfer-function chapter needs, G(s) = C(sI − A)⁻¹B + D. The Φ section is a natural place to introduce it.
- A point in Jordan's favour that also connects the two: the pole order of (sI − A)⁻¹ at λ equals the size of the largest Jordan block at λ. So Laplace can see how long the longest chain is, but not how many blocks there are. That second number, m_g, is exactly what decides controllability. It's a neat sentence that ties the two sections together.

**How I'd weigh it as course design:**
- **Laplace:** a short section with the identity and one 2×2 example, plus the link to G(s). Most of the current Laplace section is really the worked nonhomogeneous mass-spring problem. That problem is about the convolution integral, not about Laplace, and could live under "Nonhomogeneous solution".
- **Jordan:** full conceptual treatment (blocks, chains, the block exponential, and "What the blocks tell you"). Computing chains by hand is only needed up to 3×3, and I'd make that clear to students.
- **Caveat:** Jordan asks for more linear-algebra maturity, and it's useless numerically. Frame it as a tool for thinking, which the notes already do.

In short: Laplace is the bridge to transfer functions, and Jordan is the explanation of how the system behaves. If one has to shrink, shrink Laplace.

If you'd like, I can add the pole-order sentence to the Jordan section, or move the mass-spring convolution example out of the Laplace section.
