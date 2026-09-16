class Gehaltsbeleg:
    def __init__(self, brutto):
        self.brutto = brutto

class Kapitalertrag:
    def __init__(self, ertrag):
        self.ertrag = ertrag

def berechne_steuer(beleg):
    match beleg:
        case Gehaltsbeleg(brutto=brutto):
            return brutto * 0.35
        case Kapitalertrag(ertrag=ertrag):
            return ertrag * 0.25

def exportiere_pdf(beleg):
    match beleg:
        case Gehaltsbeleg(brutto=brutto):
            print(f"PDF-Zeile: Gehalt {brutto} EUR")
        case Kapitalertrag(ertrag=ertrag):
            print(f"PDF-Zeile: Kapitalertrag {ertrag} EUR")


belege = [Gehaltsbeleg(4500), Kapitalertrag(1200)]

summe = sum(berechne_steuer(b) for b in belege)
print(summe)

for b in belege:
    exportiere_pdf(b)