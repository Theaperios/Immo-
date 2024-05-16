from django.urls import path
from .views import*

urlpatterns = [
    path('inscription/', singup, name='singup'),
    path('login/', singin, name='singin'),
    path('deconnexion/',deconnexion, name='deconnexion'),
    path('user_profil/',user_pofil,name='user_profil'),
    path('set_password/',update_password, name='update_password')
]
