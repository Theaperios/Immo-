from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from shop.models import profil
from django.contrib import messages
from .forms  import*
from django.contrib.auth import  login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth.decorators import login_required

# Create your views here.

def singup(request):
    if request.method == "POST":
        form = ProfilForm(request.POST)
        user_form =UserCreationForm(request.POST)
        
        if form.is_valid():
            user = user_form.save()  # Sauvegarde l'utilisateur
            profil = form.save(commit=False)
            profil.user = user  # Associe l'utilisateur au profil
            profil.save()  # Enregistre le profil
            
            usernam = user_form.cleaned_data["username"]
            passwor = user_form.cleaned_data["password"]
            user_log = authenticate(request, username=usernam, password=passwor)    
            if user_log is not None:
                login(request, user_log)
                return redirect("home")
        else:
            messages.error(request,'Formulaire invalide.')
            # Redirection ou autre action après l'enregistrement réussi
    else:
        # Si la requête n'est pas de type POST, afficher les formulaires vides
        form = ProfilForm()
        user_form = UserCreationForm()
                     
    return render(request,'compte/inscrip.html', {"form":form, "user":user_form})
              
        
        
 
        
def singin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usernam = form.cleaned_data["username"]
            passwor = form.cleaned_data["password"]
            user = authenticate(request, username=usernam, password=passwor)    
            if user is not None:
                login(request, user)
                return redirect("home")
 
    else:
        form =AuthenticationForm()
    return render(request, "compte/login.html", {"form": form})


def deconnexion(request):
    logout(request)
    return redirect("home")

def user_pofil(request):
    user=request.user
    return render(request,"compte/profil.html",{"profil":user})

@login_required(login_url="singin")
def update_password(request):
    if request.method=="POST":
        form=change_password(request.POST)
        if form.is_valid():
            last_password=form.cleaned_data["last_password"]
            user=request.user
            if not user.check_password(last_password):
                messages.error("mot de passe actuel incorrect.")
            else:
                new_password=form.cleaned_data["new_password"]
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user) 
                return redirect("user_profil")
    else:
        form=change_password()           
    
    return render(request,"compte/password.html",{"form":form})

    

        

