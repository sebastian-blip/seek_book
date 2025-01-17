from django.urls import path
from .views import BookListView, BookDetailView, BookAveragePriceView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<str:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/average/<int:year>/', BookAveragePriceView.as_view(), name='book-average-price'),
]
