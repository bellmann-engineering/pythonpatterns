class House:
    def __init__(self, size, rooms, location):
        self.size = size
        self.rooms = rooms
        self.location = location
    
    # Copy Constructor
    def __init__(self, other_house=None):
        if other_house:
            self.size = other_house.size
            self.rooms = other_house.rooms
            self.location = other_house.location
        else:
            # Default Constructor
            self.size = 0
            self.rooms = 0
            self.location = "Unbekannt"
    
    def show_info(self):
        print(f"Haus in {self.location} mit {self.size}m² und {self.rooms} Zimmern\n")

# Beispiel für Copy Constructor
original_house = House(150, 5, "Stadt")
copy_house = House(original_house)  # Kopiert das ursprüngliche Haus

original_house.show_info()
copy_house.show_info()
