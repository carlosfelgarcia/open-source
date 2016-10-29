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
        self._current_py_handle = None
        self._data_analysis = None

    def get_data_file(self, path):
        """
            TODO
        """
        if os.path.exists(path):
            _, ext = os.path.splitext(path)
            handle = self._factory.get_class(ext)()
            file_data = handle.read_file(path)
            self._data_analysis = data_analysis.DataAnalysis(file_data)
            
        return self._data_analysis.get_data_frame_list()
    
    def add_new_fucntion(self, name, function):
        """
            TODO
        """
        # Make sure is a new function
        if name in self._data_analysis.get_function_list():
            return False
        self._current_py_handle = self._factory.get_class('.py')()
        self._data_analysis.add_function(name, function,
                                         self._current_py_handle)
        return True
    
    def add_new_column(self, new_col_name, col1_name, col2_name, fun_name):
        """
        TODO
        """
        # TODO Check for names of columns
        try:
            self._data_analysis.add_new_column(new_col_name, col1_name,
                                               col2_name, fun_name)
            if self._current_py_handle:
                self._data_analysis.clear_backup(self._current_py_handle)
                self._current_py_handle = None
         
        except Exception, e:
            if self._current_py_handle:
                self._data_analysis.rollback_backup(self._current_py_handle)
                self._data_analysis.clear_backup(self._current_py_handle)
                self._current_py_handle = None
            raise e
        
        return self._data_analysis.get_data_frame_list()

