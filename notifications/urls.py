from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

    
urlpatterns = [
    path('notifications/',notifications),
    path('notification_detail/',notification_detail),
    path('data/notifications/content/' , Notification_serializer),
    path('data/notifications/content/update/' , Notification_update),
    path('data/Circular/content/' , Circular_serializer),
    path('data/Circular/content/update/' , Circular_update),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)