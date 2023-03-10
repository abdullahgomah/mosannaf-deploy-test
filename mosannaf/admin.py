from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MosannafCategory)
admin.site.register(Type)
admin.site.register(Mosannaf)
admin.site.register(Field)
admin.site.register(Branch)
admin.site.register(SubBranch)
admin.site.register(Lang)
admin.site.register(Formats)
admin.site.register(Forms)
admin.site.register(Street)
admin.site.register(NearLandMark)
admin.site.register(Measurement)
admin.site.register(Preparation)
admin.site.register(Author)
admin.site.register(Checker)
admin.site.register(CoverArtists)
admin.site.register(Specialization)

admin.site.register(Rate)  # جدول التقييمات
admin.site.register(TranslatedMosannaf)


admin.site.register(UnitType)


admin.site.register(PrintingHouse)
