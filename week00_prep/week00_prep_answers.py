# EXERCISE 1
def square(x):  # inputs to the function are placed inside the parentheses
    """Calculate the square of a function."""  # This line is called a "docstring"; it is optional but recommended! It lets you explain what the function does.
    return x**2  # define what the function returns. Note that ** is the power operator, * is multiply.

# Step 2: Define our inputs and then call the function
x = 2  # define a variable "x", which has a value of 2
y = square(x)  # call function "square" on variable x, and assign the output of "square" to variable "y"
print('The value of y is', y)  # print the value of variable "y" to the console

x = 16
y = square(x)
print('The square of 16 is ',y)

#EXERCISE 2
def evaluate_line(a, b, c, x):
    """Calculate y = a*x**2 + b*x+ c for a number x."""
    return a*x**2 + b*x+ c

# Example of calling evaluate_line
a, b, c, x = 1, 2, 1, 1  # define function inputs (using "unpacking", which allows multiple variable definitions on the same line)
y = evaluate_line(a, b, c, x)  # call the function
print(f'The value of {a}*{x}**2 + {b}*{x} + {c} is {y}')  # Here I've used f-string formatting for fancier printing. Look up a tutorial to get more info!

#EXERCISE 3
long_text = 'I love cats quite a lot. And to be honest dogs are pretty cool as well. But nothing is quite like a good slice of cake.'
sentences = long_text.split()
