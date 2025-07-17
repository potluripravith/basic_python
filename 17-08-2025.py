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


## @staticmethod when we dont self which is instance method and cls which is classmethod
 
### dependency inversion vs dependence injection youtube 

### abc and protocols

from abc import ABC, abstractmethod
from typing import Protocol

class Logger(Protocol):
    def log (self,message:str):
        ...
        
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount: float) :
        pass


class PayPalGateway(PaymentGateway):
    def authenticate(self) :
        print("Authenticated with PayPal.")
        return True

    def pay(self, amount: float) :
        print(f"Paid Rs.{amount} using PayPal.")
        
        
class StripeGateway(PaymentGateway):
    def authenticate(self) :
        print("Authenticated with Stripe.")
        return True

    def pay(self, amount: float):
        print(f"Paid Rs.{amount} using Stripe.")
        
class ConsoleLogger:
    def log(self, message: str):
        print(f"[Console] {message}")
        
class FileLogger:
    def log(self, message: str) :
        with open("log.txt", "a") as f:
            f.write(f"{message}\n")
            
class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway, logger: Logger):
        self.gateway = gateway
        self.logger = logger

    def process_payment(self, amount: float):
        if self.gateway.authenticate():
            self.gateway.pay(amount)
            self.logger.log(f"Payment of Rs. {amount} processed successfully.")
        else:
            self.logger.log("Authentication failed.")
            
if __name__ == "__main__":
    paypal = PayPalGateway()
    console_logger = ConsoleLogger()

    processor = PaymentProcessor(paypal, console_logger)
    processor.process_payment(5000.0)