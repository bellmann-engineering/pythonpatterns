# Definition der Haus-Klasse, die das Endprodukt darstellt
class House:
    def __init__(self, roof, doors = None, windows = None, frames = None):
        self.doors = doors
        self.windows = windows
        self.roof = roof
        self.frames = frames

    def __str__(self):
        return f"Haus: Türen: {self.doors}, Fenster: {self.windows}, Dach: {self.roof}, Rahmen: {self.frames}"


h = House(
    roof="Flachdach"
    )

    

# Definition des HouseBuilder, der die schrittweise Erstellung des Hauses ermöglicht
class HouseBuilder:

    error_dict = {}

    def __init__(self):
        self.house = House()

    def with_doors(self, doors):
        """Setzt die Anzahl der Türen."""
        self.house.doors = doors
        return self

    def with_windows(self, windows):
        if windows <= 1:
            raise AttributeError("Fensteranzahl ungültig")
        
        self.house.windows = windows
        return self

    def with_roof(self, roof_type):
        """Setzt den Dachtyp."""
        self.house.roof = roof_type
        return self

    def with_frames(self, frame_type):
        """Setzt den Rahmentyp."""
        self.house.frames = frame_type
        return self

    def build(self):
        if self.house.roof is None:
            raise Exception("Ohne Dach gehts nicht")

        """Gibt das fertig erstellte Haus zurück."""
        return self.house

# Verwendung des HouseBuilder zur Erstellung eines Hauses
if __name__ == "__main__":
    house = (HouseBuilder()
             .with_doors(4)
             .with_windows(10)
             .with_roof("Ziegeldach")
             .with_frames("Holzrahmen")
             .build())

    print(house) 
