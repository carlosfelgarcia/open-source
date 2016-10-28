'''
Created on Oct 13, 2016

@author: Carlos Garcia
'''

def test(f='hello world'):
    print f

def male_female_child(passenger):
    # Take the Age and Sex
    age,sex = passenger
    # Compare the age, otherwise leave the sex
    if age < 16:
        return 'child'
    else:
        return sex
