# Envío de Correos con Archivos Adjuntos de Entrenamiento Personalizado
Este proyecto de Python permite enviar correos electrónicos personalizados a los clientes de un servicio de entrenamiento, adjuntando un archivo PDF que contiene su plan de ejercicios. Dependiendo del número de días de entrenamiento, se adjunta un PDF específico en el correo enviado al cliente.

## Descripción del Código
El script principal utiliza la librería smtplib para enviar correos electrónicos mediante el protocolo SMTP y el módulo email.mime para construir el mensaje en formato MIME, permitiendo adjuntar archivos y personalizar el cuerpo del correo con HTML.

## Funciones y Características Principales
### 1. enviar_correo_con_imagen
Esta función principal se encarga de:
- Seleccionar el archivo PDF adecuado según el número de días de entrenamiento del cliente.
- Crear el correo electrónico en formato MIME, con un cuerpo en HTML que incluye un mensaje personalizado para el cliente.
- Adjuntar el archivo PDF al correo.
- Configurar y conectar al servidor SMTP de Gmail para enviar el correo electrónico.
### 2. Asignación del Archivo PDF
El archivo PDF que contiene la tabla de ejercicios se selecciona de acuerdo al número de días de entrenamiento que el usuario especifica. Actualmente, el código soporta archivos para tres, cuatro y cinco días de entrenamiento (entreno3dias.pdf, entreno4dias.pdf, entreno5dias.pdf), y selecciona el archivo correcto en función del valor de la variable numEntrenamientos.

### 3. Creación del Cuerpo HTML del Correo
El cuerpo del correo incluye un mensaje de bienvenida y motivación, además de una explicación del plan de entrenamiento. Este cuerpo se estructura en HTML y se adjunta como parte del mensaje MIME.

### 4. Adjuntar el Archivo PDF
El archivo PDF se adjunta al mensaje utilizando MIMEApplication, configurado para manejar documentos en formato PDF. Esto asegura que el archivo adjunto sea enviado correctamente y esté accesible para el destinatario.

### 5. Enviar el Correo a través de SMTP
La función configura la conexión al servidor SMTP de Gmail y utiliza el puerto 587. Después de autenticarse con las credenciales del remitente, se envía el correo electrónico y luego se cierra la conexión de forma segura.

## Uso del Script
Para usar el script, asegúrate de que tienes Python instalado y sigue estos pasos:

### 1. Configura tus credenciales: 
Por seguridad, es recomendable almacenar la contraseña en una variable de entorno en lugar de incluirla directamente en el código.
### 2. Ejecuta el script:
Puedes ejecutar el script desde la línea de comandos. El script te pedirá el correo electrónico del destinatario y el número de días de entrenamiento para seleccionar el archivo PDF adecuado.

> python3 script.py

## Ejemplo de Uso

> Introduce el número de días que va a entrenar -> 3
> Introduce el correo electrónico -> cliente@example.com

## Dependencias
Este código utiliza solo módulos estándar de Python:

- smtplib
- email.mime para construir y enviar el correo electrónico en formato MIME.
- OS para manejar rutas de archivos.

## Notas de Seguridad
Para proteger la contraseña del correo electrónico, recomendamos almacenarla en una variable de entorno en lugar de incluirla directamente en el código. Puedes hacerlo utilizando la biblioteca os de Python:

> import os
> password = os.getenv("EMAIL_PASSWORD")

Configura la variable de entorno en tu sistema o en un archivo .env en el entorno de tu proyecto.

## Mejoras Futuras
- Agregar una interfaz gráfica para facilitar la introducción de datos.
- Incluir soporte para otros proveedores de correo electrónico aparte de Gmail.
- Añadir manejo de errores adicionales para mejorar la robustez del código.

## Contribución
*** Si deseas contribuir a este proyecto, puedes hacer un fork del repositorio y enviar un Pull Request con tus propuestas de mejora o corrección. ***
