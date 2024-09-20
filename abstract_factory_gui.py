# Schritt 1: Abstrakte GUI-Komponenten

class Button:
    def click(self):
        pass

class Checkbox:
    def check(self):
        pass


# Schritt 2: Konkrete Implementierungen der GUI-Komponenten

class WindowsButton(Button):
    def click(self):
        print("Windows Button clicked!")

class MacButton(Button):
    def click(self):
        print("Mac Button clicked!")

class LinuxButton(Button):
    def click(self):
        print("Linux Button clicked!")


class WindowsCheckbox(Checkbox):
    def check(self):
        print("Windows Checkbox checked!")

class MacCheckbox(Checkbox):
    def check(self):
        print("Mac Checkbox checked!")

class LinuxCheckbox(Checkbox):
    def check(self):
        print("Linux Checkbox checked!")


# Schritt 3: Abstrakte Factory

class GUIFactory:
    def create_button(self) -> Button:
        pass
    
    def create_checkbox(self) -> Checkbox:
        pass


# Schritt 4: Konkrete Factories für jedes Betriebssystem

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()


# Schritt 5: Client Code

def create_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    
    button.click()
    checkbox.check()


# Schritt 6: Teste verschiedene Factories

if __name__ == "__main__":
    os_type = input("Welches Betriebssystem verwenden Sie? (windows/mac/linux): ").strip().lower()
    
    if os_type == "windows":
        factory = WindowsFactory()
    elif os_type == "mac":
        factory = MacFactory()
    elif os_type == "linux":
        factory = LinuxFactory()
    else:
        print("Ungültiges Betriebssystem")
        exit(1)
    
    create_gui(factory)
