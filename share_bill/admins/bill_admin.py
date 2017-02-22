# coding=utf-8

from xadmin import site
from share_bill import models


class BillAdmin(object):
    app_label = 'share_bill'
    menu_group = 'bill_base'
    order = 1
    list_display = ("id", "title", "ware", "cost", "remark", "update_time", "create_time")

site.register(models.Bill, BillAdmin)