from django.db import models
from django.urls import reverse
from gallery.models import Circular_Images
from django.utils import timezone
from extensions.utils import jalali_converter
from ckeditor_uploader.fields import RichTextUploadingField

# models are created here

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="ادرس ای پی ")
    class Meta:
        verbose_name = 'آی پی'
        verbose_name_plural = 'آی پی ها'
class Notification(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', "منتشر شده"),
    )
    title = models.CharField(max_length=100,blank=False,null=False,verbose_name=u"عنوان اطلاعیه",)
    text = RichTextUploadingField(blank=False,null=False,verbose_name=u"متن اطلاعیه")
    create_time = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")
    hits = models.ManyToManyField(IPAddress, blank=True, related_name="hits", verbose_name="بازدید ها")
    
    
    class Meta:
        verbose_name = 'اطلاعیه'
        verbose_name_plural = 'اطلاعیه ها'
        db_table = 'Notifications'
   	
    def __str__(self):
         return self.title


    def jpublish(self):
	    return jalali_converter(self.create_time)
    jpublish.short_description = 'زمان انتشار'
    
    
    def get_absolute_url(self):
	    return reverse("users:notification-list")
    
    
    
    
class Circular(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', "منتشر شده"),
    )
    title = models.CharField(max_length=100,blank=False,null=False,verbose_name=u"عنوان بخشنامه",)
    text = RichTextUploadingField(blank=False,null=False,verbose_name=u"متن بخشنامه")
    image = models.ImageField(upload_to='images/',verbose_name=u"تصویر بخشنامه") 
    create_time = models.DateTimeField(default=timezone.now,blank=False,null=False,verbose_name='تاریخ انتشار بخشنامه')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")
    visits = models.ManyToManyField(IPAddress, blank=True, related_name="visits", verbose_name="بازدید ها")
    
    
    

    
    def save(self,*args, **kwargs):
        super(Circular, self).save(*args, **kwargs)
        image = self.image
        Circular_Images.objects.create(image = image)
    
        
    class Meta:
        verbose_name = 'بخشنامه'
        verbose_name_plural = 'بخشنامه ها'
        db_table = 'Circular'
    	
     
    def __str__(self):
          return self.title

    def jpublish(self):
	    return jalali_converter(self.create_time)
    jpublish.short_description = 'زمان انتشار'


    def get_absolute_url(self):
	    return reverse("users:notification-list")
    
  