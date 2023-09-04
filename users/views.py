from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSignInSerializer

# Create your views here.
class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSignInAPIView(APIView):
    def post(self, request):
        serializer = UserSignInSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            return Response({
                'access_token': str(refresh.access_token),
            })

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
