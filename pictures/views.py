from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.status import *
from rest_framework.decorators import *
from rest_framework.response import Response


@api_view(['GET' , 'POST'])
def HomePictures_serializer(request):
    
    if request.method == "GET":
        try:
            content = HomePictures.objects.all()
        except HomePictures.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = HomePicturesSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = HomePicturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)



@api_view(['GET' , 'POST'])
def HomeInfo_serializer(request):
    
    if request.method == "GET":
        try:
            content = HomeInfo.objects.all()
        except HomeInfo.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = HomeInfoSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = HomeInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)