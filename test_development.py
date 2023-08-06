# dependencies
import pandas as pd
import unittest
import os
import sys

# software testing levels include:
# 'good paths / happy paths' - test the code with the correct input
# 'bad paths / sad paths' - test the code with the incorrect input
'''for example, if you have 'if and else' statements, you might want to test 
both the if and else statements seperately'''

# four-levels of testing:
# 1. unit testing - testing the smallest unit of code (usually a function)
# 2. integration testing (development env) - testing the code as a whole (usually a script)
# 3. system testing (production env) - testing the code as a whole (usually a script)
# 4. user acceptance testing (production env) - testing the code as a whole (usually a script)

# test driven and behavior driven development
# test driven development (tdd) - focuses on how the system works from the inside
    # pros: tests drive the design (bottom-up approach)
    # you write the tests first, then write the code
    # focuses on: "are we building the thing right?"
# behavior driven development (bdd) - focuses on the the behaviot of the system from the 'outside'
    # pros: works great for integration testing, uses syntax that both developers and stakeholders can understand (top-down approach)
    # focuses on: "are we building the right thing?"
# when testing, you will use both tdd and bdd

def area_of_a_triangle(base: float, height: float) -> float:
    '''function to calculate the area of a triangle given
    non-negative numbers for the base and height'''
    if type(base) not in [int, float]:
        raise TypeError('The base must be a non-negative real number.')
    
    elif type(height) not in [int, float]:
        raise TypeError('The height must be a non-negative real number.')
    
    # check if we have the correct parameter valyes
    elif base < 0: 
        raise ValueError('The base must be a non-negative real number.')
    elif height < 0:
        raise ValueError('The height must be a non-negative real number.')

    return (base/2) * height

test_data = [(3.5,8.5), # float
             (4,9), # int
             (-1,5), # negative
             (0,0), # zero
             (True, 5), # boolean
             ("base", 5)] # string

for data in test_data:
    print(f'The area of a triangle {data}'\
          f' is: {area_of_a_triangle(*data)}')
    
    # tip: avoid raising too broad of an exception
    # ideally, you want to be as explicit and specific as possible when raising errors

    