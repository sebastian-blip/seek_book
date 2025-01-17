from datetime import date, datetime
from django.conf import settings



books_data = [
    {"title": "El Gran Gatsby", "author": "F. Scott Fitzgerald", "published_date": datetime(1925, 4, 10),
     "genre": "Ficción", "price": 10.99},
    {"title": "1984", "author": "George Orwell", "published_date": datetime(1949, 6, 8), "genre": "Distopía",
     "price": 8.99},
    {"title": "Cien Años de Soledad", "author": "Gabriel García Márquez", "published_date": datetime(1967, 6, 5),
     "genre": "Realismo Mágico", "price": 12.50},
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes", "published_date": datetime(1605, 1, 1),
     "genre": "Aventura", "price": 15.00},
    {"title": "El Principito", "author": "Antoine de Saint-Exupéry", "published_date": datetime(1943, 4, 6),
     "genre": "Fábula", "price": 7.99},
]


collection = settings.MONGO_DB["books"]
collection.insert_many(books_data)