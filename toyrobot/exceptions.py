from typing import Text, Optional


class MoveOutOfBoundsError(Exception):

    def __init__(self, exception_str: Optional[Text] = None):
        self.exception_str = exception_str or \
                             "Oops!!! The toy went out of bounds"
        print(self.exception_str)


class MissingPlaceError(Exception):

    def __init__(self, exception_str: Optional[Text] = None):
        self.exception_str = exception_str or "Oops!!! Missed Place move"
        print(self.exception_str)
