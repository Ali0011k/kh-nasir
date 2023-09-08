from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('sections/handout/create/', add_new_section_choices),
    path('handouts/' , handout_sections),
    path('handout/detail/section/' , all_handouts),
    path('handouts_detail/' , handout_detail),
    path('faq/' , faq_list),
    path('faq/detail/section/' , faq),
    path('data/Handout/content/' , Handout_serializer),
    path('data/Faq/content/' , Faq_serializer)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
