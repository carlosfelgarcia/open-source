'''
Created on Oct 25, 2016

@author: User
'''
# Internal Imports
import data_functions


class DataAnalysis(object):
    '''
    classdocs
    '''

    def __init__(self, data_frame):
        '''
        Constructor
        '''
        self._data_frame = data_frame
        self._function_list = dir(data_functions)
        self._function_path = 'data_functions.py'
        
    def set_data_frame(self, data_frame):
        """
        TODO
        """
        self._data_frame = data_frame
        
    def get_data_frame(self):
        """
        TODO
        """
        return self._data_frame
    
    def add_function(self, name, function, py_handle):
        """
        TODO
        """
        py_handle.write_file(self._function_path, function, 'a', True)
        try:
            reload(data_functions)
            self._function_list.append(name)
            return True
        except SyntaxError:
            py_handle.rollback(self._function_path)
            return False
    
    def clear_backup(self, py_handle):
        """
        TODO
        """
        py_handle.delete_backup()
        
    def rollback_backup(self, py_handle):
        """
        TODO
        """
        py_handle.rollback(self._function_path)
    
    def get_function_list(self):
        """
        TODO
        """
        return self._function_list
    
    def add_new_column(self, new_col_name, col1_name, col2_name, fun_name):
        """
        TODO
        """
        function = getattr(data_functions, fun_name)
        new_column = self._data_frame[[col1_name, col2_name]].apply(function,
                                                                    axis=1)
        self._data_frame[new_col_name] = new_column
        return self._data_frame
    
    def del_column(self, column_names):
        """
        TODO
        """
        self._data_frame = self._data_frame.drop(column_names, axis=1)
        return self._data_frame
