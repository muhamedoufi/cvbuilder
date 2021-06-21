from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *
# from .widgets import BootstrapDateTimePickerInput


# class CreateNewUser(UserCreationForm):
#     class Meta:
#         model = User
#         fields=['username','email','password1','password2']
#     #     username = forms.CharField(
#     #     max_length=254,
#     #     widget=forms.TextInput(attrs={'class': "input"}),
#     # )
#     # password = forms.CharField(widget=forms.PasswordInput)
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm,self).__init__(*args,**kwargs)
#         self.fields['username'].widget.attrs.update({'class':'input'})
#         self.fields['email'].widget.attrs.update({'class':'input'})
#         self.fields['password1'].widget.attrs.update({'class':'input'})
#         self.fields['password2'].widget.attrs.update({'class':'input'})

# class CandidatForm(ModelForm):
#     # dateNaissance = forms.DateField(
#     #     input_formats=['%d/%m/%Y'], 
#     #     widget=BootstrapDateTimePickerInput()
#     # )
#     class Meta:
#         model=Candidat
#         fields="__all__"
#         exclude = ["user"]
        # widgets = {
        #     'dateNaissance': forms.DateInput(attrs={'class':'datepicker'}),
        # }  
class LangueForm(ModelForm ):

    class Meta:
        model=Langue
        fields="__all__"
        exclude = ["id_candidat"]
    
#     Niveau = forms.ChoiceField(
#     label="Select your university",
    
#     empty_value="--- youre empty value here ---",
# )

class ExperienceForm(ModelForm ) :

    class Meta:
        model=Experience
        fields="__all__"
        exclude = ["id_candidat"]

class CompetenceForm(ModelForm ) :

    class Meta:
        model=Competence
        fields="__all__"
        exclude = ["id_candidat"]

class InteretForm(ModelForm ) :

    class Meta:
        model=Interet
        fields="__all__"
        exclude = ["id_Personne"]

class CertificationForm(ModelForm ) :

    class Meta:
        model=Certification
        fields="__all__" 
        exclude = ["id_candidat"]

class DeclarationPersonForm(ModelForm ) :

    class Meta:
        model=DeclarationPerson
        fields="__all__"   
        exclude = ["id_candidat"]
          

class RéfférenceForm(ModelForm ) :

    class Meta:
        model=Réfférence
        fields="__all__" 
        exclude = ["id_candidat"] 

class FormationForm(ModelForm) :
    
    class Meta:
        model=Formation
        fields="__all__"
        exclude = ["id_candidat"] 
    #     widgets = {'id_candidat': forms.HiddenInput()} 
    # def __init__(self, *args, **kwargs):
    #     initial = kwargs.get('initial', {})
    #     initial['id_candidat'] = Candidat.id
    #     kwargs['initial'] = initial
    #     super(ModelForm, self).__init__(*args, **kwargs)
class CVForm(ModelForm) :

    class Meta:
        model=CV
        fields=['interet','Langues','Certifications','Experiences','Competence','Refferances','Declaration','Formations'] 
        exclude = ["candidat"] 
        


    def __init__(self, user, *args, **kwargs):
        super(CVForm, self).__init__(*args, **kwargs)
        self.fields['Formations'].queryset =Formation.objects.filter(id_candidat=user)
        self.fields['interet'].queryset =Interet.objects.filter(id_Personne=user)
        self.fields['Langues'].queryset =Langue.objects.filter(id_candidat=user)
        self.fields['Certifications'].queryset =Certification.objects.filter(id_candidat=user)
        self.fields['Experiences'].queryset =Experience.objects.filter(id_candidat=user)
        self.fields['Refferances'].queryset =Réfférence.objects.filter(id_candidat=user)
        self.fields['Competence'].queryset =Competence.objects.filter(id_candidat=user)
        self.fields['Declaration'].queryset =DeclarationPerson.objects.filter(id_candidat=user)
        
        self.fields['Refferances'].required = False 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.fields['candidat'].queryset =Candidat.objects.filter(user=user)

    # Formations =forms.ModelMultipleChoiceField(queryset=Formation.objects.all())  
    # def __init__(self, *args, **kwargs):
        # super(ModelForm,self).__init__(*args,**kwargs)
        # self.fields['username'].widget.attrs.update({'class':'input'})
        # self.fields['interet'].widget.attrs.update({'class':'custom-select'})
        # self.fields['interet'].widget.attrs.update({'class':'custom-select'})
        # self.fields['interet'].widget.attrs.update({'class':'custom-select'})
        # self.fields['interet'].widget.attrs.update({'class':'custom-select'})
         
        # for field in self.fields: 
        #  self.fields[field].widget.attrs.update({'class':'custom-select'})