% --- regula: nalezy/2 ---

nalezy(A, [A|_]).
nalezy(A, [_|T]) :- nalezy(A, T).

% --- Reguła: dlugosc/2 ---

dlugosc([], 0).
dlugosc([_|T], N) :- dlugosc(T, N2), N is N2 + 1.
