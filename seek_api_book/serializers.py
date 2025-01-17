from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    genre = serializers.CharField(max_length=50)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
