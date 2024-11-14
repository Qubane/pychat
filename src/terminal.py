"""
Terminal manipulations
"""


import os
import string
import asyncio
from src.colors import *
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

    _f_width: int = width - 2
    _f_cursor: int = 0
    _f_buffer: list[str] = list()

    bg_color: Color = BGColor.BLACK
    bg_field_color: Color = bg_color
    bg_field_cursor_color: Color = BGColor.GREEN

    fr_color: Color = FRColor.WHITE
    fr_field_color: Color = fr_color
    fr_field_cursor_color: Color = fr_color

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
        print("\x1b[H" + cls._buffer.replace(Color.RESET, cls.bg_color + cls.fr_color),
              end="", flush=True)
        cls.update_input_field()

    @classmethod
    async def clear(cls) -> None:
        """
        Clears screen and buffer
        """

        cls._buffer = f"{Color.RESET}"
        os.system("cls" if os.name == "nt" else "clear")
        cls.update_input_field()

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
            cls.insert_char_into_field(key, cls._f_cursor)
            cls.move_field_cursor(1)
        elif key == "space":
            cls.insert_char_into_field(" ", cls._f_cursor)
            cls.move_field_cursor(1)
        elif key == "backspace":
            cls.move_field_cursor(-1)
            cls.pop_char_from_field(cls._f_cursor)
        elif key == "delete":
            cls.pop_char_from_field(cls._f_cursor)
        elif key == "enter":
            asyncio.create_task(cls.command_callback(''.join(cls._f_buffer)))
            cls._f_buffer.clear()
            cls._f_cursor = 0
        elif key == "left":
            cls.move_field_cursor(-1)
        elif key == "right":
            cls.move_field_cursor(1)
        else:
            asyncio.create_task(cls.key_callback(key))

        # update input field
        cls.update_input_field()

    @classmethod
    def insert_char_into_field(cls, char: str, pos: int):
        """
        Inserts a character at given pos into user input field buffer
        :param char: character to insert
        :param pos: position at which to insert a character
        """

        cls._f_buffer.insert(pos, char)

    @classmethod
    def pop_char_from_field(cls, pos: int):
        """
        Pops a character from user input field buffer
        :param pos: position at which to remove a character
        """

        if 0 < len(cls._f_buffer) != pos:
            cls._f_buffer.pop(pos)

    @classmethod
    def move_field_cursor(cls, offset: int):
        """
        Moves cursor around user input field
        :param offset: cursor offset amount
        """

        cls._f_cursor = min(len(cls._f_buffer), max(0, cls._f_cursor + offset))

    @classmethod
    def update_input_field(cls):
        """
        Updates user input field
        """

        if len(cls._f_buffer) > cls._f_width:
            part = cls._f_cursor // cls._f_width
            cursor = cls._f_cursor % cls._f_width
            buf = cls._f_buffer[part * cls._f_width:(part + 1) * cls._f_width]
        else:
            cursor = cls._f_cursor
            buf = cls._f_buffer

        left = ''.join(buf[:cursor])
        middle = buf[cursor] if cursor != len(buf) else " "
        right = ''.join(buf[cursor + 1:])

        print(f"\x1b[{cls.height};0H"
              f"{cls.bg_field_color}{cls.fr_field_color}{left}"
              f"{cls.bg_field_cursor_color}{cls.fr_field_cursor_color}{middle}"
              f"{cls.bg_field_color}{cls.fr_field_color}{right}\x1b[0K",
              end="", flush=True)
