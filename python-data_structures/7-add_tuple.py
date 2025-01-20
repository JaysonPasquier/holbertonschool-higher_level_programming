#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
	# Ensure tuple_a has at least two elements by appending (0, 0) if necessary
	tuple_a += (0, 0)
	# Ensure tuple_b has at least two elements by appending (0, 0) if necessary
	tuple_b += (0, 0)
	# Add the first two elements of each tuple and return the result as a new tuple
	return tuple(map(lambda x, y: x + y, tuple_a[:2], tuple_b[:2]))
