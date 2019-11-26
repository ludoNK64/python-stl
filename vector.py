"""Vector container

This container implements these methods:
	at -> access specified element with bounds checking
	[] -> access specified element
	front -> access the first element
	back  -> access the last element
	data -> direct access to the underlying array
	forward_iter -> returns an iterator for forward iterations
	backward_iter -> returns an iterator for backward iterations
	size -> returns the number of elements
	capicity -> returns the number of elements that can be held in currently allocated storage
	clear -> clears contents
	insert -> inserts elements
	erase -> erases elements
	push_back -> adds an element to the end
	pop_back -> removes the last element
	resize -> changes the number of elements stored
	swap -> swaps the contents
"""

__all__ = ['typecodes', 'vector']

typecodes = {'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'f', 'd'}

def _is_int(value):
	return isinstance(value, int)

def _is_slice(value):
	return isinstance(value, slice)

class vector:
	"""Vector container to store elements with a specific type."""
	def __init__(self, typecode, args=[], *, length=0, default=None):
		"""Constructor

		Arguments: 
			typecode: 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'f', 'd', 
				'A' (any)
			length : default length
			default: default value assign to elements if length not 0.
			args:
				elements used for initialization
		"""
		if typecode in typecodes:
			if length and length > 0:
				self._array = [default] * length
			elif args:
				# Type checking in args
				self._array = list(args)
			else:
				self._array = []
		else:
			raise ValueError("Invalid typecode, value must be: %s" % 
				str(typecodes))

	def at(self, index, default=None):
		"""Access specified element at index with bounds checking.

		If index is out of range, default is return.
		"""
		if not _is_int(index):
			raise TypeError("Invalid type for 'index', got %s" % type(index))
		if index < 0 or index >= len(self):
			return default
		return self._array[index]

	def front(self, default=None):
		"""Access the first element."""
		if self._array:
			return self._array[0]
		return default

	def back(self, default=None):
		"""Access the last element."""
		if self._array:
			return self._array[-1]
		return default

	def data(self):
		"""Direct access to the underlying array."""
		return self._array

	def copy(self):
		"""Returns a shallow copy of the vector."""
		return self._array.copy()

	def size(self):
		"""Returns the number of elements."""
		return len(self)

	def reverse(self):
		"""Reverses storage."""
		self._array.reverse()

	def clear(self):
		"""Clears all elements."""
		self._array.clear()

	def insert(self, index, value):
		"""Inserts element before index."""
		if not _is_int(index):
			raise TypeError("Invalid type for 'index', got %s" % type(index))
		if index < 0 or index >= len(self):
			raise IndexError("Index out of range, bounds (0, %d)" % len(self))
		self._array.insert(index, value)

	def erase(self, index):
		"""Erases element at index."""
		if not _is_int(index):
			raise TypeError("Invalid type for 'index', got %s" % type(index))
		if index < 0 or index >= len(self):
			raise IndexError("Index out of range, bounds (0, %d)" % len(self))
		self._array.pop(index)

	def push_back(self, value):
		"""Adds element at the end."""
		self._array.append(value)

	def pop_back(self, default=None):
		"""Removes and returns the last element."""
		if self._array:
			return self._array.pop()
		else:
			return default

	def swap(self, other):
		"""Swaps vectors content."""
		if isinstance(other, vector):
			self._array, other._array = other._array, self._array

	def capacity(self):
		return self.size()

	def forward_iter(self):
		"""Returns an iterator for forward iteration."""
		for i in range(self.size()):
			yield self._array[i]  

	def backward_iter(self):
		"""Returns an iterator for backward iteration."""
		current_index = self.size() - 1
		while current_index >= 0:
			yield self._array[current_index]
			current_index -= 1

	def resize(self, count):
		"""Resizes the container to contain count elements."""
		if isinstance(count, int) and count > 0:
			self._array = self._array[:count]
		# otherwise, does nothing.

	# Special methods
	def __len__(self):
		return len(self._array)

	def __getitem__(self, index):
		if _is_int(index) or _is_slice(index):
			# Bounds limits verification here!
			return self._array[index]

	def __setitem__(self, index, value):
		if _is_int(index) or _is_slice(index):
			# Bounds limits verification here!
			self._array[index] = value 

	def __delitem__(self, index):
		if _is_int(index) or _is_slice(index):
			# Bounds limits verification here!
			del self._array[index]

	def __contains__(self, value):
		return value in self._array 

	def __iter__(self):
		return iter(self._array)

	def __next__(self):
		return next(self._array)
