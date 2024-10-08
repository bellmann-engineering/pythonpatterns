from abc import ABC, abstractmethod

# Mediator Interface
class AirTrafficControl(ABC):
    @abstractmethod
    def notify(self, airplane, event):
        ...

# Konkreter Mediator: Flugkontrollzentrum
class Tower(AirTrafficControl):
    def __init__(self):
        self.airplanes_in_air = []
        self.runway_free = True

    def notify(self, airplane, event):
        if event == "request_landing":
            if airplane in self.airplanes_in_air:
                if self.runway_free:
                    print(f"Tower an {airplane.name}: Landen erlaubt.")
                    self.runway_free = False
                else:
                    print(f"Tower an {airplane.name}: Warten, Landebahn besetzt.")
            else:
                print(f"Tower an {airplane.name}: Du bist nicht in der Luft.")

        elif event == "landed":
            print(f"Tower: {airplane.name} hat gelandet. Landebahn frei.")
            self.runway_free = True
            if airplane in self.airplanes_in_air:
                self.airplanes_in_air.remove(airplane)

        elif event == "request_takeoff":
            if not airplane.in_air:
                if self.runway_free:
                    print(f"Tower an {airplane.name}: Starten erlaubt.")
                    self.runway_free = False
                else:
                    print(f"Tower an {airplane.name}: Warten, Landebahn besetzt.")
            else:
                print(f"Tower an {airplane.name}: Du bist bereits in der Luft.")

        elif event == "took_off":
            print(f"Tower: {airplane.name} hat abgehoben. Landebahn frei.")
            self.runway_free = True
            self.airplanes_in_air.append(airplane)

# Kollege: Flugzeuge, die mit dem Tower kommunizieren
class Airplane:
    def __init__(self, name, tower):
        self.name = name
        self.tower = tower
        self.in_air = False  # Flugzeuge starten auf dem Boden

    def request_landing(self):
        if self.in_air:
            print(f"{self.name} an Tower: Erbitte Landung.")
            self.tower.notify(self, "request_landing")
        else:
            print(f"{self.name} ist nicht in der Luft und kann nicht landen.")

    def land(self):
        if self.in_air:
            print(f"{self.name}: Landung im Gange...")
            self.in_air = False
            self.tower.notify(self, "landed")
        else:
            print(f"{self.name} ist bereits gelandet.")

    def request_takeoff(self):
        if not self.in_air:
            print(f"{self.name} an Tower: Erbitte Startfreigabe.")
            self.tower.notify(self, "request_takeoff")
        else:
            print(f"{self.name} ist bereits in der Luft und kann nicht starten.")

    def takeoff(self):
        if not self.in_air:
            print(f"{self.name}: Start im Gange...")
            self.in_air = True
            self.tower.notify(self, "took_off")
        else:
            print(f"{self.name} ist bereits in der Luft.")

# Verwendung des Mediator Patterns
if __name__ == "__main__":
    # Erstellen des Towers (Mediator)
    tower = Tower()

    # Erstellen der Flugzeuge (Kollegen)
    plane1 = Airplane("Flugzeug 1", tower)
    plane2 = Airplane("Flugzeug 2", tower)

    # Flugzeuge versuchen zu starten
    plane1.request_takeoff()
    plane1.takeoff()

    plane2.request_takeoff()
    plane2.takeoff()

    # Flugzeuge versuchen zu landen
    plane1.request_landing()
    plane1.land()

    plane2.request_landing()
    plane2.land()
