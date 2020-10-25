# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:06:41 2019

@author: jclcf
"""

def aspirate (LiquidClass,Volume1,Volume2,Volume3,Volume4,Grid,Site,Code):
    ''' não sei ainda o que estou fazendo
    '''
    
    if LiquidClass is str:
        LiquidClass = '"' + LiquidClass + '"'
    else:
        LiquidClass = '"' + str(LiquidClass) + '"'
    
    
    if Volume1 != 0:
        Volume1 = '"' + str(Volume1) + '"'
    else:
        Volume1 = str(Volume1)
        
    if Volume2 != 0:
        Volume2 = '"' + str(Volume2) + '"'
    else:
        Volume2 = str(Volume2)
        
    if Volume3 != 0:
        Volume3 = '"' + str(Volume3) + '"'
    else:
        Volume3 = str(Volume3)
        
    if Volume4 != 0:
        Volume4 = '"' + str(Volume4) + '"'
    else:
        Volume4 = str(Volume4)

    record = 'B;Aspirate(' + '6' + ',' + LiquidClass + ',' + Volume1 + ','+ Volume2 + ',' + Volume3 + ','+ Volume4 + ',' + '0' + ','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ '0' +','+ str(Grid) +','+ str(Site) + ',' + '1' + ',' +'"'+ str(Code)+'"' + ',' + '0' + ',' + '0' + ');\n'

    return record
