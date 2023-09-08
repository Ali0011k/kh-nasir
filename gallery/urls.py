from django.urls import path
from .views import *


urlpatterns = [
    path('data/gallery/Works/content/' , Works_Images_serializer),
    path('data/gallery/Circular/content/' , Circular_Images_Serializer),
]