from django import forms
from django.forms import models, widgets 
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = () #quero tudo do model

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}), # o nome ficar marcado ao clicar
            'data_nascimento':forms.DateInput(attrs={'class':'form-control'}), # Input q é pra ficarem em inputs do bootstrap
            'email':forms.EmailInput(attrs={'class':'form-control'}) 
        
        }