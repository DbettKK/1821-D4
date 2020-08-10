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


# 放后面防止循环导入发生冲突
from .view.user import UserRegister, UserLogin
from .view.userinfo import UserChkOldPwd, UserInfo





