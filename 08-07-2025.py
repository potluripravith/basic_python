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
