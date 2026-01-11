from abc import ABC, abstractmethod

print("Proxy Pattern")

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject: Executing primary request"

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject
    
    def request(self):
        if self.verify_permissions():
            response = self._real_subject.request()
            self.record_activity()
            return response
        return "Authorization failed"
    
    def verify_permissions(self):
        print("Proxy: Validating access rights before proceeding")
        return True
    
    def record_activity(self):
        print("Proxy: Recording request timestamp in audit log")
