'''
Created on Oct 18, 2016

@author: User
'''
from abc import ABCMeta, abstractmethod


class DataInterface:
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def read_file(self, path):
        pass
    
    @abstractmethod
    def write_file(self, path, content):
        pass
