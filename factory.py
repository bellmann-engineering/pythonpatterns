# Fahrzeug-Basisinterface
class Vehicle:
    def drive(self):
        pass

# Konkrete Fahrzeugklassen
class Car(Vehicle):
    def drive(self):
        return "Auto fährt"

class Motorcycle(Vehicle):
    def drive(self):
        return "Motorrad fährt"

# Das Factory Pattern verlagert die Logik der Objekterstellung in eine separate "Factory"-Klasse
# Die Factory-Klasse zur Erstellung von Fahrzeugen
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'motorcycle':
            return Motorcycle()
        else:
            raise ValueError("Unbekannter Fahrzeugtyp")

# Benutzung der Factory
vehicle_type = 'motorcycle'
vehicle = VehicleFactory.create_vehicle(vehicle_type)

print(vehicle.drive())  # Output: Motorrad fährt
