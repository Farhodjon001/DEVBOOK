from django.urls import path
from .views import UserSignInAPIView,SignUpUserAPIView

urlpatterns=[
    path('signin/', UserSignInAPIView.as_view(), name='user-signin'),
    path('signup/',SignUpUserAPIView.as_view())
]