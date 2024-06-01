from email.headerregistry import Group
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import Group


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='image_categorie/', null=True)
    description = models.TextField(null=True)
    
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name    
        
        
        
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    nombre_piece = models.IntegerField(default=3)
    adresse= models.CharField(default="Abidjan", max_length=40)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image =models.FileField(upload_to='images/',default="1.jpg", null= True)
    image2 =models.FileField(upload_to='images/',default="1.jpg", null= True)
    image3 =models.FileField(upload_to='images/',default="1.jpg", null= True)
    image4 =models.FileField(upload_to='images/',default="1.jpg", null= True)
    image5 =models.FileField(upload_to='images/',default="1.jpg", null= True)
    lot= models.CharField(max_length=50, unique=True) #numéro du lot bien à ajouter(id)
    date_added = models.DateTimeField(auto_now=True) 
    # is_supprimer = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.title  
    
    
class profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number= models.IntegerField()
    pays= models.CharField(max_length=250)
    adresse=models.CharField(max_length=500)
    photo=models.FileField(upload_to="photo_user", null=True)
    
class consultation(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    commentaire = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added= models.DateField(auto_now_add=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
class favoris(models.Model):
    produit= models.ForeignKey(Product, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    is_favoris = models.BooleanField(default=True)


        
    
    
    