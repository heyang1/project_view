from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'jsonp.html')

import json
def callback(request):
    callback_name = request.GET.get('callback')

    result = {'username': '梦克', 'age': 18}
    result_str = json.dumps(result)
    if callback_name is not None:
        result_str = "%s(%s)" % (callback_name, result_str)
        return HttpResponse(result_str)
    else:
        return HttpResponse(result_str,
                            content_type='application/json;charset=utf-8')
