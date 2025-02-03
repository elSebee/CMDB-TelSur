-- Eliminar tablas en orden para evitar conflictos por claves for�neas
DROP TABLE PROCT_SERV_CI CASCADE CONSTRAINTS;
DROP TABLE PROCT_DEPENDENCIAS CASCADE CONSTRAINTS;
DROP TABLE PROCT_SERVICIOS CASCADE CONSTRAINTS;
DROP TABLE PROCT_CMDB_CONF_ITEMS CASCADE CONSTRAINTS;
DROP TABLE PROCT_PERSONAS CASCADE CONSTRAINTS;
DROP TABLE PROCT_AREAS CASCADE CONSTRAINTS;

-- Tabla PROCT_AREAS
CREATE TABLE PROCT_AREAS (
    id_area NUMBER NOT NULL PRIMARY KEY,
    nombre VARCHAR2(100) NOT NULL,
    empresa VARCHAR2(100),
    desc_area VARCHAR2(800)
);

-- Tabla PROCT_PERSONAS
CREATE TABLE PROCT_PERSONAS (
    RUT VARCHAR2(15) NOT NULL PRIMARY KEY,
    nomb_persona VARCHAR2(50),
    id_area NUMBER,
    desc_gerencia VARCHAR2(100),
    desc_cargo VARCHAR2(100),
    mail VARCHAR2(50),
    celular NUMBER,
    codi_horario NUMBER,
    mtdo_aviso_default VARCHAR2(20),
    CONSTRAINT fk_persona_area FOREIGN KEY (id_area) REFERENCES PROCT_AREAS (id_area)
);

-- Tabla PROCT_CMDB_CONF_ITEMS
CREATE TABLE PROCT_CMDB_CONF_ITEMS (
    ID_CI NUMBER NOT NULL PRIMARY KEY,
    alias VARCHAR2(100) NOT NULL,
    prioridad VARCHAR2(10),
    tipo_ci VARCHAR2(30),
    estado VARCHAR2(16),
    fech_actualizacion DATE,
    dire_ip VARCHAR2(15),
    puerto NUMBER,
    desc_ci VARCHAR2(800),
    url VARCHAR2(2000),
    CONSTRAINT ck_tipo_ci CHECK (tipo_ci IN ('Servidor', 'Aplicación', 'Base de Datos', 'Web Service', 'Listener DB', 'Esquema', 'Sitio Web', 'Vista', 'Otros'))
);

-- Tabla PROCT_SERVICIOS
CREATE TABLE PROCT_SERVICIOS (
    ID_SERVICIO NUMBER NOT NULL PRIMARY KEY,
    alias VARCHAR2(30) NOT NULL,
    id_area_responsable NUMBER,
    nomb_servicio VARCHAR2(100),
    desc_servicio VARCHAR2(1000),
    CONSTRAINT fk_servicio_area FOREIGN KEY (id_area_responsable) REFERENCES PROCT_AREAS (id_area)
);

-- Tabla PROCT_DEPENDENCIAS
CREATE TABLE PROCT_DEPENDENCIAS (
    ID_RELACION NUMBER NOT NULL PRIMARY KEY,
    id_ci_origen NUMBER,
    id_ci_destino NUMBER,
    id_servicio NUMBER,
    tipo_relacion VARCHAR2(30),
    CONSTRAINT fk_dep_ci_origen FOREIGN KEY (id_ci_origen) REFERENCES PROCT_CMDB_CONF_ITEMS (ID_CI),
    CONSTRAINT fk_dep_ci_destino FOREIGN KEY (id_ci_destino) REFERENCES PROCT_CMDB_CONF_ITEMS (ID_CI),
    CONSTRAINT fk_dep_servicio FOREIGN KEY (id_servicio) REFERENCES PROCT_SERVICIOS (ID_SERVICIO)
);

-- Tabla PROCT_SERV_CI
CREATE TABLE PROCT_SERV_CI (
    ID_SERVICIO NUMBER NOT NULL,
    ID_CI NUMBER NOT NULL,
    desc_relacion VARCHAR2(300),
    PRIMARY KEY (ID_SERVICIO, ID_CI),
    CONSTRAINT fk_serv_ci_servicio 
        FOREIGN KEY (ID_SERVICIO) 
        REFERENCES PROCT_SERVICIOS (ID_SERVICIO)
        ON DELETE CASCADE,
    CONSTRAINT fk_serv_ci_ci 
        FOREIGN KEY (ID_CI) 
        REFERENCES PROCT_CMDB_CONF_ITEMS (ID_CI)
        ON DELETE CASCADE
);
