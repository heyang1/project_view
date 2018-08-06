from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

# Create your views here.

def index(request):

    return HttpResponse(content="Hello Django!", charset='utf-8',
                        status=200, reason='Success',
                        content_type="text/html;charset=utf-8")


def rs(request):
    return HttpResponse("重定向的页面")


def test_rs(request):
    return HttpResponseRedirect(redirect_to='/response/rs/')


def return_json(request):
    """测试json"""
    return JsonResponse({'code': 200, 'message':'success'})


def template(request):

    return render(request, 'test_render.html', {'msg': 'abc'})
