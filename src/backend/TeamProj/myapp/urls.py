from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('user/list/', views.UserInfoList.as_view(), name='userList'),
    path('user/info/', views.UserInfo.as_view(), name='userinfo'),
    path('user/modify/', views.UserChkOldPwd.as_view()),
    path('', views.Index.as_view(), name='userList'),
]