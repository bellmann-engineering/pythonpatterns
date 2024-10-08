class Vehicle:
    # Klassenattribut
    total_vehicles = 0

    def __init__(self, model):
        self.model = model
        # Wenn eine Instanz erstellt wird, wird das Klassenattribut inkrementiert
        Vehicle.total_vehicles += 1

    # Klassenmethode
    @classmethod
    def show_total_vehicles(cls):
        print(f"Es gibt insgesamt {cls.total_vehicles} Fahrzeuge.")

    # Instanzmethode
    def show_model(self):
        print(f"Dieses Fahrzeug ist ein {self.model}. ")


if __name__ == "__main__":
    # Zwei Fahrzeuginstanzen erstellen
    car1 = Vehicle("Tesla Model S")
    car2 = Vehicle("Ford Mustang")

    # Instanzmethoden aufrufen
    car1.show_model()  # Ausgabe: "Dieses Fahrzeug ist ein Tesla Model S."
    car2.show_model()  # Ausgabe: "Dieses Fahrzeug ist ein Ford Mustang."

    # Klassenmethode aufrufen
    Vehicle.show_total_vehicles()  # Ausgabe: "Es gibt insgesamt 2 Fahrzeuge."
