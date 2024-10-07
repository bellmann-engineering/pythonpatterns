# Das Facade Pattern, bei dem wir ein komplexes Subsystem (z.B. ein Heimkinosystem) 
# durch eine einfache Schnittstelle (die Fassade) abstrahieren.

# Subsystem 1: DVD-Player
class DVDPlayer:
    def on(self):
        print("DVD-Player ist eingeschaltet.")

    def play(self, movie):
        print(f"Film '{movie}' wird abgespielt.")

    def off(self):
        print("DVD-Player ist ausgeschaltet.")

# Subsystem 2: Lichtsteuerung
class TheaterLights:
    def dim(self, level):
        print(f"Licht wird auf {level}% gedimmt.")

    def on(self):
        print("Licht ist an.")

# Subsystem 3: Surround-Sound-System
class SurroundSoundSystem:
    def on(self):
        print("Surround-Sound-System ist eingeschaltet.")

    def set_volume(self, level):
        print(f"Die Lautstärke des Surround-Sound-Systems ist auf {level} gesetzt.")

    def off(self):
        print("Surround-Sound-System ist ausgeschaltet.")

# Subsystem 4: Projektor
class Projector:
    def on(self):
        print("Projektor ist eingeschaltet.")

    def off(self):
        print("Projektor ist ausgeschaltet.")

# Die Fassade, die alle Subsysteme vereinfacht und eine einfache Schnittstelle bereitstellt
class HomeTheaterFacade:
    def __init__(self, dvd_player, lights, sound_system, projector):
        self.dvd_player = dvd_player
        self.lights = lights
        self.sound_system = sound_system
        self.projector = projector

    def watch_movie(self, movie):
        print(f"Vorbereitung zum Abspielen des Films: {movie}")
        self.lights.dim(10)
        self.projector.on()
        self.sound_system.on()
        self.sound_system.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Film beenden und Heimkino ausschalten.")
        self.lights.on()
        self.projector.off()
        self.sound_system.off()
        self.dvd_player.off()

# Verwendung des Facade Patterns
if __name__ == "__main__":
    # Erstellen der Subsysteme
    dvd_player = DVDPlayer()
    lights = TheaterLights()
    sound_system = SurroundSoundSystem()
    projector = Projector()

    # Erstellen der Fassade, die die Subsysteme steuert
    home_theater = HomeTheaterFacade(dvd_player, lights, sound_system, projector)

    # Verwenden der Fassade, um einen Film zu starten und zu beenden
    home_theater.watch_movie("Inception")
    print()
    home_theater.end_movie()
