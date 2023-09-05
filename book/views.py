from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .permissions import BookCreateUpdatePermission,AuthorCreateUpdatePermissions


from .models import Book,Author,Genre
from .serialilzers import BookSerializers,AuthorSerializers
from rest_framework import generics

# Create your views here.

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (IsAuthenticated,)
class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (IsAuthenticated,)

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (BookCreateUpdatePermission,AuthorCreateUpdatePermissions)

class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (BookCreateUpdatePermission,AuthorCreateUpdatePermissions)

class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (BookCreateUpdatePermission,AuthorCreateUpdatePermissions)



























