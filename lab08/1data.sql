INSERT INTO Studenci (imie, nazwisko, rok, kierunek) VALUES
('Anna', 'Kowalska', 1, 'Informatyka'),
('Jan', 'Nowak', 3, 'Informatyka'),
('Maria', 'Wiśniewska', 2, 'Matematyka'),
('Krzysztof', 'Malinowski', 3, 'Informatyka');

INSERT INTO Przedmioty (nazwa) VALUES
('Analiza'),
('Algebra'),
('Programowanie');

INSERT INTO Oceny (student_id, przedmiot_id, ocena) VALUES
(1, 1, 4.5),
(1, 2, 5.0),
(2, 1, 3.5),
(2, 3, 4.0),
(3, 2, 4.0),
(4, 1, 5.0),
(4, 3, 4.5);