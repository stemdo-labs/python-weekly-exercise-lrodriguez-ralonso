#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE $POSTGRES_DB;

	GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;

    USE $POSTGRES_DB;
    
    CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        edad INTEGER,
        fecha_nacimiento DATE);

    INSERT INTO personas (id, nombre, apellido, edad, fecha_nacimiento)
        VALUES
            (1, 'Juan', 'Perez', 25, '2000-01-01'),
            (2, 'Maria', 'Garcia', 30, '1994-05-10'),
            (3, 'Pedro', 'Rodriguez', 18, '2006-12-25'),
            (4, 'Ana', 'Lopez', 22, '1992-07-04'),
            (5, 'Jose', 'Martinez', 35, '1989-09-15'),
            (6, 'Laura', 'Gonzalez', 28, '1996-03-20'),
            (7, 'Carlos', 'Sanchez', 20, '2004-11-08'),
            (8, 'Sofia', 'Hernandez', 19, '2005-06-12'),
            (9, 'David', 'Diaz', 27, '1997-02-14'),
            (10, 'Andrea', 'Ruiz', 23, '1991-10-27');
EOSQL

