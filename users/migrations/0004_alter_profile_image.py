# Generated by Django 4.1.5 on 2023-01-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_المستخدم_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics/', verbose_name='صورة الملف الشخصي'),
        ),
    ]