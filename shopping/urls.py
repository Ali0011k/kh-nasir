from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Works/' , works),
    path('Works/detail/' , works_detail),
    path('data/Works/content/' , WorkApiView.as_view()),
    path('data/Works/content/<int:pk>/' , WorkUpdateApiView.as_view()),
]