from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float):
        pass

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Wetterstation (Subject)
class Wetterstation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0
        self._humidity = 0.0
    
    def register_observer(self, observer: Observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)
    
    def set_weather_data(self, temperature: float, humidity: float):
        self._temperature = temperature
        self._humidity = humidity
        self.notify_observers()

# Concrete Observer - Display
class Display(Observer):
    def __init__(self, name: str):
        self.name = name
        self._temperature = 0.0
        self._humidity = 0.0
    
    def update(self, temperature: float, humidity: float):
        self._temperature = temperature
        self._humidity = humidity
        self.display()
    
    def display(self):
        print(f"{self.name} Anzeige -> Temperatur: {self._temperature}°C, Luftfeuchtigkeit: {self._humidity}%")

if __name__ == "__main__":
    wetterstation = Wetterstation()
    
    display1 = Display("Anzeige 1")
    display2 = Display("Anzeige 2")
    
    wetterstation.register_observer(display1)
    wetterstation.register_observer(display2)
    
    wetterstation.set_weather_data(22.5, 60)
    wetterstation.set_weather_data(25.0, 55)
