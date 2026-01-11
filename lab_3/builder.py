class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""
    
    def __str__(self):
        return f"Пицца: dough = {self.dough}, sauce = {self.sauce}, topping = {self.topping}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def build_dough(self):
        self.pizza.dough = "cross"
    
    def build_sauce(self):
        self.pizza.sauce = "mild"
    
    def build_topping(self):
        self.pizza.topping = "ham+pineapple"
    
    def get_result(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


print("\n Builder Test")
builder = PizzaBuilder()
director = PizzaDirector(builder)

director.construct_pizza()
pizza = builder.get_result()

print(f"Pizza: {pizza}")
