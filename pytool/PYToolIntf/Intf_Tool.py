# -*- coding:utf-8 -*-
'''
Created on 2017��6��27��

@author: Administrator
'''
import inspect

def get_current_function_name():
    return inspect.stack()[1][3]

class Intf_Tool():
    
    def use(self):        
        raise Exception(self.__class__.__name__+"未实现"+get_current_function_name()+"方法。")
        
    def init(self):
        raise Exception(self.__class__.__name__+"未实现"+get_current_function_name()+"方法。")

    def get_Tool_Name(self):
        return self._tool_name    

    def set_Tool_Name(self,str_tool_name):
        self._tool_name = str_tool_name
        
if __name__ == "__main__" :    
    it = Intf_Tool()    
    it.use()