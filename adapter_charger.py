# Die Klasse, die gewrappt wird - Standard-Ladegerät
class StandardCharger:
    def charge_standard(self, vehicle):
        print(f"Lädt {vehicle} mit dem Standard-Ladegerät.")

# Fahrzeuge mit unterschiedlichen Steckertypen
class Type2Vehicle:
    def connect_type2(self):
        print("Verbunden mit Type-2-Stecker.")

class CHAdeMOVehicle:
    def connect_chademo(self):
        print("Verbunden mit CHAdeMO-Stecker.")

# Adapter für Type-2-Stecker
class Type2Adapter:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.charger = StandardCharger()

    def charge_standard(self):
        self.vehicle.connect_type2()
        self.charger.charge_standard("Type-2 Fahrzeug")

# Adapter für CHAdeMO-Stecker
class CHAdeMOAdapter:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.charger = StandardCharger()

    def charge_standard(self):
        self.vehicle.connect_chademo()
        self.charger.charge_standard("CHAdeMO Fahrzeug")

# Ladestation, die den passenden Adapter verwendet
class ChargerStation:
    def charge_vehicle(self, adapter):
        adapter.charge_standard()

# Anwendung des Systems
def main():
    # Erstellen der Fahrzeug- und Adapter-Objekte
    type2_vehicle = Type2Vehicle()
    chademo_vehicle = CHAdeMOVehicle()

    type2_adapter = Type2Adapter(type2_vehicle)
    chademo_adapter = CHAdeMOAdapter(chademo_vehicle)

    # Ladestation verwendet den passenden Adapter
    station = ChargerStation()
    station.charge_vehicle(type2_adapter)
    station.charge_vehicle(chademo_adapter)

if __name__ == "__main__":
    main()
