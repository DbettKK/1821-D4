from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    """
    用户类
    """
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=128, verbose_name='password')
    phone_num = models.CharField(max_length=11, verbose_name='电话')
    email = models.EmailField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def set_pwd(self, password):
        self.password = make_password(password)
        return None

    def check_pwd(self, password):
        return check_password(password, self.password)


class UserToken(models.Model):
    """用户token表"""
    user = models.OneToOneField('User', on_delete=models.CASCADE)  # 与用户一对一关系
    token = models.CharField(max_length=64, verbose_name='token')
