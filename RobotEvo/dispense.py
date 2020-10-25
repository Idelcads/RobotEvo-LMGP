# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:28:05 2019

@author: jclcf
"""

def dispense (LiquidClass,Volume1,Volume2,Volume3,Volume4,Grid,Site,Code):
    ''' não sei ainda o que estou fazendo
    '''
    record = 'B;Dispense('+ '15' + ',' + '"'+str(LiquidClass)+'"' + ',' + '"'+str(Volume1)+'"' + ',' +'"'+str(Volume2)+'"' + ',' +'"'+str(Volume3)+'"' + ',' +'"'+str(Volume4)+'"' + ','  + '0' + ','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ str(Grid)+',' + str(Site) + ',' + '1' + ',' + '"'+str(Code)+'"' + ',' + '0' + ',' + '0' +  '); \n'
    return record
    