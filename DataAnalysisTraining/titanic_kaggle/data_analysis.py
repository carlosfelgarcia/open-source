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

    def __init__(self):
        '''
        Constructor
        '''
        self._data_frame = None
        self._function_list = dir(data_functions)
        self._function_path = 'data_functions.py'
        self._data_frame_list = []
        
    def add_data_frame(self, data_frame):
        """
        TODO
        """
        self._data_frame_list.append(data_frame)
        
    def set_data_frame(self, index):
        """
        TODO
        """
        self._data_frame = self._data_frame_list[index]
        
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
    
    def add_new_column(self, new_col_name, cols_names, fun_name):
        """
        TODO
        """
        function = getattr(data_functions, fun_name)
        try:
            list_p = []
            new_column = self._data_frame[cols_names].apply(function,
                                                            axis=1,
                                                            args=(list_p,))
        except TypeError:
            new_column = self._data_frame[cols_names].apply(function,
                                                            axis=1)
        self._data_frame[new_col_name] = new_column
    
    def del_column(self, column_names):
        """
        TODO
        """
        self._data_frame = self._data_frame.drop(column_names, axis=1)
    
    def get_information(self, column_name, opperation):
        """
        TODO
        """
        if opperation == 'Mean':
            try:
                return str(self._data_frame[column_name].mean())
            except TypeError:
                return
        elif opperation == 'Value Count':
            info = self._data_frame[column_name].value_counts().to_dict()
            value = ''
            for k, v in info.iteritems():
                value += ': '.join((str(k), str(v)))
                value += '\n'
            return value
