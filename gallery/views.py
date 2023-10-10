from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.status import *


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Works_Images_serializer(request):
    
    if request.method == "GET":
        try:
            content = Works_Images.objects.all()
        except Works_Images.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = Works_ImagesSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Works_ImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def work_image_update(request):
    if request.GET.get('id'):
        try:
        
            id = request.GET.get('id')
            work_image = Works_Images.objects.get(id = id)

        except Works_Images.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = Works_ImagesSerializer(instance=work_image)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = Works_ImagesSerializer(instance=work_image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            work_image.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)    


@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Circular_Images_Serializer(request):
    
    if request.method == "GET":
        try:
            content = Circular_Images.objects.all()
        except Circular_Images.DoesNotExist:
            return Response({
                'error':'the content does not exist'
            } ,status=HTTP_404_NOT_FOUND)
        serializer = Circular_ImagesSerializer(content , many = True)

        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Circular_ImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated , IsAdminUser])
def Circular_Images_update(request):
    if request.GET.get('id'):    
        try:
        
            id = request.GET.get('id')
            Circular_Image = Circular_Images.objects.get(id = id)

        except Works_Images.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = Works_ImagesSerializer(instance=Circular_Image)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = Works_ImagesSerializer(instance=Circular_Image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            Circular_Image.delete()
            return Response(status=HTTP_204_NO_CONTENT)
    else:
        raise ParseError('you should send an id with your query parametrs' , code=HTTP_400_BAD_REQUEST)