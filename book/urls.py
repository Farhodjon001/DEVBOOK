from django.urls import path
from .views import BookUpdateAPIView,BookCreateAPIView,BookDetailAPIView,BookListAPIView,AuthorListAPIView,AuthorSearchAPIView,BookSearchAPIView,AuthorCreateAPIView

urlpatterns = [
    path('all/',BookListAPIView.as_view()),
    path('detail/<int:pk>/',BookDetailAPIView.as_view()),
    path('update/<int:pk>/',BookUpdateAPIView.as_view()),
    path('create/',BookCreateAPIView.as_view()),
    path('authors/',AuthorListAPIView().as_view()),
    path("author/create/",AuthorCreateAPIView.as_view()),
    path("author/update/<int:pk>",AuthorCreateAPIView.as_view()),
    path('author/search/',AuthorSearchAPIView.as_view()),
    path("book/search/",BookSearchAPIView.as_view()),

]