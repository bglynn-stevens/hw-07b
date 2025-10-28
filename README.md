# HW-07b: Triangle Classification Testing

## Project Description
This project contains a Python implementation of a triangle classification function and a comprehensive test suite. The goal was to identify and fix bugs in an existing implementation through systematic testing.

## Files
- **Triangle.py**: Contains the `classifyTriangle()` function that classifies triangles based on side lengths
- **TestTriangle.py**: Contains unit tests for the triangle classification function

## How to Run Tests
```bash
python -m unittest TestTriangle
```

## Triangle Classification Rules
The function classifies triangles into the following categories:
- **Equilateral**: All three sides are equal
- **Isoceles**: Exactly two sides are equal
- **Scalene**: No sides are equal
- **Right**: Satisfies the Pythagorean theorem (a² + b² = c²)
- **NotATriangle**: Does not satisfy triangle inequality theorem
- **InvalidInput**: Invalid input (non-integer, zero, negative, or over 200)

## Author
Brooke Glynn

## Course
SSW 567 - Software Testing, Quality Assurance and Maintenance
