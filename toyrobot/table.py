class Table(object):
    """Generic Table class"""
    def __init__(self, lower_left_corner, upper_right_corner):
        self.lower_left_corner = lower_left_corner
        self.upper_right_corner = upper_right_corner

    def contains(self, point):
        """Check if the given point falls between the
        max edges of the table."""
        return self.lower_left_corner <= point <= self.upper_right_corner
