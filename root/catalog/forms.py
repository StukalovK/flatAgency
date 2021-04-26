from django import forms
from .models import Offer, District


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('title', 'about', 'content', 'owner', 'category', 'district', 'address', 'floor', 'price')


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('name', )