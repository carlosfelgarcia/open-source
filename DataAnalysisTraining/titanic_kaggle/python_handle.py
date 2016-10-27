'''
Created on Oct 18, 2016

@author: User
'''

# Internal Imports
from interface_data import DataInterface
from shutil import copy2, move
from os import remove


class PythonHandle(DataInterface):
    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        """
        self._backup_path = None
    
    def read_file(self, path):
        """
        TODO
        """
        pass
    
    def write_file(self, path, content, mode='a', backup=False):
        """
        TODO
        """
        # Create backup if need it
        if backup:
            self.create_backup(path)
        
        # Open file
        with open(path, mode) as utils_file:
            # Make sure is a new line
            utils_file.write('\n')
            # Write Function
            utils_file.write(content)
            utils_file.write('\n')
            
    def create_backup(self, path):
        """
        TODO
        """
        path_without_ext = path.split('.py')[0]
        self._backup_path = "%s%s.py" % (path_without_ext, '_backup')
        copy2(path, self._backup_path)
        
    def delete_backup(self):
        """
        TODO
        """
        remove(self._backup_path)
        
    def rollback(self, path):
        """
        TODO
        """
        move(self._backup_path, path)

