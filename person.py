from dataclasses import dataclass
from datetime import datetime

@dataclass
class Office:
    floor: str
    location: str
    max_empl_number : int

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = datetime.strptime(birthdate, '%d.%m.%Y')

    def __str__(self) -> str:
        return f"Ich bin {self.name} und bin {self.age} Jahre alt."
    
    def __repr__(self) -> str:
        return f"PERSON: {self.name} ({self.age})"
    
    # @property
    # def age(self) -> int:
    #     return datetime.now - self.birthdate
    
    
    

p1 = Person("Hans", '1.6.1980')
#p1.age

o = Office("Mainfloor", "Hauptstr", 24)
print(o)


