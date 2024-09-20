from abc import ABC, abstractmethod

# Abstrakte GPS-Klasse
class GPS(ABC):
    @abstractmethod
    def get_coordinates(self):
        pass

# Abstrakte LocationInfo-Klasse
class LocationInfo(ABC):
    @abstractmethod
    def get_location_type(self):
        pass

# Konkrete GPS-Implementierung: Satelliten-GPS
class SatelliteGPS(GPS):
    def get_coordinates(self):
        return "Satelliten-Koordinaten: 40.7128 N, 74.0060 W"

# Konkrete GPS-Implementierung: Mobilfunknetz-GPS
class CellularGPS(GPS):
    def get_coordinates(self):
        return "Mobilfunknetz-Koordinaten: 48.8566 N, 2.3522 E"

# Konkrete LocationInfo für Satelliten-GPS
class SatelliteLocationInfo(LocationInfo):
    def get_location_type(self):
        return "Ort befindet sich auf dem Land (via Satellit erkannt)"

# Konkrete LocationInfo für Mobilfunknetz-GPS
class CellularLocationInfo(LocationInfo):
    def get_location_type(self):
        return "Ort befindet sich im Stadtgebiet (via Mobilfunknetz erkannt)"

# Abstrakte GPSFactory zur Erstellung von GPS und LocationInfo Objekten
class GPSFactory(ABC):
    @abstractmethod
    def create_gps(self):
        pass

    @abstractmethod
    def create_location_info(self):
        pass

# Factory für Satelliten-GPS
class SatelliteGPSFactory(GPSFactory):
    def create_gps(self):
        return SatelliteGPS()

    def create_location_info(self):
        return SatelliteLocationInfo()

# Factory für Mobilfunknetz-GPS
class CellularGPSFactory(GPSFactory):
    def create_gps(self):
        return CellularGPS()

    def create_location_info(self):
        return CellularLocationInfo()

# Funktion, die die GPS-Factory verwendet, um GPS und Standortinformationen zu erhalten
def get_gps_and_location(factory: GPSFactory):
    gps = factory.create_gps()
    location_info = factory.create_location_info()
    
    print(gps.get_coordinates())
    print(location_info.get_location_type())

# Verwende die Factory für Satelliten-GPS
satellite_factory = SatelliteGPSFactory()
print("Verwende Satelliten-GPS:")
get_gps_and_location(satellite_factory)

# Verwende die Factory für Mobilfunknetz-GPS
cellular_factory = CellularGPSFactory()
print("\nVerwende Mobilfunknetz-GPS:")
get_gps_and_location(cellular_factory)
