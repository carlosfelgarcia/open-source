'''
Created on Nov 2, 2016

@author: co2_k
'''
# External Libraries Imports
import seaborn as sns


class PlotGenerator(object):
    '''
    classdocs
    '''

    def __init__(self, data_frame):
        '''
        Constructor
        '''
        self._data_frame = data_frame
    
    def test(self):
        sns.factorplot(x='Sex', data=self._data_frame)
