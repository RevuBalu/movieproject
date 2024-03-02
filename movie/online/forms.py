from django import forms
from online.models import Online
class onlineform(forms.ModelForm):
    class Meta:
        model= Online
        fields="__all__"