from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

# Create your views here.


def print_request(request):
    """打印request对象的属性"""
    print(request.POST) # 获取POST请求的参数，其实就是请求体中的数据
    print(request.GET) # 获取Get请求的参数，其实就是QueryString数据
    print(request.method) # 打印请求方法
    print(request.META) # request元信息，是个字典
    print(request.path) # 获取请求路径(url)，包含请求host和port以及请求的query string
    print(request.body) # 获取请求体中的数据，字节
    print(request.get_full_path()) # 获取请求路径：去除host和port
    print(request.get_full_path_info()) # 获取请求路径信息
    print(request.is_ajax()) # 是否是XMLHTTPRequest请求(即ajax请求)， bool

    return HttpResponse('打印HttpRequest对象')


def index(request):
    return render(request, "index.html")


# 接收一键一值
@require_GET
def handler_one(request):
    # 接收参数
    a = request.GET.get('a') # 获取一个值
    b = request.GET.get('b')
    return render(request, "handler_one.html", context={'a':a, 'b':b})


@require_GET
def handler_multi(request):
    # 接收参数
    a = request.GET.getlist('a', 0)
    b = request.GET.get('b', 1)
    return render(request, "handler_multi.html", context={'a': a, 'b': b})