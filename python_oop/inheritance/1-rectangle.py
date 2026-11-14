#!/usr/bin/env python3
"""Modulo que define un rectángulo que hereda de BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con ancho y alto validados."""

    def __init__(self, width, height):
        """Inicializa el rectángulo validando el ancho y el alto."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
