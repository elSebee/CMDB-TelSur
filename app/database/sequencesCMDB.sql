DECLARE
    v_exists NUMBER;
BEGIN
    -- Verifica si la sequence existe
    SELECT COUNT(*)
    INTO v_exists
    FROM USER_SEQUENCES
    WHERE SEQUENCE_NAME = 'PROCQ_IDSERVICIOS';

    -- Si existe, elimínala
    IF v_exists > 0 THEN
        EXECUTE IMMEDIATE 'DROP SEQUENCE PROCQ_IDSERVICIOS';
    END IF;

    -- Crea la sequence
    EXECUTE IMMEDIATE '
        CREATE SEQUENCE PROCQ_IDSERVICIOS
        MINVALUE 0
        MAXVALUE 9999999999999999999999999
        START WITH 1
        INCREMENT BY 1
        CACHE 20';
END;
/

DECLARE
    v_exists NUMBER;
BEGIN
    -- Verifica si la sequence existe
    SELECT COUNT(*)
    INTO v_exists
    FROM USER_SEQUENCES
    WHERE SEQUENCE_NAME = 'PROCQ_IDDEPENDENCIAS';

    -- Si existe, elimínala
    IF v_exists > 0 THEN
        EXECUTE IMMEDIATE 'DROP SEQUENCE PROCQ_IDDEPENDENCIAS';
    END IF;

    -- Crea la sequence
    EXECUTE IMMEDIATE '
        CREATE SEQUENCE PROCQ_IDDEPENDENCIAS
        MINVALUE 0
        MAXVALUE 9999999999999999999999999
        START WITH 1
        INCREMENT BY 1
        CACHE 20';
END;
/

DECLARE
    v_exists NUMBER;
BEGIN
    -- Verifica si la sequence existe
    SELECT COUNT(*)
    INTO v_exists
    FROM USER_SEQUENCES
    WHERE SEQUENCE_NAME = 'PROCQ_IDCMDB_CONF_ITEMS';

    -- Si existe, elimínala
    IF v_exists > 0 THEN
        EXECUTE IMMEDIATE 'DROP SEQUENCE PROCQ_IDCMDB_CONF_ITEMS';
    END IF;

    -- Crea la sequence
    EXECUTE IMMEDIATE '
        CREATE SEQUENCE PROCQ_IDCMDB_CONF_ITEMS
        MINVALUE 0
        MAXVALUE 9999999999999999999999999
        START WITH 1
        INCREMENT BY 1
        CACHE 20';
END;
/

DECLARE
    v_exists NUMBER;
BEGIN
    -- Verifica si la sequence existe
    SELECT COUNT(*)
    INTO v_exists
    FROM USER_SEQUENCES
    WHERE SEQUENCE_NAME = 'PROCQ_IDAREAS';

    -- Si existe, elimínala
    IF v_exists > 0 THEN
        EXECUTE IMMEDIATE 'DROP SEQUENCE PROCQ_IDAREAS';
    END IF;

    -- Crea la sequence
    EXECUTE IMMEDIATE '
        CREATE SEQUENCE PROCQ_IDAREAS
        MINVALUE 0
        MAXVALUE 9999999999999999999999999
        START WITH 1
        INCREMENT BY 1
        CACHE 20';
END;
/

DECLARE
    v_exists NUMBER;
BEGIN
    -- Verifica si la sequence existe
    SELECT COUNT(*)
    INTO v_exists
    FROM USER_SEQUENCES
    WHERE SEQUENCE_NAME = 'PROCQ_IDCONSULTA';

    -- Si existe, elimínala
    IF v_exists > 0 THEN
        EXECUTE IMMEDIATE 'DROP SEQUENCE PROCQ_IDCONSULTA';
    END IF;

    -- Crea la sequence
    EXECUTE IMMEDIATE '
        CREATE SEQUENCE PROCQ_IDCONSULTA
        MINVALUE 0
        MAXVALUE 9999999999999999999999999
        START WITH 13
        INCREMENT BY 1
        CACHE 20';
END;
/
