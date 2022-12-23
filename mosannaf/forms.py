from .models import Rate
from django import forms 

class RateForm(forms.ModelForm): 

    class Meta:
        model = Rate 
        fields = ['details']
    
class AddRate(forms.Form):
    details = forms.CharField(label='', max_length=200, widget=forms.TextInput) 
