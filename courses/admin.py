from django.contrib import admin
from .models import *
from django.utils.html import format_html


class FileInline(admin.StackedInline):
    model = File


@admin.register(Handout)
class HandoutAdmin(admin.ModelAdmin):
    
    list_display = ['id','title','create_time']
    inlines = [FileInline]
    
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    
    list_display = ['id','question','create_time']
    
@admin.register(SectionChoice)
class SectionChoice(admin.ModelAdmin):
    list_display = ['id' , 'display_text']