from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from account.decorators import notLoggedUsers, allowedUsers,forAdmins
from django.contrib.auth.models import Group 
from django.views.decorators.clickjacking import xframe_options_deny 
from django.views.decorators.clickjacking import xframe_options_sameorigin
# Create your views here.

@login_required(login_url='index')
# @allowedUsers(allowedGroups=['personne'])
def home(request):
 
    
    return render(request, 'pages/cadidat.html')  


# def index(request):
#     return render(request, 'pages/index.html')
# def navbar(request):
#     return render(request, 'pages/navbar.html') 

# def home(request):
#     return HttpResponse('Hello') 
# @notLoggedUsers
# def userLogin(request):
#     if request.user.is_authenticated:
#         return redirect('candidat')
#     else:
#        if request.method == 'POST':
#         username =request.POST.get('username')
#         password =request.POST.get('password')
#         user =authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request,user) 
#             return redirect('candidat')
#         else:
#             messages.info(request, "credential error ")
#             # return render(request, 'pages/index.html')
#         # context={}
#     return render(request, 'pages/index.html')
# # @notLoggedUsers
# def register(request):
#     if request.user.is_authenticated:
#         return redirect('candidat')
#     else:
#         form = CreateNewUser()
#         if request.method == 'POST':
#             form = CreateNewUser(request.POST)
#             if form.is_valid():
#                 user=form.save()
#                 username= form.cleaned_data.get('username')
#                 messages.success(request, username + 'Created Successfuly!')
#                 group = Group.objects.get(name = 'personne')
#                 user.groups.add(group)
#                 return redirect('index')
#         context={'form': form}
#         return render(request, 'pages/register.html',context)


# def userLogout(request):
#     logout(request)
#     return redirect('index')

# def create(request):
#     # candidat = request.user.candidat
#     form=CandidatForm() #instance = candidat
#     if request.method=='POST':
#         # print(request.POST)
#         form=CandidatForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context={'form':form}
#     return render(request, 'pages/candid_form.html',context)

def createLanguage(request):
    langue_form=LangueForm ()
    if request.method=='POST':
        # print(request.POST)
        langue_form=LangueForm (request.POST)
        if langue_form.is_valid():
            langue_form= langue_form.save(commit=False)
            langue_form.id_candidat = Candidat.objects.get(user=request.user.candidat.user)
            langue_form.save()
            return redirect('/sections/langue')
    context={'langue_form':langue_form}
    return render(request, 'pages/langue_form.html',context)

def createExprience(request):
    Experience_form=ExperienceForm()
    if request.method=='POST':
        # print(request.POST)
        Experience_form=ExperienceForm (request.POST)
        if Experience_form.is_valid():
            Experience_form= Experience_form.save(commit=False)
            Experience_form.id_candidat = Candidat.objects.get(user=request.user.candidat.user)
            Experience_form.save()
            return redirect('/sections/Experience')
    context={'Experience_form':Experience_form}
    return render(request, 'pages/ExperienceForm.html',context)

def createCompetence(request):
    Competence_form=CompetenceForm()
    if request.method=='POST':
        # print(request.POST)
        Competence_form=CompetenceForm (request.POST)
        if Competence_form.is_valid():
            Competence_form= Competence_form.save(commit=False)
            Competence_form.id_candidat = Candidat.objects.get(user=request.user.candidat.user)
            Competence_form.save()
            return redirect('/sections/Competence')
    context={'Competence_form':Competence_form}
    return render(request, 'pages/competence_form.html',context)    

def createInteret(request):
    Interet_form=InteretForm()
    if request.method=='POST':
        # print(request.POST)
        Interet_form=InteretForm(request.POST)
        if Interet_form.is_valid():
            Interet_form= Interet_form.save(commit=False)
            Interet_form.id_Personne = Candidat.objects.get(user=request.user.candidat.user)
            Interet_form.save()
            return redirect('/sections/Interet')
    context={'Interet_form':Interet_form}
    return render(request, 'pages/InteretForm.html',context)  

def createCertification(request):
    Certification_form=CertificationForm()
    if request.method=='POST':
        # print(request.POST)
        Certification_form=CertificationForm(request.POST)
        if  Certification_form.is_valid():
            Certification_form= Certification_form.save(commit=False)
            Certification_form.id_candidat = Candidat.objects.get(user=request.user.candidat.user)
            Certification_form.save()
        return redirect('/sections/Certification')
    context={'Certification_form': Certification_form}
    return render(request, 'pages/Certification_Form.html',context)  

def createDeclarationPerson(request):
    DeclarationPerson_form=DeclarationPersonForm()
    if request.method=='POST':
        # print(request.POST)
        DeclarationPerson_form=DeclarationPersonForm(request.POST)
        if DeclarationPerson_form.is_valid():
            DeclarationPerson_form= DeclarationPerson_form.save(commit=False)
            DeclarationPerson_form.id_candidat = Candidat.objects.get(user=request.user.candidat.user)
            DeclarationPerson_form.save()
        return redirect('/sections/DeclarationPerson')
    context={'DeclarationPerson_form':  DeclarationPerson_form}
    return render(request, 'pages/DeclarationPersonForm.html',context) 

