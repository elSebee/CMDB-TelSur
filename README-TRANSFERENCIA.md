## 1.- Crear una nueva cuenta GitHub corporativa y crear un nuevo repositorio
Ejemplo:
- Nombre: Proyecto-CMDB
- URL: https://github.com/OSS/Proyecto-CMDB.git
- No inicializar con README, .gitignore ni licencias.

## 2.- En el servidor 10.1.202.65 conectar el nuevo repositorio
El proyecto CMDB-app en el servidor ahora no está apuntando ningún repositorio, por lo que:
- Desde el home~ del servidor: cd Scripts/CMDB-app/
- git remote add origin https://github.com/OSS/Proyecto-CMDB.git
- git remote -v
  - Si aparece la nueva url entonces el proyecto está conectado al nuevo repositorio.

## 3.- Subir el código al nuevo repositorio
- git branch -M main
- git push -u origin main

Siguiendo estos pasos el proyecto dentro del servidor ahora apunta a un repositorio corporativo, y es en este repositorio donde se pueden subir los nuevos avances a la CMDB-app. Así también se puede hacer un repositorio de control de versiones de los Scripts python de monitoreo que no se alcanzó a revisar.
