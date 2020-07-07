from django import forms
from blogapp.models import Article,CustomUser

class ArticleForm(forms.Form):
    title=forms.CharField(max_length=150)
    description=forms.CharField(max_length=250,widget=forms.Textarea)
    created_at=forms.DateField()

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['email','image']
