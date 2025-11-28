% --- fakty: krawedz/2 ---
krawedz(1, 2).
krawedz(2, 3).
krawedz(3, 4).

krawedz(5, 6).
krawedz(6, 7).

% --- regula: sciezka/3 ---

sciezka(Start, End, [Start, End]) :- krawedz(Start, End).
sciezka(Start, End, [Start|Tail]) :- krawedz(Start, X), sciezka(X, End, Tail).
