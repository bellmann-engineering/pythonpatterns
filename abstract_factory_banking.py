# Schritt 1: Abstrakte Bankprodukte

class Account:
    def account_type(self):
        pass

class CreditCard:
    def card_type(self):
        pass


# Schritt 2: Konkrete Implementierungen der Bankprodukte

class TraditionalCheckingAccount(Account):
    def account_type(self):
        return "Traditionelles Girokonto"

class OnlineCheckingAccount(Account):
    def account_type(self):
        return "Online-Girokonto"


class TraditionalCreditCard(CreditCard):
    def card_type(self):
        return "Physische Kreditkarte"

class VirtualCreditCard(CreditCard):
    def card_type(self):
        return "Virtuelle Kreditkarte"


# Schritt 3: Abstrakte Factory

class BankFactory:
    def create_account(self) -> Account:
        pass
    
    def create_credit_card(self) -> CreditCard:
        pass


# Schritt 4: Konkrete Factories für traditionelle und Online-Banken

class TraditionalBankFactory(BankFactory):
    def create_account(self) -> Account:
        return TraditionalCheckingAccount()
    
    def create_credit_card(self) -> CreditCard:
        return TraditionalCreditCard()

class OnlineBankFactory(BankFactory):
    def create_account(self) -> Account:
        return OnlineCheckingAccount()
    
    def create_credit_card(self) -> CreditCard:
        return VirtualCreditCard()


# Schritt 5: Client Code

def create_bank_products(factory: BankFactory):
    account = factory.create_account()
    card = factory.create_credit_card()
    
    print(f"Konto erstellt: {account.account_type()}")
    print(f"Kreditkarte erstellt: {card.card_type()}")


# Schritt 6: Teste verschiedene Factories

if __name__ == "__main__":
    bank_type = "online"
    
    if bank_type == "traditional":
        factory = TraditionalBankFactory()
    elif bank_type == "online":
        factory = OnlineBankFactory()
    
    create_bank_products(factory)
