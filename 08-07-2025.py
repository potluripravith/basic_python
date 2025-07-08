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
####Interface segregation Principle


        