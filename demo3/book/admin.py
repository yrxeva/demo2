from django.contrib import admin
from .models import Book,Hero
# Register your models here.

# 创建关联表
class HeroInline(admin.StackedInline):
    model = Hero
    # 关联一个，然后可以手动添加多个
    extra = 1
# 自定义模型管理类,原生类名+Admin
class BookAdmin(admin.ModelAdmin):
    # 显示多列
    list_display = ['title','pub_date']
    # 过滤器
    list_filter = ['title','pub_date']
    # 查询
    search_fields = ['title','pub_date']

    # 用于关联
    inlines = [HeroInline]

class HeroAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill']

admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)