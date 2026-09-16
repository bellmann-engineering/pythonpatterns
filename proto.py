import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Enemy(Prototype):
    def __init__(self, name, health, weapons=None):
        self.name = name
        self.health = health
        self.weapons = weapons if weapons is not None else []

    def __repr__(self):
        return f"Enemy(name={self.name}, health={self.health}, weapons={self.weapons})"


# Prototyp erstellen (aufwendig konfiguriert)
orc_prototype = Enemy("Orc", health=100, weapons=["Axt", "Schild"])

# Klone erzeugen statt neu zu instanziieren
orc1 = orc_prototype.clone()
orc2 = orc_prototype.clone()

# Klone unabhängig anpassen
orc1.name = "Orc-Krieger"
orc1.weapons.append("Speer")

print(orc_prototype)  # Enemy(name=Orc, health=100, weapons=['Axt', 'Schild'])
print(orc1)            # Enemy(name=Orc-Krieger, health=100, weapons=['Axt', 'Schild', 'Speer'])
print(orc2)            # Enemy(name=Orc, health=100, weapons=['Axt', 'Schild'])


class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, name, prototype):
        self._prototypes[name] = prototype

    def create(self, name):
        return self._prototypes[name].clone()


registry = PrototypeRegistry()
registry.register("orc", Enemy("Orc", 100, ["Axt"]))
registry.register("goblin", Enemy("Goblin", 40, ["Dolch"]))

new_orc = registry.create("orc")
new_goblin = registry.create("goblin")