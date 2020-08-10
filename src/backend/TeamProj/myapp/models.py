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
    isActive = models.BooleanField()

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


# 标题、内容、文档基础信息、创建时间、修改时间、权限、作者信息(和user一对多)、评论(和user多对多)、分享连接(可通过id)
class File(models.Model):
    """文档类"""
    permissions = (
        (1, '可查看'), (2, '可评论'), (3, '可修改'), (4, '可分享')
    )
    team_permissions = (
        (1, '成员可查看'), (2, '成员可评论'), (3, '成员可修改'), (4, '成员可分享')
    )
    file_name = models.CharField(max_length=64, verbose_name='文档名')
    file_title = models.CharField(max_length=64, verbose_name='文档标题')
    file_content = models.CharField(max_length=128, verbose_name='文档内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='文档创建时间')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='文档最后一次修改时间')
    permission = models.IntegerField(choices=permissions, verbose_name='总权限')
    team_permission = models.IntegerField(choices=team_permissions, verbose_name='团队内部权限')
    creator = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='myfile',
        verbose_name='文档创建者'
    )
    comments = models.ManyToManyField(
        'User',
        through='Comment',
        through_fields=('file', 'person'),
        verbose_name='评论'
    )
    share = models.CharField(max_length=64, verbose_name='分享')


class Comment(models.Model):
    person = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        verbose_name='评论人'
    )
    file = models.ForeignKey(
        'File',
        on_delete=models.CASCADE,
        verbose_name='被评论的文档'
    )
    content = models.CharField(max_length=128, verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论创建时间')

