'''
Created on Oct 12, 2016

@author: User
'''
# External Libraries Imports
import pandas as pd
from pandas import DataFrame, Series

# BuiltIn Imports
import os

# Internal Classes
import utils


class Main_Titanic(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.avaiable_funct = []
    
    def get_data(self, data_set):
        data_frame = None
        if os.path.splitext(data_set)[1] == '.csv':
            data_frame = pd.read_csv(data_set).to_dict('list')
        return data_frame
    
    def add_fucntion_to_file(self, function):
        # Open file
        with open('utils.py', 'a') as utils_file:
            # Make sure is a new line
            utils_file.write('\n')
            # Write Function
            utils_file.write(function)
            utils_file.write('\n')
    
    def test_utils(self, txt):
        reload(utils)
        utils.test(txt)
