Proyecto Book - Django

Este es un proyecto de Django para gestionar una librería en línea. La aplicación permite administrar libros, autores y categorías, y proporciona una API para interactuar con los datos. Está diseñada para ser desplegada en Docker y AWS Fargate.
Resumen del Funcionamiento

La aplicación Book está diseñada para gestionar libros, autores y categorías. Los usuarios pueden agregar, actualizar, eliminar y listar libros, así como asociar libros con autores y categorías. La aplicación también permite la búsqueda de libros por título, autor o categoría.
Componentes principales:

    Modelos:
        Libro: Contiene información sobre el libro, como título, autor, categoría, y fecha de publicación.
        Autor: Contiene información sobre los autores de los libros.
        Categoría: Permite clasificar los libros en diferentes categorías.

    API:
        La aplicación expone una API RESTful que permite interactuar con los datos de los libros, autores y categorías.

    Base de Datos:
        Utiliza MongoDB como base de datos para almacenar la información de los libros, autores y categorías.

Flujo de Trabajo:

    El usuario puede interactuar con la API para agregar, actualizar o eliminar libros, autores y categorías.
    La base de datos se mantiene sincronizada con las operaciones realizadas a través de la API.
    La aplicación está diseñada para ser escalable y se puede desplegar en AWS Fargate para manejar el tráfico de manera eficiente.

Requisitos

    Docker: Para crear y ejecutar contenedores de la aplicación.
    AWS Fargate: Para desplegar la aplicación en un entorno gestionado sin necesidad de administrar servidores.
    MongoDB Atlas: Para almacenar la base de datos de la aplicación.

Instalación y Despliegue
1. Clonar el repositorio

git clone https://github.com/sebastian-blip/seek_book.git
cd book-django

2. Configurar la base de datos MongoDB

Asegúrate de tener una cuenta en MongoDB Atlas y crea una base de datos llamada library. Obtén las credenciales de conexión para MongoDB.
3. Recuerda agregar la url de mongo en setting, ya sea directamente o agregar un archivo .env

4. Construir y ejecutar con Docker

Asegúrate de tener Docker instalado en tu máquina. Luego, construye la imagen de Docker y ejecuta el contenedor:

docker build -t book-django .

Nota: en este paso ya podria ejecutar el servicio django localmente con docker run -p 8000:8000 book-django

5. Desplegar en AWS Fargate
5.1 Crear un repositorio en Amazon ECR

    Inicia sesión en la consola de AWS y ve a Amazon ECR.
    Crea un repositorio llamado book-django.
    Sigue las instrucciones para autenticarte en el repositorio y subir tu imagen de Docker.

5.2 Configurar el servicio en AWS Fargate

    En la consola de ECS, crea un Cluster de tipo Fargate.
    Define una tarea de Fargate que utilice la imagen de Docker almacenada en ECR.
    Configura el servicio para que se ejecute automáticamente y asegúrate de que esté en la misma VPC que tu base de datos de MongoDB Atlas.
    Configura las variables de entorno necesarias (como DATABASE_URL, SECRET_KEY, etc.) en el contenedor.

5.3 Configurar el balanceador de carga (opcional)

Si necesitas un balanceador de carga, puedes configurarlo en Elastic Load Balancing (ELB) para distribuir el tráfico entre varias instancias de tu servicio Fargate.
