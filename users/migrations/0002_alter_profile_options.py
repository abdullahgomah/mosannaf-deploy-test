# Generated by Django 4.1.5 on 2023-01-15 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'ملف شخصي', 'verbose_name_plural': 'الملفات الشخصية'},
        ),
    ]
