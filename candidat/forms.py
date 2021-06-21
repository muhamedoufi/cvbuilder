from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *


class CandidatForm(ModelForm):
   
    class Meta:
        model=Candidat
        fields="__all__"
        exclude = ["user"]
    def __init__(self, *args, **kwargs):
        super(CandidatForm, self).__init__(*args, **kwargs)
        for key in self.fields:
          self.fields[key].required = False 
        
        # dateNaissance = forms.DateField(
    #     input_formats=['%d/%m/%Y'], 
    #     widget=BootstrapDateTimePickerInput()
    # )
class PersonneForm(ModelForm):
   
    class Meta:
        model=Personne
        fields="__all__"
        # exclude = ["util"] 
