"""
PyChat main starting file
"""


import asyncio
from time import sleep

from src.globals import *
from src.classes import *
from src.terminal import *
from src.connection import *


class Application:
    """
    Main application for pychat
    """

    def __init__(self):
        self.connection: ClientConnection | None = None

        self.scroll: int = 0
        self.messages: list[Message] = list()
        self.users: list[User] = list()

    def run(self):
        """
        Runs the application
        """

        Terminal.init()
        Terminal.clear()

    async def user_command_callback(self, user_input: str):
        """
        User input callback
        """

    async def user_key_callback(self, key: str):
        """
        User key
        """


def main():
    app = Application()
    app.run()


async def debug():
    Terminal.init()
    await Terminal.clear()

    await Terminal.print("Hello World!\nThis is a small test!")

    sleep(1)
    await Terminal.clear()


if __name__ == '__main__':
    # main()
    asyncio.run(debug())
