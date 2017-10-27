# Calculator Input Program

# import
from CA1_Calculator import Calculator 

#  Maths Operations
operation = input('''
****************
*  Calculator  * 
****************

---- Available Operations -----

+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
s for square  
r for square root
c for cube
f for floor division
S for Sine (note use capital S)
C for Cosine (note use capital C)
T for Tangent (note use capital T)

------------------------------

Please type in the math operation you would like to complete: 
''')
    
# Input number 
number1 = int(input('Please enter number: '))

# Input 2nd number if required
if operation != 's' and operation != 'r' and operation != 'c'and operation != 'S' and operation != 'C' and operation != 'T':
   number2 = int(input('Please enter a second number: '))

# Perform requested operations
# Addition
if operation == '+': 
   print(Calculator().add(number1,number2))
# Subtraction
elif operation == '-':
    print(Calculator().subtract(number1,number2))
# Multiplication
elif operation == '*':
    print(Calculator().multiply(number1,number2))
# Division
elif operation == '/':
    print(Calculator().divide(number1,number2)) 
# Exponent    
elif operation == '**':
    print(Calculator().exponent(number1,number2))
# Modulo
elif operation == '%':
    print(Calculator().modulo(number1,number2)) 
# Floor Division
elif operation == 'f':
    print(Calculator().floor_division(number1,number2)) 
# Square Root
elif operation == 'r':
    print(Calculator().square_root(number1)) 
# Cube
elif operation == 'c':
    print(Calculator().cube(number1)) 
# Square
elif operation == 's':
    print(Calculator().square(number1))  
# Sine
elif operation == 'S':
    print(Calculator().sine_degrees(number1)) 
# Cosine
elif operation == 'C': 
    print(Calculator().cosine_degrees(number1))  
# Tangent
elif operation == 'T':
    print(Calculator().tangent_degrees(number1))  
# Otherwise report Error Message
else:
   print('You have not typed a valid operator, please run the program again.')
#x=30
#sine_degrees = math.sin(math.radians(x))
#print ('rounded sine of x is ', round(sine_degrees,20))
#
#x=30
#cosine_degrees = math.cos(math.radians(x))
#print ('rounded cosine of x is ', round(cosine_degrees,20))
#
#x=30
#tangent_degrees = math.tan(math.radians(x))
#print ('rounded tangent of x is ', round(tangent_degrees,20))
