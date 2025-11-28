% --- fakt: dziecko/2 ---

dziecko(hela, anna).
dziecko(asia, anna).
dziecko(anna, olaf).
dziecko(paul, alek).
dziecko(fela, alek).
dziecko(alek, olaf).
dziecko(olaf, mela).

% --- regula: rodzenstwo/2 ---

rodzenstwo(A, B) :- dziecko(A, Rodzic), dziecko(B, Rodzic).

% --- Reguła: dziadek/2 ---

dziadek(Dziadek, Wnuk) :- dziecko(Rodzic, Dziadek), rodzic(Wnuk, Rodzic).

% --- Reguła: przodek/2 ---

przodek(Przodek, Potomek) :- dziecko(Potomek, Przodek).
przodek(Przodek, Potomek) :- dziecko(Posrednik, Przodek), przodek(Posrednik, Potomek).