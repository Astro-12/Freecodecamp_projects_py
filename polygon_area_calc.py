class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int | float:
        return self.width * self.height

    def get_perimeter(self) -> int | float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape) -> int:
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def set_width(self, side: int) -> None:
        self.width = side
        self.height = side

    def set_height(self, side: int) -> None:
        self.width = side
        self.height = side

    def set_side(self, side: int) -> None:
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.width})"
