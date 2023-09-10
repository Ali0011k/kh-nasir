from django.urls import path
from .views import *

urlpatterns = [
    path('data/Home/Pictures/content/' , HomePictures_serializer),
    path('data/Home/Info/content/' , HomeInfo_serializer),   
]
