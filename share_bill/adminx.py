# coding=utf-8

import xadmin

from xadmin.views.dashboard import AppDashboard


class ShareBillIndex(AppDashboard):
    app_label = 'share_bill'
    template = 'app_dashboard.html'
    widget_customiz = False

xadmin.site.register_appindex(ShareBillIndex)

import pages
import views
import admins
