from django.db import models
# 导入系统名字
from django.contrib.auth.models import User
# Create your models here.
# 博客分为几个模块
# 标签
class Tag(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = '标签'
        verbose_name_plural = verbose_name
# 分类
class Classify(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = '分类'
        verbose_name_plural = verbose_name
# 正文
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    # 默认阅读数为0
    views = models.PositiveIntegerField(default=0)
    # 外键
    classify = models.ForeignKey(Classify,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    auther = models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = '文章'
        verbose_name_plural = verbose_name

