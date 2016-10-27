'''
Created on Oct 25, 2016

@author: User
'''
import data_functions


class DataAnalysis(object):
    '''
    classdocs
    '''

    def __init__(self, data_frame):
        '''
        Constructor
        '''
        self._current_data_frame = data_frame
        self._function_list = dir(data_functions)
        self._function_path = 'data_functions.py'
        
    def set_data_frame(self, data_frame):
        """
        TODO
        """
        self._current_data_frame = data_frame
        
    def get_data_frame(self):
        """
        TODO
        """
        return self._current_data_frame
    
    def add_function(self, name, function, py_handle):
        """
        TODO
        """
        self._function_list.append(name)
        py_handle.write_file(self._function_path, function, 'a', True)
        try:
            reload(data_functions)
            py_handle.delete_backup()
        except SyntaxError:
            py_handle.rollback(self._function_path)
            return 'Error: There are some Syntax errors in your function'
    
    def get_function_list(self):
        """
        TODO
        """
        return self._function_list
