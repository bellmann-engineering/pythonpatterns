from abc import ABC, abstractmethod

# Gemeinsames Thermometer-Interface
class Thermometer(ABC):
    @abstractmethod
    def get_temperature(self):
        pass

# Celsius-Thermometer, das korrekt funktioniert
class CelsiusThermometer(Thermometer):
    def get_temperature(self):
        return 37.0  # Beispiel für die Temperatur in Celsius

# Fahrenheit-Thermometer, das keine Möglichkeit hat, Celsius direkt zu liefern
class FahrenheitThermometer:
    def get_temperature_fahrenheit(self):
        return 98.6  # Gibt die Temperatur in Fahrenheit zurück

# Adapter, der Fahrenheit in Celsius umrechnet und das Thermometer-Interface implementiert
class ThermometerAdapter(Thermometer):
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        # Ruft die Fahrenheit-Temperatur ab
        fahrenheit_temp = self.fahrenheit_thermometer.get_temperature_fahrenheit()
        # Rechnet Fahrenheit in Celsius um
        celsius_temp = (fahrenheit_temp - 32) * 5 / 9
        return round(celsius_temp, 2)

# Verwendung des Adapter Patterns mit einem gemeinsamen Interface
if __name__ == "__main__":
    # Celsius-Thermometer
    celsius_thermometer = CelsiusThermometer()
    print(f"Celsius-Thermometer: {celsius_thermometer.get_temperature()}°C")  # Ausgabe: 37.0°C

    # Fahrenheit-Thermometer, das die Temperatur in Fahrenheit liefert
    fahrenheit_thermometer = FahrenheitThermometer()

    # Der Adapter, der Fahrenheit in Celsius umwandelt und das Thermometer-Interface implementiert
    adapter = ThermometerAdapter(fahrenheit_thermometer)
    print(f"Adapter (Fahrenheit -> Celsius): {adapter.get_temperature()}°C")  # Ausgabe: 37.0°C
