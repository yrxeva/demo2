from django.shortcuts import render,get_object_or_404

from django.core.paginator import Paginator
from .models import Article
from django.http import HttpResponse
# Create your views here.
def index(request):
    # 获取当前页,使用get方法不存在不报错为None
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum==None else pagenum
    # 根据访问量进行排序
    articles = Article.objects.all().order_by('-views')
    # 参数：对象列表，每页数目
    paginator = Paginator(articles,1)
    # 传入页码，得到一个页面，page包含所有信息
    page = paginator.get_page(pagenum)
    return render(request,'index.html',{'page':page})


def detail(request,id):
    article = get_object_or_404(Article,pk=id)
    return render(request,'single.html',locals())

