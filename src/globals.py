"""
PyChat global constant variables
"""


CONNECTION_PORT: int = 13700        # port
CONNECTION_HEARTBEAT: int = 5       # seconds

MESSAGE_RECV_BUFFER: int = 2**16
MESSAGE_TERMINATION: bytes = b'\n'
