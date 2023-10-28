from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

    
urlpatterns = [
    path('notifications/',notifications),
    path('notification_detail/',notification_detail),
    path('data/notifications/content/' , NotificationApiView.as_view()),
    path('data/notifications/content/<int:pk>/' , NotificationUpdateApiView.as_view()),
    path('data/Circular/content/' , CircularApiView.as_view()),
    path('data/Circular/content/<int:pk>/' , CircularUpdateApiView.as_view()),
]