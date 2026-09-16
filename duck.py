from abc import ABC, abstractmethod

# class INotifyable(ABC):
#     @abstractmethod
#     def send(self):
#         pass

class Mobile():
    def send(self, msg):
        print("Sende per Handy")

class Mail():
    def send(self, msg):
        print("Sende per Mail")

class Fax():
    def send(self, msg):
        print("Sende per Fax")




def notify():
    mo = Mobile()
    ma = Mail()
    f = Fax()
    devices = [mo, ma, f]
    for d in devices:
        d.send("Hallo")


notify()