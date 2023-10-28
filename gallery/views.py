from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.status import *
from rest_framework import generics


class WorkImageApiView(generics.ListCreateAPIView):
    queryset = Works_Images.objects.all()
    serializer_class = Works_ImagesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class WorkImageUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Works_Images.objects.all()
    serializer_class = Works_ImagesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    
    
class CircularImageApiView(generics.ListCreateAPIView):
    queryset = Circular_Images.objects.all() 
    serializer_class = Circular_ImagesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CircularImageUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circular_Images.objects.all()
    serializer_class = Circular_ImagesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
