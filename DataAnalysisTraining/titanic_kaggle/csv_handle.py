'''
Created on Oct 18, 2016

@author: User
'''

# External Libraries Imports
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
        return pd.read_csv(path)

    def write_file(self, path, content):
        pass
