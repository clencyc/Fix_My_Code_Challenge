class Square:
    """Represents a square with width and height properties."""

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes a Square object with width and height.

        Args:
            width (int): Width of the square.
            height (int): Height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self) -> int:
        """
        Calculates the area of the square.

        Returns:
            int: Area of the square (width * width).
        """
        return self.width * self.width

    def perimeter_of_my_square(self) -> int:
        """
        Calculates the perimeter of the square.

        Returns:
            int: Perimeter of the square (2 * width + 2 * height).
        """
        return 2 * self.width + 2 * self.height

    def __str__(self) -> str:
        """
        Returns a string representation of the square in the format "width/height".

        Returns:
            str: String representation of the square.
        """
        return f"{self.width}/{self.height}"
