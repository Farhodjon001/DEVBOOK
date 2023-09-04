from django.urls import path
from .views import UserSignInAPIView

urlpatterns=[
    path('signin/', UserSignInAPIView.as_view(), name='user-signin'),
]