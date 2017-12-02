# -*- coding: utf-8 -*-
"""
Calculator with Lists using lambda and map functions  
Student No: 10362185  
CA5 Part B 
"""

# Class - Calculator - for Lists using lambda and map functions
class Calculator():
   #Addition
   def add(self,a,b,c): 
       #return list of added numbers
       return map(lambda x,y,z:x+y+z, a,b,c)
   #Subtraction
   def subtract(self,a,b):
       #return list of subtracted numbers
       return map(lambda x,y:x-y, a,b)
   #Multiplication
   def multiply(self,a,b,c): 
       #return list of multiplied numbers
       return map(lambda x,y,z:x*y*z, a,b,c)
   #Division
   def divide(self,c,d):
       #return list of divided numbers
       return map(lambda x,y:x/y, c,d) 
   #Exponent    
   def exponent(self,a,b):
       #return list of exponential numbers
       return map(lambda x,y:x**y, a,b)
   #Square Root    
   def square_root(self,c):
       #return list of square roots
       return map(lambda x,y = 0.5:x**y, c)
   #Square   
   def square(self,a):
       #return list of squares
       return map(lambda x :x*x, a) 
   #Cube       
   def cube(self,a):
       #return list of cube numbers
       return map(lambda x :x**x, a)
   #Modulo   
   def modulo(self,c,d):
       #return list of modulos
       return map(lambda x,y :x%y, c,d) 
   #Floor Division
   def floor_division(self,c,d):
       #return floor division list of numbers
       return map(lambda x,y : x // y, c,d)  
       
