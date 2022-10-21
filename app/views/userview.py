from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import authenticate
from django.conf import settings

from app.utils.login import LoginRequired
from app.utils.response import HttpJsonResponse
from app.utils.redis import RedisConnection
from app.utils.token import HmacSHA1
# Create your views here.
import json
import uuid
import time

class user:

    __login_expire_time = 60 * 60 *24 * 7

    """
    Todo: 添加token到redis中用于验证
    """
    @require_POST
    def login(request):
        request_data = json.loads(request.body)
        user = authenticate(username=request_data['username'], password=request_data['password'])
        if user:
            # cache = RedisConnection.connect()
            token = HmacSHA1(settings.SECRET_KEY, str(user) + ' ' + str(int(time.time())))
            # cache.set()
            return HttpJsonResponse(data=user.get_username() + '|' + str(user.id) + '|' + token)
        else:
            return HttpJsonResponse(code=500, message='login failed.')

    """
    Todo: 删除redis中的缓存
    """
    @require_GET
    @LoginRequired
    def logout(request):
        data = {
            'ping': 'user logout'
        }
        return HttpResponse(json.dumps(data))

    """登陆失败时跳转

    """
    @require_GET
    def failed(request):
        data = {
            'code': 500,
            'message': 'No permission to access, login first.',
            'data': []
        }
        return HttpJsonResponse(data)