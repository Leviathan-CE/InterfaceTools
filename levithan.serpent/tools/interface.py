from abc import abstractmethod
from abc import ABCMeta, ABC
import types


class InterfaceInstancingError(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def interface(cls:type) -> type:   
    '''
    ### Decorator class wrapper
    if @interface above any class will enforce partial interfaceing behavoiur to the class.
    mainly, the class cannot be directly made into an object.

    you can still have base classes on this object and are not require to implement the interfaces functions.
    is compatible with ABC package for abstract methods and functions.
    '''

    class metaInterface:
        __slots__ = ()
        def __new__(cls, *args, **kwargs):

            print(cls)
            print(cls.__bases__)
            if cls.__bases__.__contains__(metaInterface):
                raise InterfaceInstancingError("Interfaces cannot be instances by them selves.")
            return object.__new__(cls,*args,**kwargs)     
   
   
    jclass = types.new_class(cls.__name__, (cls,metaInterface), cls.__annotations__) 
    return jclass



##TESTING: will move to tests once complete

class yolo(metaclass=ABCMeta):
    
    def yolo2(self):pass

@interface
class MyClass(metaclass=ABCMeta):
   
   @abstractmethod
   def method_1(self): 
            pass
    


class My2Class(MyClass, yolo):
    
    def __init__(self):
        pass
    
    def method_2(self):
        pass

    def method_1(self):pass

try:
    foo = MyClass()  # Should raise an error
except InterfaceInstancingError as e:
    print(f"interface instancing worked {e}")

# try:
#     foo = yolo()  # Should raise an error
# except InterfaceInstancingError as e:
#     print(f" {e}")
fog = My2Class()  # Creating an instance should work fine

#print(dir(fog))

print(isinstance(fog, MyClass))  # Should return True
print(isinstance(fog, My2Class))  # Should return True
print(isinstance(MyClass, My2Class))  # Should return False