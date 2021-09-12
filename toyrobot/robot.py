from math import pi, sin, cos
from typing import List

from toyrobot.point import Point
from toyrobot.table import Table
from toyrobot.exceptions import MoveOutOfBoundsError, MissingPlaceError


class Robot(object):
    """Generic Robot Class."""
    def __init__(self, location=Point(0.0, 0.0),
                 facing: float = 0.0,
                 table: Table = None,
                 directions=None):
        self.location = location
        self.facing = facing
        self.table = table
        self.directions: List = directions

    def left(self):
        """Turn the robot on the left side."""
        return self.place(self.location, (self.facing - 0.5) % 2, self.table)

    def right(self):
        """Turn the robot on the right side."""
        return self.place(self.location, (self.facing + 0.5) % 2, self.table)

    def move(self):
        """Move the robot."""
        return self.place(
            self.location + Point(
                sin(pi * self.facing),
                cos(pi * self.facing)
            ),
            self.facing,
            self.table)

    def report(self):
        """Report the position of the robot."""
        if self.table is not None:
            print(
                round(self.location.x_co_ordinate),
                round(self.location.y_co_ordinate),
                self.directions[round(self.facing * 2)])
        return self

    def place(self, location, facing, table):
        """Place the robot on the table."""
        if not table:
            raise MissingPlaceError()
        if not table.contains(location):
            raise MoveOutOfBoundsError()
        return Robot(location, facing, table, self.directions)
