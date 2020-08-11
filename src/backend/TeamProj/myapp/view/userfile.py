from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.views import APIView, Response
from django.contrib.auth.hashers import make_password
from myapp.models import User, File, UserBrowseFile, UserKeptFile
from myapp.serializers import UserInfoSer
from myapp.views import chk_token


def chk_file_id(file_id):
    try:
        f = File.objects.get(pk=file_id)
    except:
        return Response({
            'info': '文件不存在',
            'code': 403,
        }, status=403)
    return f


class BrowseFile(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        file_id = request.GET.get('file_id')
        print(token)
        print(file_id)
        user_id = chk_token(token)
        if isinstance(user_id, Response):
            return user_id
        u = User.objects.get(pk=user_id)

        f = chk_file_id(file_id)
        if isinstance(f, Response):
            return f

        UserBrowseFile.objects.update_or_create(person=u, file=f)
        ubf = UserBrowseFile.objects.filter(person=u, file=f).values()
        print(ubf)
        return Response({
            'info': 'success',
            'code': 200,
            'data': ubf
        }, status=200)


class Favorites(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        file_id = request.GET.get('file_id')
        print(token)
        print(file_id)

        user_id = chk_token(token)
        if isinstance(user_id, Response):
            return user_id
        u = User.objects.get(pk=user_id)

        f = chk_file_id(file_id)
        if isinstance(f, Response):
            return f
        if len(UserKeptFile.objects.filter(person=u, file=f)) > 0:
            return Response({
                'info': '你已经收藏过该文档了',
                'code': 403,
            }, status=403)

        UserKeptFile.objects.update_or_create(person=u, file=f)
        ukf = UserKeptFile.objects.filter(person=u, file=f).values()
        print(ukf)
        return Response({
            'info': 'success',
            'code': 200,
            'data': ukf
        }, status=200)


class CancelFavorite(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        file_id = request.GET.get('file_id')
        print(token)
        print(file_id)
        user_id = chk_token(token)
        user_id = chk_token(token)
        if isinstance(user_id, Response):
            return user_id
        u = User.objects.get(pk=user_id)

        f = chk_file_id(file_id)
        if isinstance(f, Response):
            return f
        ukf = UserKeptFile.objects.filter(person=u, file=f)
        print(ukf)
        if len(ukf) > 0:
            file_id = ukf.get().file_id
            ukf.get().delete()
            return Response({
                'info': 'success',
                'code': 200,
                'data': [{'file_id': file_id}]
            }, status=200)

        return Response({
            'info': '你未收藏过该文档, 无法删除',
            'code': 403,
        }, status=403)
