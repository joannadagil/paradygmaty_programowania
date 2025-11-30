class Observer:
    def update(self, dane):
        raise NotImplementedError

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self, dane):
        for o in self.observers:
            o.update(dane)
            
# Przykład użycia
class Logger(Observer):
    def update(self, dane):
        print(f"[LOG]: {dane}")

class Alarm(Observer):
    def update(self, dane):
        if dane > 100:
            print("⚠ Alarm! Dane przekroczyły 100")

subject = Subject()
subject.attach(Logger())
subject.attach(Alarm())

subject.notify(50)
subject.notify(120)
