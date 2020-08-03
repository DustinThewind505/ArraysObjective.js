"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
def print_integer(num, str):
    print(num + int(str))


# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
def print_string(num, string):
    print(f'{str(num)}{string}')


print_integer(x, y)

print_string(x, y)