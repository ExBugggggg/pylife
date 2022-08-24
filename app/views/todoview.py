from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

class todo:

    def index(request):
        data = {
            'ping': 'todo'
        }
        return HttpResponse(json.dumps(data))