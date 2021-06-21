
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from .models import models

# Register your models here.
from .models import *


# admin.site.register(Candidat)
admin.site.register( Formation)
admin.site.register(DeclarationPerson)
admin.site.register(Langue)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(CV)
admin.site.register(Interet)
admin.site.register(Competence)
admin.site.register(Réfférence)