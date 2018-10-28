from collections import deque


class RingBuffer:
    def __init__(self, size):
        self.size = size
        self._data = deque(maxlen=size)

    def __len__(self):
        return len(self._data)

    def append(self, item):
        if len(self) < self.size:
            self._data.append(item)
        else:
            raise IndexError("append to a full RingBuffer")

    def popleft(self):
        try:
            return self._data.popleft()
        except IndexError:
            raise IndexError("popleft from an empty RingBuffer")

    def clear(self):
        self._data.clear()

    def __contains__(self, item):
        return item in self._data


class cRingBuffer:
    """Implementation study: cRingBuffer stores only bytes and uses 'pointers'
    to the beginning and end of the used part, as you would do in C or Assembler.

    To be able to distinguish a full buffer from an empty one, we allocate one
    record more than the user requested.  Hence the modulo operations can be
    optimized when the user requests a size of (2^n)-1 rather than 2^n."""
    def __init__(self, size):
        self.size = size
        self._size = size+1  # actual number of allocated records
        self._head = 0
        self._tail = 0
        self._buffer = bytearray(self._size)

    def __len__(self):
        return (self._size + self._head - self._tail) % self._size

    def append(self, item):
        if len(self) < self.size:
            self._buffer[self._head] = item
            self._head = (self._head + 1) % self._size
        else:
            # in a C implementation we would use a non-zero return value instead of an exception
            raise IndexError("append to a full RingBuffer")

    def popleft(self):
        if len(self):
            item = self._buffer[self._tail]
            self._tail = (self._tail + 1) % self._size
        else:
            # in a C implementation we would use a non-zero return value instead of an exception
            raise IndexError("popleft from an empty RingBuffer")

    def clear(self):
        self._head = self._tail

    def __contains__(self, item):
        return item in self._buffer

