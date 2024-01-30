
CREATE TABLE ciudad (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    provincia VARCHAR(50)
);

CREATE TABLE agente (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    ciudad INT REFERENCES ciudad(id),
    direccion VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(50),
    titulo VARCHAR(50)
);

CREATE TABLE inmueble (
    id INT PRIMARY KEY,
    tipo VARCHAR(50),
    direccion VARCHAR(100),
    ciudad VARCHAR(50),
    precio DECIMAL(10,2),
    estado VARCHAR(50),
    descripcion TEXT
);

CREATE TABLE agente_asesora_inmueble (
    id_agente INT REFERENCES agente(id),
    id_inmueble INT REFERENCES inmueble(id),
    PRIMARY KEY (id_agente, id_inmueble)
);

CREATE TABLE cliente (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    direccion VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE cliente_propietario_inmueble (
    id_cliente INT REFERENCES cliente(id),
    id_inmueble INT REFERENCES inmueble(id),
    PRIMARY KEY (id_cliente, id_inmueble)
);

CREATE TABLE cliente_comprador (
    id_cliente INT INT REFERENCES cliente(id),
    id_contrato INT INT REFERENCES contrato(id),
    PRIMARY KEY (id_cliente, id_contrato)
);

CREATE TABLE contrato (
    id INT PRIMARY KEY,
    fecha_inicio DATE,
    fecha_fin DATE,
    tipo VARCHAR(50),
    comision DECIMAL(10,2),
    id_inmueble INT
);


CREATE TABLE estado (
    id INT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE inmueble_estado (
    id_inmueble INT REFERENCES inmueble(id),
    id_estado INT REFERENCES estado(id),
    PRIMARY KEY (id_inmueble, id_estado)
);

CREATE TABLE ciudad_inmueble (
    id_ciudad INT REFERENCES ciudad(id),
    id_inmueble INT REFERENCES inmueble(id),
    PRIMARY KEY (id_ciudad, id_inmueble)
);

-- Insertar datos en la tabla 'agente'
INSERT INTO agente (id, nombre, apellido, edad, direccion, telefono, email, titulo)
VALUES (1, 'Jeremy', 'Apellido', 35, 'Direccion Jeremy', '1234567890', 'jeremy@email.com', 'Agente');

-- Insertar datos en la tabla 'cliente' para Marco (propietario)
INSERT INTO cliente (id, nombre, apellido, edad, direccion, telefono, email)
VALUES (2, 'Marco', 'Apellido', 45, 'Direccion Marco', '2345678901', 'marco@email.com');

-- Insertar datos en la tabla 'cliente' para Mateo (comprador)
INSERT INTO cliente (id, nombre, apellido, edad, direccion, telefono, email)
VALUES (3, 'Mateo', 'Apellido', 30, 'Direccion Mateo', '3456789012', 'mateo@email.com');

-- Insertar datos en la tabla 'ciudad'
INSERT INTO ciudad (id, nombre, provincia)
VALUES (1, 'Cuenca', 'Provincia');

-- Insertar datos en la tabla 'estado' para 'Disponible'
INSERT INTO estado (id, nombre)
VALUES (1, 'Disponible');

-- Insertar datos en la tabla 'estado' para 'Vendido'
INSERT INTO estado (id, nombre)
VALUES (2, 'Vendido');

-- Insertar datos en la tabla 'inmueble'
INSERT INTO inmueble (id, tipo, direccion, ciudad, precio, estado, descripcion)
VALUES (1, 'Casa con piscina', 'Direccion Casa', 1, 200000.00, 1, 'Casa con piscina en Cuenca');

-- Insertar datos en la tabla 'cliente_propietario_inmueble'
INSERT INTO cliente_propietario_inmueble (id_cliente, id_inmueble)
VALUES (2, 1);

-- Insertar datos en la tabla 'agente_asesora_inmueble'
INSERT INTO agente_asesora_inmueble (id_agente, id_inmueble)
VALUES (1, 1);

-- Insertar datos en la tabla 'contrato'
INSERT INTO contrato (id, fecha_inicio, fecha_fin, tipo, comision, id_inmueble)
VALUES (1, '2022-01-01', '2022-12-31', 'Venta', 20000.00, 1);

-- Insertar datos en la tabla 'cliente_comprador'
INSERT INTO cliente_comprador (id_cliente, id_contrato)
VALUES (3, 1);

-- Actualizar el estado del inmueble a 'Vendido'
UPDATE inmueble
SET estado = 2
WHERE id = 1;

-- Insertar datos en la tabla 'inmueble_estado'
INSERT INTO inmueble_estado (id_inmueble, id_estado)
VALUES (1, 2);

-- Insertar datos en la tabla 'ciudad_inmueble'
INSERT INTO ciudad_inmueble (id_ciudad, id_inmueble)
VALUES (1, 1);