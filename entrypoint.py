from re import compile, X
from sys import argv

from toyrobot.constants import directions, patterns, BASE_X_CORDINATE, BASE_Y_CORDINATE
from toyrobot.helpers import parse_data
from toyrobot.point import Point
from toyrobot.robot import Robot
from toyrobot.table import Table


def main(file, pattern="dir"):
    pattern = compile(patterns[pattern], X)
    table = Table(Point(BASE_X_CORDINATE, BASE_X_CORDINATE), Point(BASE_Y_CORDINATE, BASE_Y_CORDINATE))
    robot = Robot(directions=directions)
    parse_data(pattern=pattern, table=table, robot=robot, file=file)


if __name__ == '__main__':
    if len(argv) == 2:
        exit(main(argv[1]))
    else:
        print("****  usage: python entrypoint.py <input file>  ****")
        exit(1)
