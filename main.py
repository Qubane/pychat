"""
PyChat main starting file
"""


import asyncio
from src.globals import *
from src.terminal import *
from src.connection import *


class Application:
    """
    Main application for pychat
    """

    def __init__(self):
        self.connection: ClientConnection | None = None

        self.scroll: int = 0
        self.messages: list[str] = list()

    def run(self):
        """
        Runs the application
        """

        Terminal.init()
        Terminal.clear()


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
