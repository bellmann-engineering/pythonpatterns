# Celsius-Thermometer, das nicht richtig funktioniert
class CelsiusThermometer:
    def get_temperature(self):
        return "Defekt"  # Das Thermometer gibt keine korrekten Werte aus

# Fahrenheit-Thermometer, das korrekt funktioniert
class FahrenheitThermometer:
    def get_temperature_fahrenheit(self):
        return 98.6  # Gibt die Temperatur in Fahrenheit zurück

# Adapter, der Fahrenheit in Celsius umrechnet
class ThermometerAdapter:
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        # Ruft die Fahrenheit-Temperatur ab
        fahrenheit_temp = self.fahrenheit_thermometer.get_temperature_fahrenheit()
        # Rechnet Fahrenheit in Celsius um
        celsius_temp = (fahrenheit_temp - 32) * 5 / 9
        return round(celsius_temp, 2)

# Verwendung des Adapter Patterns
if __name__ == "__main__":
    # Das defekte Celsius-Thermometer
    celsius_thermometer = CelsiusThermometer()
    print(f"Celsius-Thermometer: {celsius_thermometer.get_temperature()}")  # Ausgabe: Defekt

    # Das funktionierende Fahrenheit-Thermometer
    fahrenheit_thermometer = FahrenheitThermometer()
    print(f"Temperatur in °F: {fahrenheit_thermometer.get_temperature_fahrenheit()}")

    # Der Adapter, der Fahrenheit in Celsius umwandelt
    adapter = ThermometerAdapter(fahrenheit_thermometer)
    print(f"Adapter (repariertes Celsius-Thermometer): {adapter.get_temperature()}°C")
