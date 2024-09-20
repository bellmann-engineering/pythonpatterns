class Store:
    def __init__(self):
        self.products = []
        self.new_products = []

    # Füge ein neues Produkt hinzu und speichere es in der neuen Produktliste
    def add_product(self, product):
        self.products.append(product)
        self.new_products.append(product)

    # Kunden fragen den Store, ob es neue Produkte gibt
    def check_for_new_products(self):
        if self.new_products:
            return self.new_products
        return []

    # Wenn die neuen Produkte "abgefragt" wurden, wird die Liste geleert
    def clear_new_products(self):
        self.new_products = []

class Customer:
    def __init__(self, name):
        self.name = name

    # Kunden fragen aktiv nach neuen Produkten im Store
    def inquire_new_products(self, store):
        new_products = store.check_for_new_products()
        if new_products:
            print(f'{self.name} wurde informiert: Neue Produkte - {", ".join(new_products)}')
            store.clear_new_products()
        else:
            print(f'{self.name} hat nach neuen Produkten gefragt, aber es gibt keine neuen Produkte.')

# Erstelle den Store
store = Store()

# Erstelle Kunden
customer1 = Customer('Alice')
customer2 = Customer('Bob')

# Kunden fragen den Store nach neuen Produkten
customer1.inquire_new_products(store)
customer2.inquire_new_products(store)

# Füge ein neues Produkt hinzu
store.add_product('Laptop')

# Kunden fragen erneut nach neuen Produkten
customer1.inquire_new_products(store)
customer2.inquire_new_products(store)

# Nochmals fragen, obwohl keine neuen Produkte hinzugefügt wurden
customer1.inquire_new_products(store)
customer2.inquire_new_products(store)
