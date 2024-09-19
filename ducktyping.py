# In Python ist eine gängige Praxis mit weniger statischen Typprüfungen zu arbeiten 
# und stattdessen auf das tatsächliche Verhalten von Objekten zu vertrauen.

class JSONExporter:
    def export(self, data):
        return f"Exportiere Daten als JSON: {data}"


class CSVExporter:
    def export(self, data):
        return f"Exportiere Daten als CSV: {data}"


class XMLExporter:
    def export(self, data):
        return f"Exportiere Daten als XML: {data}"


class DataExporter:
    def __init__(self, exporter):
        self.exporter = exporter

    def export_data(self, data):
        # Statt explizit auf eine bestimmte Klasse zu prüfen, rufen wir einfach die 'export'-Methode auf
        return self.exporter.export(data)


if __name__ == "__main__":
    data = {"name": "John", "age": 30}

    # JSON Export
    json_exporter = JSONExporter()
    exporter = DataExporter(json_exporter)
    print(exporter.export_data(data))

    # CSV Export
    csv_exporter = CSVExporter()
    exporter = DataExporter(csv_exporter)
    print(exporter.export_data(data))

    # XML Export
    xml_exporter = XMLExporter()
    exporter = DataExporter(xml_exporter)
    print(exporter.export_data(data))
