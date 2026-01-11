class Singleton:
    _single_instance = None
    
    def __new__(cls):
        if cls._single_instance is None:
            cls._single_instance = object.__new__(cls)
        return cls._single_instance
    
    def display(self):
        print("Singleton pattern example, only one instance exists")

print("Singleton Pattern Test")
obj1 = Singleton()
obj2 = Singleton()
obj1.display()
print(f"obj1 is obj2: {obj1 is obj2}")  
