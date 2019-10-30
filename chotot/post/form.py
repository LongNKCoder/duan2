from django import forms
from django.core import validators
from .models import  Post,Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['state','create_date','update_date','user']

class ImageForm(forms.ModelForm):
    pic = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))
    class Meta:
        model = Image
        fields = ('pic',)

class PostFormUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['state','title','price']