

from typing import Any


class InterfaceInstancingError(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def interface(cls:type) -> type:   
    

    class metaInterface:
        
        def __new__(clss, *args, **kwargs):
            print(clss)
            if issubclass(cls, metaInterface):
                print("foobargggggg")
            return object.__new__(clss,*args,**kwargs)

   
    
    jclass = type(cls.__name__, (cls,metaInterface), cls.__annotations__)
    inst = jclass()
    
 

        #raise InterfaceInstancingError("Interfaces cannot be instances by them selves.")
        
    
    #print(jclass)
    
    return jclass


@interface
class MyClass:
   
    def method_1(): 
            pass

class My2Class(MyClass):
    
    def __init__(self):
        pass
    
    def method_2():
        pass

foo = MyClass()  # Should raise an error
fog = My2Class()  # Creating an instance should work fine

#print(dir(fog))
print(isinstance(fog, MyClass))  # Should return True
print(isinstance(fog, My2Class))  # Should return True
print(isinstance(MyClass, My2Class))  # Should return False