DROP TABLE IF EXISTS contrato_venta CASCADE;
DROP TABLE IF EXISTS contrato_compra CASCADE ;
DROP TABLE IF EXISTS cliente CASCADE;
DROP TABLE IF EXISTS inmueble CASCADE;
DROP TABLE IF EXISTS agente CASCADE;
DROP TABLE IF EXISTS ciudad CASCADE;
DROP TABLE IF EXISTS imagenes_inmueble CASCADE;
DROP TABLE IF EXISTS localizacion CASCADE;


CREATE TABLE localizacion (
    id SERIAL PRIMARY KEY,
    ciudad VARCHAR(50),
    provincia VARCHAR(50)
);

CREATE TABLE agente (
    cedula VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    localizacion INT REFERENCES localizacion(id),
    direccion VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(50),
    titulo VARCHAR(50)
);

CREATE TABLE inmueble (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    direccion VARCHAR(100),
    localizacion INT REFERENCES localizacion(id),
    precio DECIMAL(10,2),
    descripcion TEXT,
    num_de_pisos INT,
    anio_de_construccion INT,
    piscina BOOLEAN,
    area NUMERIC(10,2),
    num_de_banos INT,
    estacionamiento BOOLEAN,
    num_de_cuartos INT
);

CREATE TABLE cliente (
    id VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    localizacion INT REFERENCES localizacion(id),
    direccion VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(50)
);


CREATE TABLE contrato_compra (
    id SERIAL PRIMARY KEY,
    fecha_inicio DATE CHECK (fecha_inicio >= CURRENT_DATE),
    fecha_fin DATE CHECK (fecha_fin IS NOT DISTINCT FROM NULL OR fecha_fin >= fecha_inicio),
    cliente_comprador VARCHAR(50) REFERENCES cliente(id),
    id_inmueble INT REFERENCES inmueble(id)
);

CREATE TABLE contrato_venta (
    id SERIAL PRIMARY KEY,
    asesor VARCHAR(50) REFERENCES agente(cedula),
    fecha_inicio DATE CHECK (fecha_inicio >= CURRENT_DATE),
    fecha_fin DATE CHECK (fecha_fin >= fecha_inicio),
    cliente_vendedor VARCHAR(50) REFERENCES cliente(id),
    tipo VARCHAR(50),
    comision DECIMAL(10,2),
    id_inmueble INT REFERENCES inmueble(id) 
);


INSERT INTO localizacion VALUES (1, 'Cuenca','Azuay');
INSERT INTO localizacion VALUES (2, 'Cuenca','Baños');


-- Insert data into 'agente'
INSERT INTO agente (cedula, nombre, apellido,localizacion, direccion, telefono, email, titulo)
    VALUES 
    ('1', 'Jeremy', 'Smith', 1,'123 Main St', '1234567890', 'jeremy@email.com', 'Senior Agent'),
    ('2', 'Rachel', 'Johnson',1, '456 Pine St', '2345678901', 'rachel@email.com', 'Junior Agent');


INSERT INTO inmueble (id, tipo, direccion, localizacion, precio, descripcion,num_de_pisos,anio_de_construccion,piscina,area,num_de_banos,estacionamiento,num_de_cuartos)
    VALUES
    (1,'Particular','123 Main St', 1, 100000, 'Casa cerca del lago', 1, 2000, TRUE, 100, 2, TRUE, 3),
    (2,'Comercial','456 Pine St', 2, 200000, 'Cerca de montañas', 2, 2000, TRUE, 100, 2, FALSE, 3),
    (3,'Comercial','OtroASAPE', 2, 150000, 'Cerca de Jaimito', 2, 2000, FALSE, 2000, 4, FALSE, 3);
    
-- Insert data into 'cliente'
INSERT INTO cliente(id, nombre, apellido,localizacion, direccion, telefono, email)
    VALUES 
    ('1234567890', 'Marcos', 'Siguenza',1, '123 Main St', '1234567890','john@ucuenca.com'),
    ('2345678901', 'Jane', 'Doe',1, '456 Pine St', '2345678901','Doe@gmail.com'),
    ('3456789012', 'John', 'Smith',1, '789 Oak St', '3456789012','smith@gmail.com');

-- Insert data into 'contrato_venta'
INSERT INTO contrato_venta (asesor, fecha_inicio, fecha_fin, cliente_vendedor,tipo,comision,id_inmueble)
    VALUES 
    ('1', CURRENT_DATE,'2030-01-31', '2345678901','Alquiler',3.5, 1),
    ('2', CURRENT_DATE, '2030-01-31','3456789012', 'Venta', 2.5, 2),
    ('2', CURRENT_DATE, '2030-01-31','3456789012', 'Venta', 2.5, 3);
-- Insert data into 'contrato_compra'
INSERT INTO contrato_compra (id, fecha_inicio, fecha_fin, cliente_comprador, id_inmueble)
    VALUES (1, '2025-01-07', '2029-01-24','1234567890', '1');



