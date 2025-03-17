from servo import Servo 

# Initialize the stepper motor
motor = Servo(in1_pin=0, in2_pin=4, in3_pin=16, in4_pin=17, step_mode="full", speed=1500)

# Move forward 512 steps
motor.step_motor(1, 512)

# Move backward 256 steps
motor.step_motor(-1, 256)

# Rotate exactly 90 degrees
motor.rotate_degrees(90)

# Switch to half-step mode for smoother motion
motor.set_step_mode("half")
motor.step_motor(1, 1024)  # Move with higher resolution

