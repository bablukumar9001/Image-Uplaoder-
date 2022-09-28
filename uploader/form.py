from django import forms
from .models import Image 
from django.forms import fields  
# from django.db import models  

class ImageForm(forms.ModelForm):
 class Meta:
     model= Image 
     fields ='__all__'
    #  fields =('photo','caption')
     lables={'photo':''}
