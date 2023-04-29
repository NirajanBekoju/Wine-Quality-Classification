from django.db import models

# Create your models here.
class WineQuality(models.Model):
    class Meta:
        verbose_name = "Wine Quality"
        verbose_name_plural = "Wine Quality"
    
    fixed_acidity =  models.FloatField(blank=False, null=False)
    volatile_acidity = models.FloatField(blank=False, null=False)
    citric_acid = models.FloatField(blank=False, null=False)
    residual_sugar = models.FloatField(blank=False, null=False) 
    chlorides = models.FloatField(blank=False, null=False)
    free_sulfur_dioxide = models.FloatField(blank=False, null=False) 
    total_sulfur_dioxide = models.FloatField(blank=False, null=False)
    density = models.FloatField(blank=False, null=False)
    pH = models.FloatField(blank=False, null=False)
    sulphates = models.FloatField(blank=False, null=False) 
    alcohol = models.FloatField(blank=False, null=False)
    quality = models.IntegerField(blank=True, null=True) # actual value
    lr_pred = models.IntegerField(blank=True, null=True) # prediction by logistic regression
    xgb_pred = models.IntegerField(blank=True, null=True) # prediction by xgboost classifier
    rf_pred = models.IntegerField(blank=True, null=True) # prediction by xgboost classifier
    svm_pred = models.IntegerField(blank=True, null=True) # prediction by xgboost classifier
    

    

