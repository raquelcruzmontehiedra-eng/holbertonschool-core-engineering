#!/usr/bin/env python3
"""Extends the built-in list class with notifications."""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print the number of items added."""
        previous_length = len(self)
        super().extend(iterable)
        count = len(self) - previous_length
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Print a notification and remove an item."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification and return the removed item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
