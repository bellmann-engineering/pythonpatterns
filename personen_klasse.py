class Person:
    def __init__(self, vorname : str, nachname : str = None):
        self.__vorname = vorname
        self.nachname = nachname

    @property
    def vorname(self):
        return self.__vorname
    
    @vorname.setter
    def vorname(self, name: str):
        if not name:
            raise ValueError("Name muss gesetzt werden")
        if len(name) < 3: 
            raise ValueError("Name zu kurz")
        self.__vorname = name

    def __str__(self) -> str:
        return self.vorname
    
    def __repr__(self) -> str:
        #return self.vorname
        cls_name = self.__class__.__name__
        attrs = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{cls_name}({attrs})"

    
    @property
    def fullname(self):
        if self.nachname is not None:
            return f"{self.vorname} {self.nachname}"
        else:
            return f"{self.vorname}"
        
    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.vorname = first
        self.nachname = last



p1 = Person("Max")
p2 = Person("Peter", "Pan")

#p1.vorname = "M"

personen = [p1, p2]
print(personen)
# for p in personen:
#     print(p.fullname)
