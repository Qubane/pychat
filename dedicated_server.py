"""
PyChat server starting file
"""


import asyncio
from src.globals import CONNECTION_PORT
from src.connection import ServerConnection


class ServerApp(ServerConnection):
    """
    Main application for pychat
    """

    def __init__(self):
        super().__init__()

    def run(self):
        """
        Runs the application
        """

        asyncio.run(self.start_server("", CONNECTION_PORT))


def server():
    app = ServerApp()
    app.run()


if __name__ == '__main__':
    server()
