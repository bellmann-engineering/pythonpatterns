from abc import ABC, abstractmethod

# Schnittstelle für das Bild
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Konkrete Klasse für das echte Bild
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()
    
    def load_image_from_disk(self):
        print(f"Lade Bild {self.filename} von der Festplatte...")
    
    def display(self):
        print(f"Zeige Bild {self.filename}")

# Proxy-Klasse, die das Laden des Bildes verzögert
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
    
    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Anwendung des Proxys
if __name__ == "__main__":
    # Erstelle Proxy für das Bild
    image = ProxyImage("großes_bild.jpg")

    # Erstmaliges Anzeigen des Bildes (lädt das Bild)
    print("Bild wird das erste Mal angezeigt:")
    image.display()

    # Zweites Anzeigen des Bildes (verwendet bereits geladenes Bild)
    print("\nBild wird ein zweites Mal angezeigt:")
    image.display()
