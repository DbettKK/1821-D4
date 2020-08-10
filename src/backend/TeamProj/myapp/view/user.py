
from django.contrib.auth.hashers import make_password, check_password
from myapp.models import User, UserToken, EmailRecord
from myapp.serializers import UserInfoSer
from myapp.views import md5
from rest_framework.views import APIView, Response
from rest_framework import generics
import hashlib
import time
from django.conf import settings
from django.core.mail import send_mail
from random import Random 
import datetime

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

class GetBackPassword(APIView):
    '找回密码类'
    authentication_classes = []
    def post(self, request):
        username = request.POST.get('username')
        email= request.POST.get('email')
        pwd_new = request.POST.get('password_new')
        code = request.POST.get('code')
        if not all([username, pwd_new]):
            return Response({
                'info': '参数不完整',
                'code': 400
            })
        current_time = datetime.datetime.now()
        if EmailRecord.objects.filter(email=email,code=code,exprie_time_gte=current_time, send_choice='findpassword'):
            user=User.objects.filter(username=username)
            user.password = pwd_new
            user.save()
            return Response(
                {
                    'info':'找回成功',
                    'code': 200
                },
                status=200
            )
        else:
            return Response(
                {
                    'info':'密码错误',
                    'code':400
                },
                status=400
            )
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
        code=request.POST.get('code')
        if not all([username, pwd, pwd2, email, phone_num, code]):
            return Response({
                'info': '参数不完整',
                'code': 400
            },status=400)
        current_time = datetime.datetime.now()
        if EmailRecord.objects.filter(email=email,code=code,exprie_time_gte=current_time, send_choice='register'):
            u = User.objects.create(
                username=username,
                password=pwd,
                email=email,
                phone_num=phone_num,
                isActive=True
            )
            res = {'info': 'success', 'code': 200, 'data': UserInfoSer(u).data}
            res=Response(res)
            res.set_cookie('username',username,3600,path='/')
            return res
        else:
            return Response({
                'info':'验证码错误',
                'code':403
            },status=403)

class UserInfoList(generics.ListAPIView):
    """用户详情页视图"""
    queryset = User.objects.all()
    serializer_class = UserInfoSer  # id, name, email, phone_num

# 生成随机字符串
def random_str(randomlength=8):
    """
    随机字符串
    :param randomlength: 字符串长度
    :return: String 类型字符串
    """
    retstr = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        retstr += chars[random.randint(0, length)]
    return retstr

class TestEmail2(APIView):
    '''找回密码的邮箱api'''
    authentication_classes = []
    def post(self, request):
        # 生成随机数码
        code=random_str(16)
        # 主题
        subject = '金刚石文档欢迎注册'
        # message表示发送的纯文本，
        # 如果需要发送带样式的，则使用html_message
        # 用html_message时，message为空字符串
        message = ''
        # 收件人列表
        receiver = [request.POST.get('email')]
        # 需要发送的带样式内容
        html_message = '<h1>金刚石文档提醒：您在修改账号密码</h1>' \
                       '您本次修改的验证码为：{0},验证码将在5分钟后失效<br>'.format(code) \
 
        # 发送者
        sender = settings.EMAIL_FROM
        #　发送邮件
        send_mail(subject, message, sender, receiver, html_message=html_message)
        time_delta=datetime.datetime.now()+datetime.timedelta(minutes=5)
        email_record = EmailRecord.objects.create(email=request.POST.get('email'), code=code, exprie_time=time_delta, send_choice='findpassword')
        return Response({
            'info': True
        })

class TestEmail(APIView):
    '''注册的邮箱api'''
    authentication_classes = []
    def post(self, request):
        # 生成随机数码
        code=random_str(16)
        # 主题
        subject = '金刚石文档欢迎注册'
        # message表示发送的纯文本，
        # 如果需要发送带样式的，则使用html_message
        # 用html_message时，message为空字符串
        message = ''
        # 收件人列表
        receiver = [request.POST.get('email')]
        # 需要发送的带样式内容
        html_message = '<h1>欢迎注册金刚石文档账号</h1>' \
                       '您本次注册的验证码为：{0},验证码将在5分钟后失效<br>'.format(code) \
 
        # 发送者
        sender = settings.EMAIL_FROM
        #　发送邮件
        send_mail(subject, message, sender, receiver, html_message=html_message)
        time_delta=datetime.datetime.now()+datetime.timedelta(minutes=5)
        email_record = EmailRecord.objects.create(email=request.POST.get('email'), code=code, exprie_time=time_delta, send_choice='register')
        return Response({
            'info': True
        })
