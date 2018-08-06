from django.shortcuts import render
from django.http import HttpResponse,QueryDict
from employee.models import SaleGrade
from django.views.decorators.http import require_GET,require_http_methods

# Create your views here.

def index(request):
    """跳转到页面"""
    return render(request, "index.html")


def test1(request):
    """ajax请求地址"""
    return HttpResponse("这是后台返回的文本。。。")


import json
def test2(request):
    """ajax请求地址"""
    r = {'abc': '这是json文本内容'}
    # return HttpResponse(content='{"abc":"这是json文本内容。。"}',
    #                     content_type="application/json;charset=utf-8")
    return HttpResponse(content=json.dumps(r),
                        content_type="application/json;charset=utf-8")


# 通过主键获取salegrade的数据
@require_GET
def get_salegrade(request):
    pk = request.GET.get('id')
    # 查询数据库
    salegrade = {}
    try:
        salegrade = SaleGrade.objects.values('grade', 'lowsal', 'higsal') \
            .get(pk=pk)
    except Exception as e:
        pass
    # 返回结果
    # r = {'grade': 1, 'lowsal': 2000, 'higsal': 3000}
    return HttpResponse(content=json.dumps(salegrade),
                        content_type="application/json;charset=utf-8")

@require_http_methods('put')
def update(request):
    params = request.body
    print(params)
    params = params.decode(encoding='utf-8')
    #params = str(params,encoding = 'utf-8')
    query_dict =QueryDict(params)
    print(query_dict)
    print('获取手机号：',query_dict.get('phone'))
    print('获取Email:',query_dict.get('email'))
    context = {'code': 200, 'message': 'Success!'}
    return HttpResponse(content=json.dumps(context),
                        content_type="application/json;charset=utf-8")

@require_http_methods("PUT")
def update_json_params(request):
    params = request.body # 返回的是byte
    print(params)
    # 把byte转成字符串
    # params = params.decode(encoding='utf-8')
    params = str(params, encoding='utf-8')
    # {"phone":"124555555555","email":"13455666666"}
    param_dict = json.loads(params, encoding='utf-8') # 是反序列化成字典
    print(param_dict)
    print('获取手机号：', param_dict.get('phone'))
    print('获取Email：', param_dict.get('email'))
    context = {'code':200, 'message': 'Success!'}
    return HttpResponse(content=json.dumps(context),
                        content_type="application/json;charset=utf-8")






@require_http_methods("DELETE")
def delete(request):
    """解析delete的参数"""
    pass
