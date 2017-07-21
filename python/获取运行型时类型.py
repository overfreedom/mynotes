import inspect

def get_current_function_name():
    return inspect.stack()[1][3]
class MyClass:
    def function_one(self):
        print ("%s.%s invoked"%(self.__class__.__name__, get_current_function_name()))

class MyClassSon(MyClass):        
    def Otherfuntion(self):
        return ;
        
class MyClassSon2(MyClass):        
    def Otherfuntion(self):
        return;
        
if __name__ == "__main__":
    MyClassSon = MyClassSon()
    MyClassSon.function_one()