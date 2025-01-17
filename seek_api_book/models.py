from django.conf import settings
from bson.objectid import ObjectId

class Book:
    collection = settings.MONGO_DB["books"]

    @staticmethod
    def create(data):
        """Crea un libro en la colección."""
        return Book.collection.insert_one(data)

    @staticmethod
    def get_all():
        """Obtiene todos los libros."""
        return list(Book.collection.find())

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


