
from InterfaceTools.interface import InterfaceInstancingError, interface


class yolo:
    
    def yolo2(self):pass

@interface
class MyClass():
   
   
   def method_1(self): 
            pass
@interface    
class Myinter():
    
    def method_3(self):pass

class My2Class(MyClass, yolo):
    
    def __init__(self):
        pass
    
    def method_2(self):
        pass

    def method_1(self):pass


def interface_instance_test():
    try:
        foo = MyClass()  # Should raise an error
        assert False
    except InterfaceInstancingError as e:
        assert True
        print(f"interface instancing worked {e}")    
        

def instancing_test():
    try:
        fog = My2Class()  # Creating an instance should work fine
    except Exception as e:
        print(e)
        assert False
    print(isinstance(fog, MyClass))  # Should return True
    print(isinstance(fog, My2Class))  # Should return True
    print(isinstance(MyClass, My2Class))  # Should return False
    print(isinstance(fog,Myinter)) # should be false

    assert True