
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from Base.models import Student,Prof


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # You can add custom claims to the token here if needed
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user is None:
            raise AuthenticationFailed("Incorrect username or password")

        # Assuming your user model has 'first_name' and 'last_name' fields
        refresh = self.get_token(user)

        # Accessing the primary group of the user if available
        primary_group = None
        if user.groups.exists():
            primary_group = user.groups.first().name

        data['user'] = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'group': primary_group,  # Include the primary group
            # 'token': str(refresh.access_token)
        }
        data['status'] = True
        data['Code'] = status.HTTP_200_OK
        return data
     
class SignUpStudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','univ_number','password']

class serializerStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','univ_number','profile_pic']
