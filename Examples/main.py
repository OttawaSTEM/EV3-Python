#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Color, Port, Button
from pybricks.tools import wait

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
motor_b = Motor(Port.B)

# Initialize a motor at port B.
touch_sensor_1 = TouchSensor(Port.S1)

while True:
    # Initialize the EV3 brick.
    ev3.light.on(Color.RED)
    # Wait
    wait(1000)
    # Turn the light off
    ev3.light.off()


    # Play a sound.
    ev3.speaker.beep()

    # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
    motor_b.run_target(500, 90)
    
    if touch_sensor_1.pressed():
        # Play another beep sound.
        ev3.speaker.beep(1000, 500)
        # Wait
        wait(200)

