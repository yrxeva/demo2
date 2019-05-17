from django.shortcuts import render

# Create your views here.
# 需要先引入httpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Book,Hero

def index(request):
    # 1加载模板
    template = loader.get_template('book/index.html')
    # 2构建参数字典，没有参数可以省略
    contex = {}
    # 3使用模板渲染动态数据
    result = template.render(contex)
    return HttpResponse(result)


def list(request):
    # 查询所有书籍
    allBook = Book.objects.all()

    # 加载模板
    template = loader.get_template('book/list.html')
    # 构建参数
    contex = {'allBook': allBook}
    # 使用模板渲染
    result = template.render(contex)
    return HttpResponse(result)


def detail(request,id):
    # 查找书名对应的所有主角
    book = None
    try:
        # pk代表主键
        book = Book.objects.get(pk=id)
    except Exception as e:
        return HttpResponse('没有主角信息')
    temp = loader.get_template('book/detail.html')
    # 为防止book不存在在开头为book设置为None
    result = temp.render({'book':book})
    return HttpResponse(result)

def deletebook(request,id):
    Book.objects.get(pk=id).delete()
    return HttpResponseRedirect('/book/list/')
def deletehero(request,id):
    hero = Hero.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    return HttpResponseRedirect('/book/detail/%s/'%(bookid,))