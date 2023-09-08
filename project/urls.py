from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path('auth/super_admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',include('users.urls')),
    path('',include('notifications.urls')),
    path('',include('gallery.urls')),
    path('',include('shopping.urls')),
    path('',include('courses.urls')),
    path('',include('pictures.urls'))
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

