from django.db import models
from django_countries.fields import CountryField
from mosannaf.models import UnitType, Street

# Create your models here.



# publisher models
class Publisher(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=255)  # اسم
    # country = models.CharField(verbose_name="الدولة", max_length=150)  # دولة
    country = CountryField(verbose_name='دولة')
    territory = models.CharField(
        max_length=100, verbose_name='إقليم')  # اقليم
    county = models.CharField(
        max_length=100, verbose_name='مقاطعة')  # مقاطعة
    region = models.CharField(max_length=100, verbose_name='منطقة')  # منطقة
    city = models.CharField(max_length=100, verbose_name='مدينة')  # مدينة
    governorate = models.CharField(
        max_length=100, verbose_name='محافظة')  # محافظة
    village = models.CharField(max_length=100, verbose_name='قرية')  # قرية
    neighborhood = models.CharField(max_length=100, verbose_name='حي')  # حي
    street = models.ForeignKey("mosannaf.Street", verbose_name='شارع',
                               on_delete=models.SET_NULL, null=True, blank=True)  # شارع
    building = models.IntegerField(
        default=0, verbose_name='بناية رقم')  # بناية رقم
    floor = models.IntegerField(default=0, verbose_name='الدور')  # الدور
    # unit = models.CharField(verbose_name='الوحدة', max_length=20)  # الوحدة
    unit_type = models.ForeignKey(
        'mosannaf.UnitType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع الوحدة')
    unit_number = models.IntegerField(verbose_name='رقم الوحدة', default=0)
    nearest_landmark = models.ForeignKey(
        "mosannaf.NearLandMark", on_delete=models.SET_NULL, blank=True, null=True, verbose_name='أقرب معلم بارز')
    coordinates = models.CharField(
        max_length=100, verbose_name='إحداثيات')  # إحداثيات
    landline_number = models.CharField(
        max_length=20, verbose_name='هاتف رقم')  # هاتف رقم
    phone_number = models.CharField(
        max_length=20, verbose_name='جوال رقم')  # جوال رقم
    fax_number = models.CharField(
        max_length=25, verbose_name='فاكس رقم')  # فاكس رقم
    telex = models.CharField(max_length=50, verbose_name='تلكس')  # تلكس
    pobox = models.CharField(
        max_length=50, verbose_name='صندوق بريد')  # صندوق بريد
    postal_code = models.CharField(
        max_length=50, verbose_name='الرمز البريدي')  # الرمز البريدي
    email = models.EmailField(
        verbose_name="البريد الإلكتروني", max_length=150)  # البريد الإلكتروني


    class Meta: 
        verbose_name='ناشر'
        verbose_name_plural ='ناشرون'
        