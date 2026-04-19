import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Reproducibility
# -----------------------------
np.random.seed(42)

# -----------------------------
# Simulation
# -----------------------------
t = np.linspace(0, 20, 1000)
true_level = 0.25
acc = np.sin(0.5 * t)

A = 0.05
omega = 2
sloshing = A * np.sin(omega * t) * np.exp(-0.1 * t) * acc

noise = np.random.normal(0, 0.002, size=len(t))
measured = true_level + sloshing + noise

imu_acc = acc + np.random.normal(0, 0.01, size=len(t))

# -----------------------------
# Smooth IMU
# -----------------------------
imu_smooth = np.convolve(imu_acc, np.ones(10)/10, mode='same')

# -----------------------------
# Adaptive Kalman Filter
# -----------------------------
x = 0.25
P = 1.0

Q = 1e-6
base_R = 1e-3

estimates = []

for i in range(len(t)):
    z = measured[i]

    R = base_R + 0.08 * abs(imu_smooth[i])
    R = np.clip(R, 1e-4, 0.02)

    x_pred = x
    P_pred = P + Q

    K = P_pred / (P_pred + R)
    x = x_pred + K * (z - x_pred)
    P = (1 - K) * P_pred

    estimates.append(x)

estimates = np.array(estimates)

# -----------------------------
# Moving Average
# -----------------------------
window = 20
moving_avg = np.convolve(measured, np.ones(window)/window, mode='same')

# -----------------------------
# RMSE CALCULATION (FIXED)
# -----------------------------
true_signal = true_level * np.ones_like(t)

rmse_raw = np.sqrt(np.mean((measured - true_signal)**2))

# remove edge distortion
valid = slice(window, -window)
rmse_ma = np.sqrt(np.mean((moving_avg[valid] - true_signal[valid])**2))

rmse_adaptive = np.sqrt(np.mean((estimates - true_signal)**2))

print("RMSE Raw:", rmse_raw)
print("RMSE Moving Avg:", rmse_ma)
print("RMSE Adaptive:", rmse_adaptive)

# Convert to mm (for paper)
print("\nIn mm:")
print("Raw:", rmse_raw * 1000)
print("Moving Avg:", rmse_ma * 1000)
print("Adaptive:", rmse_adaptive * 1000)

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(12,6))

plt.plot(t, true_signal, label="True Level", linewidth=2)
plt.plot(t, measured, label="Raw Sensor", alpha=0.4)
plt.plot(t, moving_avg, label="Moving Average", linestyle="--")
plt.plot(t, estimates, label="Adaptive Kalman", linewidth=2)

plt.legend()
plt.title("Final Sloshing Compensation Comparison")
plt.xlabel("Time")
plt.ylabel("Level")
plt.grid()

plt.show()