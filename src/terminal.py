"""
Terminal manipulations
"""


import os
import string
import asyncio
from typing import Any
from collections.abc import Callable, Awaitable
from sshkeyboard import listen_keyboard_manual


class Terminal:
    """
    Class representing terminal
    """

    width: int = 120
    height: int = 30

    key_callback: Callable[[str], Awaitable[None]] | None = None
    command_callback: Callable[[str], Awaitable[None]] | None = None

    _buffer: str = ""

    _key_cursor: int = 0
    _key_buffer: list[str] = list()

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

        asyncio.create_task(listen_keyboard_manual(
            on_press=cls._keypress,
            delay_second_char=0.05,
            lower=False))

    @classmethod
    async def print(cls, text: str, end: str = "\n") -> None:
        """
        Prints text to the terminal
        """

        cls._buffer += text + end
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

    @classmethod
    async def _keypress(cls, key: str) -> None:
        """
        Controls user keyboard input
        """

        if key in string.printable:
            cls._key_buffer.insert(cls._key_cursor, key)
        elif key == "space":
            cls._key_buffer.insert(cls._key_cursor, " ")
        elif key == "backspace":
            cls._key_buffer.pop(cls._key_cursor - 1)
        elif key == "delete":
            cls._key_buffer.pop(cls._key_cursor)
        elif key == "enter":
            asyncio.create_task(cls.command_callback(''.join(cls._key_buffer[::-1])))
            cls._key_buffer.clear()
        elif key == "left":
            cls._key_cursor -= 1
        elif key == "right":
            cls._key_cursor += 1
        else:
            asyncio.create_task(cls.key_callback(key))
