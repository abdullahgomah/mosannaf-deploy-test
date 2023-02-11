from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# from publisher.models import Publisher
# from printinghouse.models import PrintingHouse

# Create your models here


class Mosannaf(models.Model):
    name = models.CharField(max_length=255, verbose_name='اسم المصنف')
    meaning = models.TextField(verbose_name='تفسير اسم المصنف')
    summary = models.TextField(verbose_name='نبذه عن المصنف')

    m_type = models.ForeignKey(
        'Type', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع المصنف')

    chain = models.CharField(max_length=200, verbose_name='سلسلة')

    related_to = models.ForeignKey(
        "Mosannaf", on_delete=models.SET_NULL, null=True, blank=True, verbose_name='ذو علاقة', related_name='mosannaf_related_to')
    competitor = models.ForeignKey(
        "Mosannaf", on_delete=models.SET_NULL, verbose_name="منافس", null=True, blank=True, related_name='mosannaf_competitor')
    contrary = models.ForeignKey(
        "Mosannaf", on_delete=models.SET_NULL, blank=True, null=True, verbose_name='منافي', related_name='mosannaf_contrary')

    fields = models.ManyToManyField("Field", verbose_name="المجالات")

    category = models.ForeignKey(
        "MosannafCategory", verbose_name="الفئة", on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.ForeignKey(
        "Specialization", verbose_name="التخصصص", on_delete=models.SET_NULL, null=True, blank=True)
    original_lang = models.ForeignKey(
        "Lang", verbose_name="أصل لغة المصنف", on_delete=models.SET_NULL, null=True, blank=True)
    date_published = models.DateField(
        verbose_name='تاريخ النشر', null=True, blank=True)
    parts_count = models.IntegerField(default=0, verbose_name='الأجزاء')
    pages_count = models.IntegerField(default=0, verbose_name='الصفحات')
    units_count = models.IntegerField(default=0, verbose_name='اﻷبواب')
    chapters_count = models.IntegerField(default=0, verbose_name='الفصول')
    # subject = models.ForeignKey("Subject", verbose_name="الموضوع",
    #                             on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.CharField(
        verbose_name="الموضوع", blank=True, null=True, max_length=100)
    branch = models.ForeignKey(
        "Branch", verbose_name='القسم', on_delete=models.SET_NULL, blank=True, null=True)
    # branch = models.CharField(max_length=200, verbose_name="القسم")
    sub_branch = models.ForeignKey(
        "SubBranch", verbose_name='القسم الفرعي', on_delete=models.SET_NULL, blank=True, null=True)
    # sub_brnach = models.CharField(max_length=200, verbose_name="القسم الفرعي")

    # chapter = models.ForeignKey(
    #     "Chapter", verbose_name="الفصل", on_delete=models.SET_NULL, blank=True, null=True)
    chapter = models.CharField(max_length=200, verbose_name="الفصل")
    # field = models.ForeignKey(
    #     'Field', verbose_name='المجال', on_delete=models.SET_NULL, blank=True, null=True)
    field = models.CharField(max_length=200, verbose_name="المجال")

    # activity = models.ForeignKey(
    #     "Activity", verbose_name='النشاط', on_delete=models.SET_NULL, blank=True, null=True)
    activity = models.CharField(max_length=200, verbose_name="النشاط")

    image = models.ImageField(verbose_name='صورة المصنف', upload_to='covers/',
                              height_field=None, width_field=None, max_length=None)
    file = models.FileField(verbose_name='ملف المصنف',
                            upload_to='mosannafat/', max_length=100)
    m_format = models.ForeignKey(
        "Formats", verbose_name="صيغة المصنف", blank=True, null=True, on_delete=models.SET_NULL)

    m_form = models.ForeignKey(
        "Forms", verbose_name="شكل المصنف", blank=True, null=True, on_delete=models.SET_NULL)
    # m_form = models.CharField(max_length=200, verbose_name="شكل المصنف")

    # size = models.ForeignKey(
    #     "Size", verbose_name="حجم المصنف", blank=True, null=True, on_delete=models.SET_NULL)
    m_size = models.CharField(max_length=200, verbose_name="حجم المصنف")

    measurement = models.ForeignKey(
        "Measurement", verbose_name="قياس المصنف", blank=True, null=True, on_delete=models.SET_NULL)

    # measurement = models.CharField(max_length=200, verbose_name="قياس المصنف")

    preparation = models.ForeignKey(
        "Preparation", verbose_name='إعداد', on_delete=models.SET_NULL, blank=True, null=True)
    # preparation = models.CharField(max_length=200, verbose_name="إعداد")

    author = models.ForeignKey(
        "Author", verbose_name='المؤلف', on_delete=models.SET_NULL, blank=True, null=True)

    # author = models.CharField(max_length=200, verbose_name="تأليف")

    checker = models.ForeignKey(
        "Checker", verbose_name='المحقق', on_delete=models.SET_NULL, blank=True, null=True)
    # checker = models.CharField(max_length=200, verbose_name="المحقق")

    publisher = models.ForeignKey(
        "Publisher", verbose_name='ناشر', on_delete=models.SET_NULL, blank=True, null=True)

    printing_house = models.ForeignKey(
        "PrintingHouse", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المطبعة")

    print_year = models.CharField(verbose_name="سنة الطباعة", max_length=20)
    print_number = models.CharField(verbose_name="رقم طبعة", max_length=20)

    publish_year = models.CharField(verbose_name="سنة النشر", max_length=20)
    # publish_year = models.DateField(verbose_name="سنة النشر", viewMode='years')

    isbn = models.CharField(verbose_name='ردمك', max_length=50)

    # 18# ردمد
    issn = models.CharField(verbose_name='ردمد', max_length=50)

    # 19# رقم الايداع
    deposit_number = models.CharField(
        verbose_name='رقم الايداع', max_length=60)

    # iso
    iso = models.CharField(max_length=200, verbose_name='ايزو')

    # 20# فنان الغلاف
    # cover_artist = models.CharField(max_length=200, verbose_name="فنان الغلاف")
    cover_artist = models.ForeignKey(
        "CoverArtists", verbose_name="فنان الغلاف", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'مصنف'
        verbose_name_plural = 'المصنفات'


# فنان الغلاف
class CoverArtists(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=200)

    class Meta:
        verbose_name = 'فنان غلاف'
        verbose_name_plural = 'فنانين الأغلفة'


# تقييم المصنف
class Rate(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='المستخدم', related_name='rated_user', null=True)
    mosannaf = models.ForeignKey(
        Mosannaf, on_delete=models.CASCADE, verbose_name="المصنف", related_name='mosannaf_rate')
    details = models.CharField(max_length=250, verbose_name="التقييم")
    score = models.IntegerField(verbose_name='عدد النجوم', default=0, validators=[
        MinValueValidator(0), 
        MaxValueValidator(5)
    ])

    def __str__(self):
        return f"تقييم {self.mosannaf.name}"

    class Meta:
        verbose_name = 'تقييم'
        verbose_name_plural = "التقييمات"


class Type(models.Model):
    name = models.CharField(max_length=250, verbose_name='نوع المصنف')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نوع المصنف'
        verbose_name_plural = 'أنوع المصنفات'


class MosannafCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name='فئة المصنف')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فئة المصنف'
        verbose_name_plural = 'فئات المصنفات'


class Specialization(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'تخصص'
        verbose_name_plural = 'التخصصات'


class Lang(models.Model):
    name = models.CharField(max_length=50, verbose_name='اللغة')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'لغة'
        verbose_name_plural = 'اللغات'


# جدول الباب
class Unit(models.Model):
    name = models.CharField(max_length=255, verbose_name='باب')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'باب'
        verbose_name_plural = 'الأبواب'


# جدول الموضوع
class Subject(models.Model):
    name = models.CharField(verbose_name='موضوع', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'المواضيع'


# جدول القسم
class Branch(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان القسم (بالإنجليزية)")
    name = models.CharField(max_length=200, verbose_name="القسم")
    img = models.ImageField(upload_to='branches/', verbose_name='صورة المصنف', null=True, blank=True)
    background_hex = models.CharField(verbose_name='كود Hex لون الخلفية', max_length=20, null=True, blank=True)
    color_hex = models.CharField(verbose_name='كود Hex لون الخط', max_length=20, null=True, blank=True)
    view_in_home = models.BooleanField(default=False, verbose_name="عرض في الصفحة الرئيسية")
    slug = models.SlugField(verbose_name='الاسم الظاهر في الرابط', max_length=100, allow_unicode=True, null=True, blank=True, unique=True)

    def arabic_slugify(self, str):
        str = str.replace(" ", "-")
        str = str.replace(",", "-")
        str = str.replace("(", "-")
        str = str.replace(")", "")
        str = str.replace("؟", "")
        return str

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = self.arabic_slugify(self.name)
        super(Branch, self).save(*args, **kwargs)


    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'قسم'
        verbose_name_plural = 'اﻷقسام'


# جدول القسم الفرعي
class SubBranch(models.Model):
    branch = models.ForeignKey(
        "Branch", verbose_name='القسم', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name="القسم الفرعي")
    img = models.ImageField(upload_to='branches/', verbose_name='صورة المصنف', null=True, blank=True)
    background_hex = models.CharField(verbose_name='كود Hex لون الخلفية', max_length=20, null=True, blank=True)
    color_hex = models.CharField(verbose_name='كود Hex لون الخط', max_length=20, null=True, blank=True)
    slug = models.SlugField(verbose_name='الاسم الظاهر في الرابط', max_length=100, allow_unicode=True, null=True, blank=True, unique=True)

    def arabic_slugify(self, str):
        str = str.replace(" ", "-")
        str = str.replace(",", "-")
        str = str.replace("(", "-")
        str = str.replace(")", "")
        str = str.replace("؟", "")
        return str

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = self.arabic_slugify(self.name)
        super(SubBranch, self).save(*args, **kwargs)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "قسم فرعي للمكتبة"
        verbose_name_plural = "اﻷقسام الفرعية للمكتبة"

# جدول المجال


class Field(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم المجال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مجال'
        verbose_name_plural = 'المجالات'

# جدول النشاط


class Activity(models.Model):
    name = models.CharField(max_length=250, verbose_name='اسم النشاط')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نشاط'
        verbose_name_plural = 'الأنشطة'


# صيغ المصنفات
class Formats(models.Model):
    name = models.CharField(max_length=20, verbose_name='اسم الصيغة')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'صيغة مصنف'
        verbose_name_plural = 'صيغ المصنفات'


# جدول شكل المصنف
class Forms(models.Model):
    name = models.CharField(max_length=50, verbose_name='الشكل')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شكل مصنف'
        verbose_name_plural = 'أشكال المصنفات'


class Size(models.Model):
    name = models.CharField(max_length=50, verbose_name='الحجم')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'حجم مصنف'
        verbose_name_plural = 'أحجام المصنفات'


class Measurement(models.Model):
    name = models.CharField(max_length=50, verbose_name='القياس')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'قياس مصنف'
        verbose_name_plural = 'قياسات المصنفات'


# preparation
class Preparation(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'معد'
        verbose_name_plural = 'المعدين'


# authors
class Author(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مؤلف'
        verbose_name_plural = 'المؤلفون'


# checkers
class Checker(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'محقق'
        verbose_name_plural = 'المحققين'


class Chapter(models.Model):
    name = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name='الاسم')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فصل'
        verbose_name_plural = 'الفصول'


# Translated Mosannaf مصنف مترجم
class TranslatedMosannaf(models.Model):
    mosannaf = models.ForeignKey(
        Mosannaf, on_delete=models.CASCADE, verbose_name='المصنف')

    # 1# اللغة
    language = models.ForeignKey(
        Lang, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='اللغة')

    # 2# تاريخ الإصدار المترجم
    data_published = models.DateField(
        auto_now=False, verbose_name="تاريخ الإصدار المترجم", null=True, blank=True)

    # 3# ناشر الترجمة
    translate_publisher = models.CharField(
        max_length=200, verbose_name='ناشر الترجمة')

    # 4# صورة المصنف المترجم
    cover = models.ImageField(
        verbose_name="صورة المصنف المترجم", upload_to="Motargam/Covers")

    # 5# صيغة المصنف
    tm_format = models.ForeignKey(
        Formats, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="صيغة المترجم")

    # 6# شكل المصنف
    tm_form = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="شكل المصنف")

    # 7# حجم المصنف
    tm_size = models.CharField(
        max_length=100, verbose_name='حجم المصنف المترجم')

    # 8# قياس المصنف
    tm_mesaurement = models.CharField(
        max_length=100, verbose_name="قياس المصنف")

    # 9# إعداد
    preparation = models.CharField(max_length=100, verbose_name='اعداد')

    # 10 حقل المؤلف
    publisher = models.CharField(max_length=100, verbose_name="الناشر")

    # 11# المحقق
    checker = models.CharField(max_length=200, verbose_name='المحقق')

    # 12# الناشر
    publisher = models.ForeignKey(
        "Publisher", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الناشر")

    # 13# طبعة سنة
    print_year = models.CharField(verbose_name="سنة الطباعة", max_length=20)

    # 14# طبعة رقم
    print_number = models.CharField(verbose_name="رقم الطباعة", max_length=20)

    # 15# مطبعة
    printing_house = models.ForeignKey(
        "PrintingHouse", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المطبعة")

    # 16# سنة النشر
    publish_year = models.CharField(verbose_name="سنة النشر", max_length=20)

    # 17# ردمك الترجمة
    translation_isbn = models.CharField(
        verbose_name='ردمك الترجمة', max_length=50)

    # 18# ردمد
    issn = models.CharField(verbose_name='ردمد', max_length=50)

    # 19# رقم الايداع
    deposit_number = models.CharField(
        verbose_name='رقم الايداع', max_length=60)

    # iso
    iso = models.CharField(max_length=200)

    # 20# فنان الغلاف
    cover_artist = models.CharField(max_length=200, verbose_name="فنان الغلاف")

    # 21# سلسلة
    chain = models.CharField(max_length=100, verbose_name="السلسلة")

    # fields = models.ManyToManyField("Field", verbose_name= 'المجالات', null=True, blank=True)

    fields = models.ManyToManyField("Field", verbose_name="المجالات")

    # 22# قسم
    branch = models.CharField(max_length=100, verbose_name="القسم")

    def __str__(self):
        return f"مترجم {self.mosannaf.name}"

    class Meta:
        verbose_name = 'مصنف مترجم'
        verbose_name_plural = "مصنف مترجم"


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
    street = models.ForeignKey("Street", verbose_name='شارع',
                               on_delete=models.SET_NULL, null=True, blank=True)  # شارع
    building = models.IntegerField(
        default=0, verbose_name='بناية رقم')  # بناية رقم
    floor = models.IntegerField(default=0, verbose_name='الدور')  # الدور
    # unit = models.CharField(verbose_name='الوحدة', max_length=20)  # الوحدة
    unit_type = models.ForeignKey(
        'UnitType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='نوع الوحدة')
    unit_number = models.IntegerField(verbose_name='رقم الوحدة', default=0)
    nearest_landmark = models.ForeignKey(
        "NearLandMark", on_delete=models.SET_NULL, blank=True, null=True, verbose_name='أقرب معلم بارز')
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

    # حقل النطاق
    p_range = models.CharField(verbose_name='النطاق', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ناشر'
        verbose_name_plural = "الناشرون"


class UnitType(models.Model):
    name = models.CharField(verbose_name='الاسم', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نوع وحدة قياس'
        verbose_name_plural = "نوع وحدة القياس"


# printing house models

class Street(models.Model):
    name = models.CharField(max_length=100, verbose_name='شارع')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شارع'
        verbose_name_plural = 'شوارع'


class NearLandMark(models.Model):
    name = models.CharField(max_length=200, verbose_name='الاسم')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'أقرب معلم بارز'
        verbose_name_plural = 'أقرب معلم بارز'


class PrintingHouse(models.Model):
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
    # street = models.CharField(max_length=100, verbose_name='شارع')  # شارع
    street = models.ForeignKey("Street", verbose_name='شارع',
                               on_delete=models.SET_NULL, null=True, blank=True)  # شارع
    building = models.IntegerField(
        default=0, verbose_name='بناية رقم')  # بناية رقم
    floor = models.IntegerField(default=0, verbose_name='الدور')  # الدور
    unit = models.CharField(verbose_name='الوحدة', max_length=20)  # الوحدة
    # nearest_landmark = models.CharField(max_length=150, verbose_name='أقرب معلم بارز')  # أقرب معلم بارز
    nearest_landmark = models.ForeignKey(
        "NearLandMark", on_delete=models.SET_NULL, blank=True, null=True, verbose_name='أقرب معلم بارز')
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مطبعة'
        verbose_name_plural = "المطابع"
