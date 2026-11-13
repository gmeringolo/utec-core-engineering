#!/usr/bin/env python3
"""Demostración de herencia y polimorfismo con animales."""


class Animal:
    """Clase padre que representa a un animal cualquiera."""

    def speak(self):
        """Devuelve el sonido genérico de un animal."""
        return "Some sound"


class Dog(Animal):
    """Clase hija que representa a un perro."""

    def speak(self):
        """Devuelve el sonido de un perro."""
        return "Woof"


class Cat(Animal):
    """Clase hija que representa a un gato."""

    def speak(self):
        """Devuelve el sonido de un gato."""
        return "Meow"


if __name__ == "__main__":
    animals = [Dog(), Cat(), Dog()]

    for animal in animals:
        print(animal.speak())

    dog = Dog()

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))

    print(issubclass(Dog, Animal))
