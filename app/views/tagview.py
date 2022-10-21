from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST

from app.utils.tools import generate_random_string
from app.models.tagmodels import tag as Tag
from app.utils.response import HttpJsonResponse
from app.utils.login import LoginRequired
# Create your views here.
import json

class tag:

    @require_POST
    @LoginRequired
    def add(request):
        request_data = json.loads(request.body)
        name = request_data['name']
        description = request_data['description']
        tagid = 't' + generate_random_string(4)

        if Tag.objects.filter(tagid = tagid):
            return HttpJsonResponse(code=500, message='no message')
        else:
            return HttpJsonResponse(code=200, message='OK')
        