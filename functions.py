##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
############################# SPAM FUNCTIONs #############################

## Variables
regular_spam = "SSSSSSSSSPPPPPPPPPPAAAAAAAAAAAAAAMMMMMMMMMMMMMMMMM"
more_spam = "********** SPAM **********"

## DO_twice function
#  1. Change do_twice so it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
def do_twice(function, x):
    function(x)
    function(x)
#    
## spam funciton
def spam(x):
    print(x)
#
#
do_twice(spam, more_spam)


## PRINT_twice function
#  2. Define a function called print_twice that takes one argument and prints the value of that argument twice.
def print_twice(x):
    print(x)
    print(x)
#
#
print_twice("*!$vCrazyv$!*")

#  3. Use the changed version of do_twice to call print_twice twice, passing 'spam' as an argument.
do_twice(print_twice, regular_spam)

## DO_four function
#  4. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
def do_four(function, x):
   function(x)
   function(x)

do_four(print_twice, more_spam)