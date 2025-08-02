import matplotlib.pyplot as plt
import numpy as np

epsilon = np.linspace(0, 0.1, 100)
delta_E = epsilon * 1e-6  # Simulación de corrimiento energético

plt.plot(epsilon, delta_E)
plt.xlabel("ε (noncommutativity parameter)")
plt.ylabel("ΔE (energy shift)")
plt.title("Exclusion Plot for Hydrogen Spectroscopy")
plt.grid(True)
plt.savefig("figures/exclusion_plot.png")
plt.show()
