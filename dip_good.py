from abc import ABC, abstractmethod


# Abstraktion
class WeatherDisplayTemperatur(ABC):
    @abstractmethod
    def show(self, temp, humidity):
        pass


# Konkrete Empfänger
class PhoneDisplay(WeatherDisplay):
    def show(self, temp, humidity):
        print(f"[Phone] {temp}°C, {humidity}% Luftfeuchtigkeit")


class FileLogger(WeatherDisplay):
    def show(self, temp, humidity):
        print(f"[Log-Datei] Eintrag: {temp}°C, {humidity}%")


class HeatAlarm(WeatherDisplay):
    def show(self, temp, humidity):
        if temp > 35:
            print("[ALARM] Hitzewarnung ausgelöst!")


class WebDashboard(WeatherDisplay):
    def show(self, temp, humidity):
        print(f"[Web-Dashboard] Aktualisiere Anzeige: {temp}°C, {humidity}%")


# High-Level-Modul hängt nur von der Abstraktion ab
class WeatherStation:
    def __init__(self, displays: list[WeatherDisplay]):
        self.displays = displays

    def measurements_changed(self, temp, humidity):
        for display in self.displays:
            display.show(temp, humidity)