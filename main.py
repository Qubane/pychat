"""
PyChat main starting file
"""


import asyncio
from src.globals import CONNECTION_PORT, MESSAGE_TERMINATION
from src.connection import ClientConnection, connect_to_host, send_message, receive_message


class Application:
    """
    Main application for pychat
    """

    def __init__(self):
        self.connection: ClientConnection | None = None
        self.messages: list[str] = list()

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

        address = input("Enter address: ")
        try:
            self.connection = await connect_to_host(address, CONNECTION_PORT)
        except asyncio.TimeoutError:
            return

        await send_message(self.connection, b'Random user joined!')
        while True:
            print(await receive_message(self.connection))


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
