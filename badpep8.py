# multiple imports, each library should be on separate line
# these imports are unused so should be deleted
import sys
import random


# indentation should be consistent - always 4 spaces
# For top level functions(not in classes), there should be 2 blank lines between them
# function and variables names are all lower case and have underscore between words
def foo_bar(arg1, arg2, arg3, arg4):         # not fooBar
    return arg1, arg2, arg3, arg4          # not arg1,arg2,arg3,arg4


def bar(*args):
    # bad spacing
    # when operator is not in function call there must be spaces around it
    return 2 + 2        # not 2+2
# 2 blank lines between classes and other functions


# Bad class name, bad spacing, bad indentation
# For methods in class there should be one blank line between them
class Treehouse:
    def one(self):
        return 1

    def two(self):
        return 2


# bad identation and whitespace
# when arguments are too long they can be each on separate line
# variables shoudn't be named by single letter
alpha, beta, charlie, delta = foo_bar(
    "a long string", 
    "a longer string", 
    "yet another long string", 
    "and other crazy string")


# bad spacing
one = 1
three = 3
fourteen = 14   # make fourteen equal to 12

print(alpha)
print(fourteen)

print(Treehouse().two())


# run flake8 badpep8.py to see all errors or on http://pep8online.com/
# to see rules of pep20 -> 'import this'