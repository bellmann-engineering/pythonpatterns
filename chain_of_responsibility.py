from abc import ABC, abstractmethod

# Gemeinsames Interface für die Handler in der Kette
class SupportHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, issue_level):
        pass

# Erster Support-Level
class LevelOneSupport(SupportHandler):
    def handle_request(self, issue_level):
        if issue_level == 1:
            print("Level 1 Support: Problem gelöst.")
        elif self.next_handler:
            print("Level 1 Support: Leitet das Problem weiter.")
            self.next_handler.handle_request(issue_level)

# Zweiter Support-Level
class LevelTwoSupport(SupportHandler):
    def handle_request(self, issue_level):
        if issue_level == 2:
            print("Level 2 Support: Problem gelöst.")
        elif self.next_handler:
            print("Level 2 Support: Leitet das Problem weiter.")
            self.next_handler.handle_request(issue_level)

# Dritter Support-Level
class LevelThreeSupport(SupportHandler):
    def handle_request(self, issue_level):
        if issue_level == 3:
            print("Level 3 Support: Problem gelöst.")
        elif self.next_handler:
            print("Level 3 Support: Keine weiteren Support-Level verfügbar. Problem nicht lösbar.")

# Verwendung der Support-Kette
if __name__ == "__main__":
    # Erstelle die Support-Handler
    level1 = LevelOneSupport()
    level2 = LevelTwoSupport()
    level3 = LevelThreeSupport()

    # Setze die Chain of Responsibility
    level1.set_next(level2).set_next(level3)

    # Teste verschiedene Support-Anfragen
    print("Anfrage mit Level 1:")
    level1.handle_request(1)

    print("\nAnfrage mit Level 2:")
    level1.handle_request(2)

    print("\nAnfrage mit Level 3:")
    level1.handle_request(3)

    print("\nAnfrage mit höherem Level als unterstützt:")
    level1.handle_request(4)
