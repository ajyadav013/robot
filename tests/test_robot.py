from toyrobot.point import Point
from toyrobot.robot import Robot
from toyrobot.table import Table
from toyrobot.constants import directions
from toyrobot.exceptions import MissingPlaceError, MoveOutOfBoundsError
import pytest


@pytest.mark.xfail(raises=MissingPlaceError)
def test_robot_place_negative_missing_place_error():
    point_obj = Point(0, 0)
    robot_obj = Robot()
    robot_obj.place(point_obj, "NORTH", None)


@pytest.mark.xfail(raises=MoveOutOfBoundsError)
def test_robot_place_negative_missing_place_error():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_2)
    robot_obj = Robot()
    robot_obj.place(point_3, "NORTH", table_obj)


def test_robot_place_positive():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_3)
    robot_obj = Robot()
    robot_obj.place(point_2, "NORTH", table_obj)


def test_robot_left_positive():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_3)
    robot_obj = Robot(point_2, 1, table_obj, directions=directions)
    robot_obj.left()


def test_robot_right_positive():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_3)
    robot_obj = Robot(point_2, 1, table_obj, directions=directions)
    robot_obj.right()


def test_robot_move_positive():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_3)
    robot_obj = Robot(point_2, 1, table_obj, directions=directions)
    robot_obj.move()


def test_robot_report_positive():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_3)
    robot_obj = Robot(point_2, 1, table_obj, directions=directions)
    robot_obj.report()
