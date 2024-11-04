"""
Terminal manipulations
"""


import os


class Terminal:
    """
    Class representing terminal
    """

    width: int = 120
    height: int = 30

    @classmethod
    def init(cls):
        """
        Initializes terminal
        """

        os.system("")
        print("\x1b[?25l", end="", flush=True)
        try:
            size = os.get_terminal_size()
            cls.width = size.columns
            cls.height = size.lines
        except OSError:
            pass

    @staticmethod
    def clear() -> None:
        """
        Clears screen and buffer
        """

        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def goto(x, y) -> None:
        """
        Go to X Y pos in terminal
        """

        print(f"\x1b[{y};{x}H", end="", flush=True)
