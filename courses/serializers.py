from rest_framework import serializers
from .models import *


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'
        
class HandoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handout
        fields = '__all__'