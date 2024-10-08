from abc import ABC, abstractmethod

# Abstract Expression Interface
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# Terminal Expression für eine Zahl
class Number(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self):
        return self.number

# Non-Terminal Expression für die Addition
class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

# Non-Terminal Expression für die Subtraktion
class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

# Verwendung des Interpreter Patterns
if __name__ == "__main__":
    # Ausdruck: 5 + 2 - 3
    expression = Subtract(Add(Number(5), Number(2)), Number(3))

    # Interpretation des Ausdrucks
    result = expression.interpret()
    print(f"Das Ergebnis von 5 + 2 - 3 ist: {result}")
