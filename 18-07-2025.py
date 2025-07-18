from abc import ABC, abstractmethod

class Velichle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class car(Velichle):
    def __init__(self):
        self.number_of_doors = 4  
    def start_engine(self):
         print(f"Car engine started with {self.number_of_doors}")
         
obj = car()
obj.start_engine()

         
### we can define attributes which are not present in abstraction class
from abc import ABC, abstractmethod

class Velichle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class car(Velichle):
    def __init__(self):
        self.number_of_doors = 4  
    def start_engine(self, name):
         print(f"Car engine started{name}")

obj = car()
obj.start_engine("Alice")

### The code still runs but it is bad practice

### we can define attributes which are not present in abstraction class
from abc import abstractmethod, ABC
class Shape(ABC):
    @abstractmethod
    def area(self, height:int) -> float: ...

class cone(Shape):
    def __init__(self, radius: int):  # Expected int
        self.radius = radius

    def area(self, height :int| float) -> float:
        return 3.14 * self.radius * height

# But at runtime, nothing stops you from doing:
c = cone(10)  # No error, but area() will raise TypeError
print(c.area(10))

## but it violates Liskov Substitution Principle


## same with Protocols 
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Rectangle:
    def draw(self) -> int:  # Signature mismatch
        return 1

def render(obj: Drawable):
    print(obj.draw())

render(Rectangle())


## to access the private variable

class person:
    def __init__(self, age:int):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be int")
        self._age = value
p = person(25)
p.age = 30          # Valid
print(p.age)        # 30
# p.age = "thirty"    # ValueError

##
from abc import ABC
class name(ABC):
    pass
obj = name()

from abc import ABC, abstractmethod

class name(ABC):
    @abstractmethod
    def say(self):  # now it's abstract
        pass

# obj = name()  

## after one abstractmethod creation it shows error u cant create
from abc import ABC, abstractmethod


class Velichle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    # @abstractmethod
    # def side_parts(self):
    #     pass             if abstractmethod in ABC  inhertited class then it must there in  there sub class
    
    
class car(Velichle):
    def __init__(self):
        self.number_of_doors = 4  
    def start_engine(self, name):
         print(f"Car engine started{name}")

obj = car()
obj.start_engine("Alice")

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def walk(self):
        return "Walking..."
## we can create concrete methods also inside abstraction class


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def __init__(self, name: str):
        self.name = name
## we can create constructor in abc but if you not having the constructor in the subclass, instantiation fails.


