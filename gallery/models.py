from django.db import models



class Circular_Images(models.Model):
    locatin = models.CharField(default='بخشنامه ها', max_length=100)
    image = models.ImageField(upload_to='images/')
    
    
    class Meta:
        db_table = 'Circular_Images'
        verbose_name = 'تصاویر'
        verbose_name_plural = 'تصاویر بخشنامه ها'
    
    
    def __str__(self):
        return '{}'.format(self.pk)
    
    
    
    
class Works_Images(models.Model):
    locatin = models.CharField(default='نمونه کار ها', max_length=100)
    image = models.ImageField(upload_to='images/')
    
    class Meta:
        db_table = 'Works_Images'
        verbose_name = 'تصاویر'
        verbose_name_plural = 'تصاویر نمونه کار ها'
    
    
    def __str__(self):
        return '{}'.format(self.pk)
    
    