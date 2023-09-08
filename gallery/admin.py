from django.contrib import admin
from .models import Works_Images, Circular_Images
from django.utils.html import format_html

@admin.register(Works_Images)
class ImageAdmin(admin.ModelAdmin):
    
    def image_html(self, obj ):
        return format_html('<a href = "{}" target="_blank"><img src="{}" style="max-width:90px; max-height:90px"/></a>'.format(obj.image.url,obj.image.url),)
    
    image_html.short_description = 'تصاویر'

    list_display = ['id','image_html' , ]
    

@admin.register(Circular_Images)
class ImageAdmin(admin.ModelAdmin):
    
    def image_html(self, obj ):
        return format_html('<a href = "{}" target="_blank"><img src="{}" style="max-width:90px; max-height:90px"/></a>'.format(obj.image.url,obj.image.url),)
    
    image_html.short_description = 'تصاویر'

    list_display = ['id','image_html',]    