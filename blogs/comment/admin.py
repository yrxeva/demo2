from django.contrib import admin
# 引入模板模块
from .models import *
# Register your models here.
admin.site.register(Comment)