"""
PyChat class definitions
"""


class UserID:
    """
    Used ID
    """

    def __init__(self, identity: int):
        self._id: int = identity

    def __repr__(self):
        return f"{{id:{self._id}}}"

    def __int__(self):
        return self._id


class User:
    """
    Basic user class
    """

    def __init__(self, uid: UserID, nickname: str, **kwargs):
        self.user_id: UserID = uid
        self.nickname: str = nickname
        self.description: str = "no description"

        for arg, val in kwargs.items():
            setattr(self, arg, val)

    def update_info(self, **kwargs):
        """
        Updates information about the user
        :param kwargs: keyword arguments
        """

        for arg, val in kwargs.items():
            if arg == "user_id":
                raise Exception("Unable to change user id for existing user")
            setattr(self, arg, val)


class Message:
    """
    Basic message class
    """

    def __init__(self, sender: UserID, message: str, **kwargs):
        self.sender: UserID = sender
        self.message: str = message

        for arg, val in kwargs.items():
            setattr(self, arg, val)

    def __repr__(self):
        return f"{{msg by {self.sender}}}"
