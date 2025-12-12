# Autonomous USV Control System ⚓

![ROS 2 Jazzy](https://img.shields.io/badge/ROS_2-Jazzy-blue?logo=ros&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Ubuntu_24.04-orange?logo=ubuntu&logoColor=white)
![Language](https://img.shields.io/badge/Language-Python_3.10-yellow?logo=python&logoColor=white)

## 📋 Project Overview
This repository contains a modular control software stack for an Unmanned Surface Vehicle (USV), designed for autonomous station-keeping and safety-critical navigation. 

Built on **ROS 2 Jazzy**, the system implements a decoupled **"Sense-Think-Act"** architecture commonly used in naval robotics. It features real-time state estimation, a geofencing safety watchdog, and fail-safe propulsion control.

##  System Architecture

### 1. Perception Layer (The Sense)
* **Node:** `dummy_gps`
* **Function:** Simulates NMEA-style GPS telemetry and transforms raw coordinates into a local metric frame.
* **Visualization:** Publishes `geometry_msgs/PointStamped` for real-time vector tracking in RViz2.

### 2. Autonomy Layer (The Think)
* **Node:** `nav_brain`
* **Function:** Acts as the primary decision-making engine.
* **Algorithm:** Implements a **Geofence Watchdog**. It continuously monitors the vessel's distance from the home datum. If drift exceeds the safety radius (5m), it autonomously triggers a critical state.

### 3. Actuation Layer (The Act)
* **Node:** `motor_driver`
* **Function:** Simulates the hardware interface to the propulsion system.
* **Safety:** Priority-based command execution. It listens for `STOP_ENGINES` interrupts from the autonomy layer to cut power immediately during fault conditions.

##  Getting Started

### Prerequisites
* Ubuntu 24.04 LTS (Noble Numbat)
* ROS 2 Jazzy Jalisco
* Python 3.12+

### Installation
1.  **Create a Workspace:**
    ```bash
    mkdir -p ~/usv_ws/src
    cd ~/usv_ws/src
    ```

2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Indianaman9/autonomous_usv_control.git](https://github.com/Indianaman9/autonomous_usv_control.git)
    ```

3.  **Build the System:**
    ```bash
    cd ~/usv_ws
    colcon build --symlink-install
    source install/setup.bash
    ```

##  Usage

### One-Command Launch
Launch the entire stack (Sensors, Autonomy, Motors) using the custom launch file:
```bash
ros2 launch usv_control system_launch.py
```


## Visualization

To view the vessel's real-time position and vector:

Open a new terminal.

Run RViz2:
    Bash
```
    ros2 run rviz2 rviz2
```
   Add a PointStamped display listening to topic /usv/vis_point.
   Ensure Fixed Frame is set to map.

 Tech Stack & Skills
   Middleware: ROS 2 (DDS/RTPS communication)
   Language: Python (rclpy)
   Tools: Gazebo (Simulation concepts), RViz (Visualization), Git (VC)
   Concepts: QoS (Quality of Service), TF2 (Coordinate Transforms), Pub/Sub Pattern


