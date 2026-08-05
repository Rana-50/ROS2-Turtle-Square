# 🐢ROS2-Turtle-Square

## 📌 Project Overview

This project demonstrates how to control the TurtleSim robot in ROS 2 Humble using a Python publisher. The turtle moves forward and performs four 90-degree left turns to draw a square.

## ✨ Features

- Control TurtleSim using a ROS 2 Publisher.
- Move the turtle forward.
- Turn left by 90 degrees.
- Draw a complete square.
- Stop automatically after completing the path.

## 🛠 Requirements

- Ubuntu 22.04 LTS
- ROS 2 Humble
- Python 3
- turtlesim
- rclpy

## ▶️ How to Run

1. Start TurtleSim:
ros2 run turtlesim turtlesim_node

2. Open another terminal and source ROS 2:
source /opt/ros/humble/setup.bash

3. Navigate to the project folder:
cd ~/turtle_scripts

4. Run the script:
python3 turtle_square.py

## 💻 Technologies Used

- ROS 2 Humble
- Python
- rclpy
- TurtleSim

## ✅ Result

The turtle successfully draws a square by moving forward and turning 90 degrees four times.
