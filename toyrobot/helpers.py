"""
Entrypoint to the whole program.
"""
from typing import Text

from toyrobot.constants import directions
from toyrobot.point import Point
from toyrobot.table import Table
from toyrobot.robot import Robot
from toyrobot.exceptions import MoveOutOfBoundsError, MissingPlaceError


def parse_data(pattern: Text, table: Table, robot: Robot, file=None) -> None:
    """Parse and process the data from the input file
    :param pattern: regular expression pattern
    :param table: table object of the grid
    :param robot: robot object with its attributes
    :param file: input file
    :return:
    """
    if file:
        try:
            with open(file) as f:
                for line in f:  # Will read one line at a time and
                    # avoid loading the huge file into the memory
                    m = pattern.match(line.rstrip('\n'))
                    try:
                        if m is not None and m.group("cmd") == "PLACE":
                            robot = robot.place(
                                Point(
                                    float(m.group("x")),
                                    float(m.group("y"))
                                ),
                                directions.index(m.group("dir")) / 2.0,
                                table)
                        elif m is not None and hasattr(
                                robot,
                                m.group("cmd").lower()
                        ):
                            robot = getattr(robot, m.group("cmd").lower())()
                    except MoveOutOfBoundsError as mob:  # noqa F841
                        pass  # logic to be handled inside Exception
                    except MissingPlaceError as mp: # noqa F841
                        pass  # logic to be handled inside Exception
        except FileNotFoundError:
            print("Oops!!! The mentioned file doesn't exist.")
        except Exception as e:
            print(f"Exception Occurred - {e}")
