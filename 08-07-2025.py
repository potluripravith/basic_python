### Time 9 : 30 youtube on abstraction

### Time 11:00
#### Solid principles 3) LSP

### subtypes has to be substitutable for theier base types without changing correctness of th eprogram 

from typing import Any
class database :
    def save(self, data : dict) -> int:
        "Returns ID for saved record"
        
        return id 
class LoggingDatabase(database):
    def save(self, data: dict) ->None:
        super().save(data)
        print("data saved") 
# here we change the data type of sub class which is wrong according LSP and also adding New exception type is also wrong for example


class A:
    def process(self , amount:float):
        "may throw payment error"
        
    
class B(A):
    def process(self, amount):
        if amount > 10000:
            "throw fraud error"
        return super().process(amount)
## it is wrong class a process throws payment error and class b sub class of a throws fraud error which is new and un excepted
### and we should not change the attributes values in sub classes like change the sides of rectangle height for two equal instead of the we create shape and do the tasks 


class Bird:
    def fly(self):
        return "flying"
class Ostrich(Bird):
    def fly(self):
        pass

bird = Ostrich()
bird.fly()

## here it is wrong no need to inhertiate fly from bird if ostrich cant fly
#### state mutation surprises we should not change the behaviour of the supoer claas funcction

###Time 12:00 PM--------
#### TIme 1:00 PM
###Interface segregation Principle
#### Clients should not be forced to depend on interfaces they don't use 
from abc import ABC, abstractmethod
class MultiFunctionPrinter(ABC):
    @abstractmethod
    def print(self, document): 
        pass
    
    @abstractmethod
    def scan(self):
        pass 
    
    @abstractmethod
    def fax(self, document): 
        pass

class BasicPrinter(MultiFunctionPrinter):
    def print(self, document):
        print(f"Printing: {document}")
    
    def scan(self):
        raise NotImplementedError("Scan not supported!")  # Forced to implement
    
    def fax(self, document):
        raise NotImplementedError("Fax not supported!")  # Forced to implement
#instead of force to apply 
from typing import Protocol
class Printer(Protocol):
    def print(self, document: str) -> None: 
        pass

class Scanner(Protocol):
    def scan(self) -> str:
        pass

class Fax(Protocol):
    def fax(self, document: str) -> None: 
        pass

class BasicPrinter(Printer):
    def print(self, document: str) -> None:
        print(f"Printing: {document}")

class MultiFunctionDevice(Printer, Scanner, Fax):
    def print(self, document: str) -> None: 
        pass
    def scan(self) -> str:
        pass
    def fax(self, document: str) -> None: 
        pass

class DocumentProcessor:
    def __init__(self, printer: Printer):  # Depends ONLY on Printer
        self.printer = printer
    
    def process_report(self):
        self.printer.print("Annual Report")
        
        
        
#another example
##Payment system 

class paymentProcessor(ABC):
    @abstractmethod
    def process_credit(self, amount):
        pass
    @abstractmethod
    def process_paypal(self, amount):
        pass
    @abstractmethod
    def process_crpto(self, amount):
        pass
class paypalgateway(paymentProcessor):
    def process_credit(self, amount):
        raise NotImplementedError # not supported
# instead we can do this 
class CreditCardProcessor(Protocol):
    def process_credit_card(self, amount): 
        pass

class PayPalProcessor(Protocol):
    def process_paypal(self, amount): 
        pass

class CryptoProcessor(Protocol):
    def process_crypto(self, amount):
        pass

class PayPalGateway(PayPalProcessor):
    def process_paypal(self, amount):
        pass# Only implement needed method



### Dependency Inversion Principle 

### high level modules should not depend on low level modules .both should depend on abstractions

### abstractions should not depend on details .details depend on abstractions

##low level moodule 
class MySQLDatabase :
    def save(self, order_data:dict)-> None :
        print("saving to mysql")
        
