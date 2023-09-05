from django.urls import path
from .views import BookUpdateAPIView,BookCreateAPIView,BookDetailAPIView,BookListAPIView,AuthorListAPIView

urlpatterns = [
    path('all/',BookListAPIView.as_view()),
    path('detail/<int:pk>/',BookDetailAPIView.as_view()),
    path('update/<int:pk>/',BookUpdateAPIView.as_view()),
    path('create/',BookCreateAPIView.as_view()),
    path('authors/',AuthorListAPIView().as_view()),
]