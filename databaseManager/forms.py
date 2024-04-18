#Defines Django forms that contain fields drawn from models defined in models.py(of databaseManager)
from django import forms
from databaseManager.models import saveUsername

class saveUsernameForm(forms.ModelForm):
    class Meta:
        model = saveUsername
        fields = ("username",) 