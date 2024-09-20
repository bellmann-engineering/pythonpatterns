# Das Subject, das Benachrichtigungen verschickt
class Store:
    def __init__(self):
        self.products = []
        self.observers = []

    # Kunden können sich für Benachrichtigungen registrieren
    def add_observer(self, observer):
        self.observers.append(observer)

    # Ein Produkt wird hinzugefügt und alle Observer werden benachrichtigt
    def add_product(self, product):
        self.products.append(product)
        self.notify_observers(product)

    def notify_observers(self, product):
        for observer in self.observers:
            observer.update(product)

# Das Observer Interface, welches von Kunden implementiert wird
class Customer:
    def __init__(self, name):
        self.name = name

    # Die Methode, die aufgerufen wird, wenn eine Benachrichtigung erfolgt
    def update(self, product):
        print(f'{self.name} wurde benachrichtigt: Neues Produkt hinzugefügt - {product}')

# Erstelle den Store
store = Store()

# Erstelle Kunden, die als Observer agieren
customer1 = Customer('Alice')
customer2 = Customer('Bob')

# Kunden abonnieren die Benachrichtigungen des Stores
store.add_observer(customer1)
store.add_observer(customer2)

# Füge ein neues Produkt hinzu, und benachrichtige die Kunden
store.add_product('Laptop')
