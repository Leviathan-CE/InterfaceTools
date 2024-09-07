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
        
        def __new__(cls, *args, **kwargs):

            print(cls)
            print(cls.__bases__)
            if cls.__bases__.__contains__(metaInterface):
                raise InterfaceInstancingError("Interfaces cannot be instances by them selves.")
            return object.__new__(cls,*args,**kwargs)     
   
   
    jclass = types.new_class(cls.__name__, (cls,metaInterface), cls.__annotations__) 
    return jclass
