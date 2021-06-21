from django.db import models

from candidat.models import Candidat
class Langue(models.Model):
    niveau  = (
        ('','---selectionner votre niveau---'),
        ('Debutant','Debutant'),
        ('Intermédiaire','Intermédiaire'),
        ('Bien','Bien'),
        ('Très bien','Très bien'),
        ('Excellent','Excellent')
    )
    Nom= models.CharField(max_length=100)
    Niveau= models.CharField(max_length=100,choices=niveau,)
    
    id_candidat = models.ForeignKey(Candidat,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nom

class Experience(models.Model):
    NomEntreprise= models.CharField(max_length=100)
    PosteOccuppet= models.CharField(max_length=100) 
    contexte = models.CharField(max_length=250)
    institution = models.CharField(max_length=250,null=True)
    resume = models.CharField(max_length=250)
    dateDebut = models.DateField(max_length=250)
    dateFin = models.DateField(max_length=250)
    id_candidat = models.ForeignKey(Candidat, null= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.PosteOccuppet

class Competence(models.Model):
    sexe = (
        ('20','Debutant'),
        ('40%','Intermédiaire'),
        ('60%','Bien'),
        ('80%','Très bien'),
        ('100%','Excellent')
    )
    libellé = models.CharField(max_length=100)
    id_candidat = models.ForeignKey(Candidat, null= True, on_delete=models.SET_NULL) 
    Type = models.CharField(max_length=250,default='programation')
    Niveau = models.CharField(max_length=100,null=True,choices=sexe,)
    Description = models.TextField(blank=True)
    def __str__(self):
        return self.libellé

class Interet(models.Model):
    intitulé = models.CharField(max_length=100)
    id_Personne = models.ForeignKey(Candidat, null= True, on_delete=models.SET_NULL,)
    def __str__(self):
        return self.intitulé

# class Avoir(models.Model):
#     id_candidat = models.ForeignKey(Candidat, null= True,on_delete=models.SET_NULL)
#     id_interet = models.ForeignKey(Interet, null= True, on_delete=models.SET_NULL)
class Certification(models.Model):
    titre = models.CharField(max_length=250)
    autorite = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    date = models.DateField()
    id_candidat = models.ForeignKey(Candidat, null= True, on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.titre

class DeclarationPerson(models.Model):
    titre = models.CharField(max_length=100,null= True)
    Text = models.TextField()
    id_candidat = models.ForeignKey(Candidat, null= True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.titre

class Réfférence(models.Model):
    Nom = models.CharField(max_length=100)
    Numero = models.CharField(max_length=100)
    Email = models.CharField(max_length=100,null=True)
    ContactProffessionnel = models.CharField(max_length=100)
    Entreprise = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)
    id_candidat = models.ForeignKey(Candidat, null= True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.Nom

class Formation(models.Model):
    Nom = models.CharField(max_length=100)
    Niveau = models.CharField(max_length=200)
    institution = models.CharField(max_length=100)
    contexte = models.CharField(max_length=100)
    Description = models.TextField()
    DateDebut = models.DateField(null=True)
    DateFin = models.DateField(null=True)
    id_candidat = models.ForeignKey(Candidat, null= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Nom
class CV(models.Model):
    interet = models.ManyToManyField(Interet,blank=True)
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    Langues = models.ManyToManyField(Langue,blank=True)
    Certifications= models.ManyToManyField(Certification,symmetrical=False,blank=True)
    Experiences= models.ManyToManyField(Experience,related_name='experiences' ,blank=True)
    Competence = models.ManyToManyField(Competence,blank=True)
    Refferances= models.ManyToManyField(Réfférence,blank=True)
    Declaration = models.ForeignKey(DeclarationPerson, null= True, on_delete=models.CASCADE,related_name="declaration")
    Formations = models.ManyToManyField(Formation,blank=True)

    
# Create your models here.
