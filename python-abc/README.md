# Python ABC (Abstract Base Classes) Project

This project explores various concepts of Object-Oriented Programming in Python, focusing on Abstract Base Classes (ABC), inheritance, mixins, and duck typing.

## Tasks Overview

### 0. Abstract Animal Class
- Implementation of an abstract base class `Animal`
- Creation of concrete classes `Dog` and `Cat`
- Demonstrates use of `@abstractmethod` decorator
- File: `task_00_abc.py`

### 1. Shapes and Duck Typing
- Abstract `Shape` class with area and perimeter methods
- Concrete implementations: `Circle` and `Rectangle`
- Demonstrates duck typing through `shape_info` function
- File: `task_01_duck_typing.py`

### 2. VerboseList Implementation
- Extension of Python's built-in list class
- Adds notification messages for list operations
- Overrides methods: append, extend, remove, pop
- File: `task_02_verboselist.py`

### 3. CountedIterator
- Custom iterator that tracks iteration count
- Extends Python's iterator functionality
- Implements `__iter__` and `__next__` methods
- File: `task_03_countediterator.py`

### 4. FlyingFish - Multiple Inheritance
- Demonstrates multiple inheritance
- Parent classes: `Fish` and `Bird`
- Child class: `FlyingFish` combining both behaviors
- File: `task_04_flyingfish.py`

### 5. Dragon - Mixin Pattern
- Implementation of mixins: `SwimMixin` and `FlyMixin`
- Demonstrates composition through mixins
- `Dragon` class combining multiple behaviors
- File: `task_05_dragon.py`

## Key Concepts Covered
- Abstract Base Classes
- Inheritance and Multiple Inheritance
- Duck Typing
- Mixins and Composition
- Method Overriding
- Iterator Protocol
- Class Extension

## Requirements
- Python 3.x
- ABC module from Python standard library

## Usage
Each task can be tested using its corresponding main file:
```bash
./main_00_abc.py
./main_01_duck_typing.py
./main_02_verboselist.py
./main_03_countediterator.py
./main_04_flyingfish.py
./main_05_dragon.py