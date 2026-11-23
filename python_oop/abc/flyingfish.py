#!/usr/bin/env python3
"""Demonstrates multiple inheritance in Python."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print the swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print the flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish using multiple inheritance."""

    def fly(self):
        """Override the flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat."""
        print("The flying fish lives both in water and the sky!")
