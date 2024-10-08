import copy

# Schritt 1: Abstrakte Klasse für Dokumente

class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def clone(self):
        return copy.deepcopy(self)
    
    def show_info(self):
        print(f"Dokument: {self.title}\nInhalt: {self.content}\n")


# Schritt 2: Konkrete Dokumenttypen

class Report(Document):
    def __init__(self):
        super().__init__(title="Standardbericht", content="Dies ist ein generischer Bericht.")

class Contract(Document):
    def __init__(self):
        super().__init__(title="Standardvertrag", content="Dies ist ein generischer Vertrag.")

class Memo(Document):
    def __init__(self):
        super().__init__(title="Standard-Memo", content="Dies ist ein generisches Memo.")


# Schritt 3: Dokumentenfactory für das Klonen von Dokumentvorlagen

class DocumentFactory:
    def __init__(self):
        self.document_prototypes = {
            "report": Report(),
            "contract": Contract(),
            "memo": Memo()
        }
    
    def create_document(self, doc_type):
        if doc_type in self.document_prototypes:
            return self.document_prototypes[doc_type].clone()
        else:
            print("Unbekannter Dokumenttyp")
            return None


# Schritt 4: Simuliere die Erstellung von Dokumenten

if __name__ == "__main__":
    factory = DocumentFactory()
    
    # Erstelle einen Bericht und passe den Inhalt an
    document = factory.create_document("report")
    if document:
        document.content = "Dies ist der Bericht für das Jahr 2024."
        document.show_info()
    
    # Erstelle einen Vertrag und passe den Titel und Inhalt an
    document = factory.create_document("contract")
    if document:
        document.title = "Vertrag für Projekt X"
        document.content = "Dies ist ein Vertrag für die Zusammenarbeit an Projekt X."
        document.show_info()
    
    # Erstelle ein Memo und passe den Inhalt an
    document = factory.create_document("memo")
    if document:
        document.content = "Bitte beachten Sie die neuen Richtlinien für Home-Office."
        document.show_info()
