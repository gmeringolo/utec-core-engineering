!/usr/bin/env python3
"""Modulo que define un cuadrado con posición y representación en texto."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con su tamaño y su posición."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y asigna el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y asigna la posición del cuadrado."""
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size

    def __str__(self):
        """Devuelve el cuadrado como texto, respetando la posición."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines += [row] * self.__size
        return "\n".join(lines)

    def my_print(self):
        """Imprime el cuadrado con el carácter #."""
        print(self)
