import numpy as np
import matplotlib.pyplot as plt

# Simulation
t = np.linspace(0, 20, 1000)
true_level = 0.25
acc = np.sin(0.5 * t)

A = 0.05
omega = 2
sloshing = A * np.sin(omega * t) * np.exp(-0.1 * t) * acc

noise = np.random.normal(0, 0.002, size=len(t))
measured_level = true_level + sloshing + noise

delay = 20
measured_level = np.roll(measured_level, delay)

# Filtering
window_size = 20
filtered_level = np.convolve(
    measured_level,
    np.ones(window_size)/window_size,
    mode='same'
)

# Plot
plt.figure(figsize=(12,6))

plt.plot(t, true_level*np.ones_like(t), label="True Level", linewidth=2)
plt.plot(t, measured_level, label="Raw Sensor", alpha=0.6)
plt.plot(t, filtered_level, label="Filtered Output", linewidth=2)

plt.title("Filtering Effect")
plt.xlabel("Time")
plt.ylabel("Level")
plt.legend()
plt.grid()

plt.show()