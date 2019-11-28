"""Queue class container.

This class provides to the programmer the functionnality
of a queue-specifically, a FIFO (first-in, first-out) data
structure.

The queue class contains these methods:
    front -> access the first element
    back  -> access the last element
    empty -> checks whether the underlying container is empty
    size  -> returns the number of elements
    push  -> inserts element at the end
    pop   -> removes the first element
    swap  -> swaps the contents
    copy  -> shallow copy of the stack
    clear -> removes all elements

The default container used is deque. 
"""

from .deque import deque 

class queue:
    """Queue class container."""
    def __init__(self, typecode, args=[], *, length=0, default=None):
        """Construtor

        typecodes are those available in vector.py
        """
        _length, _default = length, default
        self.container = deque(typecode, args, length=_length, 
            default=_default)

    @property
    def typecode(self):
        return self.container.typecode

    def front(self):
        """Access the first element."""
        return self.container.front()

    def back(self):
        """Access the last element."""
        return self.container.back()

    def empty(self):
        """Checks whether the underlying container is empty."""
        return self.container.empty()

    def size(self):
        """Returns the number of elements."""
        return self.container.size()

    def push(self, value):
        """Inserts element at the end."""
        self.container.push_back(value)

    def pop(self):
        """Removes the first element."""
        self.container.pop_front()

    def swap(self, other):
        """Swaps the contents."""
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
