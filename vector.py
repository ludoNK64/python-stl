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

import array

typecodes = array.typecodes + '*' # '*' means everything

def _is_int(value):
	return isinstance(value, int)

def _is_slice(value):
	return isinstance(value, slice)

class vector:
	"""Vector container to store elements with a specific type."""
	def __init__(self, typecode, args=[], *, length=0, default=None):
		"""Constructor

		Arguments: 
			typecode: valid typecode contains in typecodes
			args    : elements used for initialization (tuple, list, ...)
			length  : default vector length
			default : default value assign to elements if length is not 0.

		'*' as typecode means everything so it's possible to an element of
		any type in the vector.
		"""
		if length and length > 0:
			arr = [default] * length
		elif args:
			arr = list(args)
		else: 
			pass 
		if typecode in typecodes:
			self._typecode = typecode
			if typecode != '*':
				try:
					self._array = array.array(typecode)
					self._array.fromlist(arr)
				except TypeError: 
					raise 
			else:
				self._array = []
		else:
			raise ValueError("Invalid typecode, value must be in: %s" % 
				str(typecodes))

	@property
	def typecode(self):
		return self._typecode 
		
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
		if isinstance(self._array, list):
			return self._array
		else:
			return self._array.tolist()

	def copy(self):
		"""Returns a shallow copy of the vector."""
		if isinstance(self._array, list):
			return self._array.copy()
		else:
			return list(self._array)

	def size(self):
		"""Returns the number of elements."""
		return len(self)

	def reverse(self):
		"""Reverses storage."""
		self._array.reverse()

	def clear(self):
		"""Clears all elements."""
		if isinstance(self._array, list):
			self._array.clear()
		else:
			self._array = array.array(self.typecode)

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
			self._typecode, other._typecode = other._typecode, self._typecode
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
		# otherwise, do nothing.

	# Special methods
	def __len__(self):
		return len(self._array)

	def __getitem__(self, index):
		if _is_int(index) or _is_slice(index):
			return self._array[index]

	def __setitem__(self, index, value):
		if _is_int(index) or _is_slice(index):
			self._array[index] = value 

	def __delitem__(self, index):
		if _is_int(index) or _is_slice(index):
			del self._array[index]

	def __contains__(self, value):
		return value in self._array 

	def __iter__(self):
		return iter(self._array)

	def __next__(self):
		return next(self._array)

	def __str__(self):
		return "vector('%s', %s)" % (self.typecode,
			", ".join([str(elt) for elt in self._array]))

	def __repr__(self):
		return str(self)
