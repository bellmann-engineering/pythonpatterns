# Das Proxy Pattern wird hier verwendet, um den Zugriff auf eine externe API zu optimieren. 
# Durch Caching vermeidet der Proxy wiederholte API-Anfragen und verbessert die Effizienz. 

from abc import ABC, abstractmethod
import time

# Gemeinsames Interface für den echten Wetterdienst und den Proxy
class WeatherService(ABC):
    @abstractmethod
    def get_weather(self, city):
        pass

# Konkreter Wetterdienst, der die Wetterinformationen von einer externen API abruft
class RealWeatherService(WeatherService):
    def get_weather(self, city):
        print(f"Anfrage an die externe Wetter-API für {city}...")
        time.sleep(2)  # Simuliert eine langsame API-Anfrage
        return f"Wetterdaten für {city}: Sonnig, 25°C"

# Proxy-Wetterdienst, der den Zugriff auf den echten Wetterdienst steuert
class WeatherServiceProxy(WeatherService):
    def __init__(self):
        self.real_weather_service = RealWeatherService()
        self.cache = {}

    def get_weather(self, city):
        if city not in self.cache:
            print(f"Proxy: Keine Daten für {city} im Cache, API wird kontaktiert.")
            weather_data = self.real_weather_service.get_weather(city)
            self.cache[city] = weather_data
        else:
            print(f"Proxy: Verwende gecachte Daten für {city}.")
        return self.cache[city]

# Verwendung des Proxy Patterns
if __name__ == "__main__":
    # Client greift auf den Proxy-Wetterdienst zu
    proxy = WeatherServiceProxy()

    # Erste Anfrage: Die echte API wird kontaktiert
    print(proxy.get_weather("Berlin"))

    # Zweite Anfrage für dieselbe Stadt: Die gecachten Daten werden verwendet
    print(proxy.get_weather("Berlin"))

    # Anfrage für eine andere Stadt: Die echte API wird erneut kontaktiert
    print(proxy.get_weather("München"))

    # Zweite Anfrage für die neue Stadt: Die gecachten Daten werden verwendet
    print(proxy.get_weather("München"))
