from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from app.utils.response import HttpJsonResponse
# Create your views here.
import json

class bill:

    @require_GET
    def get(request):
        data = {
            'message': 'test',
            'data': [],
            'code': 200,
            'ping': 'bill get'
        }
        return HttpJsonResponse(data)

    @require_POST
    def add(request):
        data = {
            'ping': 'bill add'
        }
        return HttpResponse(json.dumps(data))

    @require_POST
    def edit(request):
        data = {
            'ping': 'bill edit'
        }
        return HttpResponse(json.dumps(data))