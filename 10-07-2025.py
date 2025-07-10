# ####magic methods
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # def __del__(self):
    #     print("object was deleted")
        
p = Person("Alice", 25)

class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __add__(self , other):
        return Vector(self.x + other.x, self.y+ other.y)
    def __repr__(self):
        return f"X:{self.x},Y:{self.y}"
    
    
v1 = Vector(10,20)
v2 = Vector(30,20)
v3 = v1 + v2
print(v3.x,v3.y)
print(v3)


### generators  
def mygenrator(n):
    for x in range(n):
        yield x ** 3
values = mygenrator(1000)       
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

def infinte_sequene():
    result = 1
    while True:
        yield result
        result *=5
        
values = infinte_sequene()       
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))


class Person:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    # @property    
    # def Name(self):
    #     return self.__name
    
    # @Name.setter
    # def Name(self,value):
    #     self.__name = value
    
        
p1 = Person("Sunny",21,"M")

print(p1.Name)
p1.Name = "BOB"

print(p1.Name)



