
#### Decorators & Closures
def make_adder(x):
    def adder(y):
        return x+y
    return adder

add7 = make_adder(7)
print(add7(10))


def add(x,y):
    return x+y

def logger_add(x,y):
    print("calling add")
    return add(x,y)

logger_add(3,4)

def make_logged(func):
    def inner(*args,**kargs):
        print(f'calling {func.__name__}')
        return func(*args,**kargs)
    return inner

logger_add = make_logged(add)
logger_add(5,6)


def require_role(role_required):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role_required:
                return f"Access denied for user '{user.get('name')}'"
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user, target_user):
    return f"{user.get('name')} deleted {target_user}"

# Test users
admin_user = {"name": "Pravith", "role": "admin"}
regular_user = {"name": "John", "role": "user"}

# Calls
print(delete_user(admin_user, "Bob"))   
print(delete_user(regular_user, "Bob"))  

#### Protocols

from typing import Protocol
class Greetable(Protocol):
    def greet(self)->str:
        ...
class Person:
    def greet(self) ->str:
        return "Hello"
    
def say_Hello(entity:Greetable):
    print(entity.greet())
    
p = Person()
say_Hello(p)    


##Protocols in python is way of defining structural subtyping similar to duck typing Think of protocol as an interface you must have this behavior , not you must inherit from me
from typing import Protocol 

class Flyer(Protocol):
    def fly(self):
        ...
class Bird():
    def fly(self):
        return "I am flying!"
    
def let_it_fly(thing: Flyer):
    print(thing.fly())
    
bird = Bird()
let_it_fly(bird)
    
from typing import Protocol
class Named(Protocol):
    name:str
    
class Person:
    def __init__(self,name):
        self.name = name
        
def greet(entity:Named):
    print(f"Hello {entity.name}")
    
greet(Person("Alice"))

###
from typing import runtime_checkable, Protocol

@runtime_checkable
class Closer(Protocol):
    def close(self) -> None:
        ...

class File:
    def close(self):
        print("Closed")

f = File()
print(isinstance(f, Closer))  

### Meta Classses 
## we class where we can create objects it is blurprint and we attributes 
##every thing python is a object so we can know that there is another class which we make any other class
## ther is a metaclass which tell behaviour of+ the classes 
class sunny:
    y = 20
a = sunny()
print(type(a))
print(type(sunny))

b = type('python', (sunny,),{'x':10})
obj = b()
print(obj.x)
print(obj.y)
print(type(b))
### custom Meta Classes

class Meta(type):
    pass
class pravith(metaclass= Meta):
    pass
print(type(pravith))
print(type(Meta))

class Metatwo(type):
    
    def __init__(self,name,bases,attr):
        print("this")
        
class Python(metaclass= Metatwo):
    pass

class Metatwo(type):
    def __new__(self,name,bases ,attr):
        print("hello") 


