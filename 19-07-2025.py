from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self, sound: str) -> str: 
        return sound
    
obj = Dog()
print(obj.speak("Bow bow"))

### if we extra parameters it will run but it violates


# class Cat(Animal):
#     def make_sound(self): 
#         return "Meow"

# cat = Cat()
# we should add ABC class  method if we inhertitate

# class X:
#     @x.setter   
#     def x(self, value):
#         self._x = value

from typing import Protocol

class flyer(Protocol):
    def fly(self) -> str:
        ...
        
class parrot:
    def fly(self) -> int:
        return 42
    
def launch(f: flyer):
    print(f.fly())
launch(parrot())

### return type is changed still it works in python mypy will report error

# class Jet:
#     def fly(self, speed: int) -> str:  
#         return f"Zoom {speed}"
# launch(Jet()) we can not give extra aruguments or mismatch

from abc import ABC, abstractmethod
from typing import Protocol

class A(ABC):
    @abstractmethod
    def ping(self): ...

class B(Protocol):
    def ping(self): ...

class C(A, B):
    def ping(self): print("Ping from C")

c = C()  # Works because ABC's requirement is fulfilled
#No conflict: Protocol does not enforce anything at runtime.

class A(ABC):
    @abstractmethod
    def run(self, speed: int): ...

class B(A):
    def run(self, speed: int = 5):  #
        print(speed)
## it still fine because u just add default values
## classmethod
class Myclass:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
        print(f"{cls.count}")

obj =Myclass()
obj.increment()
### Because without @classmethod, Python treats it like an instance method, and the first argument will still be the instance 
### Can access/modify class-level data

## Static Method 
## Because you still want the function logically grouped inside the class, but don't want it to access or depend on the class/instance.

class MyMath:
    @staticmethod
    def add(x, y):
        return x + y
obj = MyMath()
print(obj.add(5,6))




#### Software design youtube 

## if we fixed string names we create it using ENUM 
## code duplication is bad so we need create generic method 
## use built in python
## use boolean flags to do 2 different things
### catching and igonore exceptions
## define customs error handling to give messages 
class A(Exception):
    def __init__(self, a,b,message):
        self.a = a
        self.b =b
        self.message = message
        super().__init__(message)
    

