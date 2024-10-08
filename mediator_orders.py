# Mediator Interface
class Mediator:
    def notify(self, sender, event):
        pass

# Konkreter Mediator
class NotificationMediator(Mediator):
    def __init__(self):
        self.order_service = None
        self.inventory_service = None
        self.email_service = None

    def set_services(self, order_service, inventory_service, email_service):
        self.order_service = order_service
        self.inventory_service = inventory_service
        self.email_service = email_service

    def notify(self, sender, event):
        if event == "order_placed":
            print("Mediator: Bestellung wurde platziert, prüfe den Bestand.")
            self.inventory_service.check_stock()
        elif event == "stock_confirmed":
            print("Mediator: Bestand bestätigt, sende Bestätigungs-E-Mail.")
            self.email_service.send_confirmation()
        elif event == "out_of_stock":
            print("Mediator: Produkt nicht auf Lager, sende E-Mail über Verzögerung.")
            self.email_service.send_out_of_stock_notification()

# Bestellservice
class OrderService:
    def __init__(self, mediator):
        self.mediator = mediator

    def place_order(self):
        print("Bestellservice: Bestellung wird platziert.")
        self.mediator.notify(self, "order_placed")

# Bestandsservice
class InventoryService:
    def __init__(self, mediator):
        self.mediator = mediator

    def check_stock(self):
        # Beispiel: Angenommen, das Produkt ist auf Lager
        product_in_stock = True
        if product_in_stock:
            print("Bestandsservice: Produkt ist verfügbar.")
            self.mediator.notify(self, "stock_confirmed")
        else:
            print("Bestandsservice: Produkt ist nicht auf Lager.")
            self.mediator.notify(self, "out_of_stock")

# E-Mail-Service
class EmailService:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_confirmation(self):
        print("E-Mail-Service: Bestellbestätigung wird gesendet.")

    def send_out_of_stock_notification(self):
        print("E-Mail-Service: Produkt nicht auf Lager, Benachrichtigung über Verzögerung wird gesendet.")


def main():
    # Erstelle den Mediator
    mediator = NotificationMediator()

    # Erstelle die Services und weise den Mediator zu
    order_service = OrderService(mediator)
    inventory_service = InventoryService(mediator)
    email_service = EmailService(mediator)

    # Setze die Services in den Mediator
    mediator.set_services(order_service, inventory_service, email_service)

    # Simuliere das Platzieren einer Bestellung
    order_service.place_order()

if __name__ == "__main__":
    main()
