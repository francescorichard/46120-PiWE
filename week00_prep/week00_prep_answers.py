# Step 1: Define our function
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
