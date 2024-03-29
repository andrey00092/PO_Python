from math import pi


class Figure:
    """
    Базовый класс для геометрических фигур.
    """

    def __init__(self, color: str):
        """
        Конструктор класса Figure.

        Аргументы:
        color (str): Цвет фигуры.
        """
        self._color = color

    def area(self) -> float:
        """
        Возвращает площадь фигуры.

        Возвращает:
        float: Площадь фигуры.
        """
        pass  # Этот метод будет перегружен в дочерних классах

    def __str__(self) -> str:
        """
        Возвращает строковое представление фигуры.

        Возвращает:
        str: Строковое представление фигуры.
        """
        pass  # Этот метод будет перегружен в дочерних классах

    def __repr__(self) -> str:
        """
        Возвращает строковое представление фигуры.

        Возвращает:
        str: Строковое представление фигуры.
        """
        pass  # Этот метод будет перегружен в дочерних классах


class Circle(Figure):
    """
    Класс для круга, наследующий базовый класс Figure.
    """

    def __init__(self, color: str, radius: float):
        """
        Конструктор класса Circle.

        Аргументы:
        color (str): Цвет круга.
        radius (float): Радиус круга.

        Пример создания экземпляра класса:
        >>> circle_1 = Circle(color = "Красный", radius = 1)
        """
        super().__init__(color)
        self._radius = radius

    def area(self) -> float:
        """
        Перегруженный метод для вычисления площади круга.

        Возвращает:
        float: Площадь круга.
        """
        return pi * self._radius ** 2

    def __str__(self) -> str:
        """
        Перегруженный метод для строкового представления круга.

        Возвращает:
        str: Строковое представление круга.
        """
        return f"Круг {self._color} цвета с радиусом {self._radius}"

    def __repr__(self) -> str:
        """
        Перегруженный метод для строкового представления круга.

        Возвращает:
        str: Строковое представление круга.
        """
        return f"Круг(цвет: {self._color}, радиус: {self._radius})"


class Rectangle(Figure):
    """
    Класс для прямоугольника, наследующий базовый класс Figure.
    """

    def __init__(self, color: str, width: float, height: float):
        """
        Конструктор класса Rectangle.

        Аргументы:
        color (str): Цвет прямоугольника.
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.

        Пример создания экземпляра класса:
        >>> rectangle_1 = Rectangle(color = "Красный", width = 10, height = 5)
        """
        super().__init__(color)
        self._width = width
        self._height = height

    def area(self) -> float:
        """
        Перегруженный метод для вычисления площади прямоугольника.

        Возвращает:
        float: Площадь прямоугольника.
        """
        return self._width * self._height

    def __str__(self) -> str:
        """
        Перегруженный метод для строкового представления прямоугольника.

        Возвращает:
        str: Строковое представление прямоугольника.
        """
        return f"Прямоугольник {self._color} цвета с шириной {self._width} и высотой {self._height}"

    def __repr__(self) -> str:
        """
        Перегруженный метод для строкового представления прямоугольника.

        Возвращает:
        str: Строковое представление прямоугольника.
        """
        return f"Прямоугольник(цвет: {self._color}, ширина: {self._width}, высота: {self._height})"
