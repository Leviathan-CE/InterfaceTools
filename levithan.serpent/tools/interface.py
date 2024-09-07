

from typing import Any


class InterfaceInstancingError(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def interface(cls:type) -> type:   
    

    class metaInterface:
        
        def __new__(clss, *args, **kwargs):
            print(clss)
            print(clss.__bases__)
            #print(dir(clss))
            if clss.__bases__.__contains__(metaInterface):
                raise InterfaceInstancingError("Interfaces cannot be instances by them selves.")
            
            #print(clss.__dict__.items())
            print(str(clss.__class__))
            
            class_child = clss.__class__
            print(class_child.__qualname__)
        
           

            return object.__new__(clss,*args,**kwargs)

   
    
    jclass = type(cls.__name__, (cls,metaInterface), cls.__annotations__)
   
    
 

        
        
    
    #print(jclass)
    
    return jclass


@interface
class MyClass:
   
    def method_1(self): 
            pass
    
class yolo:

    def yolo(self):pass

class My2Class(MyClass, yolo):
    
    def __init__(self):
        pass
    
    def method_2(self):
        pass

try:
    foo = MyClass()  # Should raise an error
except:
    print("interface instancing worked")
fog = My2Class()  # Creating an instance should work fine

#print(dir(fog))

print(isinstance(fog, MyClass))  # Should return True
print(isinstance(fog, My2Class))  # Should return True
print(isinstance(MyClass, My2Class))  # Should return False