#high level module
class OrderProcessor:
    def __init__(self):
        # Direct dependency on concrete implementation
        self.db = MySQLDatabase()
        
    def process_order(self, order: dict) -> None:
        # Core business logic
        if order["amount"] > 1000:
            order["discount"] = 0.1
        
        # Direct call to low-level implementation
        self.db.save(order) 
        
## here it is directly call low level module so we can create abstraction or protcol so that it will depend on them
class Order(Protocol):
    def save (self, order_data:dict)->None:
        pass
class OrderProcessor:
    def __init__(self, repository: Order):
        # Direct dependency on concrete implementation
        self.repository = repository
        
    def process_order(self, order:dict ) -> None:
        # Core business logic
        if order["amount"] > 1000:
            order["discount"] = 0.1
        
        # Direct call to low-level implementation
        self.repository.save(order)
class MySQLDatabase :
    def save(self, order_data:dict)-> None :
        print(f"saving to mysql:{order_data}")


#### 9:00 pm

###oops

###classes and objects one is the blue print and another one is instances

class DynamicClass:
    def save(self):
        print("save money")
obj = DynamicClass()
obj.save()

##Class vs Instance Variable

class Counter:
    count = 0
    def __init__(self):
        self.id = id(self)
        
c1 = Counter()
c2 = Counter()
Counter.count += 1
print(c1.count,c2.count)

## so class variable is shared along all the objects where as instance is may different from different objects and if we change class varaible it will change for all
#### Inheritance enables code to have hierarchical relationships between classes .

class Animal:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("subclass must implement this method")
    
    
class Dog(Animal):
    def speak(self):
        return "Bow"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
animals = {Dog("Buddy"),Cat("sass")}

for animal in animals:
    print(f"{animal.name}: {animal.speak()}")
### and we can use super() for parent Access
### MRO Method Resolution Order
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")
        super().method()

class C(A):
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    def method(self):
        print("D.method")
        super().method()
        
d = D()
d.method()
### A superclass and b and c are subclasses of A and B and C are super classes of D 

## so first in prints D and then B is the first super class of D so it goes to B print B and and then c and then it will print a 
###Encapsulation Protects object integrity by controlling access to internal state 

class Bank:
    def __init__(self, balance, code):
        self._balance = balance # Protected
        self.__code = code ### Private
        
    def balance(self):
        return self._balance
    
### so we protected if we want our subclasses to use but private cannot used by subclasses

###Polymorphism allows objects of different types to treated as objects of a common supertype.

### Duck typing :

class PdfExporter:
    def export(self, data):
        return f"PDF :{data}"
class CsvExporter:
    def export(self, data):
        return f"CSV:{data}"
def export_report(exporter, report_data):
    """Works with any object having an export() method"""
    return exporter.export(report_data)

pdf = PdfExporter()
csv = CsvExporter()


print(export_report(pdf, ["Sales", 1000]))  # PDF: ['Sales', 1000]
print(export_report(csv, ["Sales", 1000]))  # CSV: Sales,1000


### Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Polymorphic addition operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """Polymorphic multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

# Usage
v1 = Vector(2, 3)
v2 = Vector(1, 1)
print(v1 + v2)  
print(v1 * 3)   

### Abstract Base Classes (ABCs) define interfaces that enforce method implementation .they create formal contracts for polymorphism and inheritance.


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass  # No implementation here

# Subclass must implement the abstract method
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class UPIProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")
# Valid
credit = CreditCardProcessor()
credit.process_payment(1000)

upi = UPIProcessor()
upi.process_payment(500)

# Invalid: Can't instantiate abstract class
# invalid = PaymentProcessor() 
### @property access methofs like attributes 
class Circle:
    def __init__(self, radius):
        self._radius = radius  # protected

    @property
    def radius(self):
        return self._radius  # getter

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.1416 * self._radius ** 2  # read-only
c = Circle(5)
print(c.radius)    
print(c.area)        

c.radius = 10       
print(c.area)        

# c.radius = -5      


