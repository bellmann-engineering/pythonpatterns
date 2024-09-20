from functools import wraps

def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Singleton:
    def __init__(self):
        print("Singleton Instanz erstellt")

@singleton
class Logger:
    def __init__(self):
        print("Logger Instanz erstellt")

singleton1 = Singleton()
singleton2 = Singleton()
logger1 = Logger()
logger2 = Logger()

print(singleton1)
print(singleton2)
print(logger1)
print(logger2)

print(singleton1 == singleton2)  # Output: True (es ist die gleiche Instanz)
