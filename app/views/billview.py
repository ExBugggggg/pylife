from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

class bill:

    def index(request):
        data = {
            'ping': 'bill'
        }
        return HttpResponse(json.dumps(data))