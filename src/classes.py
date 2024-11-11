"""
PyChat class definitions
"""


from dataclasses import dataclass


@dataclass
class User:
    """
    Basic user class
    """

    user_id: int
    nickname: str
    description: str


@dataclass(frozen=True)
class Message:
    """
    Basic message class
    """

    user_id: int
    message_id: int
    content: str
