# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""
import datetime
import unittest


from triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles_1(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangles_2(self): 

        self.assertEqual(classifyTriangle(7,7,7),'Equilateral','7,7,7 is a equilateral triangle')


    def testEquilateralTriangles_3(self): 

        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 is a equilateral triangle')


   



    def testIsosceles_1(self): 

        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 is a Isosceles triangle')
    

    def testIsosceles_2(self): 

        self.assertEqual(classifyTriangle(4,4,5),'Isosceles','4,4,5 is a Isosceles triangle')


    def testScalene_1(self):

        self.assertEqual(classifyTriangle(10,11,12),'Scalene','10,11,12 is a Scalene triangle')    



    def testScalene_2(self):

        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')    


    
    def testRight_1(self): 

        self.assertEqual(classifyTriangle(9,40,41),'Right','9,40,41 is a Right triangle')
        

    def testRight_2(self): 

        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
    

    def testRight_3(self): 

        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a Right triangle')
    


    def testInvalid_1(self):

      self.assertEqual(classifyTriangle(-4,-6,-10),'InvalidInput','Only positive values valid' )
    

    def testInvalid_2(self):

      self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','Only positive values valid' )


    def testInvalid_3(self):

      self.assertEqual(classifyTriangle(300,200,100),'InvalidInput')
    
    #def testFloatingPoint_1(self):
        #self.assertEqual(classifyTriangle(3.0, 4.0, 5.0), "Right")
        #self.assertTrue(math.isclose(5.0, 5.00000000001))
        #self.assertAlmostEqual(classifyTriangle(3.00000000001, 4.00000000001, 5.00000000001), "Right")

    #def testFloatingPoint_2(self):
        #self.assertEqual(classifyTriangle(5.2, 5.2, 5.2), "Equilateral", "5.2,5.2,5.2 is a equilateral triangle")



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
