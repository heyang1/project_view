from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import datetime
def set_cookie(request):
    """设置cookie"""
    response = HttpResponse("测试设置cookie")

    t = request.GET.get('type', 1) # 返回的是字符串
    t = int(t)

    if t == 1:
        # 这样设置，默认cookie是会话cookie，当浏览器关闭时cookie失效
        # 默认域名是当前访问的域名， 默认path是根路径即所有url都可以访问
        response.set_cookie("normal", '上海尚学堂'.encode(encoding='utf-8'))
    elif t == 2:
        """设置过期时间，max-age单位是秒"""
        response.set_cookie('max_age_cookie', '1234565', max_age=15)
    elif t == 3:
        """设置过期时间，expires是到什么时间过期，
        如果设置了expires那么max_age就会失效"""
        response.set_cookie("expire_cookie", '123456', max_age=15,
                            expires=datetime.datetime(2018, 7, 31, 14, 28, 59))
    elif t == 4:
        """这是path，就只能在这个url下访问，默认是根路径"""
        response.set_cookie("path_cookie", '1234456', path='/cookie/read_cookie/')
    elif t == 5:
        """设置访问域名，如果此域名是顶级域名，
        那么所以域名下的子级域名都可以访问，
        如果不是，那么只能在当前域名下访问，
        不能设置其他域名下的cookie"""
        response.set_cookie('domain_cookie', '123456', domain='shsxt.com')

    elif t == 6:
        """secure设置安全的cookie，只能在https请求中设置"""
        response.set_cookie("secure_cookie", "1234",secure=True)

    elif t == 7:
        """设置httponly, 不能再js客户端进行操作cookie, 只能服务端获取"""
        response.set_cookie("http_only_cookie", '1234', httponly=True)
    elif t == 8:
        """加密设置cookie，采用base64加密--解密， MD5不能解密"""
        response.set_signed_cookie("salt_cookie", '1234556', salt="shsxt")

    return response

from django.core import signing
def read_cookie(request):
    # http_only_cookie = request.COOKIES.get('http_only_cookie')
    # print("http_only_cookie: ", http_only_cookie)

    cookies = request.COOKIES # 返回的是字典
    # 怎样遍历字典
    # for key in cookies.keys():
    #     print(key, ':', cookies.get(key))
    for key, value in cookies.items():
        print(key, ':', value)
        if key == 'salt_cookie':
            unsigned_value = signing.get_cookie_signer(salt=key + "shsxt").unsign(value)
    return render(request, "read_cookie.html", context={'cookies': cookies})


def read_signed_cookie(request):
    """获取加密cookie"""
    key = request.GET.get('key', '')
    value = request.get_signed_cookie(key, salt='shsxt')
    return HttpResponse(value)


def delete_cookie(request):
    name = request.GET.get('name')
    """删除cookie， 其删除的本质是将cookie设置过期"""
    response = HttpResponse("删除cookie")
    # 默认情况下domain是当前访问的域名，path默认是根路径
    response.delete_cookie("normal", domain='127.0.0.1', path='/')
    return response

def js_cookie(request):
    return render(request,'js_cookie.html')