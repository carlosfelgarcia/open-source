'''
Created on Oct 18, 2016

@author: User
'''
# Internal Imports
import csv_handle
import python_handle


class DataFactory(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._class_list = {'.csv': csv_handle.CSVHandle, '.py': python_handle.PythonHandle}
        
    def get_class(self, data_type):
        return self._class_list[data_type]
