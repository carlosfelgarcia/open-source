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
    
    def get_data_frame_list(self):
        """
        TODO
        """
        return self._data_frame.to_dict('list')
    
    def add_function(self, name, function, py_handle):
        """
        TODO
        """
        self._function_list.append(name)
        py_handle.write_file(self._function_path, function, 'a', True)
        try:
            reload(data_functions)
        except SyntaxError:
            py_handle.rollback(self._function_path)
            return 'Error: There are some Syntax errors in your function'
    
    def clear_backup(self, py_handle):
        """
        TODO
        """
        py_handle.delete_backup()
        
    def rollback(self, py_handle):
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
        print "new funct ", dir(data_functions)
        function = getattr(data_functions, fun_name)
        print type(function)
        new_column = self._data_frame[[col1_name, col2_name]].apply(function,
                                                                    axis=1)
        self._data_frame[new_col_name] = new_column
        return self._data_frame
