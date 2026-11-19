Preguntas de reflexión – RELEASE y DEPLOY
Práctica 5 – Fase RELEASE
1. ¿Por qué es importante identificar cada versión del software?

Porque permite reconocer los cambios realizados, mantener un historial y recuperar versiones anteriores si se presenta algún problema.

2. ¿Qué diferencia existe entre un commit, un tag y un release?
- Commit: guarda los cambios realizados en el código.
- Tag: identifica una versión específica del proyecto.
- Release: es la versión preparada y publicada para su distribución en GitHub.
3. ¿Por qué se ejecutan las pruebas antes de publicar una versión?

Para comprobar que el sistema funciona correctamente y evitar publicar una versión que contenga errores.

4. ¿Qué ocurre si las pruebas fallan durante el proceso de liberación?

El proceso de liberación se detiene y no se publica la versión hasta corregir los errores y ejecutar nuevamente las pruebas.

5. ¿Qué ventajas ofrece generar automáticamente el paquete de distribución?

Permite ahorrar tiempo, evitar errores al seleccionar archivos manualmente y generar un paquete organizado con los archivos necesarios del sistema.

6. ¿Por qué es importante conservar un historial de versiones?

Porque permite conocer los cambios realizados, identificar versiones anteriores y recuperar una versión estable cuando una actualización presenta problemas.

7. ¿Qué diferencia existe entre liberar una versión y desplegarla?

Liberar significa preparar y publicar una versión del software para su distribución, mientras que desplegar consiste en instalarla y ejecutarla en un entorno donde será utilizada.
Práctica 7 – Fase DEPLOY
1. ¿Cuál es la diferencia entre liberar una versión y desplegarla?

Liberar consiste en preparar y publicar una versión del sistema en GitHub, mientras que desplegar significa instalarla y ejecutarla en un entorno de destino para comprobar que funciona.

2. ¿Por qué se utiliza el paquete generado en la fase RELEASE?

Porque contiene los archivos necesarios para ejecutar el sistema y permite instalar una versión específica sin tener que copiar manualmente todos los archivos del proyecto.

3. ¿Qué función tiene el entorno de destino?

Es la computadora o máquina virtual donde se instala y ejecuta el sistema para que pueda utilizarse y comprobarse su funcionamiento.

4. ¿Qué información se necesita para establecer una conexión SSH?

Se necesita la dirección IP o nombre del servidor, el usuario, la llave privada SSH y el puerto de conexión.

5. ¿Por qué es importante utilizar secretos de GitHub?

Porque permiten almacenar información confidencial, como las llaves privadas y los datos de conexión, evitando que se expongan directamente en el código.

6. ¿Qué ventajas ofrece automatizar el despliegue?

Permite ahorrar tiempo, reducir errores humanos, transferir archivos automáticamente y facilitar la instalación de nuevas versiones del sistema.

7. ¿Qué problemas pueden presentarse cuando el entorno de destino no cumple los requisitos?

El sistema puede no iniciar, presentar errores de ejecución o no funcionar correctamente debido a la falta de herramientas, dependencias o versiones necesarias.

8. ¿Por qué es necesario contar con un procedimiento de recuperación?

Porque permite regresar a una versión anterior que funcionaba correctamente cuando una actualización presenta errores, evitando perder la funcionalidad del sistema.

Relación con lo que realizamos en la práctica
Estas son las evidencias que ya conseguiste durante el trabajo:
Actividad	Resultado
Crear versión v1.0.0	Realizado
Ejecutar 5 pruebas automatizadas	Realizado
Crear versión v1.1.0	Realizado
Agregar tiene_existencias()	Realizado
Simular un error en v1.1.0	Realizado
Recuperar y comprobar v1.0.0	Realizado
Crear etiquetas Git	Realizado
Subir etiquetas a GitHub	Realizado
