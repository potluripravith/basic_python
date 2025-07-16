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
    def run(self):pass