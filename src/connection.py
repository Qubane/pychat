"""
Connection module for PyChat
"""


import ssl
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


class ServerConnection:
    """
    Controls the server hosting the chat
    """

    def __init__(self):
        self.server: asyncio.Server | None = None

    async def start_server(self, host: str, port: int, ctx: ssl.SSLContext | None = None):
        """
        Starts the server
        """

        self.server = await asyncio.start_server(
            host=host, port=port, ssl=ctx,
            client_connected_cb=self.client_handle)

        async with self.server:
            await self.server.serve_forever()

    async def client_handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """
        Server client connection handler
        """
