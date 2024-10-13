"""
PyChat main starting file
"""


import asyncio
from src.globals import CONNECTION_PORT, MESSAGE_TERMINATION
from src.connection import ClientConnection, connect_to_host, send_message


class Application:
    """
    Main application for pychat
    """

    def __init__(self):
        self.connection: ClientConnection | None = None

    def run(self):
        """
        Runs the application
        """

        # NOTE: temporary code, must be removed later
        asyncio.run(self.run_coro())

    async def run_coro(self):
        """
        Run coroutine
        """

        # NOTE: temporary code, must be removed later
        self.connection = await connect_to_host("127.0.0.1", CONNECTION_PORT)  # connect to loopback

        await send_message(self.connection, b'Hello world')


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
