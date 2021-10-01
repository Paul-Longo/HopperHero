from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Likes, Wod
from .serializers import WodSerializer, LikesSerializer


# Create your views here.

class AllWods(APIView):
    def get(self, request):
        wod = Wod.objects.all()
        serializer = WodSerializer(wod, many=True)
        return Response(serializer.data)


class WodsView(APIView):
    def post(self, request):
        serializer = WodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wod=request.wod)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        wod = Wod.objects.filter(id=id)
        serializer = WodSerializer(wod, many=True)
        return Response(serializer.data)


class LikesView(APIView):
    def post(self, request):
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        likes = Likes.objects.get(pk=id)
        likes.delete()
        return Response(status=status.HTTP_200_OK)
        

class UserLikesView(APIView):
    def get(self, request, id):
        likes = Likes.objects.filter(user=id)
        serializer = LikesSerializer(likes, many=True)
        return Response(serializer.data)

