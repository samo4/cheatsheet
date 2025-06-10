# Basic simulation methods

## Indirect method

Is useful when we can express the highest order derivative and when the input doesn't have any derivatives.

$$y^{(n)} = -f(y^{(n-1)}, y^{(n-2)}, \ldots, y', y, u; t)$$

- step 1: express the highest order derivative in terms of the input and the state variables (derviatives)
- step 2: create a cascade of integrators to integrate the highest order derivative to the state variables (and output)
- step 3: generate negative function using negative summation

```mermaid
graph LR
    U[u(t)] --> F["-f"]
    F --> I1["∫ dt"]
    I1 --> I2["∫ dt"]
    I2 --> I3["∫ dt"]
    I3 --> Y[y(t)]

    %% Labels for derivatives
    F -.-> |"y^(n)"| F
    I1 -.-> |"y^(n-1)"| I1
    I2 -.-> |"y^(n-2)"| I2
    I3 -.-> |"y'"| I3

    %% Feedback loops
    I1 --> F
    I2 --> F
    I3 --> F
    Y --> F

    %% Styling
    classDef inputOutput fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef integrator fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef function fill:#fff3e0,stroke:#e65100,stroke-width:2px

    class U,Y inputOutput
    class I1,I2,I3 integrator
    class F function
```
