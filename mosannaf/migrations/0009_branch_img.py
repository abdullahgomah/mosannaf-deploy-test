# Generated by Django 4.1.5 on 2023-02-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosannaf', '0008_rename_category_mosannafcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='branches/', verbose_name='صورة المصنف'),
        ),
    ]
