# Test for Trafilea

Prueba para vacante de desarrollador Python/Django

## Instalación

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

* Crear la carpeta "migrations" dentro de la carpeta "security". Y dentro de la carpeta "Migrations" crear un archivo llamado "\_\_init\_\_.py"

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/configuracion.png)

**Nota**:_Lo anterior es por si mas de un programador trabaja en el mismo archivo, no haya conflicto con migraciones o configuraciones_


## Instrucciones de Uso

### Importar/Exportar información:

Se incluyo en el administrador de la aplicacion una forma simple de importar datos. Ejemplo:

En la seccion de Usuarios apareceran dos botones llamados "Importar" y "Exportar":

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/export_inicio.png)

Dar click en Importar y seleccionar archivo con la informacion:

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/export_select.png)

El archivo debera tener las siguientes columnas y el la fecha en texto con el siguiente formato:

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/testa_data.png)

Una vez seleccionado el archivo se mostrara un preview de los datos que se importaran:

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/export_preview.png)

Al dar click al boton "Confirmar Importacion" la informacion estara correctamente cargada:

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/export_fin.png)


### Documentación:

Se incluyo una paquina que describe los endpoint que pueden ser utilizados. Dicha pagina puede ser consultada en la siguiente URL

```
$ /docs/
```

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/documentacion_api.png)

### End Point Login

Para poder hacer uso del endpoint "/users/" se debera de firmar en la aplicacion a travez de una petición POST de la siguiente forma:

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/test_login.png)

Lo anterior devolvera un token que debera ser enviado en los Hearders de las peticiones que se hagan.

### End Point Users

Para consultar los usuarios con el endpoint "/users/", se debera de contar ya con un token valido (estar firmado en la aplicacion) y hacer la peticion GET de la siguiente forma:

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/test_consulta.png)

En caso de no tener un token valido devolvera el siguiente mensaje:

![alt text](https://github.com/carloxdev/trafileatest/blob/master/images/fail_request.png)
