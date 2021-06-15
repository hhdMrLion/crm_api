import json

from django import http
from django.contrib.auth import logout
from django.shortcuts import render
from django.views import View

from account import serializers
from account.forms import LoginForm
from utils.response import BadRequestJsonResponse, MethodNotAllowedJsonResponse, UnauthorizedJsonResponse


def user_login(request):
    """ 用户登录接口 """
    if request.method == 'POST':
        # 用户表单验证
        form = LoginForm(request.POST)
        # 验证通过，执行登录
        if form.is_valid():
            user = form.do_login(request)
            data = {
                'user': serializers.UserSerializers(user).to_dict()
            }
            return http.JsonResponse(data)
        else:
            err = json.loads(form.errors.as_json())
            return BadRequestJsonResponse(err)
    else:
        # 请求不被允许
        return MethodNotAllowedJsonResponse()


def user_logout(request):
    """ 用户推出接口 """
    logout(request)
    return http.HttpResponse('退出登录', status=201)


class UserDetailView(View):
    """ 用户详细接口 """

    def get(self, request):
        # 获取用户信息
        user = request.user
        # 如果是游客用户，返回401状态码
        if not user.is_authenticated:
            return UnauthorizedJsonResponse()
        else:
            # 返回信息
            data = {
                'user': serializers.UserSerializers(user).to_dict()
            }
            return http.JsonResponse(data)