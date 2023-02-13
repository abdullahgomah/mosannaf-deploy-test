# Generated by Django 4.1.5 on 2023-02-13 18:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosannaf', '0002_branch_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='عدد النجوم'),
        ),
    ]
