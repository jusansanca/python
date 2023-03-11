
--creacion base de datos
CREATE DATABASE revistas;

--selccionar base de datos
USE revistas;

--creacion de tablas

CREATE TABLE tbrevistas(issn INT(50) PRIMARY KEY NOT NULL, titulorevista VARCHAR(50), numrevista INT, anopublica DATE);

CREATE TABLE tbautores(idautor INT(30) PRIMARY KEY NOT NULL, nombreaut VARCHAR(40), correoaur VARCHAR(30), adscripaut VARCHAR(30), posarticu INT);

CREATE TABLE tbarticulos(idarticulo INT(30) PRIMARY KEY NOT NULL, tituloarticulo VARCHAR(50) UNIQUE, paginicio INT, pagfin INT, idautor INT(30),
 issn INT, FOREIGN KEY (issn) REFERENCES tbrevistas(issn), FOREIGN KEY (idautor) REFERENCES tbautores(idautor));

 --crud

--insercion de datos:
--create
INSERT INTO tbrevistas (issn, titulorevista, numrevista, anopublica) VALUES(123456789,"revista shock",45,"2019-05-24");
INSERT INTO tbrevistas (issn, titulorevista, numrevista, anopublica) VALUES(123478945,"revista jimeno",1,"1990-02-26");
INSERT INTO tbrevistas (issn, titulorevista, numrevista, anopublica) VALUES(123432145,"revista atlas",25,"1987-12-01");
INSERT INTO tbrevistas (issn, titulorevista, numrevista, anopublica) VALUES(123432659,"revista pocillo",32,"2021-02-24");
INSERT INTO tbrevistas (issn, titulorevista, numrevista, anopublica) VALUES(123457458,"revista magacine",75,"2023-02-24");
INSERT INTO tbrevistas (issn, titulorevista, numrevista, anopublica) VALUES(123452568,"revista ola",45,"2020-03-25");


INSERT INTO tbautores (idautor, nombreaut, correoaur, adscripaut, posarticu) VALUES(1014203614,"gonzalo","gozalolibro@pepito.com.co","santillana",1);
INSERT INTO tbautores (idautor, nombreaut, correoaur, adscripaut, posarticu) VALUES(1125689536,"alberto","albertoarticulo@pepito.com.co","semana",2);
INSERT INTO tbautores (idautor, nombreaut, correoaur, adscripaut, posarticu) VALUES(1024859756,"libardo","librandolibro@pepito.com.co","el tiempo",2);
INSERT INTO tbautores (idautor, nombreaut, correoaur, adscripaut, posarticu) VALUES(1121857456,"leonardo","leon-ardo@pepito.com.co","la libertad",1);
INSERT INTO tbautores (idautor, nombreaut, correoaur, adscripaut, posarticu) VALUES(1023659875,"guillo","grillo.guillo@pepito.com.co","moquillo",1);

INSERT INTO tbarticulos (idarticulo, tituloarticulo, paginicio, pagfin, idautor,issn) VALUES(456,"lo que mi perro se llevo", 45, 47, 1014203614,123432659);
INSERT INTO tbarticulos (idarticulo, tituloarticulo, paginicio, pagfin, idautor,issn) VALUES(845,"el principio del final", 12,13 , 1024859756,123457458);
INSERT INTO tbarticulos (idarticulo, tituloarticulo, paginicio, pagfin, idautor,issn) VALUES(387,"vuelve la arepa al trigo", 5, 10, 1023659875,123432145);
INSERT INTO tbarticulos (idarticulo, tituloarticulo, paginicio, pagfin, idautor,issn) VALUES(659,"ya valimos madre", 1, 2, 1125689536,123452568);
INSERT INTO tbarticulos (idarticulo, tituloarticulo, paginicio, pagfin, idautor,issn) VALUES(472,"seguis valiendo madre", 7,15 , 1014203614,123432659);

--read
SELECT issn, numrevista, anopublica FROM tbrevistas ORDER BY anopublica DESC;

SELECT * FROM tbautores WHERE adscripaut LIKE   's%';

SELECT idarticulo FROM tbarticulos WHERE idautor = 1014203614;

--update

UPDATE tbarticulos
SET idarticulo = 857, tituloarticulo = "ave maria" 
WHERE idarticulo = 659 ;













