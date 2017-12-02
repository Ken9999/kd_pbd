# -*- coding: utf-8 -*-
"""
Calculator using lists with lambda and map functions Unit Test   
Student: 10362185
CA 5 Part B   
""" 
# imports
from CA5_10362185_Calculator import Calculator 
import unittest
# Create Test Lists 
a = [1,2,3,4]
b = [17,12,11,10]
c = [40,75,100,120]
d = [4,25,5,20]

#  class TestCalculator unit test cases with Lists
class TestCalculator(unittest.TestCase):
   #Addition Tests
   def test_calculator_add(self):
       result = Calculator().add(a,b,c)
       self.assertEqual([58, 89, 114, 134],result) 
   #Subtraction Tests
   def test_calculator_subtract(self):
       result = Calculator().subtract(a,b)
       self.assertEqual([-16, -10, -8, -6],result)
   #Multiplication Tests
   def test_calculator_multiply(self):
       result = Calculator().multiply(a,b,c)
       self.assertEqual([680, 1800, 3300, 4800],result) 
   #Division Tests
   def test_calculator_divide(self):
       result = Calculator().divide(c,d)
       self.assertEqual([10, 3, 20, 6],result) 
   #Exponent Tests
   def test_calculator_exponent(self): 
       result = Calculator().exponent(a,b) 
       self.assertEqual([1, 4096, 177147, 1048576],result)  
   #Square Root Tests
   def test_calculator_square_root(self): 
       result = Calculator().square_root(c)
       self.assertEqual([6.324555320336758, 8.660254037844387, 10.0, 10.954451150103322],result) 
   #Square Tests
   def test_calculator_square(self): 
       result = Calculator().square(a)
       self.assertEqual([1, 4, 9, 16],result)  
   #Square Tests
   def test_calculator_cube(self): 
       result = Calculator().cube(a)
       self.assertEqual([1, 4, 27, 256],result)  
   #Modulo Tests
   def test_calculator_modulo(self): 
       result = Calculator().modulo(c,d)
       self.assertEqual([0, 0, 0, 0],result)  
   #Modulo Tests
   def test_calculator_floor_division(self): 
       result = Calculator().floor_division(c,d)
       self.assertEqual([10, 3, 20, 6],result)   
# Main           
if __name__ == '__main__':
    unittest.main() 











