'''
Created on Oct 18, 2016

@author: User
'''

# Internal Imports
from interface_data import DataInterface


class PythonHandle(DataInterface):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def read_file(self, path):
        pass
    
    def write_file(self, path, content, mode='a'):
        # Open file
        with open(path, mode) as utils_file:
            # Make sure is a new line
            utils_file.write('\n')
            # Write Function
            utils_file.write(content)
            utils_file.write('\n')
