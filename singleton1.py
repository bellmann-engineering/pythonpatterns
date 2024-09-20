class Singleton:
    _instance = None  # Klassenattribut für die einzige Instanz

    def __new__(cls):
        # Wenn keine Instanz existiert, erstelle eine neue
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    

# Test des Singleton Patterns
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1)
print(singleton2)

print(singleton1 == singleton2)  # Output: True (beide sind die gleiche Instanz)
