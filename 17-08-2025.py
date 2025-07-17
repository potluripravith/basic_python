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
