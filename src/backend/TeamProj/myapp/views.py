from rest_framework.views import APIView, Response
from rest_framework import generics
from .models import User, UserToken
from .serializers import UserInfoSer
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
        print(request.POST)
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(username)
        print(pwd)

        if not all([username, pwd]):
            return Response({
                'info': '参数不完整',
                'code': 400
            }, status=400)
        try:
            user = User.objects.get(username=username)
        except:
            return Response({
                'info': '用户名不存在',
                'code': 403
            }, status=403)
        if user.check_pwd(pwd):
            # 登录成功后生成token
            token = md5(username)
            UserToken.objects.update_or_create(user=user, defaults={'token': token})
            res = {'info': 'success', 'token': token, 'code': 200, 'data': UserInfoSer(user).data}
            return Response(res, status=200)
        else:
            return Response({
                'info': '密码错误',
                'code': 403
            }, status=403)


class UserRegister(APIView):
    """用户注册视图"""
    authentication_classes = []

    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone_num = request.POST.get('phone_num')

        if not all([username, pwd, pwd2, email, phone_num]):
            return Response({
                'info': '参数不完整',
                'code': 400
            }, status=400)
        try:
            User.objects.get(username=username)
        except:
            if pwd != pwd2:
                return Response({
                    'info': '两次密码不一致',
                    'code': 403
                }, status=403)
            u = User.objects.create(
                username=username,
                password=pwd,
                email=email,
                phone_num=phone_num
            )
            res = {'info': 'success', 'code': 200, 'data': UserInfoSer(u).data}
            return Response(res, status=200)

        return Response({
            'info': '用户名已注册',
            'code': 403
        }, status=403)


class UserInfoList(generics.ListAPIView):
    """用户详情页视图"""
    queryset = User.objects.all()
    serializer_class = UserInfoSer  # id, name, email, phone_num
