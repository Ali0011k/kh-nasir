# Generated by Django 4.2.2 on 2023-08-22 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IP_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='ادرس ای پی ')),
            ],
        ),
        migrations.CreateModel(
            name='SectionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='کلید دسترسی به رشته')),
                ('display_text', models.CharField(max_length=100, verbose_name='نام رشته')),
            ],
        ),
        migrations.CreateModel(
            name='Handout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان جزوه')),
                ('file', models.FileField(default=None, upload_to='docs/', verbose_name='فایل جزوه')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('lesson', models.CharField(max_length=100, verbose_name='درس')),
                ('create_by', models.CharField(default=None, max_length=200, verbose_name='نام هنرآموز')),
                ('status', models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده')], default='d', max_length=1, verbose_name='وضعیت')),
                ('section', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to='courses.sectionchoice', verbose_name='رشته')),
                ('visits', models.ManyToManyField(blank=True, related_name='visits', to='courses.ip_address', verbose_name='بازدید ها')),
            ],
            options={
                'verbose_name': 'جزوه',
                'verbose_name_plural': 'جزوه ها',
                'db_table': 'handout',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_files', models.FileField(default=None, upload_to='docs/', verbose_name='فایل های دیگر جزوه')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_files', to='courses.handout')),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='سوال')),
                ('awnser', models.TextField(max_length=2000, verbose_name='جواب')),
                ('create_by', models.CharField(default=None, max_length=200, verbose_name='نام ناشر')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('status', models.CharField(choices=[('d', 'پیش\u200cنویس'), ('p', 'منتشر شده')], default='d', max_length=1, verbose_name='وضعیت')),
                ('section', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.sectionchoice', verbose_name='رشته')),
            ],
            options={
                'verbose_name': 'پرسش و پاسخ',
                'verbose_name_plural': 'پرسش و پاسخ ها',
                'db_table': 'faq',
            },
        ),
    ]
