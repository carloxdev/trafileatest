# Test for Trafilea

Prueba para vacante de desarrollador Python/Django

## Instalacion

Este manual considera que tienes ya instalado el interprete de Python y gesto de base de datos PostgreSQL con las variables de entorno correctamente configuradas.

### Base de datos:

Se debera de crear una BD con el nombre "testdb" (sin las comillas).


### Librerias:

La instalacion de librerias puede ser realizada con el siguiente comando:

```
$ pip install -r requirements.txt
```

### Configuración de la aplicación:

* Renombrar el archivo "settings.py.bk" ubicado en la carpeta TestTrafilea a "settings.py". Posteriormente configurar el usuario y password de tu gestor de BD de PostgreSQL que utilizaras para la aplicación.

* Crear la carpeta "migrations" dentro de la carpeta "security". Y dentro de la carpeta "Migrations" crear un archivo llamado "__init__.py"

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/configuracion.png)

**Nota**:_Lo anterior es por si mas de un programador trabaja en el mismo archivo, no haya conflicto con migraciones o configuraciones"
