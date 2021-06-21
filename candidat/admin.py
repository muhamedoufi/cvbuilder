
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from .models import models

# Register your models here.
from .models import *


admin.site.register(Candidat)
admin.site.register(Personne)
