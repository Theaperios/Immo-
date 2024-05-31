from .views import*
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

from . import views 


urlpatterns = [
    path('',index,name="home"),
    #path('login',login,name="login"),
    #path('inscrip',inscrip,name="inscrip"),
    path('services',services,name="services"),
    path('detail/<int:myid>',detail,name="detail"),
    path('favoris/',favori,name="favoris"), 
    path('add_to_favorites/<int:produc_id>', views.add_to_favorites, name='add_to_favorites'),
    path('supprimer/<int:product_id>',supprimer,name="supprimer"),
    # path('contact',contact,name="contact"),
    path('rdv/<int:product_id>',rdv,name="rdv"),
    path('historique',historique.as_view(),name="historique"),
    path("consultation_a_modifier/<int:consultation_id>",modifier_consultation, name="consultation_a_modifier"),
    path("consultation_a_annuler/",annuler_consultation, name="consultation_a_annuler"),
    path("modif/<int:pk>/",rdv_update.as_view(), name="modif" ),
    path("cotegorie/<int:categorie_id>",maison_par_categorie, name="maison_par_categorie")


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG==True:
    urlpatterns+=static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)