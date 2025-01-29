# Holberton School Higher Level Programming

Welcome to the Higher Level Programming repository for Holberton School. This repository contains a series of projects and exercises designed to teach and reinforce various programming concepts and languages.

## Table of Contents
- [Directories](#directories)
  - [0x00-python-hello_world](#0x00-python-hello_world)
  - [0x01-python-if_else_loops_functions](#0x01-python-if_else_loops_functions)
  - [0x02-python-import_modules](#0x02-python-import_modules)
  - [0x03-python-data_structures](#0x03-python-data_structures)
  - [0x04-python-more_data_structures](#0x04-python-more_data_structures)
  - [0x05-python-exceptions](#0x05-python-exceptions)
  - [0x06-python-classes](#0x06-python-classes)
  - [0x07-python-test_driven_development](#0x07-python-test_driven_development)
  - [0x08-python-more_classes](#0x08-python-more_classes)
- [Author](#author)

## Directories

### 0x00-python-hello_world
This directory contains introductory projects for Python programming. It covers basic syntax, printing, and simple script execution.

#### Example
```python
print("Hello, World!")
```

### 0x01-python-if_else_loops_functions
Projects in this directory focus on control flow in Python, including if/else statements, loops, and functions.

#### Example
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for i in range(10):
    print(f"{i} is even: {is_even(i)}")
```

### 0x02-python-import_modules
This directory includes exercises on how to import and use modules in Python, both built-in and custom modules.

#### Example
```python
import math

print(math.sqrt(16))
```

### 0x03-python-data_structures
Projects here cover Python data structures such as lists, tuples, and dictionaries, and their various methods and applications.

#### Example
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 0x04-python-more_data_structures
This directory extends the exploration of data structures, including sets and advanced dictionary operations.

#### Example
```python
unique_numbers = {1, 2, 3, 4, 4, 5}
print(unique_numbers)
```

### 0x05-python-exceptions
Exercises in this directory focus on handling exceptions in Python, including try/except blocks and custom exception handling.

#### Example
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 0x06-python-classes
Projects here introduce object-oriented programming in Python, covering classes, objects, attributes, and methods.

#### Example
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())
```

### 0x07-python-test_driven_development
This directory contains projects that emphasize writing tests for Python code using the `unittest` module and the principles of Test-Driven Development (TDD).

#### Example
```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()
```

### 0x08-python-more_classes
Further exploration of object-oriented programming in Python, including advanced class features and inheritance.

#### Example
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

my_cat = Cat("Whiskers")
print(my_cat.speak())
```

## Author
This repository is maintained by Jayson Pasquier. For any questions or suggestions, feel free to contact me at jayonpasquier.contact@gmail.com.
