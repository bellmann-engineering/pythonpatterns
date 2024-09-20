class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_product(self, product):
        self.products.append(product)
        self.notify_customers(product)

    def notify_customers(self, product):
        for customer in self.customers:
            print(f'Notifying {customer.name}: New product added - {product}')

class Customer:
    def __init__(self, name):
        self.name = name

# Erstelle den Store und füge Kunden hinzu
store = Store()
customer1 = Customer('Alice')
customer2 = Customer('Bob')

store.add_customer(customer1)
store.add_customer(customer2)

# Füge ein neues Produkt hinzu und benachrichtige die Kunden
store.add_product('Laptop')
