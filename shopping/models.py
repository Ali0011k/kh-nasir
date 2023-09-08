from django.db import models
from extensions.utils import jalali_converter
from gallery.models import Works_Images
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Works(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', "منتشر شده"),
    )
    name = models.CharField(max_length=200 , verbose_name= u"نام نمونه کار" )
    caption = RichTextUploadingField(verbose_name= u"توضیحات نمونه کار")
    image = models.ImageField(upload_to='images/',verbose_name=u"تصویر نمونه کار") 
    file = models.FileField(upload_to='docs/' ,default=None , verbose_name='فایل صوتی' , blank=True , null=True)
    video = models.FileField(upload_to='images/' , default=None , verbose_name= 'فایل ویدیویی' , blank=True , null=True )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")
    create_time = models.DateTimeField(auto_now_add=True,)
    
    
    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کار ها'
        db_table = 'Works'
    
    def jpublish(self):
	    return jalali_converter(self.create_time)
    jpublish.short_description = 'زمان انتشار'
    
    def save(self , *args, **kwargs):
        super(Works, self).save(*args, **kwargs)
        image = self.image
        Works_Images.objects.create(image = image)
        
    def __str__(self):
        return self.name
        
