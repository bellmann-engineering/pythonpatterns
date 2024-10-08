from abc import ABC, abstractmethod

# Abstrakte Klasse für den Zustand
class DoorState(ABC):
    @abstractmethod
    def open(self, door):
        pass
    
    @abstractmethod
    def close(self, door):
        pass

    @abstractmethod
    def lock(self, door):
        pass

# Konkreter Zustand: Geschlossen
class ClosedState(DoorState):
    def open(self, door):
        print("Die Tür öffnet sich.")
        door.set_state(OpenState())
        
    def close(self, door):
        print("Die Tür ist bereits geschlossen.")

    def lock(self, door):
        print("Die Tür wird verriegelt.")
        door.set_state(LockedState())

# Konkreter Zustand: Offen
class OpenState(DoorState):
    def open(self, door):
        print("Die Tür ist bereits offen.")
        
    def close(self, door):
        print("Die Tür schließt sich.")
        door.set_state(ClosedState())
        
    def lock(self, door):
        print("Kann nicht verriegeln. Die Tür ist offen.")

# Konkreter Zustand: Verriegelt
class LockedState(DoorState):
    def open(self, door):
        print("Kann nicht öffnen. Die Tür ist verriegelt.")
        
    def close(self, door):
        print("Die Tür ist bereits geschlossen und verriegelt.")
        
    def lock(self, door):
        print("Die Tür ist bereits verriegelt.")

# Tür-Klasse, die den aktuellen Zustand verwaltet
class Door:
    def __init__(self):
        self._state = ClosedState()  # Tür startet im geschlossenen Zustand
    
    def set_state(self, state):
        self._state = state
        
    def open(self):
        self._state.open(self)
        
    def close(self):
        self._state.close(self)
        
    def lock(self):
        self._state.lock(self)

# Anwendung
if __name__ == "__main__":
    # Tür-Objekt erstellen
    door = Door()

    # Aktionen durchführen
    door.open()    # Die Tür öffnet sich.
    door.lock()    # Kann nicht verriegeln. Die Tür ist offen.
    door.close()   # Die Tür schließt sich.
    door.lock()    # Die Tür wird verriegelt.
    door.open()    # Kann nicht öffnen. Die Tür ist verriegelt.
