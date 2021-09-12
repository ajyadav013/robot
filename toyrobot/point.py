class Point(object):
    """Generic Point class."""
    def __init__(self, x, y):
        self.x_co_ordinate: float = x
        self.y_co_ordinate: float = y

    def __add__(self, misc_co_ordinate):
        return Point(
            self.x_co_ordinate + misc_co_ordinate.x_co_ordinate,
            self.y_co_ordinate + misc_co_ordinate.x_co_ordinate
        )

    def __ge__(self, misc_co_ordinate):
        return \
            self.x_co_ordinate >= misc_co_ordinate.x_co_ordinate and \
            self.y_co_ordinate >= misc_co_ordinate.x_co_ordinate

    def __le__(self, misc_co_ordinate):
        return \
            self.x_co_ordinate <= misc_co_ordinate.x_co_ordinate and \
            self.y_co_ordinate <= misc_co_ordinate.x_co_ordinate
