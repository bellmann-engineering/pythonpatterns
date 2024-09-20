import copy

# Schritt 1: Abstrakte Klasse für Häuser

class House:
    def __init__(self, size, rooms, location):
        self.size = size  # Quadratmeter
        self.rooms = rooms  # Anzahl der Zimmer
        self.location = location  # Standort
    
    def clone(self):
        return copy.deepcopy(self)
    
    def show_info(self):
        print(f"Haus in {self.location} mit {self.size}m² und {self.rooms} Zimmern\n")


# Schritt 2: Konkrete Haustypen

class SingleFamilyHouse(House):
    def __init__(self):
        super().__init__(size=150, rooms=5, location="Vorstadt")

class Townhouse(House):
    def __init__(self):
        super().__init__(size=120, rooms=4, location="Innenstadt")

class VacationHouse(House):
    def __init__(self):
        super().__init__(size=100, rooms=3, location="Am Meer")


# Schritt 3: Hausfabrik für das Klonen von Hausvorlagen

class HouseFactory:
    def __init__(self):
        self.house_prototypes = {
            "single_family": SingleFamilyHouse(),
            "townhouse": Townhouse(),
            "vacation": VacationHouse()
        }
    
    def create_house(self, house_type):
        if house_type in self.house_prototypes:
            return self.house_prototypes[house_type].clone()
        else:
            print("Unbekannter Haustyp")
            return None


# Schritt 4: Simuliere die Erstellung von Häusern

if __name__ == "__main__":
    factory = HouseFactory()
    
    # Erstelle ein Einfamilienhaus und passe den Standort an
    house = factory.create_house("single_family")
    if house:
        house.location = "Randbezirk"
        house.show_info()
    
    # Erstelle ein Reihenhaus und passe die Anzahl der Zimmer an
    house = factory.create_house("townhouse")
    if house:
        house.rooms = 5  # Anpassung der Zimmeranzahl
        house.show_info()
    
    # Erstelle ein Ferienhaus und passe die Größe an
    house = factory.create_house("vacation")
    if house:
        house.size = 120  # Anpassung der Größe
        house.show_info()
