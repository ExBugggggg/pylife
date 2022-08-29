from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from app.utils.response import HttpJsonResponse
# Create your views here.
import json

class bill:
    """账单类
    
    接收和响应账单相关的数据
    """

    @require_GET
    def get(request):
        """处理bill的get相关请求逻辑
        
        Args:
            request: 请求
        """
        data = {
            'message': 'test',
            'data': [],
            'code': 200,
            'ping': 'bill get'
        }
        return HttpJsonResponse(data)

    @require_POST
    def add(request):
        """处理bill的add相关请求逻辑

        Args:
            request: 请求
        """
        data = {
            'ping': 'bill add'
        }
        return HttpResponse(json.dumps(data))

    @require_POST
    def edit(request):
        """处理bill的edit相关请求逻辑

        Args:
            request: 请求
        """
        data = {
            'ping': 'bill edit'
        }
        return HttpResponse(json.dumps(data))