# Generated by Django 4.1.5 on 2023-02-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosannaf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100, null=True, unique=True, verbose_name='الاسم الظاهر في الرابط'),
        ),
    ]
