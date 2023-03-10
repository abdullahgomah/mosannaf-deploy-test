# Generated by Django 4.1.5 on 2023-02-15 20:45

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mosannaf', '0005_remove_publisher_nearest_landmark_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='دولة')),
                ('territory', models.CharField(max_length=100, verbose_name='إقليم')),
                ('county', models.CharField(max_length=100, verbose_name='مقاطعة')),
                ('region', models.CharField(max_length=100, verbose_name='منطقة')),
                ('city', models.CharField(max_length=100, verbose_name='مدينة')),
                ('governorate', models.CharField(max_length=100, verbose_name='محافظة')),
                ('village', models.CharField(max_length=100, verbose_name='قرية')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='حي')),
                ('building', models.IntegerField(default=0, verbose_name='بناية رقم')),
                ('floor', models.IntegerField(default=0, verbose_name='الدور')),
                ('unit_number', models.IntegerField(default=0, verbose_name='رقم الوحدة')),
                ('coordinates', models.CharField(max_length=100, verbose_name='إحداثيات')),
                ('landline_number', models.CharField(max_length=20, verbose_name='هاتف رقم')),
                ('phone_number', models.CharField(max_length=20, verbose_name='جوال رقم')),
                ('fax_number', models.CharField(max_length=25, verbose_name='فاكس رقم')),
                ('telex', models.CharField(max_length=50, verbose_name='تلكس')),
                ('pobox', models.CharField(max_length=50, verbose_name='صندوق بريد')),
                ('postal_code', models.CharField(max_length=50, verbose_name='الرمز البريدي')),
                ('email', models.EmailField(max_length=150, verbose_name='البريد الإلكتروني')),
                ('nearest_landmark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mosannaf.nearlandmark', verbose_name='أقرب معلم بارز')),
                ('street', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mosannaf.street', verbose_name='شارع')),
                ('unit_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mosannaf.unittype', verbose_name='نوع الوحدة')),
            ],
        ),
    ]
