import imp
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    data = {}
    body = request.body
    
    print(body)

    try:
        data = json.loads(body)
    except:
        pass

    # print(data.keys())  # -> show params names sended in json
    print(request.headers)
    data['content_type'] = request.content_type
    data['headers'] = dict(request.headers)
    data['params'] = request.GET
    data['name'] = request.GET['name']

    return JsonResponse(data)

