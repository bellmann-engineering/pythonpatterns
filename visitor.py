# Das Visitor Pattern ermöglicht es, neue Operationen auf Objekte anzuwenden, 
# ohne deren Klassen zu verändern. 

from abc import ABC, abstractmethod

# Visitor Interface
class ReportVisitor(ABC):
    @abstractmethod
    def visit_json_data(self, json_data):
        pass

    @abstractmethod
    def visit_csv_data(self, csv_data):
        pass

# Concrete Visitor für HTML-Report
class HTMLReportVisitor(ReportVisitor):
    def visit_json_data(self, json_data):
        print(f"Erstelle HTML-Report für JSON-Daten: {json_data.get_content()}")

    def visit_csv_data(self, csv_data):
        print(f"Erstelle HTML-Report für CSV-Daten: {csv_data.get_content()}")

# Concrete Visitor für CSV-Report
class CSVReportVisitor(ReportVisitor):
    def visit_json_data(self, json_data):
        print(f"Erstelle CSV-Report für JSON-Daten: {json_data.get_content()}")

    def visit_csv_data(self, csv_data):
        print(f"Erstelle CSV-Report für CSV-Daten: {csv_data.get_content()}")

# Element Interface
class Data(ABC):
    @abstractmethod
    def accept(self, visitor: ReportVisitor):
        pass

    @abstractmethod
    def get_content(self):
        pass

# Concrete Element: JSON Data
class JSONData(Data):
    def __init__(self, content):
        self._content = content

    def accept(self, visitor: ReportVisitor):
        visitor.visit_json_data(self)

    def get_content(self):
        return self._content

# Concrete Element: CSV Data
class CSVData(Data):
    def __init__(self, content):
        self._content = content

    def accept(self, visitor: ReportVisitor):
        visitor.visit_csv_data(self)

    def get_content(self):
        return self._content

# Verwendung des Visitor Patterns in einem Reporting-System
if __name__ == "__main__":
    # Datenquellen erstellen
    json_data = JSONData('{"name": "John", "age": 30}')
    csv_data = CSVData("name,age\nJohn,30")

    # HTML-Report-Generator
    html_report = HTMLReportVisitor()

    # CSV-Report-Generator
    csv_report = CSVReportVisitor()

    # HTML-Report für verschiedene Datentypen erstellen
    print("HTML Report:")
    json_data.accept(html_report)
    csv_data.accept(html_report)

    print("\nCSV Report:")
    # CSV-Report für verschiedene Datentypen erstellen
    json_data.accept(csv_report)
    csv_data.accept(csv_report)
