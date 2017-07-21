# -*- coding:utf-8 -*-
'''
Created on 2017��6��30��

@author: Administrator
'''
from PYToolIntf.Intf_Tool import get_current_function_name

class Intf_Input(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def read(self):
        raise Exception(self.__class__.__name__+'未实现'+get_current_function_name()+'方法');

    
if __name__ == '__main__':    
    ii = Intf_Input();
    ii.read();