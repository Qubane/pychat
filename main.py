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

        try:
            asyncio.run(self.run_coro())
        except KeyboardInterrupt:
            print(f"\x1b[{Terminal.height}H\x1b[0K\x1b[0mExited.", end="", flush=True)

    async def run_coro(self):
        """
        Runs the application
        """

        Terminal.command_callback = self.user_command_callback
        Terminal.key_callback = self.user_key_callback

        Terminal.init()
        await Terminal.clear()

        while True:
            await asyncio.sleep(1)

    async def user_command_callback(self, user_input: str):
        """
        User input callback
        """

        if len(user_input) == 0:
            return
        if user_input[0] == "/":
            try:
                await self.process_command(user_input[1:].split(" "))
            except Exception as e:
                await Terminal.print(e.__str__())
        else:
            await Terminal.print(user_input)

    async def user_key_callback(self, key: str):
        """
        User key
        """

    async def process_command(self, command: list[str]):
        """
        Processes given client command
        """

        match command[0]:
            case "connect":
                self.connection = connect_to_host(*command[1].split(":"))


def main():
    app = Application()
    app.run()


async def debug():
    async def key(_key: str):
        await Terminal.print(_key)

    async def command(_command: str):
        await Terminal.print(_command)

    Terminal.key_callback = key
    Terminal.command_callback = command
    Terminal.init()

    await Terminal.clear()
    await Terminal.print("Hello World!\nThis is a small test!")
    sleep(1)
    await Terminal.clear()

    while True:
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    main()
    # asyncio.run(debug())
