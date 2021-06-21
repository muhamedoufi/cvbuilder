from django.urls import path
from . import views 
# app_name = 'candidat'

urlpatterns = [
    # path('login/',views.userLogin,name='index'), 
    # path('home/',views.home,name="candidat"),
    # path('register/',views.register,name="register"),
    # path('deconnecter/',views.userLogout,name="deconnecter"),
    path('create/',views.create,name="coordonnées"),
    path('personne/',views.personne,name="personne"),
    # path('langue/',views.createLanguage,name="langue"),
    # path('Experience/',views.createExprience,name="experience"),
    # path('Competence/',views.createCompetence,name="competence"),
    # path('Interet/',views.createInteret,name="interet"),
    # path('Certification/',views.createCertification,name="certification"),
    # path('DeclarationPerson/',views.createDeclarationPerson,name="declaration"),
    # path('Réfférence/',views.createRéfférence,name="reference"),
    # path('Formation/',views.createFormation,name="formation"),
    # path('CV/',views.createcv,name="create_cv") ,  #<str:pk>
    # path('form/',views.form,name="form"),
    # path('resume/',views.cv,name="cv"),
    # path('profile/',views.user_profile,name="profile")
     
]
