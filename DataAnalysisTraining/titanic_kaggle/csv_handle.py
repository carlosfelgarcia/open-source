'''
Created on Oct 18, 2016

@author: User
'''

# External Libraries Imports
from pandas import read_csv

# Internal Imports
from interface_data import DataInterface


class CSVHandle(DataInterface):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def read_file(self, path):
        data_frame = read_csv(path)
        return data_frame

    def write_file(self, path, content):
        pass
