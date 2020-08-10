from rest_framework.views import APIView, Response
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
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


def chk_token(token):
    if token is None:
        return Response({
            'info': '用户未登录',
            'code': 403
        }, status=403)
    u = UserToken.objects.filter(token=token)
    if len(u) <= 0:
        # token无效
        return Response({
            'info': '无效用户',
            'code': 403
        }, status=403)
    return u.get().user_id


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
            res = Response(res)
            res.set_cookie('username', username, 3600, path='/')
            return res
        else:
            return Response({
                'info': '密码错误',
                'code': 403
            }, status=403)


class UserRegister(APIView):
    """用户注册视图"""
    authentication_classes = []

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
                password=make_password(pwd),
                email=email,
                phone_num=phone_num
            )
            res = {'info': 'success', 'code': 200, 'data': UserInfoSer(u).data}
            res = Response(res)
            res.set_cookie('username', username, 3600, path='/')
            return res

        return Response({
            'info': '用户名已注册',
            'code': 403
        }, status=403)


class UserChkOldPwd(APIView):
    def post(self, request):
        token = request.META.get('HTTP_TOKEN')
        print(token)
        user_id = chk_token(token)
        old_pwd = request.POST.get('old_password')
        u = User.objects.get(pk=user_id)
        if u.check_pwd(old_pwd):
            return Response({
                'info': 'success',
                'code': 200,
                'data': UserInfoSer(u).data
            }, status=200)
        else:
            return Response({
                'info': '旧密码错误',
                'code': 403
            }, status=403)


class UserInfo(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        print(token)
        user_id = chk_token(token)
        res = User.objects.get(pk=user_id)
        return Response({
                'info': 'success',
                'code': 200,
                'data': UserInfoSer(res).data
            }, status=200)

    def post(self, request):
        token = request.META.get('HTTP_TOKEN')
        print(token)
        user_id = chk_token(token)
        pwd = request.POST.get('new_password')
        email = request.POST.get('email')
        phone_num = request.POST.get('phone_num')
        print(pwd)
        print(email)
        print(phone_num)
        if not all([pwd, email, phone_num]):
            return Response({
                'info': '参数不完整',
                'code': 400
            }, status=400)
        u = User.objects.get(pk=user_id)
        if u.check_pwd(pwd):
            return Response({
                'info': '新密码不能与旧密码一样',
                'code': 400
            }, status=400)
        u.password = make_password(pwd)
        u.email = email
        u.phone_num = phone_num
        u.save()
        return Response({
            'info': 'success',
            'code': 200,
            'data': UserInfoSer(u).data
        }, status=200)


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






