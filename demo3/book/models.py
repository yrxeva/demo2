from django.db import models

# Create your models here.
class Book(models.Model):
    # 创建标题属性
    title = models.CharField(max_length=30,verbose_name='标题')
    pub_date = models.DateField(auto_now_add=True,verbose_name='时间')

    def __str__(self):
        return self.title

# GENDER = ((1,'男'),(2,'女'))
class Hero(models.Model):
    name = models.CharField(max_length=30,verbose_name='名字')

    # 创建性别下拉框
    # gender = models.CharField(max_length=30,choices=GENDER)


    skill = models.CharField(max_length=100,verbose_name='技能')
    bookid = models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name='书')
    def __str__(self):
        return self.name