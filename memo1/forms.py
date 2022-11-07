from django import forms 
from .models import study_web


class study_webForm(forms.ModelForm):
    class Meta:
        model = study_web
        fields =['title','category','content','url']