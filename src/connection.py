"""
Connection module for PyChat
"""


import asyncio
from src.globals import MESSAGE_TERMINATION


class ClientConnection:
    """
    Controls client connection
    """

    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.reader: asyncio.StreamReader = reader
        self.writer: asyncio.StreamWriter = writer

    async def send_message(self, message: bytes):
        """
        Sends a terminated message to a client/host
        """

        self.writer.write(message + MESSAGE_TERMINATION)
        await self.writer.drain()

    async def receive_message(self) -> bytes:
        """
        Receive a null terminated message
        """

        try:
            return (await self.reader.readuntil(MESSAGE_TERMINATION))[:-len(MESSAGE_TERMINATION)]
        except (asyncio.IncompleteReadError, asyncio.LimitOverrunError, OSError):
            return b''


class ServerConnection:
    """
    Controls the server hosting the chat
    """

    def __init__(self):
        self.server: asyncio.Server | None = None
        self.client_list: list[ClientConnection] = []

    async def start_server(self, host: str, port: int):
        """
        Starts the server
        """

        self.server = await asyncio.start_server(
            host=host, port=port, client_connected_cb=self.client_handle)

        async with self.server:
            try:
                await self.server.serve_forever()
            except asyncio.CancelledError:
                pass

    async def client_handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """
        Server client connection handler
        """

        served_client = ClientConnection(reader, writer)
        self.client_list.append(served_client)

        # check for messages
        while message := await served_client.receive_message():  # fetch message
            # send to everyone else
            await asyncio.gather(
                *[cli.send_message(message) for cli in self.client_list if cli is not served_client])


async def connect_to_host(host: str, port: int) -> ClientConnection:
    """
    Connects to the given host
    """

    return ClientConnection(*(await asyncio.open_connection(host, port)))
