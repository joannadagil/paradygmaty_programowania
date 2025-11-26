% --- Fakty: relacje studiuje(student, kierunek) ---

studiuje(hela, informatyka).
studiuje(asia, informatyka).
studiuje(fela, informatyka).
studiuje(olaf, informatyka).
studiuje(anna, matematyka).
studiuje(paul, matematyka).
studiuje(alek, matematyka).


% --- Reguła: studiowany(kierunek, student) ---

studiowany(Kierunek, Osoba) :-
    studiuje(Osoba, Kierunek).

% --- Fakty: relacje prowadzi(osoba, kierunek) ---

prowadzi(adam, informatyka).
prowadzi(asia, matematyka).

% --- Reguła: prowadzony(kierunek, osoba) ---

prowadzony(Kierunek, Osoba) :-
    prowadzi(Osoba, Kierunek).

% --- Reguła: prowadzacy_studenta(prowadzacy, student) ---

prowadzacy_studenta(Prowadzacy, Student) :-
    prowadzi(Prowadzacy, Kierunek),
    studiuje(Student, Kierunek).

% --- Reguła: studenci_prowadzacego(student, prowadzacy) ---

studenci_prowadzacego(Prowadzacy, Student) :-
    prowadzi(Prowadzacy, Kierunek),
    studiuje(Student, Kierunek).
