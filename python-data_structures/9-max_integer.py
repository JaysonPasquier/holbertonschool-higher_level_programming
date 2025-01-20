#!/usr/bin/python3  # Shebang line to specify the interpreter

def max_integer(my_list=[]):  # Define a function named max_integer with a default empty list as an argument
	if my_list:  # Check if the list is not empty
		return sorted(my_list)[-1]  # Return the last element of the sorted list, which is the maximum
	else:  # If the list is empty
		return None  # Return None
