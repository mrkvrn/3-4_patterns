from abstract_factory import Application, WindowsFactory, MacFactory
from builder import PizzaBuilder, PizzaDirector
from factory_method import DiskLoggerCreator, TerminalLoggerCreator
from singleton import Singleton

def test_abstract_factory():
    print("Testing Abstract Factory Pattern")

    windows_app = Application(WindowsFactory())
    mac_app = Application(MacFactory())

    print("Windows приложение: ")
    windows_app.paint()

    print("\nMac приложение: ")
    mac_app.paint()

def test_builder():
    print("Testing Builder Pattern")
    
    builder = PizzaBuilder()
    director = PizzaDirector(builder)

    director.construct_pizza()
    pizza = builder.get_result()

    print(f"Pizza: {pizza}")
    
    builder2 = PizzaBuilder()
    builder2.build_dough()
    builder2.build_topping() 
    pizza2 = builder2.get_result()
    print(f"Pizza 2 (no sauce): {pizza2}")

def test_factory_method():
    print("Testing Factory Method Pattern")
    
    disk_factory = DiskLoggerCreator()
    terminal_factory = TerminalLoggerCreator()

    disk_logger = disk_factory.produce_logger()
    terminal_logger = terminal_factory.produce_logger()

    disk_logger.record_message("ERROR 404")
    terminal_logger.record_message("Приложение успешно инициализировано")
    
    disk_logger.record_message("DEBUG: User logged in")
    terminal_logger.record_message("INFO: Processing completed")

def test_singleton():

    print("Testing Singleton Pattern")

    
    obj1 = Singleton()
    obj2 = Singleton()
    
    obj1.display()
    print(f"obj1 is obj2: {obj1 is obj2}")
    print(f"obj1 id: {id(obj1)}")
    print(f"obj2 id: {id(obj2)}")
    

    obj3 = Singleton()
    obj3.display()
    print(f"obj1 is obj3: {obj1 is obj3}")

def main():
    print("DESIGN PATTERNS DEMONSTRATION")
    
    test_abstract_factory()
    test_builder()
    test_factory_method()
    test_singleton()
 
    print("All patterns tested successfully!")

if __name__ == "__main__":
    main()
