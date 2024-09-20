# Definition der Car-Klasse, die das Endprodukt darstellt
class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.engine = None
        self.color = None
        self.doors = None

    def __str__(self):
        return f"Auto: {self.brand} {self.model}, Motor: {self.engine}, Farbe: {self.color}, Türen: {self.doors}"

# Definition des CarBuilder, der die schrittweise Erstellung des Autos ermöglicht
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_doors(self, doors):
        self.car.doors = doors
        return self

    def build(self):
        return self.car

# Verwendung des CarBuilder zur Erstellung eines Autos
if __name__ == "__main__":
    builder = CarBuilder()
    car = (builder
           .set_brand("Tesla")
           .set_model("Model S")
           .set_engine("Elektrisch")
           .set_color("Rot")
           .set_doors(4)
           .build())

    print(car)
