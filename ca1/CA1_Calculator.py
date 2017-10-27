# -*- coding: utf-8 -*-
"""
Calculator   

"""
# import math for sin cos and tan functions
import math
 
class Calculator():
   #Addition
   def add(self, x, y):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types) and isinstance(y,number_types):
          return x + y
       #otherwise raise error
       else:
           raise ValueError
   #Division
   def divide(self,x,y):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types) and isinstance(y,number_types):
           if y ==0:
               return'nan' 
           return x / y
       #otherwise raise error
       else:
           raise ValueError
   #Multiplication
   def multiply(self,x,y):
       number_types =(int,float,complex)
       if isinstance(x,number_types) and isinstance(y,number_types):
           return x * y
       #otherwise raise error
       else:
           raise ValueError
   #Exponent
   def exponent(self,x,y):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types) and isinstance(y,number_types):
           return x ** y
       #otherwise raise error
       else:
           raise ValueError
 
   #Subtraction
   def subtract(self, x, y):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types) and isinstance(y,number_types):
           return x - y 
       else:
           raise ValueError
   #Square Root
   def square_root(self,x):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types):
           y = 0.5
           return x ** y  
       #otherwise raise error
       else:
           raise ValueError
   #Square   
   def square(self,x):
       number_types =(int,float,complex)
       if isinstance(x,number_types):
           y = x
           return x * y  
       #otherwise raise error
       else:
           raise ValueError 
   #Cube
   def cube(self,x):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types):
           y = 3
           return x ** y 
       #otherwise raise error
       else:
           raise ValueError
   #Modulo
   def modulo(self,x,y):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types) and isinstance(y,number_types):
           return x % y   
       #otherwise raise error
       else:
           raise ValueError
   #Floor Division
   def floor_division(self,x,y):
       #check number input
       number_types =(int,float,complex)
       if isinstance(x,number_types) and isinstance(y,number_types):
           return x // y   
       #otherwise raise error
       else:
           raise ValueError
   #Sine - use math import function to calculate 
   def sine_degrees(self,x):
       number_types =(int,float,complex)
       if isinstance(x,number_types):
          x = math.sin(math.radians(x))
          return x  
       #otherwise raise error
       else:
           raise ValueError
   #Cosine - use math import function to calculate 
   def cosine_degrees(self,x):
       number_types =(int,float,complex)
       if isinstance(x,number_types):
          x = math.cos(math.radians(x))
          return x 
       #otherwise raise error 
       else:
           raise ValueError
   #Sine - use math import function to calculate 
   def tangent_degrees(self,x):
       number_types =(int,float,complex) 
       if isinstance(x,number_types):
          x = math.tan(math.radians(x))
          return x  
       #otherwise raise error
       else:
           raise ValueError
