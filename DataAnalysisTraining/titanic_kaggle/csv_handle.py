'''
Created on Oct 18, 2016

@author: User
'''

# External Libraries Imports
import pandas as pd

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
        """
        TODO
        """
        return pd.read_csv(path)

    def write_file(self, path, content):
        """
        TODO
        """
        if isinstance(content, pd.DataFrame):
            content.to_csv(path, index=False)
