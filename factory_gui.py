# GUI Element Basisinterface
class Button:
    def render(self):
        pass

class Label:
    def render(self):
        pass

# Konkrete GUI Elemente für Windows
class WindowsButton(Button):
    def render(self):
        return "Windows Button gerendert"

class WindowsLabel(Label):
    def render(self):
        return "Windows Label gerendert"

# Konkrete GUI Elemente für Mac
class MacButton(Button):
    def render(self):
        return "Mac Button gerendert"

class MacLabel(Label):
    def render(self):
        return "Mac Label gerendert"

# GUI Factory
class GUIFactory:
    @staticmethod
    def create_button(platform):
        if platform == 'windows':
            return WindowsButton()
        elif platform == 'mac':
            return MacButton()
        else:
            raise ValueError("Unbekannte Plattform")

    @staticmethod
    def create_label(platform):
        if platform == 'windows':
            return WindowsLabel()
        elif platform == 'mac':
            return MacLabel()
        else:
            raise ValueError("Unbekannte Plattform")

# Benutzung der GUIFactory
platform = 'mac'

button = GUIFactory.create_button(platform)
label = GUIFactory.create_label(platform)

print(button.render())  # Output: Mac Button gerendert
print(label.render())   # Output: Mac Label gerendert
