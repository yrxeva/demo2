from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse('首页')
def detail(request,id):
    return HttpResponse('detail %s' %id)
