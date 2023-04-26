from django.contrib import admin
from .models import WineQuality

# Register your models here.
class WineQualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality', 'lr_pred', 'xgb_pred')
    list_display_links = ('id',)
    list_filter = ('quality', 'lr_pred', 'xgb_pred')
    list_editable = ('quality', )
    list_per_page = 30 

admin.site.register(WineQuality, WineQualityAdmin)
