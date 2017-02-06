# Graded and fixed a couple items.
# You had some spacing issues with your horizontal.
# You needed an end = " " statement to fix
# I added the "+" at end, also with end = "+" statement in print


'''
Grid Printer Exercise
Printing a Grid (adapted from Downey, “Think Python”, ex. 3.5)

Goal:
Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
hints
A couple features to get you started...

use print("+", end = " ") to print continuous line without carriage return

A print function with no arguments ends the current line and goes to the next line:

Simple string manipulation:
You can put two strings together with the plus operator:

"this" + "that" ===>  'thisthat'
Particularly useful if they have been assigned names:
plus = '+'
minus = '-'

You can also multiply strings:
'+' * 10 ===> '++++++++++'

Part 2
Making it more general

Make it a function
One of the points of writing functions is so you can write code that does similar things, but customized to input parameters. So what if we want to be able to print that grid at an arbitrary size?

Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.

For example,

print_grid(3) would print a small grid:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
print_grid(15) prints a larger grid:

+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +

Part 3:
Even more general...

A function with two parameters
Write a function that draws a similar grid with a specified number of rows and columns, and each cell a given size.

for example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
What to do about rounding? – you decide.

Another example: print_grid2(5,3):

+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +


#Part 1
for i in range(2):
        print("+" + (" - - - -" + " +"), ("- - - -" + " +"))
        for i in range(4):
               x = "|" + ("         ")
               print(3 * x)
print("+" + (" - - - -" + " +"), ("- - - -" + " +"))


#part 2

def print_grid(y):
        for i in range(2):
                print("+ " + ("- " * y + " +"), ("- " * y + " +"))
                for i in range(y):
                        x = "|" + (" " * (y + 1) * 2)
                        print(3 * x)
        print("+ " + ("- " * y + " +"), ("- " * y + " +"))

print_grid(7)

'''

#Part 3
#this one isnt configured correctly and I cant really figure out how to get it perfect. This is as close as I can get
def print_grid(units, length, width):
        for i in range(length):
                #print("+ " + ("- " * units + " +"), ("- " * units + " +"))
                tom = "- " * units + "+ "
                print("+ " + width * tom)


                for i in range(units):
                        x = "|" + ("  " * units) + " "
                        print((width + 1) * x)

        #print("+ " + ("- " * units + " +"), ("- " * units + " +"))
        print(width * ("+ " + ("- " * units)), end = "+")




print_grid(8, 4, 4)
