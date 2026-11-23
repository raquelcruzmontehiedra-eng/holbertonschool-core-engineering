#!/usr/bin/env python3
"""Demonstrates the use of mixins in Python."""


class SwimMixin:
    """Provides swimming behavior."""

    def swim(self):
        """Print the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying behavior."""

    def fly(self):
        """Print the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon with multiple abilities."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
