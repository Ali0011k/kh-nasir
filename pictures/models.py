from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class HomePictures(models.Model):
    
    image = models.ImageField(upload_to='images/',verbose_name=u"تصویر اسلایدر") 
    
    def __str__(self):
        return 'تصویر شماره {}'.format(self.pk)
    
class HomeInfo(models.Model):
    info = RichTextUploadingField(verbose_name='اطلاعات هنرستان')
    location = RichTextUploadingField(verbose_name='موقیعت مکانی هنرستان')
    phone = models.CharField(max_length=200,verbose_name=u"شماره تلفن هنرستان")
    slogan = models.CharField(max_length=200 , verbose_name=u"شعار هنرستان" ,default=None)
    def __str__(self) :
        return self.phone
    
    
    