# coding=utf-8

from __future__ import unicode_literals
from django.db import models


class Bill(models.Model):
    title = models.CharField(verbose_name="标题", max_length=500)
    ware = models.CharField(verbose_name="商品", max_length=500)
    cost = models.IntegerField(verbose_name="花费金额(单位分)")
    remark = models.CharField(verbose_name="备注", max_length=500)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "账单"
        verbose_name_plural = "账单"

