class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # __str__ für die menschenlesbare Darstellung
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} Jahre alt"

    # __repr__ für die formale Repräsentation
    def __repr__(self):
        return f"Person('{self.first_name}', '{self.last_name}', {self.age})"

    # __eq__ zum Vergleichen von Personen
    def __eq__(self, other):
        return (self.first_name == other.first_name and 
                self.last_name == other.last_name and 
                self.age == other.age)

    # __lt__ zum Vergleichen des Alters
    def __lt__(self, other):
        return self.age < other.age

    # __len__ gibt die Länge des vollständigen Namens zurück
    def __len__(self):
        return len(self.first_name) + len(self.last_name)


if __name__ == "__main__":
    person1 = Person("John", "Doe", 30)
    person2 = Person("Jane", "Doe", 25)

    print(person1)  # Ausgabe: John Doe, 30 Jahre alt
    print(repr(person2))  # Ausgabe: Person('Jane', 'Doe', 25)
    print(person1 == person2)  # Ausgabe: False
    print(person1 < person2)  # Ausgabe: False, da John älter ist als Jane
    print(len(person1))  # Ausgabe: Länge des Namens John Doe
