from abc import ABC, abstractmethod

# 1. Abstrakte Basisklasse für Fahrzeuge
class Car(ABC):
    def __init__(self, name, component_factory):
        self.name = name
        self.component_factory = component_factory
        self.battery = None

    @abstractmethod
    def assemble(self):
        pass

    def test_drive(self):
        return "Fahrzeug wird Probe gefahren"

    def quality_check(self):
        return "Fahrzeug wird qualitätsgeprüft"

    def ship(self):
        return "Fahrzeug wird ausgeliefert"

    def __str__(self):
        return f"{self.name} mit {self.battery}"

# 2. Abstrakte Komponenten-Fabrik
class VehicleComponentFactory(ABC):
    @abstractmethod
    def create_battery(self):
        pass

# 3. Konkrete Komponenten-Factories für Grünheide und Shanghai
class GermanyComponentFactory(VehicleComponentFactory):
    def create_battery(self):
        return "4680-Zellen (lokal gefertigt)"

class ChinaComponentFactory(VehicleComponentFactory):
    def create_battery(self):
        return "LFP-Zellen"

# 4. Konkrete Fahrzeugklasse, die eine Komponenten-Fabrik verwendet
class ModelY(Car):
    def assemble(self):
        self.battery = self.component_factory.create_battery()
        return f"Komponenten für {self.name} werden verbaut mit {self.battery}"

# 5. Abstrakte Gigafactory-Klasse
class Gigafactory(ABC):
    @abstractmethod
    def build_car(self, model):
        pass

    def produce_car(self, model):
        car = self.build_car(model)
        if car:
            print(car.assemble())
            print(car.test_drive())
            print(car.quality_check())
            print(car.ship())
            return car
        else:
            return "Modell nicht verfügbar"

# 6. Konkrete Gigafactories für Grünheide und Shanghai
class GigafactoryBerlin(Gigafactory):
    def build_car(self, model):
        if model == "model_y":
            return ModelY("Model Y (Grünheide)", GermanyComponentFactory())
        return None

class GigafactoryShanghai(Gigafactory):
    def build_car(self, model):
        if model == "model_y":
            return ModelY("Model Y (Shanghai)", ChinaComponentFactory())
        return None

berlin_factory = GigafactoryBerlin()
shanghai_factory = GigafactoryShanghai()

car1 = berlin_factory.produce_car("model_y")
print(car1)  # Ausgabe: Model Y (Grünheide) mit 4680-Zellen (lokal gefertigt)

car2 = shanghai_factory.produce_car("model_y")
print(car2)  # Ausgabe: Model Y (Shanghai) mit LFP-Zellen