from django.contrib import admin
from .models import Works
from django.utils.html import format_html


@admin.register(Works)
class Work_admin(admin.ModelAdmin):
    
    def image_html(self, obj ):
        return format_html('<a href = "{}" target="_blank"><img src="{}" style="max-width:90px; max-height:90px"/></a>'.format(obj.image.url,obj.image.url),)
    
    image_html.short_description = 'تصویر نمونه کار'
    
    list_display = ['id' , 'name' , 'image_html']