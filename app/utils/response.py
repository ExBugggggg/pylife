from django.http import HttpResponse
# Create your views here.
import json

RESPONSE_CODE = {
    200: 'OK',
    500: 'Failed',
    1000: 'Use correct number as response code.'
}

def HttpJsonResponse(args):
    if 'code' not in args.keys() or 'message' not in args.keys() or 'data' not in args.keys():
        return HttpResponse(json.dumps({
            'code': 500,
            'message': RESPONSE_CODE[500],
            'data': []
        }))
    if args['code'] not in RESPONSE_CODE.keys():
        return HttpResponse(json.dumps({
            'code': 1000,
            'message': RESPONSE_CODE[1000],
            'data': []
        }))
    return HttpResponse(json.dumps(args))
