-- JOIN y Subconsultas
-- La teoría de conjuntos: es una ciencia matemática que se refiere a conjuntos 
-- y se usa como la base de la manipulación de datos en el modelo relacional.

-- Existen varios tipos de JOIN pero por buenas prácticas sólo vamos a abordar
-- con ejemplos LEFT JOIN y INNER JOIN.


-- Obtener docentes y cursos que dictan 
SELECT d.nombre, d.apellido, t.nombre
FROM docente AS d
LEFT JOIN cursos AS c
	ON d.id = c.docente_id
LEFT JOIN tema AS t
	ON c.tema_id = t.id;
    
-- Sólo docentes con cursos asignados    
SELECT d.nombre, d.apellido, t.nombre
FROM docente AS d
INNER JOIN cursos AS c
	ON d.id = c.docente_id
LEFT JOIN tema AS t
	ON c.tema_id = t.id;
    
-- Subconsultas
-- Permiten desarrollar consultas compuestas, dónde el resultado de una consulta principal
-- depende de un valor o una lista de valores proveniente de otra (sub) consulta.
-- Tener en cuenta que el resultado no puede ser una tabla o tener más de una dimensión.

-- Obtener registros de cursos dónde el tema sea nivel "básico"
SELECT *
FROM cursos
WHERE tema_id = (SELECT id 
				 FROM nivel
                 WHERE nivel = 'básico'); -- monoregistro
                 
-- Subconsulta
SELECT id 
FROM nivel
WHERE nivel = 'básico';

-- Obtener registros de cursos dónde el nombre del tema empiece con "Python"
SELECT *
FROM cursos
WHERE tema_id IN (SELECT id -- (1, 2)
				 FROM tema
                 WHERE nombre LIKE 'Python%'); -- multiregistro
                 
-- Subconsulta
SELECT id 
FROM tema
WHERE nombre LIKE 'Python%';

-- Caso especial: subconsulta correlacionada
-- Cuando la subconsulta analiza la misma tabla que la consulta principal.
-- En éste caso la subconsulta se ejecuta para cada registro, por lo cual
-- si la tabla es extensa demora en obtener un resultado. La solución a ésto es usar
-- tablas temporales.

-- Obtener de cursos los que sean iguales al mayor de los cupos
SELECT tema_id, fecha_inicio, fecha_cierre
FROM cursos
WHERE cupo = (SELECT MAX(cupo)
			  FROM cursos);

SELECT MAX(cupo)
FROM cursos;