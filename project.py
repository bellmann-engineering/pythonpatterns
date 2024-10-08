# Strategy Pattern
class TravelTimeStrategy:
    def calculate_time(self, distance):
        pass

class CarTravelTime(TravelTimeStrategy):
    def calculate_time(self, distance):
        return distance / 100  # z.B. Durchschnittsgeschwindigkeit 100 km/h

class BikeTravelTime(TravelTimeStrategy):
    def calculate_time(self, distance):
        return distance / 20  # z.B. Durchschnittsgeschwindigkeit 20 km/h

class PlaneTravelTime(TravelTimeStrategy):
    def calculate_time(self, distance):
        return distance / 800  # z.B. Durchschnittsgeschwindigkeit 800 km/h

# Factory Method
class TransportFactory:
    def create_transport(self):
        pass

class CarFactory(TransportFactory):
    def create_transport(self):
        return CarTransport()

class BikeFactory(TransportFactory):
    def create_transport(self):
        return BikeTransport()

class PlaneFactory(TransportFactory):
    def create_transport(self):
        return PlaneTransport()

# Transportmittel
class Transport:
    def __init__(self, strategy):
        self.strategy = strategy

    def travel_time(self, distance):
        return self.strategy.calculate_time(distance)

class CarTransport(Transport):
    def __init__(self):
        super().__init__(CarTravelTime())

class BikeTransport(Transport):
    def __init__(self):
        super().__init__(BikeTravelTime())

class PlaneTransport(Transport):
    def __init__(self):
        super().__init__(PlaneTravelTime())

# Iterator
class TransportCollection:
    def __init__(self):
        self.transports = []

    def add_transport(self, transport):
        self.transports.append(transport)

    def __iter__(self):
        return iter(self.transports)

# Anwendung
def main():
    # Transportfabriken
    factories = [CarFactory(), BikeFactory(), PlaneFactory()]

    # Transportmittelkollektion
    transport_collection = TransportCollection()
    for factory in factories:
        transport_collection.add_transport(factory.create_transport())

    # Berechne und zeige die Reisezeit für eine gegebene Distanz
    distance = 500  # z.B. 500 km
    for transport in transport_collection:
        print(f"{transport.__class__.__name__} Reisezeit für {distance} km: {transport.travel_time(distance)} Stunden")

if __name__ == "__main__":
    main()
