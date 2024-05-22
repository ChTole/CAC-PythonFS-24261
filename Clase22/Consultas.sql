-- Lectura de los datos
-- Estructura básica de la consulta
-- SELECT campos
-- FROM tabla
-- WHERE condición (opcional)

-- Datos de la tabla principal (cursos)
-- Condición con expresión relacional
SELECT * 
FROM cursos
WHERE cupo > 8; -- expresión relacional

-- Condición con expresión lógica
-- Obtener registros del docente_id igual a 1 y con cupo mayor a 5.
SELECT * 
FROM cursos
WHERE docente_id = 1
	AND cupo > 5;

-- Pertenencia
SELECT * 
FROM cursos
WHERE tema_id IN (2, 3); -- dónde nivel pertenezca a algún elemento de la tupla


SELECT * From cursos;