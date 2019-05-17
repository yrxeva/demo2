from django.conf.urls import url
from . import views

# 给应用添加命名空间，在urls.py里面添加
app_name='book'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^list/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
]