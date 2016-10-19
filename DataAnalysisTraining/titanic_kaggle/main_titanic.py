'''
Created on Oct 12, 2016

@author: User
'''
# External Libraries Imports


# BuiltIn Imports
import os

# Internal Classes
import utils
import data_factory


class MainTitanic(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._function_list = dir(utils)
        self._factory = data_factory.DataFactory()

    def get_data(self, path):
        """
            TODO
        """
        data = None
        if os.path.exists(path):
            _, ext = os.path.splitext(path)
            handle = self._factory.get_class(ext)()
            data = handle.read_file(path)
        return data
    
    def add_new_fucntion(self, name, function):
        """
            TODO
        """
        # Make sure is a new function
        if name in self._function_list:
            return False
        
        self._function_list.append(name)
        handle = self._factory.get_class('.py')()
        handle.write_file('utils.py', function, 'a')
        return True
    
    def test_utils(self, txt):
        reload(utils)
        utils.test(txt)
