from django.forms import ModelForm
from shop.models import profil, favoris, consultation
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError


class ProfilForm(ModelForm):
    class Meta:
        model = profil
        fields = ["number", "pays", "adresse"]
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["number"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )
        
        
        self.fields["pays"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )
        
        self.fields["adresse"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )
       
       
        
class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }

    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={"class": "input100", "type": "text", "name": "email"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input100", "type": "password", "name": "pass"}
        ),
    )
class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', "last_name", 'email', 'password']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )
        
        
        self.fields["first_name"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )
        
        self.fields["last_name"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )
        self.fields["email"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )
        
        self.fields["password"].widget.attrs.update(
             {
                "class":"form-control",
             }   
        )        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet e-mail est déjà utilisé.")
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user      

class change_password(forms.Form):
          last_password=forms.CharField(label="ancien_mdp",widget=forms.PasswordInput)
          new_password=forms.CharField(label="nouveau_mdp", widget=forms.PasswordInput)
          confirm_password=forms.CharField(label="confirm_mdp",widget=forms.PasswordInput)
          
          def clean(self):
              cleaned_data=super().clean()
              new_password=cleaned_data.get("new_password")
              confirm_password=cleaned_data.get("confirm_password")
              
              if new_password!=confirm_password:
                  raise ValidationError("Les mots de passes ne correspondent pas.")
              return cleaned_data
          
# class consultation(forms.Form):
#     date_rdv=forms.DateField(label="date_rdv")
#     heure_rdv=forms.TimeField(label="heure_rdv") 
#     comment_rdv= forms.CharField(label="comment_rdv")
    
class add_favoris_form(forms.ModelForm):
    class Meta:
        models=favoris
        fields=["user", "product"]
        
class consult_form(forms.ModelForm):
    class Meta:
        model = consultation
        fields = ["date", "heure", "commentaire"]        
           
                
