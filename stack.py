"""Stack container.

This container gives the programmer the functionnality
of a stack, LIFO (last-in, first-out) data structure.

The stack class contains these methods:
    top   -> accesses the top element
    empty -> checks whether the underlying container is empty
    size  -> returns the number of elements
    push  -> inserts element at the top
    pop   -> removes the top element
    swap  -> swaps the contents
    copy  -> shallow copy of the stack
    clear -> removes all elements
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

    @property
    def typecode(self):
        return self.container.typecode

    def top(self):
        """Accesses the top element."""
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
        self.container.pop_back()

    def swap(self, other):
        """Swaps the contents"""
        if isinstance(other, self.__class__):
            self.container.swap(other.container)

    def copy(self):
        """Returns a shallow copy of the queue."""
        cpy = self.__class__(self.typecode)
        cpy.container = self.container.copy()
        return cpy 

    def clear(self):
        """Removes all elements."""
        self.container.clear()

    def __str__(self):
        c = self.container
        return "%s('%s', [%s])" % (self.__class__.__name__,
            c.typecode, ", ".join([str(elt) for elt in c.data()]))

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.size()
