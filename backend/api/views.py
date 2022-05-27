import imp
from django.http import JsonResponse

def home(request, *args, **kwwargs):
    return JsonResponse({
        "message": "Hello wolrd !"
    })

