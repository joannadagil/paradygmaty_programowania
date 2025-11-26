% --- Fakty: relacje rodzic(dorosły, dziecko) ---

rodzic(jan, anna).
rodzic(jan, piotr).
rodzic(anna, kasia).
rodzic(anna, bartek).
rodzic(piotr, ola).
rodzic(piotr, tomek).
rodzic(maria, jan).
rodzic(maria, ewa).

% --- Reguła: dziecko/2 ---

dziecko(Dziecko, Rodzic) :-
    rodzic(Rodzic, Dziecko).

% --- Reguła: przodek/2 ---

przodek(Przodek, Potomek) :-
    rodzic(Przodek, Potomek).

przodek(Przodek, Potomek) :-
    rodzic(Przodek, Posrednik),
    przodek(Posrednik, Potomek).
