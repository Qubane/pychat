"""
Terminal manipulations
"""


import os
from sshkeyboard import listen_keyboard_manual


class Terminal:
    """
    Class representing terminal
    """

    width: int = 120
    height: int = 30

    _buffer: str = ""

    @classmethod
    def init(cls) -> None:
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

    @classmethod
    async def print(cls, text: str) -> None:
        """
        Prints text to the terminal
        """

        cls._buffer += text
        await cls.update()

    @classmethod
    async def update(cls) -> None:
        """
        Updates terminal
        """

        os.system("cls" if os.name == "nt" else "clear")
        print("\x1b[H" + cls._buffer, end="", flush=True)

    @classmethod
    async def clear(cls) -> None:
        """
        Clears screen and buffer
        """

        cls._buffer = ""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    async def goto(x, y) -> None:
        """
        Go to X Y pos in terminal
        """

        print(f"\x1b[{y};{x}H", end="", flush=True)
