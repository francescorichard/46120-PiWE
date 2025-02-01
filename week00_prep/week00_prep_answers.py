import numpy as np
import matplotlib.pyplot as plt

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
def evaluate_parabola(a, b, c, x):
    """Calculate y = a*x**2 + b*x+ c for a number x."""
    return a*x**2 + b*x+ c

# Example of calling evaluate_line
a, b, c, x = 1, 2, 1, 1  # define function inputs (using "unpacking", which allows multiple variable definitions on the same line)
y = evaluate_parabola(a, b, c, x)  # call the function
print(f'The value of {a}*{x}**2 + {b}*{x} + {c} is {y}')  # Here I've used f-string formatting for fancier printing. Look up a tutorial to get more info!


#EXERCISE 3
long_text = 'I love cats quite a lot. And to be honest dogs are pretty cool as well. But nothing is quite like a good slice of cake.'
sentences = long_text.split('.')
second_sentence = sentences[1]
words = second_sentence.split()
length = len(words)
print('There are %d words in the second sentence of the text' % len(words)) 

#EXERCISE 4
def evaluate_parabola_list(a, b, c, inputs):
    '''This function creates a parabola based on
    the values inside a list'''
    output = [None]*len(inputs)
    for index, x in enumerate(inputs):
        y = evaluate_parabola(a, b, c, x)
        output[index] = y
    return output
            
a, b, c, inputs = 1, 2, 1, [1, 2, 3]
y = evaluate_parabola_list(a, b, c, inputs) 
print(f'\nThe output of the parabola {a}x^2+{b}x+{c} for {inputs} is {y}\n')     

#EXERCISE 5
# -------------------------- Setting up the data to plot --------------------------

#a_line, b_line = 2, 1  # inputs to line function
a_parab, b_parab, c_parab = 1, 2, 1  # inputs to parabola function

x = range(-10, 10)  # x-values that we want to calculate and plot

#y_line = evaluate_line_list(a_line, b_line, x)  # y-values for the line
y_parabola = evaluate_parabola_list(a_parab, b_parab, c_parab, x)  # y-values for the parabola !!! TODO: Insert code here !!!

# -------------------------- Making the plot --------------------------

fig, ax = plt.subplots(figsize=(5, 3.5))  # initalize a figure and axes, specifying the aspect ratio

#ax.plot(x, y_line, label='Line')  # plot the line data, and give it a label for the legend
ax.plot(x, y_parabola, linestyle='--', label='Parabola')  # plot the parabola data, making it a dashed line and giving a label

ax.set(xlabel='x', ylabel='y')  # add labels to the x and y axes
ax.legend()  # add a legend to the plot using the labelled data

fig.tight_layout()  # scale everything to look pretty

# Place the plotting code into a function so we can re-use it in later cells without copy-pasting
def plot_lines(x, y1, y2, label1, label2):
    """Make a function to plot two lines."""
    fig, ax = plt.subplots(figsize=(5, 3.5))  # initalize a figure and axes, specifying the aspect ratio

    ax.plot(x, y1, label=label1)  # plot the line data, and give it a label for the legend
    ax.plot(x, y2, linestyle='--', label=label2)  # plot the parabola data, making it a dashed line and giving a label

    ax.set(xlabel='x', ylabel='y')  # add labels to the x and y axes
    ax.legend()  # add a legend to the plot using the labelled data

    fig.tight_layout()  # scale everything to look pretty

    return ax

#EXERCISE 6

def clip_list(x, x_min, x_max):
    """Clip the values in a list so that they fall within the given max and min values."""
    x_clip = x.copy()
    for index, num in enumerate(x_clip):
        if num <= x_min:
            x_clip[index] = x_min
        elif num >= x_max:
            x_clip[index] = x_max            
    return x_clip


x = range(-10, 11)  # x-values that we want to calculate and plot

y_unclipped = evaluate_parabola_list(a_parab, b_parab, c_parab, x)  # unclipped values
y_clipped = clip_list(y_unclipped, -5, 5)  # clipped values

plot_lines(x, y_unclipped, y_clipped, label1='Unclipped', label2='Clipped')

#EXERCISE 7
def evaluate_parabola_numpy(a, b, c, inputs):
    '''This function creates a parabola based on
    the values inside an array'''
    inputs = np.array(inputs)
    output = a*inputs**2+b*inputs+c
    return output

x = np.linspace(-10, 10)
a, b, c = 1, 2, 1
y_list = evaluate_parabola_list(a, b, c, x)
y_numpy = evaluate_parabola_numpy(a, b, c, x)
plot_lines(x, y_list, y_numpy, label1='List', label2='Numpy')

#EXERCISE 8
yparabola = {'y_unclipped': y_unclipped,'y_clipped': y_clipped}

print('\nKEYS:',yparabola.keys())

print('\nCONTENTS:')
for key, value in yparabola.items():
    print(key, value)
    print('\n')