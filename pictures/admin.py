from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(HomePictures)
class HomePictureAdmin(admin.ModelAdmin):
    
    def image_tag(self , obj):
        return format_html('<a href = "{}" target="_blank"><img src="{}" style="max-width:90px; max-height:90px"/></a>'.format(obj.image.url,obj.image.url),)
    image_tag.short_description = 'تصویر هنرستان'
    
    list_display = ['image_tag']

@admin.register(HomeInfo)
class HomeInfoAdmin(admin.ModelAdmin):
    list_display = ['phone']
