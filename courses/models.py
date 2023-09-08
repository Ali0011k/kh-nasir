from django.db import models
from extensions.utils import jalali_converter
from ckeditor_uploader.fields import RichTextUploadingField


class SectionChoice(models.Model):
    value = models.CharField(max_length=100 , verbose_name='کلید دسترسی به رشته',blank=False, null=False)
    display_text = models.CharField(max_length=100 , verbose_name='نام رشته', blank=False, null=False)

    def __str__(self):
         return self.display_text

class IP_Address(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="ادرس ای پی ")


class Faq(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', "منتشر شده"),
    )
    question = models.CharField(max_length=500 , verbose_name='سوال')
    awnser = RichTextUploadingField(verbose_name='جواب')
    lesson_sections = models.CharField(max_length=500,verbose_name='درس',blank=False , null=False , default='')
    section = models.ForeignKey(SectionChoice , on_delete=models.CASCADE, verbose_name='رشته',default=None)
    create_by = models.CharField(max_length=200 , blank=False , null=False , default=None,verbose_name='نام ناشر')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")
    
    
    class Meta:
        db_table = 'faq'
        verbose_name = 'پرسش و پاسخ'
        verbose_name_plural = 'پرسش و پاسخ ها'

    def jpublish(self):
	    return jalali_converter(self.create_time)
    jpublish.short_description = 'زمان انتشار'
    
    def __str__(self):
        return '{}---{}'.format(self.pk , self.question)
    
    
class Handout(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', "منتشر شده"),
    )


    title = models.CharField(max_length=200,verbose_name='عنوان جزوه')
    file = models.FileField(upload_to='docs/' ,default=None , verbose_name='فایل جزوه')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    section = models.ForeignKey(SectionChoice,on_delete=models.CASCADE,max_length=150  , verbose_name='رشته' , blank=False , null=False)
    lesson = models.CharField(max_length=100  , verbose_name='درس' , blank=False , null=False)
    create_by = models.CharField(max_length=200 ,default= None, verbose_name='نام هنرآموز',null=False,blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")
    visits = models.ManyToManyField(IP_Address, blank=True, related_name="visits", verbose_name="بازدید ها")


        
    
    class Meta:
        db_table = 'handout'
        verbose_name = 'جزوه'
        verbose_name_plural = 'جزوه ها'
    
    
    def jpublish(self):
	    return jalali_converter(self.create_time)
    jpublish.short_description = 'زمان انتشار'

    
    def __str__(self):
        return '{}---{}'.format(self.pk , self.title)
    
    
class File(models.Model):
    post = models.ForeignKey(Handout , on_delete= models.CASCADE , related_name='other_files' )
    other_files = models.FileField(upload_to='docs/' ,default=None , verbose_name='فایل های دیگر جزوه')
