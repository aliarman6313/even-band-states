# Solving Even Bound States in a Finite Square Well

This project numerically finds the bound state energies (even parity) for a quantum particle in a symmetric finite potential well:

\[
V(x) = 
\begin{cases}
- V_0 & |x| \le a \\
0 & |x| > a
\end{cases}
\]

Using the dimensionless transcendental equation for even states:

\[
\sqrt{V_0 - E_u} \tan(\sqrt{V_0 - E_u}) = \sqrt{E_u}
\]

Where \( E_u \) is the dimensionless energy and \( V_0 = 10 \).

## 🔧 Features

- Solves the equation numerically using scipy.optimize.fsolve.
- Automatically detects multiple valid solutions (energy levels).
- Plots both sides of the transcendental equation to visualize the intersections.

## ▶️ How to Run

`bash
pip install -r requirements.txt
python even_bound_states.py
