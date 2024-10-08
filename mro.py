class X:
    def show(self):
        print("X.show()")

class Y(X):
    def show(self):
        print("Y.show()")

class Z(X):
    def show(self):
        print("Z.show()")

class W(Y, Z):
    pass

w = W()
w.show()  # Welche Methode wird aufgerufen?

print(W.mro())  # Zeige die Reihenfolge der Methodenauflösung
