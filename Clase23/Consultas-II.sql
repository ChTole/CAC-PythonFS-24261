USE python_24261;

-- Ordenar y agrupar
SELECT * 
FROM cursos
WHERE tema_id IN (2, 3) -- condición
ORDER BY tema_id DESC; -- ordenado por tema_id, por defecto ASCendente

-- COUNT recuenta registros
-- Cantidad de cursos con cupo = 5, agrupados por tema
SELECT tema_id, COUNT(*) AS Cantidad
FROM cursos
WHERE cupo = 5
GROUP BY tema_id;

-- DISTINCT
SELECT DISTINCT(tema_id), cupo
FROM cursos
ORDER BY cupo;

-- Datos en tema
SELECT nombre
FROM tema
WHERE nombre LIKE 'Python%'; -- que comience con Python

-- Introducción JOIN
-- Como en la tabla cursos guardo el id del tema, agrego tema para saber el nombre
SELECT t.nombre, c.cupo
FROM tema AS t, cursos AS c -- alias en las tablas
WHERE 
	c.cupo > 8
	AND c.tema_id = t.id;



SELECT * FROM cursos;
SELECT * FROM docente;
SELECT * FROM nivel;
SELECT * FROM tema;