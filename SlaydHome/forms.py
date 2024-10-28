from django import forms
from .models import *

class SlideForm(forms.ModelForm):
    class Meta:
        model = Web_Design
        fields = "__all__"