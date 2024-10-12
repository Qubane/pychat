"""
Connection module for PyChat
"""


import ssl
import asyncio


class ClientConnection:
    """
    Controls client connection
    """

    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.reader: asyncio.StreamReader = reader
        self.writer: asyncio.StreamWriter = writer


class ServerConnection:
    """
    Controls the server hosting the chat
    """

    def __init__(self):
        self.server: asyncio.Server | None = None
        self.client_list: list[ClientConnection] = []

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

        self.client_list.append(ClientConnection(reader, writer))


async def connect_to_host(host: str, port: int) -> ClientConnection:
    """
    Connects to the given host
    """

    return ClientConnection(*(await asyncio.open_connection(host, port)))
