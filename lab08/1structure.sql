CREATE DATABASE IF NOT EXISTS usos;
USE usos;

CREATE TABLE IF NOT EXISTS Studenci (
    id INT PRIMARY KEY AUTO_INCREMENT,
    imie VARCHAR(100),
    nazwisko VARCHAR(100),
    rok INT,
    kierunek VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Przedmioty (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nazwa VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Oceny (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    przedmiot_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Studenci(id),
    FOREIGN KEY (przedmiot_id) REFERENCES Przedmioty(id),
    ocena DECIMAL(2,1)
);