"""Vector container

This container implements these methods:
	assign -> assign values to the container
	at -> access specified element with bounds checking
	[] -> access specified element
	front -> access the first element
	back  -> access the last element
	data -> direct access to the underlying array
	begin -> returns an iterator to the beginning
	end -> returns and iterator to the end
	cbegin
	cend
	crbegin
	crend
	size -> returns the number of elements
	max_size -> returns the maximum possible number of elements
	reserve -> reverses storage
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
	def __init__(self, typecode, *, length=0, default=None, *args):
		"""Constructor

		Arguments: 
			typecode: 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'f', 'd', 
				'A' (any)
			length : default length
			default: default value assign to elements if length not 0.
			args:
				if 1 -> becomes length
				otherwise -> elements used for initialization
		"""
		if typecode in typecodes:
			if length and length > 0:
				self._array = [default] * length
			elif args:
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
		"""Inserts element at index."""
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

	def emplace_back(self, value):
		raise NotImplementedError

	def swap(self, other):
		raise NotImplementedError

	def max_size(self):
		return NotImplemented

	def capacity(self):
		return NotImplemented

	def begin(self):
		return NotImplemented 

	def end(self):
		return NotImplemented 

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
