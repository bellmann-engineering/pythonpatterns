# Entkopplung: Der Client muss nicht wissen, wie der Empfänger die Aktion durchführt. 
# Das Command kapselt die Logik.

from abc import ABC, abstractmethod

# Gemeinsames Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Empfänger: Licht
class Light:
    def on(self):
        print("Das Licht ist an.")

    def off(self):
        print("Das Licht ist aus.")

# Empfänger: Ventilator
class Fan:
    def on(self):
        print("Der Ventilator ist an.")

    def off(self):
        print("Der Ventilator ist aus.")

# Konkretes Command: Licht einschalten
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

# Konkretes Command: Licht ausschalten
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# Konkretes Command: Ventilator einschalten
class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()

# Konkretes Command: Ventilator ausschalten
class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.off()

    def undo(self):
        self.fan.on()

# Invoker: Die Fernbedienung
class RemoteControl:
    def __init__(self):
        self.command_history = []

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.command_history.append(self.command)

    def press_undo(self):
        if self.command_history:
            command = self.command_history.pop()
            command.undo()

# Verwendung des Command Patterns
if __name__ == "__main__":
    # Empfänger
    living_room_light = Light()
    bedroom_fan = Fan()

    # Befehle
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
    fan_on = FanOnCommand(bedroom_fan)
    fan_off = FanOffCommand(bedroom_fan)

    # Invoker: Fernbedienung
    remote = RemoteControl()

    # Verwende die Fernbedienung
    remote.set_command(light_on)
    remote.press_button()  # Licht im Wohnzimmer einschalten
    remote.press_undo()    # Licht im Wohnzimmer ausschalten

    remote.set_command(fan_on)
    remote.press_button()  # Ventilator im Schlafzimmer einschalten
    remote.press_undo()    # Ventilator im Schlafzimmer ausschalten
