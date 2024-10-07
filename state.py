# Das State Pattern ermöglicht es einem Objekt, sein Verhalten zu ändern, 
# wenn sich sein interner Zustand ändert. In diesem Beispiel implementieren
# wir das Verhalten eines iPods, der verschiedene Zustände wie "Play", "Pause" und "Stop" hat.


from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def press_play(self, ipod):
        pass

    @abstractmethod
    def press_pause(self, ipod):
        pass

    @abstractmethod
    def press_stop(self, ipod):
        pass

# Concrete State: Playing
class PlayingState(State):
    def press_play(self, ipod):
        print("iPod spielt bereits.")

    def press_pause(self, ipod):
        print("iPod wird pausiert.")
        ipod.set_state(PausedState())

    def press_stop(self, ipod):
        print("iPod wird gestoppt.")
        ipod.set_state(StoppedState())

# Concrete State: Paused
class PausedState(State):
    def press_play(self, ipod):
        print("iPod wird fortgesetzt.")
        ipod.set_state(PlayingState())

    def press_pause(self, ipod):
        print("iPod ist bereits pausiert.")

    def press_stop(self, ipod):
        print("iPod wird gestoppt.")
        ipod.set_state(StoppedState())

# Concrete State: Stopped
class StoppedState(State):
    def press_play(self, ipod):
        print("iPod wird gestartet.")
        ipod.set_state(PlayingState())

    def press_pause(self, ipod):
        print("iPod ist gestoppt und kann nicht pausiert werden.")

    def press_stop(self, ipod):
        print("iPod ist bereits gestoppt.")

# Context: iPod
class iPod:
    def __init__(self):
        # Der iPod beginnt im gestoppten Zustand
        self.state = StoppedState()

    def set_state(self, state):
        self.state = state

    def press_play(self):
        self.state.press_play(self)

    def press_pause(self):
        self.state.press_pause(self)

    def press_stop(self):
        self.state.press_stop(self)


if __name__ == "__main__":
    ipod = iPod()

    # Der iPod ist gestoppt, wir drücken Play
    ipod.press_play()  # Ausgabe: iPod wird gestartet.

    # Der iPod spielt, wir drücken Pause
    ipod.press_pause()  # Ausgabe: iPod wird pausiert.

    # Der iPod ist pausiert, wir drücken Play
    ipod.press_play()  # Ausgabe: iPod wird fortgesetzt.

    # Der iPod spielt, wir drücken Stop
    ipod.press_stop()  # Ausgabe: iPod wird gestoppt.

    # Der iPod ist gestoppt, wir drücken Pause
    ipod.press_pause()  # Ausgabe: iPod ist gestoppt und kann nicht pausiert werden.
