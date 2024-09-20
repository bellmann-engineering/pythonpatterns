import sqlite3

class DatabaseConnection:
    _instance = None  # Speichert die einzige Instanz

    def __new__(cls):
        # Erstelle nur eine Instanz, falls sie noch nicht existiert
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect('example.db')  # Verbinde zur Datenbank
        return cls._instance

    def get_connection(self):
        return self.connection

# Test des Singleton Patterns mit Datenbankverbindungen
db1 = DatabaseConnection()
db2 = DatabaseConnection()

# Beide Instanzen sollten dieselbe Verbindung nutzen
print(db1.get_connection() == db2.get_connection())  # Output: True (gleiche Verbindung)


# Use:

# Erste Datenbankoperation
db1 = DatabaseConnection()
cursor = db1.get_connection().cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO users (name) VALUES ("Alice")')
db1.get_connection().commit()

# Zweite Datenbankoperation an einer anderen Stelle im Code
db2 = DatabaseConnection()
cursor2 = db2.get_connection().cursor()
cursor2.execute('SELECT * FROM users')
print(cursor2.fetchall())  # Output: [(1, 'Alice')]