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
        
    def factorplot(self, df, column):
        """
        TODO
        """
        if len(column) > 1:
            return
        return sns.factorplot(column[0], data=df, kind='count')

    def factorplot_hue(self, df, columns):
        """
        TODO
        """
        if not len(columns) == 2:
            return
        return sns.factorplot(columns[0], hue=columns[1], data=df,
                              kind='count')
