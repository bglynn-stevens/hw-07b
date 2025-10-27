# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
test

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    #NEW

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 should be equilateral')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles','5,5,3 should be isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(3,5,5),'Isoceles','3,5,5 should be isoceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 should be scalene')

    def testInvalidInputZero(self):
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','0,1,1 should be invalid')

    def testInvalidInputNegative(self):
        self.assertEqual(classifyTriangle(-1,5,5),'InvalidInput','-1,5,5 should be invalid')

    def testInvalidInputOver200(self):
        self.assertEqual(classifyTriangle(201,100,100),'InvalidInput','201,100,100 should be invalid')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,10),'NotATriangle','1,2,10 is not a valid triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

