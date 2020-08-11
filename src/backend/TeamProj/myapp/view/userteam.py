from rest_framework.views import APIView, Response
from myapp.models import User, File, UserBrowseFile, UserKeptFile, Team
from myapp.views import chk_token


class createTeam(APIView):
    def post(self, request):
        token = request.META.get('HTTP_TOKEN')
        name = request.POST.get('team_name')
        if name is None:
            return Response({
                'info': '参数不完整',
                'code': 400,
            }, status=400)
        print(token)
        user_id = chk_token(token)
        if isinstance(user_id, Response):
            return user_id
        u = User.objects.get(pk=user_id)
        t = Team.objects.create(
            creator=u,
            name=name
        )
        t = Team.objects.filter(pk=t.pk).values()
        return Response({
            'info': 'success',
            'code': 200,
            'data': t
        }, status=200)