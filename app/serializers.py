from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name")

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "book", "author")

class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ("id", "book", "year")