from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from app.utils.response import HttpJsonResponse

class category:
    """类别类
    
    文章类别
    """

    @require_GET
    def get(request):
        """获取类别
        
        Args:
            request: 请求获取类别
        """
        data = {
            'message': 'test',
            'data': [],
            'code': 200,
            'ping': 'category get'
        }
        return HttpJsonResponse(data)

    @require_POST
    def add(request):
        """添加类别
        
        Args:
            request: 添加类别
        """
        data = {
            'message': 'test',
            'data': [],
            'code': 200,
            'ping': 'category add'
        }
        return HttpJsonResponse(data)

    @require_POST
    def edit(request):
        """添加类别
        
        Args:
            request: 添加类别
        """
        data = {
            'message': 'test',
            'data': [],
            'code': 200,
            'ping': 'category edit'
        }
        return HttpJsonResponse(data)
