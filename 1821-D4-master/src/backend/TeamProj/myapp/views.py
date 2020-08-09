from rest_framework.views import APIView, Response
from django.http import HttpResponseRedirect
from rest_framework import generics
from .models import User, UserToken
from .serializers import UserInfoSer,CreateUserSer
import hashlib
import time


def md5(user):
    """md5 加密token"""
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


class UserLogin(APIView):
    '用户登录视图类'
    authentication_classes = []

    # 登录不需要认证

    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(username)
        print(pwd)

        if not all([username, pwd]):
            return Response({
                'info': '参数不完整',
                'code': 400
            })
        try:
            user = User.objects.get(username=username)
        except:
            return Response({
                'info': '用户名不存在',
                'code': 401
            })
        if user.check_pwd(pwd):
            # 登录成功后生成token
            token = md5(username)
            UserToken.objects.update_or_create(user=user, defaults={'token': token})
            res = {'info': 'success', 'token': token, 'code': 200, 'data': UserInfoSer(user).data}
            '''
            res=Response(res)
            res.set_cookie('username',username,3600)
            '''
            return res
        else:
            return Response({
                'info': '密码错误',
                'code': 401
            })


class UserRegister(generics.ListCreateAPIView):
    """用户注册视图"""
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = CreateUserSer
    def post(self, request):
        '''
        关于COOKIES的验证
        if 'username' in request.COOKIES:
            return HttpResponseRedirect('/myapp/userinfo')
        '''
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone_num = request.POST.get('phone_num')

        if not all([username, pwd, pwd2, email, phone_num]):
            return Response({
                'info': '参数不完整',
                'code': 400
            })

        if pwd != pwd2:
            return Response({
                'info': '两次密码不一致',
                'code': 400
            })
        if (User.objects.filter(username=username).count()!=0):
            return Response({
                'info': '用户名已被注册',
                'code': 400
            })
        if (User.objects.filter(email=email).count()!=0):
            return Response({
                'info': '邮箱已被注册',
                'code': 400
            })
        if (User.objects.filter(phone_num=phone_num).count()!=0):
            return Response({
                'info': '电话已被注册',
                'code': 400
            })
        u = User.objects.create(
            username=username,
            password=pwd,
            email=email,
            phone_num=phone_num
        )
        res = {'info': 'success', 'code': 200, 'data': UserInfoSer(u).data}
        res=Response(res)
        res.set_cookie('username',username,3600,path='/')
        return res


class UserInfoList(generics.ListAPIView):
    """用户详情页视图"""
    queryset = User.objects.all()
    serializer_class = UserInfoSer  # id, name, email, phone_num

class Index(generics.ListAPIView):
    """假设是个主页"""
    serializer_class = UserInfoSer
    def get_queryset(self):
        if 'username' in self.request.COOKIES:
            return User.objects.filter(username=self.request.COOKIES.get('username'))
        else:
            return None
        