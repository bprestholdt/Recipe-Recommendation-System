#Defines Django forms that contain fields drawn from models defined in models.py(of databaseManager)
from django import forms
from .models import Recipe

class RecipeForm(forms.Form):
    ingredients = forms.CharField(label='Ingredients', widget=forms.Textarea(attrs={'rows': 3}))
