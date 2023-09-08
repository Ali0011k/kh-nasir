# Generated by Django 4.2.2 on 2023-08-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام نمونه کار')),
                ('caption', models.TextField(max_length=2000, verbose_name='توضیحات نمونه کار')),
                ('image', models.ImageField(upload_to='images/', verbose_name='تصویر نمونه کار')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='docs/', verbose_name='فایل صوتی')),
                ('video', models.FileField(blank=True, default=None, null=True, upload_to='images/', verbose_name='فایل ویدیویی')),
                ('status', models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده')], default='d', max_length=1, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'نمونه کار',
                'verbose_name_plural': 'نمونه کار ها',
                'db_table': 'Works',
            },
        ),
    ]