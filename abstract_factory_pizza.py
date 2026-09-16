from abc import ABC, abstractmethod

# 1. Abstrakte Basisklasse für Pizzas
class Pizza(ABC):
    def __init__(self, name, ingredient_factory):
        self.name = name
        self.ingredient_factory = ingredient_factory
        self.cheese = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        return "Pizza wird gebacken"

    def cut(self):
        return "Pizza wird geschnitten"

    def box(self):
        return "Pizza wird verpackt"

    def __str__(self):
        return f"{self.name} mit {self.cheese}"

# 2. Abstrakte Zutaten-Fabrik
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_cheese(self):
        pass

# 3. Konkrete Zutaten-Factories für New York und Philadelphia
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_cheese(self):
        return "Mozzarella"

class PhillyPizzaIngredientFactory(PizzaIngredientFactory):
    def create_cheese(self):
        return "Provolone"

# 4. Konkrete Pizzaklasse, die eine Zutaten-Fabrik verwendet
class CheesePizza(Pizza):
    def prepare(self):
        self.cheese = self.ingredient_factory.create_cheese()
        return f"Zutaten für {self.name} werden vorbereitet mit {self.cheese}"

# 5. Abstrakte Pizzastore-Klasse
class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        if pizza:
            print(pizza.prepare())
            print(pizza.bake())
            print(pizza.cut())
            print(pizza.box())
            return pizza
        else:
            return "Pizza-Typ nicht verfügbar"

# 6. Konkrete Pizzastores für NY und Philly
class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza("New York Käsepizza", NYPizzaIngredientFactory())
        return None

class PhillyPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza("Philadelphia Käsepizza", PhillyPizzaIngredientFactory())
        return None

ny_store = NYPizzaStore()
philly_store = PhillyPizzaStore()

pizza1 = ny_store.order_pizza("cheese")
print(pizza1)  # Ausgabe: New York Käsepizza mit Mozzarella

pizza2 = philly_store.order_pizza("cheese")
print(pizza2)  # Ausgabe: Philadelphia Käsepizza mit Provolone
