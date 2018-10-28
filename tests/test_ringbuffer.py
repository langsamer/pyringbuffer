# from ringbuffer import RingBuffer
from ringbuffer import cRingBuffer as RingBuffer
import random
import pytest


def test_ringbuffer_init():
    rb = RingBuffer(16)
    assert len(rb) == 0  # fresh buffer is empty


def test_ringbuffer_has_size():
    n = random.randint(1, 2000)
    rb = RingBuffer(n)
    assert rb.size == n


def test_ringbuffer_has_append():
    rb = RingBuffer(16)
    rb.append(42)


def test_ringbuffer_elem_in_rb_after_append():
    """After you append an item to a RingBuffer, the item is in the RingBuffer"""
    rb = RingBuffer(16)
    rb.append(42)
    assert 42 in rb


def test_ringbuffer_append_increases_length():
    """pushing to a RingBuffer increases its length by 1"""
    rblength = 16
    rb = RingBuffer(rblength)
    # fill buffer with random number of elements, but at most length-1
    n = random.randint(1,rblength-1)
    for i in range(n):
        rb.append(n)

    rb.append(42)

    assert len(rb) == n+1


def test_ringbuffer_popleft_decreases_length():
    """popping from a RingBuffer reduces its length by 1"""
    rblength = 16
    rb = RingBuffer(rblength)
    # fill buffer with random number of elements, but at least 1
    n = random.randint(1,rblength)
    for i in range(n):
        rb.append(n)

    rb.popleft()

    assert len(rb) == n-1


def test_ringbuffer_cannot_append_when_full():
    """pushing to a full RingBuffer fails"""
    rblength = 16
    rb = RingBuffer(rblength)
    for i in range(rblength):
        rb.append(i)

    with pytest.raises(IndexError):
        rb.append(42)


def test_ringbuffer_cannot_popleft_when_empty():
    """popping from an empty RingBuffer fails"""
    rb = RingBuffer(16)
    with pytest.raises(IndexError):
        rb.popleft()


def test_ringbuffer_clear_empties_buffer():
    """clearing a RingBuffer leaves it empty: len(rb)==0"""
    rblength = 16
    rb = RingBuffer(rblength)
    # fill buffer with random number of elements, but at least 1
    n = random.randint(1,rblength)
    for i in range(n):
        rb.append(n)

    rb.clear()

    assert len(rb) == 0
