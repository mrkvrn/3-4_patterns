from abc import ABC, abstractmethod

print("Responsibility Chain Pattern")

class Handler(ABC):
    def __init__(self):
        self._next_handler = None
    
    def set_next(self, handler):
        self._next_handler = handler
        return handler
    
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandler_A(Handler):
    def handle(self, request):
        if request == "A":
            return f"Handler A processed request {request}"
        else:
            return super().handle(request)

class ConcreteHandler_B(Handler):
    def handle(self, request):
        if request == "B":
            return f"Handler B processed request {request}"
        else:
            return super().handle(request)
