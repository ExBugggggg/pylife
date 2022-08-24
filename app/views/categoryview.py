from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

class category:

    def login(request):
        data = {
            'ping': 'category'
        }
        return HttpResponse(json.dumps(data))