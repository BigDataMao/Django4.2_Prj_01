from django.db import models

# Create your models here.
"""
数据库生成命令:
python manage.py makemigrations
python manage.py migrate
"""


class Users(models.Model):
    # 定义用户表
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=32)

    # 定义返回值
    def __str__(self):
        return self.username
