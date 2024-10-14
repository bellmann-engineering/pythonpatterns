from abc import ABC, abstractmethod


# Strategy Pattern: Transportstrategie
class TransportStrategy(ABC):
    @abstractmethod
    def calculate_time(self, distance):
        pass

    @abstractmethod
    def calculate_cost(self, distance):
        pass


# Konkrete Transportmethoden
class VanStrategy(TransportStrategy):
    def calculate_time(self, distance):
        # Annahme: Lieferwagen fährt 60 km/h
        return distance / 60

    def calculate_cost(self, distance):
        # Annahme: 0.5 EUR pro km
        return distance * 0.5


class BikeCourierStrategy(TransportStrategy):
    def calculate_time(self, distance):
        # Annahme: Fahrradkurier fährt 20 km/h
        return distance / 20

    def calculate_cost(self, distance):
        # Annahme: 0.2 EUR pro km
        return distance * 0.2


class DroneStrategy(TransportStrategy):
    def calculate_time(self, distance):
        # Annahme: Drohne fliegt 80 km/h
        return distance / 80

    def calculate_cost(self, distance):
        # Annahme: 1.0 EUR pro km
        return distance * 1.0


# Composite Pattern: Kombination von Transportmethoden
class TransportComposite(TransportStrategy):
    def __init__(self):
        self._strategies = []

    def add_strategy(self, strategy):
        self._strategies.append(strategy)

    def calculate_time(self, distance):
        times = [strategy.calculate_time(distance) for strategy in self._strategies]
        return sum(times) / len(times)  # Durchschnittliche Zeitberechnung

    def calculate_cost(self, distance):
        costs = [strategy.calculate_cost(distance) for strategy in self._strategies]
        return sum(costs)  # Gesamtkostenberechnung


# Factory Pattern: Transportmittel-Factory
class TransportFactory:
    @staticmethod
    def create_transport(method):
        if method == "van":
            return VanStrategy()
        elif method == "bike":
            return BikeCourierStrategy()
        elif method == "drone":
            return DroneStrategy()
        else:
            raise ValueError(f"Transportmethod '{method}' nicht unterstützt.")


# Beispiel für die Anwendung
def main():
    # Erzeuge Transportmethoden basierend auf Benutzereingabe
    available_methods = ["van", "bike", "drone"]
    user_choice = input(f"Wähle Transportmethoden ({', '.join(available_methods)}), getrennt durch Kommata: ").split(",")

    composite_transport = TransportComposite()
    
    for method in user_choice:
        method = method.strip()
        try:
            transport_strategy = TransportFactory.create_transport(method)
            composite_transport.add_strategy(transport_strategy)
        except ValueError as e:
            print(e)

    # Berechnung
    distance = float(input("Geben Sie die Distanz in km ein: "))
    time = composite_transport.calculate_time(distance)
    cost = composite_transport.calculate_cost(distance)

    print(f"\nTransportmethoden: {', '.join(user_choice)}")
    print(f"Distanz: {distance} km")
    print(f"Geschätzte Lieferzeit: {time:.2f} Stunden")
    print(f"Geschätzte Lieferkosten: {cost:.2f} EUR")


if __name__ == "__main__":
    main()
