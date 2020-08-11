from rest_framework.views import APIView, Response
from myapp.models import User, File, UserBrowseFile, UserKeptFile, Team, TeamMember
from myapp.views import chk_token


class CreateTeam(APIView):
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


class JoinTeam(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        team_id = request.GET.get('team_id')
        if team_id is None:
            return Response({
                'info': '参数不完整',
                'code': 400,
            }, status=400)
        user_id = chk_token(token)
        if isinstance(user_id, Response):
            return user_id
        u = User.objects.get(pk=user_id)
        t = Team.objects.get(pk=team_id)
        if TeamMember.objects.filter(team=t, member=u):
            return Response({
                'info': '你已经加入该团队',
                'code': 403,
            }, status=403)
        TeamMember.objects.create(team=t, member=u)
        tm = TeamMember.objects.filter(team=t, member=u).values()
        return Response({
            'info': 'success',
            'code': 200,
            'data': tm
        }, status=200)


class ExitTeam(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        team_id = request.GET.get('team_id')
        if team_id is None:
            return Response({
                'info': '参数不完整',
                'code': 400,
            }, status=400)
        user_id = chk_token(token)
        if isinstance(user_id, Response):
            return user_id
        u = User.objects.get(pk=user_id)
        t = Team.objects.get(pk=team_id)
        tm = TeamMember.objects.filter(team=t, member=u)
        if len(tm) <= 0:
            return Response({
                'info': '未加入该团队 无法退出',
                'code': 403,
            }, status=403)
        t_id = tm.get().team.pk
        tm.get().delete()
        return Response({
            'info': 'success',
            'code': 200,
            'data': [{'team_id': t_id}]
        }, status=200)



