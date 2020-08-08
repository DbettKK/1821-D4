from rest_framework.views import APIView, Response
from rest_framework import generics
from .models import User, UserToken
from .serializers import UserInfoSer, CreateUserSer
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
        user = User.objects.get(username=username)
        if user.check_pwd(pwd):
            # 登录成功后生成token
            token = md5(username)
            UserToken.objects.update_or_create(user=user, defaults={'token': token})
            res = {'info': 'success', 'token': token, 'code': 200, 'data': UserInfoSer(user).data}
            return Response(res)
        else:
            return Response({
                'info': '用户名或密码错误',
                'code': 401
            })


class UserRegister(generics.CreateAPIView):
    """用户注册视图"""
    authentication_classes = []
    # 用户注册不需要认证
    serializer_class = CreateUserSer


class UserInfoList(generics.ListAPIView):
    """用户详情页视图"""
    queryset = User.objects.all()
    serializer_class = UserInfoSer  # id, name, email, phone_num
