Script que permite comentar de forma automatica.

Obtener seguidores de ig.

Antes de ejecutar el script deberas obtener el listado de seguidos o seguidores. Esto se puede obtener con los siguientes pasos (Android):
1. Tocar las lineas de opciones en tu perfil de instagarm
2. Tu actividad
3. Descargar tu informacion
4. Descargar o transferir informacion
5. Elegi la cuenta si tenes varias
6. Parte de tu informacion
7. Seguidores y seguidos
8. Descargar en dispositivo
9. Cambiar formato a json
10. Crear archivo
11. Esperar a que instagram te descargue la informacion y luego extraer el archivo followers_1.json (En mi caso se llamaba asi, si no se llama asi ponerle ese nombre o modificar el nombre en
    la funcion "extractor_username_from_json")
13. Crear la carpeta people_to_mencion en la raiz, insertar el archivo followers_1.json y ejecutar la funcion "extractor_username_from_json" ubicada en el script "user_extractor" para generar un txt con todos tus seguidores 

Pasos para ejecutar:
1. Ejectuar el archivo chromedriver.exe para automatizar  
2. Abrir el repositorio con pycharm u otro ide/editor de texto
4. Instalar las librerias de selenium y python-dotenv
5. Dentro de la carpeta Script crear un archivo llamado credentials.env
6. Dentro del archivo credentials.env escribir:
   USERNAME=<tu usuario>
   PASSWORD=<tu contraseña>
7. En la variable "target_post" del script automatic_comments, pegar el link de la publicacion a spamear

Ignorar el mal ingles con el nombre de variables, funciones y scripts
