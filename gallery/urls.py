from django.urls import path
from .views import *


urlpatterns = [
    path('data/gallery/Works/content/' , Works_Images_serializer),
    path('data/gallery/Works/content/update/' , work_image_update),
    path('data/gallery/Circular/content/' , Circular_Images_Serializer),
    path('data/gallery/Circular/content/update/' , Circular_Images_update),
]