from rest_framework import serializers
from .models import *


class Works_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works_Images
        fields = '__all__'
        
class Circular_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circular_Images
        fields = '__all__'