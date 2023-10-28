from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('sections/handout/create/', add_new_section_choices),
    path('handouts/', handout_sections),
    path('handout/detail/section/', all_handouts),
    path('handouts_detail/', handout_detail),
    path('faq/', faq_list),
    path('faq/detail/section/', faq),
    path('data/handout/content/', HandoutApiView.as_view()),
    path('data/handout/content/<int:pk>/', HandoutUpdateApiView.as_view()),
    path('data/Faq/content/', FaqApiView.as_view()),
    path('data/Faq/content/<int:pk>/', FaqUpdateApiView.as_view()),
    
]