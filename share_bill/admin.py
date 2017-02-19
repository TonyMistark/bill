from django.contrib import admin
from .models import Bill


class BillAdmin(admin.ModelAdmin):
    list_prr_page = 20
    list_display = ("id", "title", "ware", "cost", "remark", "update_time", "create_time")

admin.site.register(Bill, BillAdmin)


