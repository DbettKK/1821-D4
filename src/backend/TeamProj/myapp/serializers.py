from rest_framework import serializers
from .models import User


# class CreateUserSer(serializers.ModelSerializer):
#     """新增用户序列化器"""
#     password2 = serializers.CharField(max_length=128, write_only=True)
#
#     def validate(self, attrs):
#         password = attrs['password']
#         password2 = attrs['password2']
#         if password != password2:
#             raise serializers.ValidationError('两次密码不一致，请重新输入！')
#         return attrs
#
#     def create(self, validated_data):
#         del validated_data['password2']
#         user = super().create(validated_data)
#         user.set_pwd(validated_data['password'])
#         user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email', 'phone_num')


class UserInfoSer(serializers.ModelSerializer):
    """用户详情信息序列化器"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_num')
