from django.conf import settings
from bson.objectid import ObjectId
import datetime

class Book:
    collection = settings.MONGO_DB["books"]

    @staticmethod
    def create(data):
        """Crea un libro en la colección y convierte `published_date` a datetime si es necesario."""

        # Convertir el `published_date` de date a datetime
        published_date = data.get('published_date')
        if isinstance(published_date, datetime.date):
            data['published_date'] = datetime.datetime.combine(published_date, datetime.time())

        return Book.collection.insert_one(data)

    @staticmethod
    def get_all():
        """Obtiene todos los libros."""
        books = list(Book.collection.find())
        for book in books:
            # Convertir el _id de MongoDB a id
            book['id'] = str(book['_id'])
            del book['_id']  # Eliminar el campo _id si ya no lo necesitas
        return books

    @staticmethod
    def get_by_id(book_id):
        """Obtiene un libro por su ID."""
        return Book.collection.find_one({"_id": ObjectId(book_id)})

    @staticmethod
    def update(book_id, data):
        """Actualiza un libro por su ID."""
        return Book.collection.update_one({"_id": ObjectId(book_id)}, {"$set": data})

    @staticmethod
    def delete(book_id):
        """Elimina un libro por su ID."""
        return Book.collection.delete_one({"_id": ObjectId(book_id)})


