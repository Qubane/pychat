"""
PyChat classes
"""


from dataclasses import dataclass


@dataclass
class User:
    """
    Class containing user data
    """

    username: str
    description: str


@dataclass(frozen=True)
class Message:
    """
    Class containing message data
    """

    content: str
    author: str
