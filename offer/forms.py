from django import forms
from offer.models import OfferAttributeSet

class OfferCreationForm(forms.ModelForm):
    conjunto_de_atributos =   forms.ModelChoiceField(queryset=OfferAttributeSet.objects.all(), empty_label="selecione o conjunto de atributos")
    
class OfferViewForm(forms.ModelForm):
    conjunto_de_atributos =   forms.ModelChoiceField(queryset=OfferAttributeSet.objects.all(), empty_label="selecione o conjunto de atributos")