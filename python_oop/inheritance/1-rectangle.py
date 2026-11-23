#!/usr/bin/env python3
"""Defines a Rectangle class."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
