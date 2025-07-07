## Time 9:08 pm

#SOLID Principles in Python

###1) Single Responsibility Principle

## why it is important a bug appears in a class ,you will know where to look  no need of whole code


### Function level SRP 

def procees(data : dict) :
    if not data.get("email") or "@" not in data["email"]:
        raise ValueError ("Invalid email")
    
    user = {
        "name": data["name"].title(),
        "email": data["email"].lower()
    }
    
    db.execute("INSERT INTO users VALUES (?, ?)", (user["name"], user["email"]))
    
    
# what is wrong here so it is doing all the responsibility in single funnction better split the the function

### good pratice is spliting

def validate_user_data(data : dict):
    if not data.get("email") or "@" not in data["email"]:
        raise ValueError ("Invalid email")
    
def format_user_data(data : dict) :
    return {
        "name": data["name"].title(),
        "email": data["email"].lower()
    }
def save_user(user : dict):
    db.execute("INSERT INTO users VALUES (?, ?)", (user["name"], user["email"]))



#### CLass level 
# here also same like functions we need split classes according the group that should belong not all function in single class


class OrderProcessor : 
    def __init__(self,order):
        self.order = order
        
    def validateO(self):
        pass
    def calculate_tax(self):
         pass
    def send_confirmation(self):
        pass
    def update_inventory(self):
        pass
    
# here which makes it a monolithic class instead of it we can divide them into classes and create objects of it and we can make 


class OrderValidator:
    pass
class TaxCalculator:
    pass
class EmailNotifier:
    pass
class InventoryUpdater:
    pass
class OrderProcessor:
    def __init__(self, order):
        self.order = order
        self.validator = OrderValidator()
        self.tax_calculator = TaxCalculator()
        self.notifier = EmailNotifier()
        self.inventory = InventoryUpdater()
    
    def process(self):
        self.validator.validate(self.order)
        self.tax_calculator.calculate(self.order)
        self.notifier.send(self.order)
        self.inventory.update(self.order)
        
# what if we have 10 functions in single class then until there are related topic we want change
### Dependency chain trap 
#### when i split the code in srp for responsibilities but a hidden dependencies between components this may create coupled system 
## so we create Constructor  so that we can given mock files or something to it or we will create ABC class
