#CA5 - 10362185 Part A 
#Create R calculator from Python calculator from CA1 -
#  

# calculator functions

#add
add <- function(x, y) {
  return(x + y)
}
# test add(1024,128) = 1152

#subtract
subtract <- function(x, y) {
  return(x - y)
}
# test subtract(2,4) = -2

#multiply
multiply <- function(x, y) {
  return(x * y)
}
#test multiply(1024,8) = 8192

#divide
divide <- function(x, y) {
  return(x / y)
}
#test divide(48,2) = 24

#exponent
exponent <- function(x, y) {
  return(x ** y)
}
#test exponent(2,3) = 8

#square root
sq_root <- function(x, y) {
  y = 0.5
  return(x ** y)
}
#test sq_root(64) = 8

#cube
cube <- function(x, y) {
  y = 3
  return (x ** y)
}
#test cube(3) = 27
#sine
sin(x)
# test sin 30 = -0.988031624092862
#cosine
cos(x)
# test cos 30 = 0.154251449887584
#tan
tan(x)
# test tan 30 = -6.40533119664628

# set up calculator operation menu
operation <- readline(prompt="Select operation. 1.Add,2.Subtract,3.Multiply,4.Divide,5.Exponent,6.SquareRoot,7.Cube,8.Sin,9.Cosine,10.Tan :")
# prompt for user input
number1 <- readline(prompt="Enter first number: ")
# convert characters into integer
operation <- as.integer(operation)
number1 <- as.integer(number1)
# prompt user for second number note- no second number required for operations sin, cos, tan
if (operation != 8 & operation != 9 & operation != 10)
  # prompt for second number
  number2 <- readline(prompt="Enter second number: ")
  #convert character to integer
  number2 <- as.integer(number2)

#chosen operator
operator <- switch(operation,"+","-","*","/","ex","sq","cu","S","C","T")
# check operator is correct - print(paste(operator))

#call calculator function and produce result
result <- switch(operation, add(number1, number2), subtract(number1, number2), multiply(number1, number2), divide(number1, number2),exponent(number1, number2),sq_root(number1, number2),cube(number1, number2),sin(number1),cos(number1),tan(number1))
# check result is correct - print(paste(result))

#print calculator function and result
print(paste(number1, operator, number2, "=", result)) 



