from email import message_from_binary_file
from django.http import HttpResponse
# Create your views here.
import json

RESPONSE_CODE = {
    200: 'OK',
    500: 'Failed',
    1000: 'Use correct number as response code.'
}

OPTIONS_CODE = [
    200,
    500
]

def HttpJsonResponse(code: int = 200, message: str = 'OK', data: any = [], options: any = {}):
    """响应JSON格式数据

    这个函数是用于返回JSON格式的数据。options参数为自定义参数，当使用该参数后，则会按开发者自定的参数
    格式返回数据。如果返回码为OPTIONS_CODE中的返回码，则可以使用自定义的message返回消息，否则强制使用
    RESPONSE_CODE中定义的返回消息。

    Args:
        code(int): 返回给客户端的返回码。非必须，默认值为200。
        message(str): 返回给客户端的消息。非必须，默认值为OK。
        data(any): 返回给客户端的数据。非必须，默认值为[]。传入的参数需要可以被序列化成JSON字符串。
        options(any)：返回给客户端的数据。非必须，默认值为{}。
    
    Examples:
        不使用自定义数据返回数据。
        HttpJsonResponse(code=200, message='this is a test message', data={'ping':'pong'})
        使用自定义数据返回数据。
        HttpJsonResponse(options={'mycode': 3001, 'mymessage': 'a message', 'data'={'hello': 'world'}})
    """
    if options != {}:
        return HttpResponse(json.dumps(options))
    if code not in RESPONSE_CODE.keys():
        code = 1000
        message = RESPONSE_CODE[code]
    elif code not in OPTIONS_CODE:
        message = RESPONSE_CODE[code]
    
    return HttpResponse(json.dumps({
        'code': code,
        'message': message,
        'data': data
    }))
