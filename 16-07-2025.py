## decorators
### we have add function so now we need add sub and division then
# def calculate(a,b):
#     return a + b

## here it supports addition now we will add substraction and divison to it using decorator
from functools import wraps

def extend_operations(original_func):
    @wraps(original_func) #Preserves function metadata
    def wrapper(a,b,operation = 'add',**kargs):
        if operation == 'subtract':
            return a-b
        elif operation == 'divide':
            if  b == 0:
                raise ValueError ("cannot divide by zero")
            return a/b
        else :
            return original_func(a,b)
        
    return wrapper


@extend_operations
def calculate(a, b):
    return a + b

print(calculate(10, 5))                
print(calculate(10, 5, operation='subtract'))  
print(calculate(10, 5, operation='divide'))    
        
 
## 
import third_party_module
third_party_module.calculate = extend_operations(third_party_module.calculate)
# Now calculate supports new operations!
print(third_party_module.calculate(10, 5))  
print(third_party_module.calculate(10, 5, operation='subtract'))  
print(third_party_module.calculate(10, 4, operation='divide'))  


### Meta classes 

class EnforceNaming(type):
    def __new__(cls,name,bases,dct):
        for method in dct:
            if callable(dct[method]) and not method.startswith("do_"):
                raise TypeError(f"method '{method}' must start with 'do_'")
        return super().__new__(cls,name,bases,dct)
class Task(metaclass=EnforceNaming):
    def do_save(self): pass
    # def run(self):pass
    
## cls MetaCLass itself
## name name of the class being defined
## bases Base classes of the new class
##dct A dict of everything defined inside the class body

###Protocols

from typing import Protocol
class Flyable(Protocol):
    def fly(self)-> str:
        ...
        
class bird():
    def fly(self):
        return "flying"
    
def launch(obj:Flyable):
    print(obj.fly())
    
launch(bird())


from typing import Protocol

class Reader(Protocol):
    def read(self)-> str:...
class Writer(Protocol):
    def write(self)->str:...
    
class readerwrite(Reader,Writer):
    ...
class File:
    def read(self):
        return "data"
    def write(self):
        print("written")
        
def test(obj:readerwrite):
    print(obj.read())
    obj.write()
        
test(File())
        


## LSP Subclasses must preserve base class behavior  
## TO fix it refactor hierachy, split protocols