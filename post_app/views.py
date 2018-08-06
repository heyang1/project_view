from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'post_index.html')


def add(request):
    """接收post请求数据"""
    params = request.POST
    print('获取参数：', params)
    uname = params.get('uname')
    upwd = params.get('upwd')
    gender = params.get('gender')
    interest = params.getlist('interest')
    print('姓名：%s\r\n密码：%s\r\n性别：%s\r\n爱好：%s' % (uname, upwd, gender, ','.join(interest)))
    # return render(request, 'add_success.html', context=params)
    context = {'uname': uname, 'upwd': upwd, 'gender': gender,
               'interest': interest}
    return render(request, 'add_success.html', context=context)