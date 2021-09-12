BASE_X_CORDINATE = 0
BASE_Y_CORDINATE = 4

directions = ["NORTH", "EAST", "SOUTH", "WEST"]

dir_regex = r"""(?<=^)                                    # start
                          (?P<cmd>MOVE$|LEFT$|RIGHT$|REPORT$|PLACE  # command
                          (?=\s?                                    # space
                          (?P<x>\d+),                               # x co-ord
                          (?P<y>\d+),                               # y co-ord
                          (?P<dir>NORTH|EAST|SOUTH|WEST)            # direction
                          $))                                       # EOL
                          """

patterns = {
    "dir": dir_regex
}
