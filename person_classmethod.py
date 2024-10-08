class Person:
    def __init__(self, vorname, nachname) -> None:
        self.vorname = vorname
        self.nachname = nachname

    @classmethod
    def from_string(cls, input):
        first, last = input.split()
        return cls(first, last)
    

personen_raw = [ "Hans Meier", "Peter Pan", "Karl Niemand" ]

personenliste = []
for p in personen_raw:
    personenliste.append(Person.from_string(p))

print(personenliste)
