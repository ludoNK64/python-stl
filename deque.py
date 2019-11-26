"""Deque container.

This is a subclass of vector but adds these methods:
    push_front -> inserts element to the beginning
    pop_front  -> removes the first element
"""

from .vector import vector

class deque(vector):
    """Double-ended queue sequence container."""
    def __init__(self, typecode, args=[], *, length=0, default=None):
        """Constructor

        Arguments are the same of vector.
        """
        _length, _default = length, default
        super().__init__(typecode, args, length=_length, default=_default)

    def push_front(self, value):
        """Inserts element to the beginning."""
        self.insert(0, value)

    def pop_front(self):
        """Removes the first element."""
        self.erase(0)
