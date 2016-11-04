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

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def test(self, df):
        return sns.factorplot('Sex', data=df, kind='count')
