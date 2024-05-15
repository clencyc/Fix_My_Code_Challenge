#!/usr/bin/python3

"""
User class
"""


class User:
    """
    Represents a user with an email address.
    """

    def __init__(self):
        """
        Initializes a User object with an empty email address.
        """
        self.__email = None

    @property
    def email(self):
        """
        Gets the user's email address.

        Returns:
            str: The user's email address, or None if not set.
        """
        return self.__email

    @email.setter
    def email(self, value): # type: ignore
        """
        Sets the user's email address.

        Args:
            value (str): The email address to set.

        Raises:
            TypeError: If the provided value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)  # Output: john@snow.com
