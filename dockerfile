# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /seek_book

# Copia los archivos de la aplicación al contenedor
COPY . /seek_book/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la app Django escuchará
EXPOSE 8000

# Establece el comando para ejecutar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
RUN python manage.py shell < scripts/populate_books.py
