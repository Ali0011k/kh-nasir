from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.status import *
from rest_framework.decorators import *
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
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

@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def homepicture_update(request):
    if request.GET.get('id'):
        try:
        
            id = request.GET.get('id')
            homePictures = HomePictures.objects.get(id = id)
            
        except HomePictures.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    
        if request.method == 'GET':
            serializer = HomePicturesSerializer(instance=homePictures)
            return Response(serializer.data)
    
        elif request.method == 'PUT':
            serializer = HomePicturesSerializer(instance=homePictures, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
        elif request.method == 'DELETE':
            homePictures.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
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
        
@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def home_info_update(request):
    if request.GET.get('id'):
        try:
        
            id = request.GET.get('id')
            homeinfo = HomeInfo.objects.get(id = id)

        except HomeInfo.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = HomeInfoSerializer(instance=homeinfo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = HomeInfoSerializer(instance=homeinfo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            homeinfo.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)