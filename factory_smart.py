from abc import ABC, abstractmethod

# Basisklasse für smarte Geräte
class SmartDevice(ABC):
    @abstractmethod
    def operate(self):
        pass

# Konkrete Geräteklassen
class SmartLight(SmartDevice):
    def operate(self):
        return "💡"

class SmartSpeaker(SmartDevice):
    def operate(self):
        return "🎵🎵"

# Factory-Klasse zur Erstellung von Smart-Geräten
class SmartDeviceFactory:
    @staticmethod
    def create_device(device_type):
        if device_type == "light":
            return SmartLight()
        elif device_type == "speaker":
            return SmartSpeaker()
        else:
            raise ValueError("Unbekannter Gerätetyp")

device1 = SmartDeviceFactory.create_device("light")
print(device1.operate()) 

device2 = SmartDeviceFactory.create_device("speaker")
print(device2.operate())  
