from django.contrib import admin
from .models import Bill


class BillAdmin(admin.ModelAdmin):
    list_prr_page = 20
    list_display = ("title", "ware", "cose")
    
admin.site.register(Bill, BillAdmin)
