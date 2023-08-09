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
# behavior driven development (bdd) - focuses on the the behavirt of the system from the 'outside'
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

# notes on tdd - 
# testing has the following benefits:
# 1. it helps you to write better code
# 2. it helps you to write code faster
# 3. it helps you to write code that is easier to maintain
# 4. it helps you to write code that is easier to debug
# 5. it helps you to write code that is easier to scale
# 6. it helps you to write code that is easier to collaborate on
# 7. it helps you to write code that is easier to document
    
# ----------------------------------------------------------------------------------------------------------------------------
# Tuesday, 08/08/2023

# red, green, refactor - refers to 
# 1. red - write a test that fails
# 2. green - write the code to make the test pass
# 3. refactor - improve the code without changing the functionality

# automate all testing - this is a key principle of DevOps
# tdd saves development time and ensures that the code is working as expected
# so what is automated testing?

# automated testing is the process of writing code to test your code
# some python testing frameworks and tools include:
# 1. unittest
# 2. pytest

# PyUnit
# this package/library is built into Python

# Pytest
# this package/library is not built into Python
# you will need to install it using pip

# DocTest
# this package/library is built into Python
# it is used to test code in docstrings
# good for low-scale testing, but not necessarily for large-scale testing

# Nose
# this package/library is not built into Python
# it is a wrapper for unittest and doctest
# Code Coverage - refers to the percentage of code that is covered by tests

# unittest examples:
# how do i create a virtual environment?
# python -m venv <name of virtual environment>
# what is the defualt name of the virtual environment?
# venv

