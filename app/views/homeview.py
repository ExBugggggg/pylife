from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST

from app.utils.login import LoginRequired
from app.utils.response import HttpJsonResponse
# Create your views here.
import json

class home:

    @require_GET
    @LoginRequired
    def index(request):
        data = {
            'ping': 'home'
        }
        return HttpResponse(json.dumps(data))

    def add(request):
        request_data = json.loads(request.body)
        pass