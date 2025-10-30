# Magnetics

## TLDR

In DC environment magnetic field is the consequence of current. Current creates magnetic field intensity, which circles
the current. Depending on \mju in each particular location in space, the density of magnetic field is defined.

In AC environment the ultimate source of the magnetic field still the same. But because the field is changing, the
induction comes into play. Induced voltage is trying to nullify the original field by creating the opposite field.
Or you can say that induced voltage is subtracting from the applied voltage, reducing the effective voltage and therefore the current.
Either way, the result is the same - the flux in AC excited magnetic circuit is defined by the applied voltage.

The matter and geometry of the magnetic field then define how "hard" it is to create the field. In other words, how
much current is needed. When you have a magnetic circuit with a low magnetic reluctance (analogous to electric resistance),
it's easy to create the field.

## DC Magnetic Fields

In a direct current (DC) environment, the relationship between current and magnetic field is governed by Ampere's Law:

$$\oint \vec{H} \cdot d\vec{l} = I_{enclosed}$$

This equation states that the line integral of the magnetic field intensity $\vec{H}$ around a closed path equals the current enclosed by that path.

The magnetic field intensity $\vec{H}$ (measured in A/m) relates to the magnetic flux density $\vec{B}$ (measured in Tesla) through the magnetic permeability $\mu$:

$$\vec{B} = \mu\vec{H} = \mu_0\mu_r\vec{H}$$

Where:

- $\mu_0 = 4\pi \times 10^{-7}$ H/m (the permeability of free space)
- $\mu_r$ is the relative permeability of the material (dimensionless)

The total magnetic flux $\Phi$ through a surface is given by:

$$\Phi = \int \vec{B} \cdot d\vec{A}$$

## AC Magnetic Fields and Induction

In alternating current (AC) environments, Faraday's law of induction becomes critical:

$$E = -N\frac{d\Phi}{dt}$$

For a sinusoidal AC current, the induced voltage in a coil is:

$$U_{rms} = 4.44 \times f \times N \times \hat{\Phi}$$

Where:

- $U_{rms}$ is the root mean square (effective) value of the voltage
- $\hat{\Phi}$ is the peak (maximum) value of the magnetic flux

## Magnetic Circuits

Similar to electrical circuits, magnetic circuits follow the principle:

$$\mathcal{F} = \Phi \times \mathcal{R}$$

Where:

- $\mathcal{F}$ is the magnetomotive force (MMF) = $NI$ (ampere-turns)
- $\Phi$ is the magnetic flux
- $\mathcal{R}$ is the magnetic reluctance

The magnetic reluctance of a uniform material section with length $l$, cross-sectional area $A$, and permeability $\mu$ is:

$$\mathcal{R} = \frac{l}{\mu A}$$

For a composite magnetic circuit (like a transformer with core and air gap):

$$\mathcal{R}_{total} = \mathcal{R}_{core} + \mathcal{R}_{gap} + ...$$

In AC magnetic circuits, we must also consider the core losses:

- Hysteresis loss: $P_h = k_h f B_{max}^n V$
- Eddy current loss: $P_e = k_e f^2 B_{max}^2 t^2 V$

Where $k_h$ and $k_e$ are constants, $t$ is the lamination thickness, and $V$ is the volume.

## Energy and Inductance

The energy stored in a magnetic field is:

$$W = \frac{1}{2}LI^2 = \frac{1}{2}\int \vec{H} \cdot \vec{B} \, dV$$

The inductance of a coil with $N$ turns and flux $\Phi$ when carrying current $I$ is:

$$L = \frac{N\Phi}{I} = \frac{N^2}{\mathcal{R}}$$

This fundamental relationship shows how the geometry and material properties directly affect the inductance of a component.
