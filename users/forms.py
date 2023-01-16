from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    email = forms.EmailField(label="البريد الإلكتروني")
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label="الاسم الأخير")


    class Meta:
        model = User 
        fields = ["username", 'first_name', 'last_name', 'email']

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ['image']