# Das Template Method Pattern definiert das Templates eines Algorithmus in einer Methode,
# wobei einige Schritte des Algorithmus von Unterklassen implementiert werden.

from abc import ABC, abstractmethod

# Abstract Template
class DataProcessor(ABC):
    # Template Method
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()

    # Diese Methoden müssen von den Unterklassen implementiert werden
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

# Concrete Class: CSVDataProcessor
class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("CSV-Daten lesen.")

    def process_data(self):
        print("CSV-Daten verarbeiten.")

    def save_data(self):
        print("CSV-Daten speichern.")

# Concrete Class: JSONDataProcessor
class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("JSON-Daten lesen.")

    def process_data(self):
        print("JSON-Daten verarbeiten.")

    def save_data(self):
        print("JSON-Daten speichern.")

# Verwendung des Template Method Patterns
if __name__ == "__main__":
    # CSV Datenverarbeitung
    csv_processor = CSVDataProcessor()
    print("Verarbeitung für CSV:")
    csv_processor.process()

    print("\nVerarbeitung für JSON:")
    # JSON Datenverarbeitung
    json_processor = JSONDataProcessor()
    json_processor.process()
