from toyrobot.table import Table
from toyrobot.point import Point


def test_contains_positive():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_3)
    result = table_obj.contains(point_2)
    assert result == True


def test_contains_negative():
    point_1 = Point(0, 0)
    point_2 = Point(1, 1)
    point_3 = Point(2, 2)
    table_obj = Table(point_1, point_2)
    result = table_obj.contains(point_3)
    assert result == False
