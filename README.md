

# 1. Descripción
Esta aplicación está diseñada e implementada para el *área de Explotación de Sistemas | Operaciones OSS* de la empresa **TelSur**. Permite gestionar componentes de infraestructura, sus dependencias y servicios asociados, estos almacenados en su **_CMDB_** oracle. Los usuarios pueden realizar operaciones _CRUD_ sobre los registros, facilitando el control de los datos de la infraestructura de sus servicios.

# 2. Características
La aplicación, al ser CRUD, permite la gestión de información dentro de la CMDB:
1. **__Leer__** la información de las tablas dentro de la CMDB, como lo son los Avisos y Logs de los monitoreos de los servicios así como toda la información de infraestructura.
2. **__Editar__** la información de la infraestructura.
3. **__Eliminar__** (o desactivar en el caso de los CI's) los elementos de infraestructura almacenados.
4. **__Agregar__** nuevos elementos a la base de datos. 

# 3. Instalación
1.- Clonar el repositorio
- git clone https://github.com/elSebee/CMDB-TelSur.git

2.- Acceder al directorio del proyecto

3.- Crear un entorno virtual
- python -m venv venv

4.- Activar el entorno
- Windows
    - venv\Scripts\activate
- Linux
    - source venv/bin/activate

5.- Instalar las [dependencias](./requirements.txt)
- pip install -r requirements.txt

6.- Crear archivo .env
```
ORACLE_USER=pproc
ORACLE_PASSWORD=
ORACLE_HOST=172.16.68.91 (desarrollo)
ORACLE_PORT=1533 (desarrollo)
ORACLE_SERVICE_NAME=desacnt (desarrollo)
ORACLE_LIB_DIR=/usr/lib/oracle/21/client64/lib
```

7.- Ejecutar la aplicación
- python run.py


# 4. Uso
Para acceder a la aplicación:
- Abre un navegador (recomendado: microsoft edge) y ve a http://localhost:7001/

# 5. Tecnologías Utilizadas
- **Framework:** Flask Python
- **Frontend:** Jinja2 | HTML, JavaScript, CSS
- **Backend:** orm SQLAlchemy, Base de Datos Oracle 

![Imágen de las tecnologías](app/views/static/images/tecnologias.png)

# 6. Estructura del Proyecto
```
CMDB-APP/
│
├── app/                # Carpeta principal con la lógica de la app
│   ├── __init__.py     # Inicialización de la app Flask
│   ├── routes/         # Definición de las rutas (endpoints)
│   ├── controller/     # Controladores (lógica del negocio)
│   ├── models/         # Modelos de la base de datos
│   ├── database/       # Conexión a la base de datos + .sql
│   └── views/          # Archivos de Frontend
│       ├── static/     # Archivos estáticos (CSS, JS, imágenes)
│       │   ├── CSS/
│       │   ├── images/
│       │   └── js/
│       └── templates/  # Plantillas HTML
├── docs/               # Documentación del proyecto
├── requirements.txt    # Dependencias del proyecto
├── config.py           # Configuración de la aplicación y de la base de datos
├── README.md           # Este archivo
├── LICENSE             # Licencia del proyecto
└── run.py              # Archivo principal para ejecutar la app
```

# 7. Licencia
Este proyecto está bajo la [MIT License](./LICENSE) - consulta el archivo LICENSE para más detalles.

