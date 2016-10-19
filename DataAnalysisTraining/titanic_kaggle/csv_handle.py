'''
Created on Oct 18, 2016

@author: User
'''

# External Libraries Imports
import pandas as pd

# Internal Imports
import interface_data


class CSVHandle(interface_data):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        pass

    def read_file(self, path):
        data_frame = pd.read_csv(path).to_dict('list')
        return data_frame

    def write_file(self, path):
        pass
