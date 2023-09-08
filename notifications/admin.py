from django.contrib import admin
from .models import *
from django.utils.html import format_html



@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    
    list_display = ['id','title','create_time']


@admin.register(Circular)
class Circular(admin.ModelAdmin):
    
    
    def image_tag(self, obj ):
        return format_html('<a href = "{}" target="_blank"><img src="{}" style="max-width:90px; max-height:90px"/></a>'.format(obj.image.url,obj.image.url),)
    
    
    image_tag.short_description = 'تصویر بخشنامه'
    list_display = ['id','title','create_time','image_tag']
    
admin.site.register(IPAddress)
    
