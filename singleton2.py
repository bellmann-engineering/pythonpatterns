class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        print("Initialisierung des Singleton")

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1)
print(singleton2)


