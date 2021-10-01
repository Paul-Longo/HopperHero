from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class UserView(APIView):

    def post(self, request, id):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        users = User.objects.get(pk=id)
        serializer = RegistrationSerializer(users)
        return Response(serializer.data)


class AllUsersView(APIView):

   def get(self, request):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data)