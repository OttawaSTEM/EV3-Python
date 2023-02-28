#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

# Initialize the EV3 brick.
ev3 = EV3Brick()

ev3.light.on(Color.RED)