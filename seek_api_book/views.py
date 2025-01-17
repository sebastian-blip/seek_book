from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.get_all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            Book.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.get_by_id(pk)
        if not book:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            updated = Book.update(pk, serializer.validated_data)
            if updated.modified_count > 0:
                return Response(serializer.data)
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        deleted = Book.delete(pk)
        if deleted.deleted_count > 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


class BookAveragePriceView(APIView):
    def get(self, request, year):
        pipeline = [
            {"$match": {"published_date": {"$regex": f"^{year}"}}},
            {"$group": {"_id": None, "average_price": {"$avg": "$price"}}}
        ]
        result = list(Book.collection.aggregate(pipeline))
        if result:
            return Response({"average_price": result[0]["average_price"]})
        return Response({"average_price": 0})


