"""
Terminal colors
"""


from enum import StrEnum


class Color(StrEnum):
    """
    Color Enum
    """

    RESET = "\x1b[0m"


class FRColor(Color):
    """
    Foreground color
    """

    BLACK = "\x1b[30m"
    BRIGHT_BLACK = "\x1b[90m"

    WHITE = "\x1b[37m"
    BRIGHT_WHITE = "\x1b[97m"

    RED = "\x1b[31m"
    BRIGHT_RED = "\x1b[91m"

    GREEN = "\x1b[32m"
    BRIGHT_GREEN = "\x1b[92m"

    YELLOW = "\x1b[33m"
    BRIGHT_YELLOW = "\x1b[93m"

    BLUE = "\x1b[34m"
    BRIGHT_BLUE = "\x1b[94m"

    MAGENTA = "\x1b[35m"
    BRIGHT_MAGENTA = "\x1b[95m"

    CYAN = "\x1b[36m"
    BRIGHT_CYAN = "\x1b[96m"


class BGColor(Color):
    """
    Background color
    """

    BLACK = "\x1b[40m"
    BRIGHT_BLACK = "\x1b[100m"

    WHITE = "\x1b[47m"
    BRIGHT_WHITE = "\x1b[107m"

    RED = "\x1b[41m"
    BRIGHT_RED = "\x1b[101m"

    GREEN = "\x1b[42m"
    BRIGHT_GREEN = "\x1b[102m"

    YELLOW = "\x1b[43m"
    BRIGHT_YELLOW = "\x1b[103m"

    BLUE = "\x1b[44m"
    BRIGHT_BLUE = "\x1b[104m"

    MAGENTA = "\x1b[45m"
    BRIGHT_MAGENTA = "\x1b[105m"

    CYAN = "\x1b[46m"
    BRIGHT_CYAN = "\x1b[106m"
