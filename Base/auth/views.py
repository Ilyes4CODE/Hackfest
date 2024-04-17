from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .serializers import SignUpStudentSerializer,serializerStudent
from django.contrib.auth.models import User
from Base.models import Student
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view,permission_classes
# Create your views here.


class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed as e:
            return Response({
                'status': False,
                'message': "Incorrect username or password"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def Signup(request):
    data = request.data
    serializer = SignUpStudentSerializer(data=data)
    if serializer.is_valid():
        if User.objects.filter(username=data['univ_number']).exists():
            return Response({'error':'user existed'},status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create(
                username = data['univ_number'],
                password = make_password(data['password'])
            )
            Student.objects.create(
                user = user,
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                univ_number = data['univ_number']
            )
            return Response({'info':'account created'},status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Auth_user(request):
    print(request.user)
    student = Student.objects.get(user=request.user)
    serializer = serializerStudent(student)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

    
