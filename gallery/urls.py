from django.urls import path
from .views import *


urlpatterns = [
    path('data/gallery/works/content/' , WorkImageApiView.as_view()),
    path('data/gallery/works/content/<int:pk>/' , WorkImageUpdateApiView.as_view()),
    path('data/gallery/circular/content/' , CircularImageApiView.as_view()),
    path('data/gallery/circular/content/<int:pk>/' , CircularImageUpdateApiView.as_view()),
]