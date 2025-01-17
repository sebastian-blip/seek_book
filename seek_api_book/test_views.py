import pytest
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book
from datetime import datetime

@pytest.fixture
def api_client():
    return APIClient()


import pytest
from pymongo import MongoClient


@pytest.fixture
def create_book():
    return Book.create({
        "title": "Libro de Prueba",
        "author": "Autor de Prueba",
        "published_date": datetime(2023, 1, 1),
        "genre": "Ficción",
        "price": 19.99
    })


@pytest.mark.django_db
def test_book_list_post(api_client):
    """Test para crear un libro"""
    data = {
        "title": "Nuevo Libro",
        "author": "Nuevo Autor",
        "published_date": "2023-01-01",
        "genre": "Misterio",
        "price": 29.99
    }

    response = api_client.post('/books/', data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == "Nuevo Libro"
    assert response.data['author'] == "Nuevo Autor"


@pytest.mark.django_db
def test_book_detail_put(api_client, create_book):
    """Test para actualizar un libro"""
    book = create_book
    updated_data = {
        "title": "Libro Actualizado",
        "author": "Autor Actualizado",
        "published_date": "2023-01-01",
        "genre": "Ficción",
        "price": 25.99
    }
    response = api_client.put(f'/books/{book.inserted_id}/', updated_data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == "Libro Actualizado"
    assert float(response.data['price']) == 25.99


@pytest.mark.django_db
def test_book_detail_delete(api_client, create_book):
    """Test para eliminar un libro"""

    book = create_book

    response = api_client.delete(f'/books/{book.inserted_id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response = api_client.get(f'/books/{book.inserted_id}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
