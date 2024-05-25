from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, consultation, favoris
from django.contrib import messages
from .utils import send_email
from account.forms  import add_favoris_form, consult_form
from django.views import View
from django.views.generic import UpdateView

#from django.contrib.auth.decorators import login_required
#login_required  # Assure que seul un utilisateur connecté peut ajouter un produit aux favoris


# Create your views here.
def index(request):
  return render(request,"index.html")

  
def services(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object=Product.objects.filter(title__icontains=item_name)
    return render(request,"services.html",{'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request,"detail.html",{'product': product_object})

def favori(request):
    favorite_products=favoris.objects.filter(user=request.user)
    return render(request,"favoris.html",{"fav":favorite_products})

def add_to_favorites(request, produc_id):
    products=Product.objects.get(id=produc_id)
    user=request.user
    produit_favoris_exist=favoris.objects.filter(produit=products,user=user).exists() 
    
    if not produit_favoris_exist:
        produit_favoris = favoris.objects.create(produit=products,user=user)
    return redirect('services')


def supprimer(request,product_id):
    products=favoris.objects.get(id=product_id).delete()
    # if request.method== "POST":
    #     products_favoris=products
    #     products_favoris.is_favoris=False
    #     products_favoris.save()  
    return redirect('favoris')
    

def contact(request):
    return render(request,"historique.html")

def rdv(request, product_id):
    product= Product.objects.get(id=product_id)
    user=request.user
    if request.method=="POST":
        data={
            "date":request.POST.get("date"),
            "heure":request.POST.get("heure"),
            "commentaire":request.POST.get("commentaire"),
            "user":user,
            "product":product
            
        }
        date=data["date"]
        produit_favoris_exist= consultation.objects.filter(product=product,user=user, date=date).exists() 
        if not produit_favoris_exist:
            consult=consultation.objects.create(**data)
            subjet="Confirmation du RDV"
            message=f"Votre rendez-vous avec l'agence IMMO-PLUS est confirmé. Nous vous attendons pour le {consult.date} à {consult.heure}. "
            destinataire=[user.email]
            send_email(subjet,message,destinataire)
            if consult:
                messages.success(request,f"Merci M/Mme {user.first_name}, votre demande de rendez-vous pour le {consult.date} à {consult.heure} a bien été pris en compte. Vous recevrez une confirmation par mail ou par appel. ")
            else:
                messages.error(request,"Formulaire invalide")    
               
        else:
            messages.info(request,"Ce RDV existe déjà.")
    return render(request,"rdv.html")


class historique(View):
    template_name="historique.html"
    context={}
    def get(self,request):
        user=request.user
        user_historique=consultation.objects.filter(user=user).order_by("date")
        taille=0
        liste =[]
        
        for val in user_historique:
            liste.append(taille)
            taille+=1
            
        self.context["user_historique"]=user_historique
        self.context["taille"]=liste
        return render(request,self.template_name,self.context)    
    
    def post(self,request):
        return render(request,self.template_name,self.context) 
    
    
   
   
def modifier_consultation(request,consultation_id): 
    consultation_a_modifier=consultation.objects.get(id=consultation_id)
    if request.method== "POST":
        date=request.POST.get("date")
        heure=request.POST.get("heure")
        commentaire=request.POST.get("commentaire")
        consultation_a_modifier.date=date
        consultation_a_modifier.heure=heure
        consultation_a_modifier.commentaire=commentaire
    return render(request,"rdv.html", {"consult":consultation_a_modifier})


from django.urls import reverse_lazy
class  rdv_update(UpdateView):
    model = consultation
    form_class = consult_form
    template_name = "rdv1.html"
    success_url = reverse_lazy('historique')
 
def annuler_consultation(request): 
    if request.method == "POST":
        id_c = request.POST.get("id_supprimer")
        consultation_a_annuler = get_object_or_404(consultation, id=id_c)   
        consultation_a_annuler.delete()
    return redirect("historique")
            

# class  profil_update(UpdateView):
   
#     template_name = "profil2.html"
#     success_url = reverse_lazy('profil')            
     



