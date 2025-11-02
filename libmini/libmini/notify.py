
from abc import ABC, abstractmethod

class Notifier(ABC):
    """Interface that defines the contract for all notifiers"""
    
    @abstractmethod
    def send(self, to: str, message: str) -> str:
        """Send a notification - must be implemented by concrete classes"""
        raise NotImplementedError # pass


class EmailNotifier(Notifier):
    """Concrete notifier that simulates sending emails"""
    
    def send(self, to: str, message: str) -> str:
        # Simulate email sending (no real API calls)
        return f"EMAIL sent to: {to} | Message: {message}"


class SMSNotifier(Notifier):
    """Concrete notifier that simulates sending SMS"""
    
    def send(self, to: str, message: str) -> str:
        # Simulate SMS sending (no real API calls)  
        return f"SMS sent to: {to} | Message: {message}"


class NotifierFactory:
    """Factory that creates the appropriate notifier based on type"""
    
    def create(self, kind: str) -> Notifier:
        kind = kind.lower().strip()
        
        if kind == "email":
            return EmailNotifier()
        elif kind == "sms":
            return SMSNotifier()
        else:
            raise ValueError(f"Unknown notifier type: {kind}")