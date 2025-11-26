from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):
    @abstractmethod # stworzenie metody abstrakcyjnej
    def pole(self):
       pass
    
class Kolo(Figura):
    def __init__(self, r):
        self.r = r
    def pole(self): # nadpisanie metody abstrakcyjnej
        return pi * self.r ** 2

class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def pole(self): # nadpisanie metody abstrakcyjnej
        return self.a * self.b

class Trojkat(Figura):
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def pole(self): # nadpisanie metody abstrakcyjnej
        return self.a * self.h / 2

if __name__ == "__main__":
    figury = [ Kolo(5), Prostokat(4, 6), Trojkat(4, 5), Kolo(3) ]
    for f in figury:
        print(f.pole())
