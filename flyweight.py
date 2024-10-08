# Flyweight Pattern wird verwendet um die Speichernutzung zu optimieren, 
# indem viele ähnliche Objekte gemeinsam genutzte Daten verwenden.

# Flyweight-Klasse für Symbole
class Icon:
    def __init__(self, icon_type, image_data):
        self.icon_type = icon_type  # Typ des Symbols (z.B. "Restaurant", "Parkplatz")
        self.image_data = image_data  # Bilddaten des Symbols

    def render(self, x, y):
        print(f"Zeige Symbol '{self.icon_type}' an Position ({x}, {y}) mit Bild: {self.image_data}")

# Flyweight Factory: Verwaltet Symbole
class IconFactory:
    _icons = {}

    @classmethod
    def get_icon(cls, icon_type, image_data):
        if icon_type not in cls._icons:
            cls._icons[icon_type] = Icon(icon_type, image_data)
        return cls._icons[icon_type]

# Marker-Klasse, die das Symbol an einer bestimmten Position anzeigt
class Marker:
    def __init__(self, x, y, icon):
        self.x = x
        self.y = y
        self.icon = icon  # Verweist auf das gemeinsame Symbol (Flyweight)

    def render(self):
        self.icon.render(self.x, self.y)

# Verwendung des Flyweight Patterns in einer Kartenanwendung
if __name__ == "__main__":
    # Erstellen der Flyweight Factory für Symbole
    factory = IconFactory()

    # Symbole für Restaurants und Parkplätze
    restaurant_icon = factory.get_icon("Restaurant", "restaurant.png")
    parking_icon = factory.get_icon("Parkplatz", "parking.png")

    # Erstellen von Markern auf der Karte
    marker1 = Marker(10, 20, restaurant_icon)
    marker2 = Marker(15, 25, restaurant_icon)
    marker3 = Marker(50, 60, parking_icon)
    marker4 = Marker(70, 80, parking_icon)

    # Rendern der Marker (es wird jeweils das gleiche Symbol für Restaurants und Parkplätze wiederverwendet)
    marker1.render()
    marker2.render()
    marker3.render()
    marker4.render()

    # Überprüfen, ob dieselben Symbole wiederverwendet werden
    print(f"Verwenden Marker1 und Marker2 dasselbe Restaurant-Symbol? {restaurant_icon is factory.get_icon('Restaurant', 'restaurant.png')}")
    print(f"Verwenden Marker3 und Marker4 dasselbe Parkplatz-Symbol? {parking_icon is factory.get_icon('Parkplatz', 'parking.png')}")
