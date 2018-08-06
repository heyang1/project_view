from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse


# Create your views here.


def index(request):
    """上传页面"""
    return render(request, 'uploader.html')


from qiniu import Auth, put_file, etag
import qiniu.config

def qiniu(key, localfile):
    access_key = 'BuyR7f5C1bovc8-IxXWjC145OFuXuX5-AEwO19fD'
    secret_key = 'keF4PpPSVondC7UFBP8oX0aZx9d3V9jRhJJXcIu7'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    bucket_name = 'shsxt' # 七牛服务器需要创建一个空间

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    # 要上传文件的本地路径
    ret, info = put_file(token, key, localfile)
    print(ret)
    print(info)

import datetime
from user.models import UserInfo
@require_POST
def upload(request):
    """处理上传文件，写入磁盘"""
    file = request.FILES.get('myfile') # 返回UploadedFile对象
    params = request.POST # 获取表单除了文件的其他表单域
    print(params)
    if file is None:
        return HttpResponse("请选择上传文件!")
    else:
        # 写入文件
        now = datetime.datetime.now().timestamp()
        # 确保文件名唯一
        filepath = 'C:/temp/%s-%s' % (now, file.name)
        with open(filepath, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        # 上传到七牛服务器
        filename = "%s-%s" % (now, file.name)
        qiniu(filename, filepath)

        # 写入数据库 name, age , header

        UserInfo.objects.create(userName=params.get('name'),
                                age=params.get('age'), header=filename)
        return render(request, 'uploader.html')



