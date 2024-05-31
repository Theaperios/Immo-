from django.contrib import admin
from .models import Category, Product, profil,consultation, favoris

# Register your models here.

class AdminCategorie(admin.ModelAdmin):
    list_display= ('name','date_added','description')

class AdminProduct(admin.ModelAdmin):
    list_display=('title','lot','price','category','date_added')
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategorie)

@admin.register(profil)
class profilAdmin(admin.ModelAdmin):
    list_display = ("number", "adresse","pays")
    

@admin.register(consultation)
class consultationAdmin(admin.ModelAdmin):
    list_display=("date","heure","commentaire","date_added", "product", "user")   

@admin.register(favoris) 
class favorisAdmin(admin.ModelAdmin):
    list_display=("produit","user")     

