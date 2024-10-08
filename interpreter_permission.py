# Abstrakte Klasse für einen Berechtigungsausdruck
class PermissionExpression:
    def interpret(self, context):
        pass

# Terminal-Ausdruck für eine einzelne Berechtigung
class Permission(PermissionExpression):
    def __init__(self, permission):
        self.permission = permission

    def interpret(self, context):
        return self.permission in context

# Nicht-terminaler Ausdruck für "und"-Bedingungen
class AndExpression(PermissionExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) and self.right.interpret(context)

# Nicht-terminaler Ausdruck für "oder"-Bedingungen
class OrExpression(PermissionExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) or self.right.interpret(context)

# Beispielhafter Aufbau eines Zugriffsregel-Ausdrucks
def build_permission_expression():
    # Beispiel: Der Benutzer muss sowohl "lesen" als auch entweder "schreiben" oder "löschen" können
    read_permission = Permission("lesen")
    write_permission = Permission("schreiben")
    delete_permission = Permission("löschen")
    
    write_or_delete = OrExpression(write_permission, delete_permission)
    expression = AndExpression(read_permission, write_or_delete)
    
    return expression



# Kontext: Welche Berechtigungen hat der Benutzer?
user_permissions = {"lesen", "schreiben"}

# Erstelle den Ausdruck und interpretiere ihn
expression = build_permission_expression()
result = expression.interpret(user_permissions)
print(f"Hat der Benutzer die erforderlichen Berechtigungen? {result}")
