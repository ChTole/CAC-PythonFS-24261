ALTER TABLE docente
	ADD COLUMN email VARCHAR(50);
    
ALTER TABLE docente
	ADD COLUMN activo BOOLEAN;
    
DESCRIBE docente; -- metadatos

SELECT * FROM docente;