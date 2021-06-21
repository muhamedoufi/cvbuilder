from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .decorators import notLoggedUsers, allowedUsers,forAdmins
from django.contrib.auth.models import Group  


# @login_required(login_url='index')
# @allowedUsers(allowedGroups=['personne'])
# def home(request):
 
#     if request.method == 'POST': 
#         return  redirect('/home/') 
        
#     else:
#        return render(request, 'pages/cadidat.html')  


# def index(request):
#     return render(request, 'pages/index.html')
# def navbar(request):
#     return render(request, 'pages/navbar.html') 

# def home(request):
#     return HttpResponse('Hello') 
# @@notLoggedUsers
def userLogin(request):
    if request.user.is_authenticated:
        return redirect('candidat')
    else:
       if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user) 
            return redirect('candidat')
        else:
            messages.info(request, "credential error ")
            # return render(request, 'pages/index.html')
        # context={}
    return render(request, 'pages/index.html')
# @notLoggedUsers
def register(request):
    if request.user.is_authenticated:
        return redirect('candidat')
    else:
        form = CreateNewUser()
        if request.method == 'POST':
            form = CreateNewUser(request.POST)
            if form.is_valid():
                user=form.save()
                username= form.cleaned_data.get('username')
                messages.success(request, username + 'Created Successfuly!')
                group = Group.objects.get(name = 'personne')
                user.groups.add(group)
                return redirect('index')
        context={'form': form}
        return render(request, 'pages/register.html',context)


def userLogout(request):
    logout(request)
    return redirect('index')

# Create your views here.
