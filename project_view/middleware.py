# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin

class TestMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print('这是处理request请求。。')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("这是process_view处理%s,%s,%s" % (view_func, view_args, view_kwargs))

    def process_template_response(self, request, response):
        print("这是处理template response")
        return response

    def process_response(self, request, response):
        print("这是处理任意响应")
        return response

    def process_exception(self, request, exception):
        print("这是处理错误。。。")

class LoggerMiddleware(MiddlewareMixin):

    # 可以去统计PV/UV
    def process_request(self, request):
        print("处理请求。。。。")

    def process_response(self, request, response):
        print("处理响应。。。。")
        try:

            path = request.path
            method = request.method
            params = None
            if method == 'GET':
                params = request.GET
            else:
                params = request.POST
            params_str = ''
            if params:
                params_str = str(dict(params))
            meta = request.META
            # 客户端IP地址。
            remote_addr = meta['REMOTE_ADDR']
            # REMOTE_HOST ：客户端主机名。
            remote_host = meta['REMOTE_HOST']
            # HTTP_HOST ：客户端发送请求HOST。
            http_host = meta['HTTP_HOST']
            # 客户端的user - agent字符串。
            user_agent = meta['HTTP_USER_AGENT']

            print("""
                    请求路径[{path}],
                    请求方法[{method}],
                    请求参数[{params}],
                    客户端IP地址[{remote_addr}],
                    客户端主机名[{remote_host}],
                    客户端发送请求主机[{http_host}],
                    客户端的user_agent[{user_agent}]
                    """.format(path=path, method=method, params=params_str,
                               remote_addr=remote_addr, remote_host=remote_host,
                               http_host=http_host, user_agent=user_agent)
                  )

            if response.streaming: # 如果响应的是流
                print("响应的content:", str(response.streaming_content, encoding='utf-8'))
            else:
                print("响应的content:", str(response.content, encoding='utf-8'))

        except Exception as e:
            print(e)

        return response
