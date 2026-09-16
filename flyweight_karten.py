class KartenFlyweight:
    """Intrinsic state: Rang, Farbe, Bilddaten - wird geteilt"""
    def __init__(self, rang: str, farbe: str, bild_daten: bytes):
        self.rang = rang
        self.farbe = farbe
        self.bild_daten = bild_daten  # z.B. 50 KB Grafik, nur einmal im Speicher

    def render(self, x: int, y: int, aufgedeckt: bool):
        # extrinsic state (x, y, aufgedeckt) kommt von außen, nicht gespeichert
        zustand = "aufgedeckt" if aufgedeckt else "verdeckt"
        print(f"{self.rang} {self.farbe} bei ({x},{y}) - {zustand}")


class KartenFactory:
    """Verwaltet den Pool - max. 52 Objekte, egal wie viele Tische aktiv sind"""
    _pool: dict[str, KartenFlyweight] = {}

    @classmethod
    def get_karte(cls, rang: str, farbe: str) -> KartenFlyweight:
        schluessel = f"{rang}_{farbe}"
        if schluessel not in cls._pool:
            print(f"Erzeuge neue Flyweight-Instanz: {schluessel}")
            bild = cls._lade_bild(rang, farbe)
            cls._pool[schluessel] = KartenFlyweight(rang, farbe, bild)
        return cls._pool[schluessel]

    @staticmethod
    def _lade_bild(rang: str, farbe: str) -> bytes:
        # simuliert teures Laden der Kartengrafik
        return f"bild_{rang}_{farbe}.png".encode()

    @classmethod
    def anzahl_flyweights(cls) -> int:
        return len(cls._pool)


class Tisch:
    """Hält nur extrinsic state - welche Karte liegt wo"""
    def __init__(self, tisch_id: int):
        self.tisch_id = tisch_id
        self.karten_auf_tisch: list[tuple[KartenFlyweight, int, int, bool]] = []

    def karte_ablegen(self, rang: str, farbe: str, x: int, y: int, aufgedeckt: bool):
        flyweight = KartenFactory.get_karte(rang, farbe)
        self.karten_auf_tisch.append((flyweight, x, y, aufgedeckt))

    def anzeigen(self):
        print(f"--- Tisch {self.tisch_id} ---")
        for flyweight, x, y, aufgedeckt in self.karten_auf_tisch:
            flyweight.render(x, y, aufgedeckt)


# Simulation: 1000 Tische, aber nur 52 mögliche Karten
if __name__ == "__main__":
    tische = [Tisch(i) for i in range(1000)]

    for tisch in tische:
        tisch.karte_ablegen("König", "Herz", x=10, y=20, aufgedeckt=True)
        tisch.karte_ablegen("Ass", "Pik", x=50, y=20, aufgedeckt=False)

    tische[0].anzeigen()
    tische[1].anzeigen()

    print(f"\nAnzahl tatsächlicher Flyweight-Objekte: {KartenFactory.anzahl_flyweights()}")
    # -> 2 (König_Herz, Ass_Pik) statt 2000 (1000 Tische x 2 Karten)