SELECT * 
FROM Studenci 
WHERE rok = 3;

SELECT s.imie, 
       s.nazwisko,
       AVG(o.ocena) AS srednia_ocen
FROM Studenci s JOIN Oceny o ON s.id = o.student_id
GROUP BY s.id;

SELECT s.imie, 
       s.nazwisko,
       AVG(o.ocena) AS srednia_ocen
FROM Studenci s JOIN Oceny o ON s.id = o.student_id
GROUP BY s.id
HAVING AVG(o.ocena) > 4.0;