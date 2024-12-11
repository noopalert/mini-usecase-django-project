from django.contrib import admin
from .models import DailyTrans

class DailyTransAdmin(admin.ModelAdmin):
    readonly_fields = [
        'date_time', 
        'slug'
    ]

admin.site.register(DailyTrans, DailyTransAdmin)
