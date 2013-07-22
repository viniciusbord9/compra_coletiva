from django import forms
from django.contrib import admin
from offer.forms import OfferCreationForm, OfferViewForm
from offer.models import OfferEntity, OfferAttribute, OfferAttributeVarchar, OfferAttributeDecimal, OfferAttributeSet, OfferAttributesOfAttributeSet, OfferAttributeType


class AttributeForm(forms.ModelForm):
    class Meta:
        model = OfferAttribute
        
class AttributesetForm(forms.ModelForm):      
    attributos = forms.ModelMultipleChoiceField(queryset=OfferAttribute.objects.all(), widget=forms.SelectMultiple)
        
    class Meta:
        model = OfferAttributeSet            
                                              
class Attribute(admin.ModelAdmin):
    form = AttributeForm
  
class Attributeset(admin.ModelAdmin):
    form = AttributesetForm
    def save_model(self, request, obj, form, change):
        obj.save();
        for attribute in form.cleaned_data["attributos"]:
            offer_attribute_of_attributeset = OfferAttributesOfAttributeSet(attribute_id=attribute,attribute_set_id = obj)
        
        offer_attribute_of_attributeset.save();
        

class OfferAttributesetForm(forms.ModelForm):
    attributes = []
    for attribute in OfferAttributeSet.objects.all():
        aux = [attribute.id,attribute.name]
        attributes.append(aux)
         
    Conjunto_atributos = forms.IntegerField(widget = forms.Select(choices=attributes))   
    
    class Meta:
        model = OfferEntity 
        exclude = ['name',] 
    
class OfferForm(forms.ModelForm):
    attributeset = -1
    
    def add_attributes_form(self,attributes):
            
        for attribute in attributes :
            indice =  OfferAttribute.objects.get(id = attribute.attribute_id_id)
            field = OfferAttributeType.objects.get(id__exact = indice.type_id)
            if field.type == 'varchar':
                field = forms.CharField(label= indice.name)
            elif field.type == 'datetime':
                field = forms.DateTimeField(label= indice.name)
            elif field.type == 'decimal':
                field = forms.FloatField(label = indice.name)
                
            self.fields[indice.code] = field
            self.base_fields[indice.code] = field 
        
                                             
                
    
    def __init__(self, *args, **kwargs): 
        super(OfferForm,self).__init__(*args, **kwargs)
        aux = kwargs['initial']
        attributeset = aux['attributeset']
        if isinstance(attributeset,unicode) :
            attributes = OfferAttributesOfAttributeSet.objects.filter(attribute_set_id=attributeset)
    
        OfferForm.add_attributes_form(self,attributes)
        
    class Meta:
        model = OfferEntity
        
class Offer(admin.ModelAdmin):
    
    def get_form(self, request, obj=None, **kwargs):
        param = request.GET
        if param.has_key('attributeset'):
            attributeset_id = param['attributeset']
            if isinstance(attributeset_id,unicode):
                attributeset = OfferAttributeSet.objects.filter(id = attributeset_id)
            else:
                attributeset = 0
        else:
            attributeset = 0
    
        if not(isinstance(attributeset,int)) and attributeset.count()== 1 : 
            return OfferForm
        else:
            return OfferAttributesetForm

      
    
    def response_add(self, request ,obj,post_url_continue='../%s/add'):
        resp = super(Offer, self).response_add(request, obj, post_url_continue)
        post = request.POST
        url = request.path;
        if post.has_key("Conjunto_atributos"):
            attributeset = post['Conjunto_atributos']
            resp['Location'] = url +"?attributeset="+attributeset;
        else:
            resp['Location'] = url
            
        return resp
    
    def save_model(self,request, obj,form, change):
        post = request.POST
        if not(post.has_key("Conjunto_atributos")):
            obj.save()
    
    
    
        

admin.site.register(OfferEntity, Offer)
admin.site.register(OfferAttribute, Attribute)
admin.site.register(OfferAttributeSet, Attributeset)