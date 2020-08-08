from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('userinfo/', views.UserInfoList.as_view(), name='userList'),
]