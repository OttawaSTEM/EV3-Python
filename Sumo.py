#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the EV3 brick.
ev3 = EV3Brick()

ev3.light.on(Color.RED)
wait(1000)
ev3.light.on(Color.YELLOW)
wait(1000)