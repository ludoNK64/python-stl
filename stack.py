"""Stack container.

This container gives the programmer the functionnality
of a stack, LIFO (last-in, first-out) data structure.

Methods implemented here:
    top   -> accesses the top element
    empty -> checks whether the underlying container is empty
    size  -> returns the number of elements
    push  -> inserts element at the top
    pop   -> removes the top element
    swap  -> swaps the contents
"""

from .deque import deque 

class stack:
    """Stack container class."""
    def __init__(self, typecode, args=[], *, length=0, default=None):
        """Constructor

        This uses deque as the default container for operations.
        """
        _length, _default = length, default
        self.container = deque(typecode, args, length=_length, 
            default=_default)

    def top(self):
        """accesses the top element."""
        return self.container.back()

    def empty(self):
        """Checks whether the underlying container is empty."""
        return self.container.empty()

    def size(self):
        """Returns the number of elements."""
        return self.container.size()

    def push(self, value):
        """Inserts element at the top."""
        self.container.push_back(value)

    def pop(self):
        """Removes the top element."""
        return self.container.pop_back()

    def swap(self, other):
        """Swaps the contents"""
        if isinstance(other, stack):
            self.container.swap(other.container)

    def __str__(self):
        c = self.container
        return "%s('%s', [%s])" % (self.__class__.__name__,
            c.typecode, ", ".join([str(elt) for elt in c.data()]))

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.size()
