class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class FileNotFoundError(Error):
    """If the input file is not found.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
