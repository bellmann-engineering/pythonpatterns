class GPS:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    def __str__(self):
        return self.get_coordinates()


class GPSFactory:
    @staticmethod
    def create_gps_from_string(gps_string):
        # Der String wird an der Komma-Stelle getrennt
        lat, lon = gps_string.split(',')
        # Wandle die Strings in Floats um
        latitude = float(lat)
        longitude = float(lon)
        # Erstelle ein GPS-Objekt mit den extrahierten Werten
        return GPS(latitude, longitude)


gps_string = "12.41232,9.123312"

# Verwende die Factory, um das GPS-Objekt zu erstellen
gps_object = GPSFactory.create_gps_from_string(gps_string)

print(gps_object)
