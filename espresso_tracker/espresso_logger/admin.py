from django.contrib import admin
from .models import CoffeeLog

@admin.register(CoffeeLog)
class CoffeeLogAdmin(admin.ModelAdmin):
    list_display = ['bean_name', 'roast_level', 'dose', 'yield_amt', 'extraction_time', 'water_temperature', 'sourness_bitterness', 'strength']
    search_fields = ['bean_name', 'notes', 'tools_used']
    list_filter = ['bean_name', 'roast_level']
