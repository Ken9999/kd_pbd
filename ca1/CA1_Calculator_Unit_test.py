# -*- coding: utf-8 -*-
"""
Calculator Unit Test

""" 
# imports
from CA1_Calculator import Calculator 
import unittest

#  class TestCalculator unit test cases
class TestCalculator(unittest.TestCase):
   #Addition Tests
   # add 5 + 5 = 10
   # add 2 + 3 = 5
   # add 2 + (-3) = -1
   # test for string values 
   def test_calculator_add(self):
       result = Calculator().add(5,5)
       self.assertEqual(10,result)
       result = Calculator().add(2,3)
       self.assertEqual(5,result)
       result = Calculator().add(2,-3)
       self.assertEqual(-1,result)
       try:
           Calculator().add('2','5')
           self.fail('should have failed')
       except ValueError:
               pass
   #Division Tests
   # divide 5/5 = 1
   # divide 5/1 = 5
   # divide 5/0.2 = 25
   # divide 5/0 = 'nan'         
   def test_calculator_divide(self):
       result = Calculator().divide(5,5)
       self.assertEqual(1,result)
       result = Calculator().divide(5,1)
       self.assertEqual(5,result)
       result = Calculator().divide(5,0.2)
       self.assertEqual(25,result)  
       result = Calculator().divide(5,4)
       self.assertEqual(1.25,result)  
       result = Calculator().divide(5,0)
       self.assertEqual('nan',result)  
       
   #Exponent Tests
   # exponent 2**2 = 4
   # exponent 7**3 = 343
   # exponent 5**5 = 3125
   # exponent 10**4 = 10000
   def test_calculator_exponent(self):
       result = Calculator().exponent(2,2)
       self.assertEqual(4,result)
       result = Calculator().exponent(7,3)
       self.assertEqual(343,result)
       result = Calculator().exponent(5,5)
       self.assertEqual(3125,result)
       result = Calculator().exponent(10,4)
       self.assertEqual(10000,result) 
    
       
   #Multiplication Tests
   # multiply 5 * 5 = 25
   # multiply 5 * 0 = 0
   # multiply 12 * 12 = 144
   # multiply 5 * 0.2 = 1
   def test_calculator_multiply(self):
       result = Calculator().multiply(5,5)
       self.assertEqual(25,result)
       result = Calculator().multiply(5,0)
       self.assertEqual(0,result)
       result = Calculator().multiply(12,12)
       self.assertEqual(144,result)
       result = Calculator().multiply(5,0.2)
       self.assertEqual(1,result)    
      
   #Subtraction Tests
   # subtract 5 - 5 = 0
   # subtract 5 - 3 = 2
   # subtract 3 - 5 = -2
   # subtract 900 - 110 = 790
   def test_calculator_subtract(self):
       result = Calculator().subtract(5,5) 
       self.assertEqual(0,result)
       result = Calculator().subtract(5,3)
       self.assertEqual(2,result)
       result = Calculator().subtract(3,5)
       self.assertEqual(-2,result)
       result = Calculator().subtract(900,110)
       self.assertEqual(790,result)
       
   #Square Root Tests
   # square root of 16 = 4
   # square root of 64 = 8
   # square root of 144 = 12
   # square root of 1024 = 32
   def test_calculator_square_root(self):
       result = Calculator().square_root(16) 
       self.assertEqual(4,result) 
       result = Calculator().square_root(64) 
       self.assertEqual(8,result) 
       result = Calculator().square_root(144)  
       self.assertEqual(12,result) 
       result = Calculator().square_root(1024) 
       self.assertEqual(32,result)  
 
   #Square Tests
   # square 4 = 16
   # square 5 = 25
   # square -2 = 4
   # square -25 = 625
   def test_calculator_square(self): 
       result = Calculator().square(4)
       self.assertEqual(16,result) 
       result = Calculator().square(5) 
       self.assertEqual(25,result)  
       result = Calculator().square(-2) 
       self.assertEqual(4,result) 
       result = Calculator().square(-25) 
       self.assertEqual(625,result) 
       
   #Cube Tests
   # cube 4 = 64
   # cube 5 = 125
   # cube -2 = -8
   # cube -250 = -15625000
   def test_calculator_cube(self): 
       result = Calculator().cube(4)
       self.assertEqual(64,result)  
       result = Calculator().cube(5) 
       self.assertEqual(125,result)  
       result = Calculator().cube(-2) 
       self.assertEqual(-8,result)  
       result = Calculator().cube(-250) 
       self.assertEqual(-15625000,result)  
       
   #Modulo Tests
   # modulo 16 % 4 = 0 
   # modulo 16 % 3 = 1
   # modulo 50 % 10 = 0 
   # modulo 119 % 3 = 2
   def test_calculator_modulo(self): 
       result = Calculator().modulo(16,4) 
       self.assertEqual(0,result) 
       result = Calculator().modulo(16,3) 
       self.assertEqual(1,result)  
       result = Calculator().modulo(50,10)  
       self.assertEqual(0,result) 
       result = Calculator().modulo(119,3) 
       self.assertEqual(2,result)  
   
   #Floor Division  Tests
   # floor division 16 % 4 = 4
   # floor division 16 % 3 = 5
   # floor division 120 % 4 = 30
   # floor division 1234 % 30 = 41
   def test_floor_divison(self): 
       result = Calculator().floor_division(16,4) 
       self.assertEqual(4,result) 
       result = Calculator().floor_division(16,3) 
       self.assertEqual(5,result)
       result = Calculator().floor_division(120,4) 
       self.assertEqual(30,result) 
       result = Calculator().floor_division(1234,30) 
       self.assertEqual(41,result) 
       
   #Sine  Tests 
   # Sine 16 degrees = 0.27563735581699916
   # Sine 20 degrees = 0.3420201433256687
   # Sine 12 degrees = 0.20791169081775934
   # Sine 123 degrees = 1.2246467991473532e-16
   def test_sine_degrees(self): 
       result = Calculator().sine_degrees(16) 
       self.assertEqual(0.27563735581699916,result)  
       result = Calculator().sine_degrees(20) 
       self.assertEqual(0.3420201433256687,result)
       result = Calculator().sine_degrees(12) 
       self.assertEqual(0.20791169081775934,result) 
       result = Calculator().sine_degrees(180) 
       self.assertEqual(1.2246467991473532e-16,result) 
       
   #Cosine  Tests
   # cosine 16 degrees = 0.9612616959383189
   # cosine 20 degrees = 0.9396926207859084
   # cosine 12 degrees = 0.9781476007338057
   # cosine 123 degrees = -1.0
   def test_cosine_degrees(self): 
       result = Calculator().cosine_degrees(16) 
       self.assertEqual(0.9612616959383189,result)  
       result = Calculator().cosine_degrees(20) 
       self.assertEqual(0.9396926207859084,result)
       result = Calculator().cosine_degrees(12) 
       self.assertEqual(0.9781476007338057,result) 
       result = Calculator().cosine_degrees(180) 
       self.assertEqual(-1.0,result) 
   #Tangent Tests
   # tan 16 degrees = 0.2867453857588079
   # tan 20 degrees = 0.36397023426620234
   # tan 12 degrees = 0.21255656167002213
   # tan 123 degrees = -1.2246467991473532e-16
   def test_tangent_degrees(self): 
       result = Calculator().tangent_degrees(16) 
       self.assertEqual(0.2867453857588079,result)  
       result = Calculator().tangent_degrees(20) 
       self.assertEqual(0.36397023426620234,result)
       result = Calculator().tangent_degrees(12) 
       self.assertEqual(0.21255656167002213,result) 
       result = Calculator().tangent_degrees(180) 
       self.assertEqual(-1.2246467991473532e-16,result)  
       

# Main          
if __name__ == '__main__':
    unittest.main()










