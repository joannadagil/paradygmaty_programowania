import time
import random

class EventEmitter:
    def __init__(self):
        self.handlers = {}
        
    def on(self, event, handler):
        """Rejestruje handler dla danego zdarzenia."""
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(handler)

    def emit(self, event, *args, **kwargs):
        """Wywołuje wszystkie handlery przypisane do zdarzenia."""
        if event in self.handlers:
            for h in self.handlers[event]:
                h(*args, **kwargs)

# ------ definiowanie i rejestrowanie handlerów ------

emitter = EventEmitter()

def zglos_burze(poziom):
    if poziom > 50:
        print(f"Uwaga! Burza o poziomie {poziom}!")

emitter.on(0, zglos_burze)

def zglos_huragan(poziom):
    print(f"Uwaga! Huragan o poziomie {poziom}!")   

emitter.on(1, zglos_huragan)

def zglos_pozar(poziom):
    print(f"Uwaga! Pożar o poziomie {poziom}!")

emitter.on(2, zglos_pozar)

# ------ symulacja strumienia zdarzeń ------

def strumien():
    while True:
        yield (random.randint(0,4), random.randint(0, 100))
        time.sleep(0.5)

def monitor(strumien):
    for zdarzenie, poziom in strumien:
        if zdarzenie < 3:
            emitter.emit(zdarzenie, poziom)

if __name__ == "__main__":
    stream = strumien()
    monitor(stream)