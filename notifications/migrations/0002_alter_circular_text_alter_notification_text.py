# Generated by Django 4.2.2 on 2023-09-07 18:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circular',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن بخشنامه'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن اطلاعیه'),
        ),
    ]
