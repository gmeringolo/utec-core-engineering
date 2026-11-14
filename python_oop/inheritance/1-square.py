#!/usr/bin/env python3
"""Modulo que define un cuadrado que hereda de Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado con un tamaño validado."""

    def __init__(self, size):
        """Inicializa el cuadrado validando su tamaño."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size
