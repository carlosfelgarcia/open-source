'''
Created on Oct 12, 2016

@author: User
'''
# External Libraries Imports
import pandas as pd
from pandas import DataFrame, Series

# BuiltIn Imports
import os

class Main_Titanic(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def get_data(self, data_set):
        data_frame = None
        if os.path.splitext(data_set)[1] == '.csv':
            data_frame = pd.read_csv(data_set).to_dict('list')
        return data_frame
