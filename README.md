# Autonomous Robotics Navigation

An autonomous robotics project developed using VEX V5 and Python. The robot navigates toward a target area, detects obstacles using an AI Vision sensor and distance sensor, avoids obstacles, and uses an arm and claw mechanism to pick up and drop a target.

## Project Overview

The robot is designed to complete an autonomous navigation and pickup mission:

1. Calibrate the drivetrain inertial sensor.
2. Move forward toward the target area.
3. Detect blue obstacles using the AI Vision sensor and distance sensor.
4. Avoid detected obstacles by turning and moving forward.
5. Detect the red target using the AI Vision sensor and distance sensor.
6. Stop and pick up the target using the arm and claw.
7. Continue moving and drop the target at the designated area.
8. Display the mission status on the VEX Brain screen.

## Technologies and Components

- Python
- VEX V5
- VEXcode
- AI Vision Sensor
- Distance Sensor
- Inertial Sensor
- Drivetrain
- Arm Motor
- Claw Motor

## Main Features

- Autonomous robot navigation
- Obstacle detection and avoidance
- Color-based object detection
- Target pickup and drop-off
- Drivetrain calibration using an inertial sensor
- Arm and claw control
- On-screen mission status messages

## Robot Configuration

The robot uses:

- Two drive motors
- One arm motor
- One claw motor
- One inertial sensor
- One AI Vision sensor
- One distance sensor

## Navigation Logic

The robot continuously checks its environment while moving:

- **Blue object:** treated as an obstacle and triggers an avoidance routine.
- **Red object:** treated as the target and triggers the pickup routine.
- **No object detected:** the robot continues moving forward.

## Code Structure

The main functions include:

- `move_forward()` – moves the drivetrain forward.
- `turn_right()` / `turn_left()` – controls robot turning.
- `obstacle_detected()` – checks the distance to an obstacle.
- `avoid_obstacle()` – performs the obstacle avoidance movement.
- `open_claw()` / `close_claw()` – controls the claw.
- `lower_arm()` / `raise_arm()` – controls the arm.
- `pick_up()` – performs the target pickup sequence.
- `drop()` – releases the target.
- `main()` – controls the overall autonomous mission.

## Project Goal

The goal of this project was to develop an autonomous robot capable of navigating an environment, responding to detected obstacles, identifying a target, and completing a pickup and drop-off task with minimal human intervention.
