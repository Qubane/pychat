"""
PyChat class definitions
"""


class User:
    """
    Basic user class
    """

    def __init__(self, user_id: int, nickname: str, **kwargs):
        self.user_id: int = user_id
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

    def __init__(self, user_id: int, message: str, **kwargs):
        self.user_id: int = user_id
        self.message: str = message

        for arg, val in kwargs.items():
            setattr(self, arg, val)

    def __repr__(self):
        return f"{{msg by {self.user_id}}}"
