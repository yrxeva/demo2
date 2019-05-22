from django import template
from ..models import Article,Classify,Tag
# 注册对象,library注意大写
register = template.Library()
@register.filter(name='mylower')
def mylower(value):
    return value.lower()

@register.filter(name='myslice')
def myslice(value,length):
    result = value[:length]
    return result

# 得到所有的分类
@register.simple_tag(name='getclassify')
def getclassify():
    return Classify.objects.all()


