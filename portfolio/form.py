from django import forms
from .models import Portfolio

class PortfolioUpload(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title','image','description']