from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *




class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']
    #     username = forms.CharField(
    #     max_length=254,
    #     widget=forms.TextInput(attrs={'class': "input"}),
    # )
    # password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'input'})
        self.fields['email'].widget.attrs.update({'class':'input'})
        self.fields['password1'].widget.attrs.update({'class':'input'})
        self.fields['password2'].widget.attrs.update({'class':'input'})
class UserForm(ModelForm):
    model = User
    fields:'__all__'
