from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
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