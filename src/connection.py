"""
Connection module for PyChat
"""


import asyncio


class ClientConnection:
    """
    Controls client connection
    """

    def __init__(self):
        self.reader: asyncio.StreamReader | None = None
        self.writer: asyncio.StreamWriter | None = None

    async def connect_to_host(self, host: str, port: int):
        """
        Connects client to host
        """

        self.reader, self.writer = await asyncio.open_connection(
            host, port)
