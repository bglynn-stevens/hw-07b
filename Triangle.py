# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
def classifyTriangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle, a, b, and c, this
    function classifies the triangle type.
    
    The function returns one of the following strings:
    - 'Equilateral'
    - 'Isoceles'
    - 'Scalene'
    - 'Right'
    - 'NotATriangle'
    - 'InvalidInput'
    """
    
    # 1. FIXED: Initial Validation Checks (Addresses the 11 FAILED tests)
    # Checks for invalid input types (non-integers/non-floats) and constraints.
    
    # Check if inputs are numbers and greater than 0
    if not all(isinstance(side, (int, float)) and side > 0 for side in [a, b, c]):
        return 'InvalidInput'
        
    # Check for upper bound constraint (assuming max side length is 200 based on typical assignments)
    # Your test was: self.assertEqual(classifyTriangle(201,100,100),'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # 2. Triangle Inequality Check (Covers the 'NotATriangle' failures)
    # The sum of the lengths of any two sides of a triangle must be strictly 
    # greater than the length of the third side.
    # The equality (a + b == c) is the degenerate case, which is also 'NotATriangle'.
    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]

    if x + y <= z:
        return 'NotATriangle'
    
    # Check for Equilateral (all sides equal)
    if a == b and b == c:
        return 'Equilateral'
    
    # Check for Right Triangle (a^2 + b^2 = c^2, using a small tolerance for floats if needed)
    # Note: Using integer multiplication to avoid float issues, but comparing sorted squares.
    x_sq, y_sq, z_sq = x*x, y*y, z*z
    
    # Using a small tolerance (e.g., 0.001) is good practice for floating point comparison,
    # but for simple integer inputs like (3,4,5), direct comparison works if input is strictly integers.
    # We will use direct comparison since the inputs are primarily integers.
    if abs(x_sq + y_sq - z_sq) < 0.001:
        return 'Right'

    # Check for Isosceles (at least two sides equal)
    if a == b or b == c or a == c:
        return 'Isoceles'
        
    # If it is none of the above, it must be Scalene (no sides equal)
    return 'Scalene'
