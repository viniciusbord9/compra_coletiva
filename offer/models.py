from django.db import models

# Create your models here.  
class OfferEntity(models.Model):
    name = models.CharField(max_length=45)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Oferta'
        
class OfferAttributeSet(models.Model):
    name = models.CharField(max_length = 60)
    class Meta:
        verbose_name = 'Conjunto de atributo'
        
    def __unicode__(self):
        return self.name
            
class OfferAttributeType(models.Model):
    type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.type
    
    def get_type(self):
        return self.type
    
class OfferAttribute(models.Model):
    type = models.ForeignKey(OfferAttributeType)
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=45)
    class Meta:
        verbose_name = 'Atributo'
    
    def __unicode__(self):
        return self.name
    
class OfferAttributeVarchar(models.Model):
    entity = models.ForeignKey(OfferEntity)
    attribute = models.ForeignKey(OfferAttribute)
    value = models.CharField(max_length=60)
    
class OfferAttributeDatetime(models.Model):
    entity = models.ForeignKey(OfferEntity)
    attribute = models.ForeignKey(OfferAttribute)
    value = models.DateField()
    
class OfferAttributeDecimal(models.Model):
    entity = models.ForeignKey(OfferEntity)
    attribute = models.ForeignKey(OfferAttribute)
    value = models.DecimalField(max_digits=10,decimal_places=5)

class OfferAttributesOfAttributeSet(models.Model):
    attribute_id = models.ForeignKey(OfferAttribute)
    attribute_set_id = models.ForeignKey(OfferAttributeSet)
    


        
    