from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.views import APIView, Response
from django.contrib.auth.hashers import make_password
from myapp.models import User, File, UserBrowseFile
from myapp.serializers import UserInfoSer
from myapp.views import chk_token


class BrowseFile(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        file_id = request.GET.get('file_id')
        print(token)
        print(file_id)
        user_id = chk_token(token)
        u = User.objects.get(pk=user_id)
        f = File.objects.get(pk=file_id)

        ubf = UserBrowseFile.objects.update_or_create(person=u, file=f)[0]
        print(ubf)
        return Response({
            'info': 'success',
            'code': 200,
            'data': {
                'file_id': ubf.file_id,
                'person_id': ubf.person_id,
                'modified_time': ubf.last_modified
            }
        }, status=200)
