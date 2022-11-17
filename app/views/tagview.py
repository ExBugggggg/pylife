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
        tagid = 'T' + generate_random_string(4)

        if Tag.objects.filter(tagid=tagid):
            return HttpJsonResponse(code=500, message='no message')
        else:
            tag = Tag(name=name, description=description, tagid=tagid)
            tag.save()
            return HttpJsonResponse(code=200, message='OK')

    @require_GET
    @LoginRequired
    def index(request):
        request_data = json.loads(request_data)
        search_name = ''
        if request_data['action'] == 'search':
            search_name = request_data['search_name']
        

    @require_POST
    @LoginRequired
    def edit(request):
        request_data = json.loads(request.body)
        tagid = request_data['tagid']
        name = request_data['name']
        description = request_data['description']
        Tag.objects.filter(tagid=tagid).update(
            name=name,
            description=description
        )
        return HttpJsonResponse(code=200, message='OK')
