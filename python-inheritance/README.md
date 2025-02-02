# Python Inheritance Project

This project demonstrates the concepts of inheritance in Python through various scripts. Below is a brief explanation of each script in the project.

## Scripts

### 4-main.py
Tests the `inherits_from` function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

### 5-base_geometry.py
Defines an empty class `BaseGeometry`.

### 5-main.py
Tests the `BaseGeometry` class by creating an instance and printing its attributes.

### 6-base_geometry.py
Defines a class `BaseGeometry` with a method `area` that raises an exception indicating it is not implemented.

### 6-main.py
Tests the `BaseGeometry` class by attempting to call the `area` method, which should raise an exception.

### 7-base_geometry.py
Defines a class `BaseGeometry` with a method `integer_validator` that validates if a value is an integer and greater than 0.

### 7-main.py
Tests the `BaseGeometry` class by calling the `integer_validator` method with various inputs to check for proper validation and error handling.

### 8-rectangle.py
Defines a class `Rectangle` that inherits from `BaseGeometry` and implements the `__init__` method to initialize width and height with validation.

### 8-main.py
Tests the `Rectangle` class by creating instances with valid and invalid inputs and printing their attributes.

### 9-rectangle.py
Extends the `Rectangle` class to include a method `area` that calculates the area of the rectangle and a `__str__` method for string representation.

### 9-main.py
Tests the `Rectangle` class by creating an instance, printing it, and printing its area.

### 10-square.py
Defines a class `Square` that inherits from `Rectangle` and initializes with a size, which is validated and used to set both width and height.

### 10-main.py
Tests the `Square` class by creating an instance, printing it, and printing its area.

### 11-square.py
Extends the `Square` class to include a `__str__` method for string representation.

### 11-main.py
Tests the `Square` class by creating an instance, printing it, and printing its area.

## Testing

To run the tests for each script, use the following command:

```sh
python3 -m doctest tests/<test_file>.txt
```

Replace `<test_file>` with the appropriate test file name.

## License

This project is licensed under the MIT License.