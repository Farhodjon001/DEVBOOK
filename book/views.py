from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .permissions import AuthorPermission,AdminPermission
from django.db.models import Q


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
    permission_classes = (AdminPermission,AuthorPermission)

class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (AdminPermission,AuthorPermission)

class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (IsAuthenticated)

class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (IsAuthenticated)

class AuthorUpdateAPIView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (AdminPermission,AuthorPermission)

class AuthorCreateAPIView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (AdminPermission,)

class AuthorDeleteAPIView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = (AdminPermission,)

class ListBookByAuthorAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (AuthorPermission,)

    def get_queryset(self):
        user = self.request.user
        author = Author.objects.get(user=user)
        return Book.objects.filter(author=author.id)

class BookSearchAPIView(generics.ListAPIView):
    serializer_class = BookSerializers
    def get_queryset(self):
        queryset=Book.objects.all()
        query=self.request.query_params.get('query',None)

        if query:
            queryset=queryset.filter(
                Q(title__icontains=query) |
                Q(genre__icontains=query)
            )
        return queryset

class AuthorSearchAPIView(generics.ListAPIView):
    serializer_class = AuthorSerializers

    def get_queryset(self):
        queryset=Author.objects.all()
        query=self.request.query_params.get('query',None)

        if query:
            queryset=queryset.filter(
                Q(user.first_name__icontains=query) |
                Q(country__icontains=query)

            )
        return queryset























