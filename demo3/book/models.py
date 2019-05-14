from django.db import models

# Create your models here.
class Book(models.Model):
    # 创建标题属性
    title = models.CharField(max_length=30)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
class Hero(models.Model):
    name = models.CharField(max_length=30)
    skill = models.CharField(max_length=100)
    bookid = models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.name