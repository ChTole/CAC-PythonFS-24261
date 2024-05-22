-- Editor de código (comentario en una línea)
/* 
Comentario 
de más
de una
línea
*/

-- Creación de la BBDD
-- Las palabras reservadas del lenguaje siempre en mayúsculas.
-- Los nombres creados (tablas, campos, DDBB) camelCase o snake_case.

CREATE DATABASE cac_python_fs;

-- Acceder a la BBDD
USE cac_python_fs;

-- Cursos: campos o atributos
-- Creación de la tabla, columnas (atributos) y filas (registros o instancias -- cursos)
/*
nombre: string;
fecha_inicio: date --> cadena
fecha_fin: date --> cadena
docente: string;
capacidad_cupo: número entero;
*/

CREATE TABLE cursos (
	nombre VARCHAR(30),
    fecha_inicio DATE, -- '2024-07-01'
    fecha_fin DATE,
    docente VARCHAR(60),
    capacidad_cupo INT);


-- Sublenguajes en SQL
-- DDL - Data Description Language
-- Creación de tablas y definición de los tipos de datos.

-- DML - Data Manipulation Language
/* Manipulación de datos
C reate
R ead
U pdate
D elete
*/

-- DCL - Data Control Language
-- Permisos y privilegios de usuarios.







