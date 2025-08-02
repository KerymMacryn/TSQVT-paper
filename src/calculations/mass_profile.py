import numpy as np

def mass_profile(r, m0=1.0, epsilon=0.01):
    """Position-dependent mass profile."""
    return m0 * (1 + epsilon * np.exp(-r**2))

# Ejemplo de uso
r_values = np.linspace(0, 10, 100)
m_values = mass_profile(r_values)
