#!/usr/bin/env python3
"""Modulo que define un cuadrado con tamaño validado y su área."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado validando su tamaño."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size
