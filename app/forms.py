from django import forms
from .models import Student, Nationality
from captcha.fields import CaptchaField

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label='Searching', required=False)
    nationality = forms.ModelChoiceField(queryset=Nationality.objects.all(), label='Nationality', required=False)

class StudentForm(forms.ModelForm):
    captcha = CaptchaField(label='Enter text', error_messages={'invalid':'Wrong text'}, generator='captcha.helpers.random_char_challenge')
    class Meta:
        model = Student
        fields = ('__all__')

class NationalityForm(forms.Form):    
    nationality = forms.CharField(max_length=30)
    
    def clean_name(self):
        nationality = self.cleaned_data.get['nationality']        
        return nationality      