def createRéfférence(request):
    Réfférence_form=RéfférenceForm()
    if request.method=='POST':
        # print(request.POST)
         Réfférence_form=RéfférenceForm(request.POST)
         if Réfférence_form.is_valid():
            Réfférence_form= Réfférence_form.save(commit=False)
            Réfférence_form.id_candidat = Candidat.objects.get(user=request.user.candidat.user)
            Réfférence_form.save()
         return redirect('/sections/Réfférence')
    context={'Réfférence_form':Réfférence_form}
    return render(request, 'pages/RéfférenceForm.html',context)


def createFormation(request):
    # INITIAL_DATA = {'id_candidat': Candidat.id}
    Formation_form=FormationForm()
    if request.method=='POST':
        # print(request.POST)
         Formation_form=FormationForm(request.POST)
         if Formation_form.is_valid():
            Formation_form= Formation_form.save(commit=False)
            Formation_form.id_candidat = Candidat.objects.get(user=request.user.candidat.user)
            Formation_form.save()
            return redirect('/sections/Formation')
    context={'Formation_form':Formation_form}
    return render(request, 'pages/FormationForm.html',context)
# @xframe_options_deny
# @xframe_options_sameorigin
# from django.views.decorators.clickjacking import xframe_options_exempt
def cv(request,pk):
    can = CV.objects.get(id=pk)

    context ={'can':can}
    return render(request, 'pages/resume.html',context)
# @xframe_options_exempt
def createcv(request):
    langue_form=LangueForm ()
    Experience_form=ExperienceForm()
    Competence_form=CompetenceForm()
    Certification_form=CertificationForm()
    DeclarationPerson_form=DeclarationPersonForm()
    Réfférence_form=RéfférenceForm()
    Formation_form=FormationForm()
    Interet_form=InteretForm()
    cv_form=CVForm(request.user.candidat)
    cv= CV.objects.filter(candidat=request.user.candidat) 
    # my_cv =CV.objects.get(pk=173)
    print(cv)
    
    if request.method=='POST':
         cv_form= CVForm(request.user.candidat, request.POST)
         mes_exp= request.POST.getlist('Experiences')
         mes_lng= request.POST.getlist('Langues')
         mes_ref= request.POST.getlist('Refferances')
         mes_frm= request.POST.getlist('Formations')
         mes_cer= request.POST.getlist('Certifications')
         mes_inter= request.POST.getlist('interet')
         mes_comp= request.POST.getlist('Competence')
        #  print(int(request.POST['Experiences']))
         if cv_form.is_valid():
            cv_form= cv_form.save(commit=False)
            cv_form.candidat = Candidat.objects.get(user=request.user.candidat.user)
            cv_form.save()
            for expr in mes_exp:
                # print(expr)
                exp = Experience.objects.get(id=expr)
                cv_form.Experiences.add(exp)
                cv_form.save()
            # langues 
            for lang in mes_lng:
                lang = Langue.objects.get(id=lang)
                cv_form.Langues.add(lang)
                cv_form.save()
            # competence
            for comp in mes_comp:
                print(comp)
                com = Competence.objects.get(id=comp)
                cv_form.Competence.add(com)
                cv_form.save()
            # refferences
            for ref in mes_ref:
                reff = Réfférence.objects.get(id=ref)
                cv_form.Refferances.add(reff)
                cv_form.save()
                # formation
            for frm in mes_frm:
                frmas = Formations.objects.get(id=frm)
                cv_form.Formations.add(frmas)
                cv_form.save()
# interet
            for inter in mes_inter:
                interet = Interet.objects.get(id=inter)
                cv_form.interet.add(inter)
                cv_form.save()
                # certifications
            for certif in mes_cer:
                certi = Certification.objects.get(id=certif)
                cv_form.Certifications.add(certi)
                cv_form.save()
            for skill in cv_form.Competence.all():
                print(skill.Niveau)
            cv=CV.objects.get(id=cv_form.id)
            print(cv)
            pk=cv.id
            # print (type(cv_form.id))
            # request.method='GET'
            # return render(request, 'pages/resume.html',context)
            return cv(request,pk)
            
    context={'cv_form':cv_form,
    'can':cv,
    'Interet_form':Interet_form,
    'langue_form':langue_form,
    'Experience_form':Experience_form,
    'Competence_form':Competence_form,
    'Certification_form':Certification_form,
    'DeclarationPerson_form':DeclarationPerson_form,
    'Réfférence_form':Réfférence_form,
    'Formation_form':Formation_form}
    return render(request, 'pages/cvform.html',context) 
def form(request):
     return render(request, 'pages/form.html')


 
def user_profile(request):
    # id = requst.user.candidat.id_candidat.all()
    # context={id,'id '}
    return render(request, 'pages/profile.html')
def sidebar(request):
    # id = requst.user.candidat.id_candidat.all()
    # context={id,'id '}
    return render(request, 'pages/sidebar.html')