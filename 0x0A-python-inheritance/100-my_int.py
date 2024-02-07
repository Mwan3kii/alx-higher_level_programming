#!/usr/bin/python3
"""This class inherits from int."""


class MyInt(int):
    """Class myint inherits from int."""

    def __eq__(self, other):
        """Does the equal one.

        Args:
            other: The other to compare to.

        Returns:
            int: The other.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Does the not equal to one.

        Args:
            other: The other to compare to.

        Returns:
            int: The other.
        """
        return super().__eq__(other)
