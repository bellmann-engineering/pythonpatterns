from abc import ABC, abstractmethod

# Grundlegende Fenster-Komponente (Komponente im Decorator Pattern)
class Window(ABC):
    @abstractmethod
    def render(self):
        pass

# Konkretes Fenster, das angezeigt werden kann (Konkrete Komponente)
class SimpleWindow(Window):
    def render(self):
        return "Fenster anzeigen"

# Basis-Dekorator für Fenster (Abstrakter Dekorator)
class WindowDecorator(Window):
    def __init__(self, window):
        self._window = window

    def render(self):
        return self._window.render()

# Konkreter Dekorator: Fügt eine vertikale Scrollbar hinzu
class VerticalScrollBarDecorator(WindowDecorator):
    def render(self):
        return self._window.render() + " mit vertikaler Scrollbar"

# Konkreter Dekorator: Fügt eine horizontale Scrollbar hinzu
class HorizontalScrollBarDecorator(WindowDecorator):
    def render(self):
        return self._window.render() + " mit horizontaler Scrollbar"

# Verwendung des Decorator Patterns
if __name__ == "__main__":
    # Einfaches Fenster erstellen
    simple_window = SimpleWindow()

    # Fenster mit vertikaler Scrollbar dekorieren
    window_with_vertical_scrollbar = VerticalScrollBarDecorator(simple_window)

    # Fenster mit horizontaler und vertikaler Scrollbar dekorieren
    window_with_both_scrollbars = HorizontalScrollBarDecorator(window_with_vertical_scrollbar)

    # Ergebnisse anzeigen
    print(simple_window.render())  # Ausgabe: Fenster anzeigen
    print(window_with_vertical_scrollbar.render())  # Ausgabe: Fenster anzeigen mit vertikaler Scrollbar
    print(window_with_both_scrollbars.render())  # Ausgabe: Fenster anzeigen mit vertikaler Scrollbar mit horizontaler Scrollbar
