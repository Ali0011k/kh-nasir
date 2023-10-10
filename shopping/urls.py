from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Works/' , works),
    path('Works/detail/' , works_detail),
    path('data/Works/content/' , Works_serializer),
    path('data/Works/content/update/' , work_update),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)