from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Wod
from .serializers import WodSerializer
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_wod(request):
    wod = Wod.objects.all()
    serializer = WodSerializer(wod, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_wod(request):
    if request.method == 'POST':
        serializer = WodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        wod = Wod.objects.filter(id=id)
        serializer = WodSerializer(wod, many=True)
        return Response(serializer.data)
