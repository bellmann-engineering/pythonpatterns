from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal

# class Printable(ABC):
#     @abstractmethod
#     def print(self):
#         pass

class Bankkonto(object):
    def __init__(self, kontonummer, inhaber, startguthaben=0.0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.kontostand = startguthaben

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
        else:
            print("Ungültiger Betrag.")

    def abheben(self, betrag):
        if 0 < betrag <= self.kontostand:
            self.kontostand -= betrag
        else:
            print("Nicht genügend Guthaben oder ungültiger Betrag.")

    def kontostand_anzeigen(self):
        return f"Kontostand ({self.kontonummer}): {self.kontostand:.2f} €"
    
    def __str__(self):
        return f"{self.inhaber} ({self.kontonummer})"

    def __repr__(self):
        return self.kontonummer
    
    def __eq__(self, other):
        return self.kontonummer == other.kontonummer

class Account:
    def buchen(self):
        print("gebucht")  

class Sparkonto(Bankkonto):
    def __init__(self, kontonummer, inhaber, startguthaben=0, zins=0):
        super().__init__(kontonummer, inhaber, startguthaben)
        self.zins = zins
    
    def __str__(self):
        return super().__str__() + f" mit {self.zins} % Verzinsung"


konto1 = Bankkonto("12345678", "Peter Pan",  100.0)
konto2 = Bankkonto("55555121", "Max Pan",  100.0)



print(konto1 != konto2)
