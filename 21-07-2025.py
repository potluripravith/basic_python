### Factory design pattern
### send different types of notifications Email, SMS, Push
class EmailNotification:
    def send(self, message: str):
        print(f"Sending Email: {message}")

class SMSNotification:
    def send(self, message:str):
        print(f"Sending SMS: {message}")
        
class PushNotification:
    def send(self, message:str):
        print(f"Sending Push: {message}")        
        
def notify_user(notification_type:str,message:str):
    if notification_type == 'email':
        notifier = EmailNotification()
    elif notification_type == "sms":
        notifier = SMSNotification()
    elif notification_type == "push":
        notifier = PushNotification()
    else:
        raise ValueError("Invalid notification type")

    notifier.send(message)
notify_user("sms", "Welcome to the service!")


from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending EMAIL: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def send(self, message: str):
        print(f"Sending PUSH: {message}")


class NotificationFactory:
    @staticmethod
    def get_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Invalid notification type")

def notify_user(notification_type: str, message: str):
    notifier = NotificationFactory.get_notification(notification_type)
    notifier.send(message)

notify_user("sms", "Welcome to the service!")
# 1. Use of Interface (Abstract Base Class)
# First version: No abstraction; the classes don't implement a shared interface or base class.

# Second version: Uses an abstract base class Notification with an abstract method send().

# 2. Separation of Concerns via Factory
# First version: The function notify_user() itself decides which class to instantiate. It contains the logic to select the correct notification type.

# Second version: That logic is moved into a dedicated NotificationFactory class.



# Factory	Encapsulates object creation
# Strategy	Encapsulates algorithm behavior

## Before strategy pattern

def calculate_price(user_type:str, price:float) ->float:
    if user_type == "regular":
        return price
    elif user_type == "member":
        return price * 0.9
    elif user_type == "vip":
        return price * 0.8
    else:
        raise ValueError("Unknown user type")

price = calculate_price("vip", 1000)
print(f"Final Price: Rs{price}")

## new users types need more if-elif statements
## Violates Open/Closed Principle (must modify existing function to add a new type)

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price

class MemberDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.9

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.8
class PriceCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
    def calculate(self, price: float) -> float:
        return self.strategy.apply_discount(price)
    
user_type = "vip"
strategies = {
    "regular": RegularDiscount(),
    "member": MemberDiscount(),
    "vip": VIPDiscount()
}
calculator = PriceCalculator(strategies[user_type])
final_price = calculator.calculate(1000)
print(f"Final Price: Rs {final_price}")

# here we can use enum
# from enum import Enum, auto

# class UserType(Enum):
#     REGULAR = auto()
#     MEMBER = auto()
#     VIP = auto()
    
# strategy_map = {
#     UserType.REGULAR: RegularDiscount(),
#     UserType.MEMBER: MemberDiscount(),
#     UserType.VIP: VIPDiscount()
# }







