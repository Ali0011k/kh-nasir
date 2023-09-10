from rest_framework import serializers
from .models import *


class HomePicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePictures
        fields = '__all__'


class HomeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeInfo
        fields = '__all__'