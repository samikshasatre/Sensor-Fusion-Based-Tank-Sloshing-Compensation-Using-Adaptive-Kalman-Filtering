# Sensor-Fusion-Based-Tank-Sloshing-Compensation-Using-Adaptive-Kalman-Filtering
# Tank Sloshing Compensation using Adaptive Kalman Filter

## Problem

Liquid level sensors become unreliable when the system is in motion due to sloshing effects.

## Solution

A simulation-based sensor fusion system using IMU data and adaptive Kalman filtering.

## Features

* Sloshing simulation model
* Noisy sensor modeling
* IMU-based motion detection
* Adaptive Kalman filter

## Results

* Raw RMSE: 12.32 mm
* Moving Average: 12.06 mm
* Adaptive Kalman: 2.69 mm
* ~78% improvement
<img width="1536" height="754" alt="raw_system" src="https://github.com/user-attachments/assets/1c7c2f22-beff-43c3-a506-1ea77aebcbb7" />

<img width="1200" height="600" alt="signals" src="https://github.com/user-attachments/assets/8a09d20d-2fc5-473d-93fc-42430c35f0cb" />

<img width="1200" height="600" alt="Filtering Effect" src="https://github.com/user-attachments/assets/c8a49199-4c39-4931-9644-f112ebb99e46" />
  
<img width="1200" height="600" alt="final_plot" src="https://github.com/user-attachments/assets/6117104e-c4fd-43bf-ad97-51789c94c5ca" />

## Tech Stack

Python, NumPy, Matplotlib

## Applications

* Fuel tanks (automotive)
* Robotics
* Industrial liquid monitoring

## Future Work

* Real sensor integration
* Embedded system deployment
