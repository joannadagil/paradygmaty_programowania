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

def przywitaj(imie):
    print(f"Cześć {imie}!")

def zegnaj(imie):
    print(f"Do zobaczenia, {imie}!")

emitter = EventEmitter()
emitter.on("powitanie", przywitaj)
emitter.on("pozegnanie", zegnaj)

emitter.emit("powitanie", "Anna")
emitter.emit("pozegnanie", "Anna")