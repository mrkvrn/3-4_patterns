from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        print("Кнопка Windows")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Чекбокс Windows")



class MacButton(Button):
    def paint(self):
        print("Кнопка Mac")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Чекбокс Mac")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()

class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()
    
    def paint(self):
        self.button.paint()
        self.checkbox.paint()


print("\n Abstract Factory Test")
windows_app = Application(WindowsFactory())
mac_app = Application(MacFactory())

print("Windows приложение: ")
windows_app.paint()

print("Mac приложение: ")
mac_app.paint()
