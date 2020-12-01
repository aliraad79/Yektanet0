from django import forms
from advertiser_mangement.models import Ad
class CreateAdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['advertiser','title', 'img', 'link']

