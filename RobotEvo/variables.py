# -*- coding: utf-8 -*-
"""
Created on Wed Nov  27 11:06:41 2019

@author: mdutoit
"""

def variables (Liste):
    ''' 6 proteins could be taken into account so recovery of the parameters for 6 proteins
    '''
    file = open("variables.txt","w+")
    file.write('T1,NR1,TR1,T2,NR2,TR2,T3,NR3,TR3,T4,NR4,TR4,T5,NR5,TR5,T6,NR6,TR6\n')
    for i in range(17):
        file.write(str(Liste[i]))
        file.write(',')
    file.write(str(Liste[17]))
    file.close()