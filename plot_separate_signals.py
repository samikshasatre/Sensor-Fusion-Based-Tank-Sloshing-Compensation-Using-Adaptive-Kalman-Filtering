import numpy as np
import matplotlib.pyplot as plt

# Simulation (same as before)
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

imu_acc = acc + np.random.normal(0, 0.01, size=len(t))

# Plot
plt.figure(figsize=(12,6))

plt.subplot(2,1,1)
plt.plot(t, true_level*np.ones_like(t), label="True Level")
plt.plot(t, measured_level, label="Measured Level")
plt.legend()
plt.title("Level Signals")

plt.subplot(2,1,2)
plt.plot(t, imu_acc, label="IMU Acceleration", color='green')
plt.legend()
plt.title("IMU Signal")

plt.tight_layout()
plt.show()