import time
import random

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
    
    def generate_data(self):
        """Symuluje generowanie danych pogodowych."""
        temp = random.randint(-20, 40)
        humidity = random.randint(0, 100)
        pressure = random.randint(950, 1050)
        return (temp, humidity, pressure)
            
# Przykład użycia
class Logger(Observer):
    def update(self, dane):
        print(f"[LOG]")

class Alarm(Observer):
    def update(self, dane):
        temp, humidity, pressure = dane
        if temp > 30:
            print("[Alarm] Temperatura przekroczyła 30°C")
        if humidity < 20:
            print("[Alarm] Wilgotność spadła poniżej 20%")
        if pressure < 980:
            print("[Alarm] Ciśnienie spadło poniżej 980 hPa")

class UI(Observer):
    def update(self, dane):
        print(f"[UI] Aktualizacja danych:")
        print(f"     Temperatura: {dane[0]}°C")
        print(f"     Wilgotność: {dane[1]}%")       
        print(f"     Ciśnienie: {dane[2]} hPa")

stacja_pogodowa = Subject()
stacja_pogodowa.attach(Logger())
stacja_pogodowa.attach(Alarm())
stacja_pogodowa.attach(UI())

while True:
    stacja_pogodowa.notify(stacja_pogodowa.generate_data())
    time.sleep(1)
