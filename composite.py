from abc import ABC, abstractmethod

# Abstrakte Komponente, die das gemeinsame Interface für Dateien und Ordner definiert
class FileComponent(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def display_info(self, indent=0):
        pass

# Blatt: Repräsentiert eine Datei
class File(FileComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display_info(self, indent=0):
        print(" " * indent + f"Datei: {self.name} ({self.size} KB)")

# Komposit: Repräsentiert einen Ordner, der andere Dateien oder Ordner enthalten kann
class Folder(FileComponent):
    def __init__(self, name):
        self.name = name
        self.children = [] # FileCompontents

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_size(self):
        # Berechne die Gesamtgröße aller Kinder (Dateien und Ordner)
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def display_info(self, indent=0):
        print(" " * indent + f"Ordner: {self.name} ({self.get_size()} KB)")
        for child in self.children:
            child.display_info(indent + 2)

# Verwendung des Composite Patterns
if __name__ == "__main__":
    # Erstelle einzelne Dateien
    file1 = File("Dokument1.txt", 120)
    file2 = File("Bild1.png", 350)
    file3 = File("Video1.mp4", 2000)

    # Erstelle Ordner und füge Dateien hinzu
    folder1 = Folder("Projekt A")
    folder1.add(file1)
    folder1.add(file2)

    folder2 = Folder("Videos")
    folder2.add(file3)

    # Erstelle einen übergeordneten Ordner und füge die anderen Ordner hinzu
    main_folder = Folder("Hauptverzeichnis")
    main_folder.add(folder1)
    main_folder.add(folder2)

    # Zeige die Struktur und die Gesamtgröße
    main_folder.display_info()  # Ausgabe der Ordnerstruktur
    print(f"Gesamtgröße: {main_folder.get_size()} KB")  # Ausgabe der Gesamtgröße
