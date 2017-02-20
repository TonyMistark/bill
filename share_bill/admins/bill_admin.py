# coding=utf-8

from xadmin import site
from share_bill import models


class BillAdmin(object):
    app_label = 'oms'
    menu_group = 'banner_group'
    order = 8
    list_display = ['ap_id', 'client_id', 'user_id', 'create_time']

site.register(models.Bill, BillAdmin)