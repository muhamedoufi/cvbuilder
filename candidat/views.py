from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
# from django.contrib.auth.models import User
from account.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# from .decorators import notLoggedUsers, allowedUsers,forAdmins
from django.contrib.auth.models import Group  

# Create your views here.




def create(request):
    candidat = request.user
    can =Candidat.objects.get(user=candidat)
    # print(request.user)
    form=CandidatForm(instance = can) #
    if request.method=='POST':
        # print(request.POST)
        form=CandidatForm(request.POST,request.FILES,instance=can)
        if form.is_valid():
            form= form.save(commit=False)
            form.user = User.objects.get(id=request.user.id)
            form.save() 
            return redirect('coordonnées')
    context={'form':form}
    return render(request, 'pages/candid_form.html',context)

def personne(request):
    personne = request.user.personne
    can =Personne.objects.get(util=personne)
    # print(request.user)
    form=PersonneForm(instance=can) #
    if request.method=='POST':
        # print(request.POST)
        form=PersonneForm(request.POST,request.FILES,instance=can)
        if form.is_valid():
            form= form.save(commit=False)
            form.util = User.objects.get(id=request.user.id)
            form.save()
            return redirect('personne')
    context={'form':form}
    return render(request, 'pages/personne.html',context)
    
    
