# Das Memento Pattern ermöglicht es, den Zustand eines Objekts zu speichern
# und später wiederherzustellen, ohne dass die interne Struktur des Objekts offengelegt wird. 

# Memento: Speichert den Zustand des Texteditors
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Originator: Der Texteditor, dessen Zustand gespeichert und wiederhergestellt werden kann
class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text):
        self._text += text

    def save(self):
        return Memento(self._text)

    def restore(self, memento):
        self._text = memento.get_state()

    def show_text(self):
        return self._text

# Caretaker: Verwaltet die Mementos (Zustände) des Texteditors
class Caretaker:
    def __init__(self, editor):
        self._editor = editor
        self._history = []

    def save(self):
        print("Zustand gespeichert.")
        self._history.append(self._editor.save())

    def undo(self):
        if not self._history:
            print("Keine vorherigen Zustände vorhanden.")
            return
        memento = self._history.pop()
        print("Zustand wiederhergestellt.")
        self._editor.restore(memento)

# Verwendung des Memento Patterns
if __name__ == "__main__":
    editor = TextEditor()
    caretaker = Caretaker(editor)

    # Benutzer schreibt Text
    editor.write("Hello, ")
    caretaker.save()  # Speichern des Zustands

    editor.write("world!")
    caretaker.save()  # Speichern des Zustands

    print(f"Aktueller Text: {editor.show_text()}")  # Ausgabe: Hello, world!

    # Undo durchführen
    caretaker.undo()  # Zustand von "Hello, world!" auf "Hello, " wiederherstellen
    print(f"Nach Undo: {editor.show_text()}")  # Ausgabe: Hello, 

    # Noch ein Undo
    caretaker.undo()  # Wiederherstellen des leeren Zustands
    print(f"Nach zweitem Undo: {editor.show_text()}")  # Ausgabe: 
