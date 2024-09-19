class Distance:
    def __init__(self, kilometers=0, meters=0):
        # Falls die Meter >= 1000, wird das in Kilometer umgewandelt
        self.kilometers = kilometers + meters // 1000
        self.meters = meters % 1000

    # __str__ für die menschenlesbare Darstellung
    def __str__(self):
        return f"{self.kilometers} km, {self.meters} m"

    # Addition von zwei Distanzobjekten
    def __add__(self, other):
        if isinstance(other, Distance):
            total_kilometers = self.kilometers + other.kilometers
            total_meters = self.meters + other.meters
            return Distance(total_kilometers, total_meters)
        return NotImplemented

    # __eq__ für den Vergleich
    def __eq__(self, other):
        return self.kilometers == other.kilometers and self.meters == other.meters


if __name__ == "__main__":
    dist1 = Distance(5, 750)
    dist2 = Distance(3, 300)

    # Ausgabe der Distanzen
    print(dist1)  # Ausgabe: 5 km, 750 m
    print(dist2)  # Ausgabe: 3 km, 300 m

    # Addition der Distanzen
    dist3 = dist1 + dist2
    print(dist3)  # Ausgabe: 9 km, 50 m

    # Vergleich von Distanzen
    print(dist1 == dist2)  # Ausgabe: False
