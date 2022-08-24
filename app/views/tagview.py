from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

class tag:

    def login(request):
        data = {
            'ping': 'tag'
        }
        return HttpResponse(json.dumps(data))