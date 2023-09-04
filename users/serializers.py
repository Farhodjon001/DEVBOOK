from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','phone','email','password','roles')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            roles = validated_data.get('roles',3)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserSignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # def validate(self, attrs):
    #     email = attrs.get('email')
    #     password = attrs.get('password')
    #
    #     if email and password:
    #         user = authenticate(request=self.context.get('request'), email=email, password=password)
    #
    #         if not user:
    #             raise serializers.ValidationError('Unable to log in with provided credentials.')
    #
    #         attrs['user'] = user
    #         return attrs
    #     else:
    #         raise serializers.ValidationError('Must include "email" and "password".')
