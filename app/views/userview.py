from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
# Create your views here.
import json

class user:

    @require_POST
    def login(request):
        data = {
            'ping': 'user'
        }
        return HttpResponse(json.dumps(data))

    @require_GET
    def logout(request):
        data = {
            'ping': 'user logout'
        }
        return HttpResponse(json.dumps(data))