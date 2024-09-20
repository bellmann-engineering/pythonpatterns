import copy

# Definition der Haus-Klasse, die das Prototype Pattern unterstützt
class House:
    def __init__(self, doors, windows, roof, frames):
        self.doors = doors
        self.windows = windows
        self.roof = roof
        self.frames = frames

    # Die clone-Methode verwendet Python's copy-Modul, um ein neues Objekt zu erstellen
    def clone(self):
        return copy.deepcopy(self)
    
    def clone_oldway(self):
        # Erstellt ein neues Objekt vom Typ `House` und überträgt die Attribute
        return House(self.size, self.rooms, self.location)

    def __str__(self):
        return f"Haus: Türen: {self.doors}, Fenster: {self.windows}, Dach: {self.roof}, Rahmen: {self.frames}"

# Verwendung des Prototype Patterns zur Erstellung von Hausobjekten
if __name__ == "__main__":
    # Erstelle ein ursprüngliches Haus-Objekt
    original_house = House(doors=4, windows=10, roof="Ziegeldach", frames="Holzrahmen")
    print(f"Original: {original_house}")

    # Klone das ursprüngliche Haus
    cloned_house = original_house.clone()

    # Modifiziere das geklonte Haus
    cloned_house.doors = 2  # Ändere die Anzahl der Türen im geklonten Haus
    print(f"Geklonte Version (modifiziert): {cloned_house}")

    # Das Original bleibt unverändert
    print(f"Original bleibt unverändert: {original_house}")
