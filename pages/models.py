from django.db import models

# Create your models here.


class Home(models.Model):
    main_sentence = models.CharField(
        max_length=150, verbose_name='الجملة الرئيسية')

    sub_sentence = models.CharField(
        max_length=250, verbose_name='الجملة الثانوية (الفرعية)')

    class Meta:
        verbose_name = 'الصفحة الرئيسية'
        verbose_name_plural = 'الصفحة الرئيسية'


class Contact(models.Model):
    facebook = models.URLField(
        verbose_name='رابط فيسبوك', null=True, blank=True)
    twitter = models.URLField(verbose_name='رابط تويتر', null=True, blank=True)
    instagram = models.URLField(
        verbose_name='رابط انستجرام', null=True, blank=True)
    youtube = models.URLField(
        verbose_name='رابط يوتيوب', null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'معلومات التواصل'
        verbose_name_plural = "معلومات التواصل"


class Message(models.Model):
    email = models.EmailField(verbose_name="البريد الإلكتروني", max_length=254)
    details = models.TextField(verbose_name='تفاصيل الرسالة')
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'رسالة'
        verbose_name_plural = "الرسائل"


class Suggestion(models.Model):
    details = models.TextField(verbose_name='اسم المصنف / المطبوعة')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.details} - {self.date}"

    class Meta:
        verbose_name = 'ترشيرح'
        verbose_name_plural = "الترشيحات"
