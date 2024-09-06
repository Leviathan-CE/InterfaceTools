

class my2Class():
    
    def __init__(self) -> None:
        print("hello world")
        pass
    
    def method_1():
        pass

class MyClass(my2Class):
    
    def __init__(self)-> None:
        print("yolo")


methods_list = [method for method in MyClass.__dict__ if callable(
    getattr(MyClass, method)) and not method.startswith("__")]
 
print("Methods using __dict__ attribute:", methods_list)