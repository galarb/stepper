from machine import Pin
from time import sleep_us, ticks_us

class Servo:
    full_step_sequence = [
        [1, 1, 0, 0],  # Step 1
        [0, 1, 1, 0],  # Step 2
        [0, 0, 1, 1],  # Step 3
        [1, 0, 0, 1],  # Step 4
    ]

    half_step_sequence = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
    ]

    def __init__(self, in1_pin, in2_pin, in3_pin, in4_pin, step_mode="full", speed=1000):
        """
        Initialize the stepper motor with given pins, step mode, and speed.

        :param in1_pin: GPIO pin for IN1
        :param in2_pin: GPIO pin for IN2
        :param in3_pin: GPIO pin for IN3
        :param in4_pin: GPIO pin for IN4
        :param step_mode: "full" for full-step, "half" for half-step
        :param speed: Delay in microseconds between steps (lower = faster)
        """
        self.pins = [Pin(in1_pin, Pin.OUT), Pin(in2_pin, Pin.OUT),
                     Pin(in3_pin, Pin.OUT), Pin(in4_pin, Pin.OUT)]
        self.speed = speed  # Microseconds delay between steps
        self.set_step_mode(step_mode)

    def set_step_mode(self, mode):
        """Set the step mode (full-step or half-step)."""
        if mode == "half":
            self.step_sequence = self.half_step_sequence
        else:
            self.step_sequence = self.full_step_sequence

    def step_motor(self, direction, steps):
        """
        Move the stepper motor.

        :param direction: 1 for forward, -1 for backward
        :param steps: Number of steps to move
        """
        step_count = len(self.step_sequence)
        for _ in range(steps):
            for step in self.step_sequence[::direction]:  # Forward or reverse
                for pin, value in zip(self.pins, step):
                    pin.value(value)
                sleep_us(self.speed)  # Control speed

    def rotate_degrees(self, degrees, direction=1):
        """
        Rotate the motor by a specified angle.

        :param degrees: Angle in degrees
        :param direction: 1 for forward, -1 for backward
        """
        steps_per_revolution = 2048 if len(self.step_sequence) == 4 else 4096
        steps_needed = int((degrees / 360) * steps_per_revolution)
        self.step_motor(direction, steps_needed)

