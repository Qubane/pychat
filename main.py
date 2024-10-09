"""
PyChat main starting file
"""


import asyncio
from src.globals import *


class Application:
    """
    Main application for pychat
    """

    def __init__(self):
        pass

    def run(self):
        """
        Runs the application
        """

    async def client_handle(self, host: str):
        """
        Handles the client's connection
        """

        reader, writer = await asyncio.open_connection(
            host, CONNECTION_PORT)

        # do something here


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
