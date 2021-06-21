from django.db import models
from django.contrib.auth.models import User


class Candidat(models.Model) :
    sexe = (
        ('FEMELLE','FEMELLE'),
        ('MALE','MALE')
    )
    prenom = models.CharField(max_length=100,null=True)
    nom = models.CharField(max_length=100 ,null= True)
    Email = models.EmailField(null= True)
    Telephone = models.CharField(max_length=100,null= True)
    age = models.IntegerField(null= True) 
    dateNaissance = models.DateField(null= True)
    lieuNaissance = models.CharField(max_length=100, null=True)
    Nationalite = models.CharField(max_length=100,null=True)
    Addresse = models.CharField(max_length=100,null=True)
    Image = models.ImageField(null=True,upload_to='media')
    Telephone = models.CharField(max_length=100,null=True)
    sexe= models.CharField(max_length=120,null=True,choices=sexe)
    site = models.CharField(max_length=100,null=True)
    linkedin = models.CharField(max_length=100,null=True)
    # user = models.ForeignKey(User, null= True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE,unique=True,related_name="candidat")
    
    def __str__(self):
        return f"candidature: {self.nom}"

# Create your models here.
class Personne(models.Model):
    prenom = models.CharField(max_length=100,null=True)
    nom = models.CharField(max_length=100 ,null= True)
    Email = models.EmailField(null= True)
    Image = models.ImageField(null=True,upload_to='media')
    util = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE,unique=True)
    
    
    def __str__(self): 
        return f"candidature: {self.nom}"