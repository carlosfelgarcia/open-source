'''
Created on Oct 12, 2016

@author: User
'''
# External Libraries Imports


# BuiltIn Imports
import os

# Internal Classes
import data_factory
import data_analysis


class MainTitanic(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._factory = data_factory.DataFactory()
        self._data_analysis = None

    def get_data_file(self, path):
        """
            TODO
        """
        data = None
        if os.path.exists(path):
            _, ext = os.path.splitext(path)
            handle = self._factory.get_class(ext)()
            file_data = handle.read_file(path)
            self._data_analysis = data_analysis.DataAnalysis(file_data)
            
        return self._data_analysis.get_data_frame()
    
    def add_new_fucntion(self, name, function):
        """
            TODO
        """
        # Make sure is a new function
        if name in self._data_analysis.get_function_list():
            return 'Error: A function with that name already exist'
        py_handle = self._factory.get_class('.py')()
        return self._data_analysis.add_function(name, function, py_handle)
    
    def add_new_column(self, new_col_name, col1_name, col2_name, fun_name):
        """
        TODO
        """
        pass

