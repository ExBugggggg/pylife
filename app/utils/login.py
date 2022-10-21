from functools import wraps
from django.http import HttpResponseRedirect
"""装饰器

Todo: 把写死的token改成从redis中获取
必须登录装饰器
"""
def LoginRequired(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # 判断是否登陆成功写入redis
        if request.META.get('HTTP_AUTHORIZATION') == 'Bearer ' + 'cookies|1|266abcaa3f30fa467a7175d2d49d33d37b51413a':
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/user/failed')
    return wrapper