#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()

# AI Vision Color Descriptions
ai_vision_7__greens = Colordesc(1, 22, 172, 49, 10, 0.2)
ai_vision_7__reds = Colordesc(2, 179, 12, 48, 10, 0.2)
ai_vision_7__blues = Colordesc(3, 103, 209, 235, 10, 0.2)

# AI Vision Code Descriptions
ai_vision_7 = AiVision(
    Ports.PORT7,
    ai_vision_7__greens,
    ai_vision_7__reds,
    ai_vision_7__blues
)

# Motors definition
arm_motor = Motor(Ports.PORT4, False)
claw_motor = Motor(Ports.PORT3, False)
left_drive_smart = Motor(Ports.PORT1, False)
right_drive_smart = Motor(Ports.PORT5, True)

drivetrain = SmartDrive(
    left_drive_smart,
    right_drive_smart,
    brain_inertial,
    259.34,
    320,
    40,
    MM,
    1
)

distance_6 = Distance(Ports.PORT6)

# Wait for sensor(s) to fully initialize
wait(100, MSEC)


# Generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)

    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000

    systemTime = brain.timer.system() * 100

    urandom.seed(int(xaxis + yaxis + zaxis + systemTime))


# Initialize random seed
initializeRandomSeed()

vexcode_initial_drivetrain_calibration_completed = False


def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    global vexcode_initial_drivetrain_calibration_completed

    sleep(200, MSEC)

    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")

    brain_inertial.calibrate()

    while brain_inertial.is_calibrating():
        sleep(25, MSEC)

    vexcode_initial_drivetrain_calibration_completed = True

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


# Calibrate the Drivetrain
calibrate_drivetrain()
#endregion VEXcode Generated Robot Configuration


# Variables
OBSTACLE_DISTANCE = 200  # mm
TARGET_DISTANCE = 100    # mm


# Navigation
def move_forward(distance, speed):
    drivetrain.set_drive_velocity(speed, PERCENT)
    drivetrain.drive_for(FORWARD, distance, MM)


def stop():
    drivetrain.stop()


def turn_right(angle):
    drivetrain.turn_for(RIGHT, angle, DEGREES)


def turn_left(angle):
    drivetrain.turn_for(LEFT, angle, DEGREES)


# Obstacle detection
def obstacle_detected():
    dist = distance_6.object_distance(MM)

    if dist is not None and dist < OBSTACLE_DISTANCE:
        return True

    return False


# Target detection
def target_detected():
    dist_t = distance_6.object_distance(MM)

    if dist_t is not None and dist_t <= TARGET_DISTANCE:
        return True

    return False


# Obstacle Avoidance
def avoid_obstacle():
    brain.screen.clear_screen()
    brain.screen.print("Blue! Avoiding Obstacle")

    stop()
    wait(200, MSEC)

    turn_right(45)
    move_forward(500, 50)


# Arm & Claw
def open_claw():
    claw_motor.spin_for(REVERSE, 90, DEGREES)


def close_claw():
    claw_motor.spin_for(FORWARD, 90, DEGREES)


def lower_arm():
    arm_motor.spin_for(FORWARD, 180, DEGREES)


def raise_arm():
    arm_motor.spin_for(REVERSE, 180, DEGREES)


def pick_up():
    brain.screen.clear_screen()
    brain.screen.print("Picking Target")

    lower_arm()
    close_claw()
    raise_arm()


def drop():
    brain.screen.clear_screen()
    brain.screen.print("Dropping Target")

    lower_arm()
    open_claw()


# Main
def main():
    raise_arm()

    move_forward(1000, 50)

    picked = False

    while not picked:

        # Check BLUE obstacle
        ai_vision_7.take_snapshot(ai_vision_7__blues)
        blue_obj = ai_vision_7.largest_object()

        if blue_obj is not None and obstacle_detected():
            avoid_obstacle()
            continue

        # Check RED ball target
        ai_vision_7.take_snapshot(ai_vision_7__reds)
        red_obj = ai_vision_7.largest_object()

        if red_obj is not None and target_detected():
            stop()
            wait(200, MSEC)

            # Signal to team B
            brain.screen.clear_screen()
            brain.screen.print("READY FOR PICKUP")

            pick_up()

            wait(200, MSEC)

            turn_left(45)

            picked = True
            break

        # Nothing detected
        move_forward(500, 50)
        wait(200, MSEC)

    # After pickup
    move_forward(500, 50)

    stop()
    wait(200, MSEC)

    drop()

    brain.screen.clear_screen()
    brain.screen.print("Mission Complete")


main()
