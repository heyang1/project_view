from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.template import loader
from .models import UserInfo
# Create your views here.


def index(request):
    messages.info(request, "这是一个message信息。。。")
    return render(request, "tpl_index.html", context={'menu': '首页'})


def find(request):
    # 第一步找模板
    template = loader.get_template("tpl_index.html") # 默认是DjangoTemplates对象
    # 第二步数据渲染
    content = template.render(context = {'content': 'Hello World!', 'menu': '首页'}, request = request)
    print(content)
    # 返回响应
    return HttpResponse(content)


def show_user(request, pk):
    user = UserInfo.objects.get(pk=pk)
    return render(request, 'tpl_user.html', {'user': user, 'menu': '首页'})


def user_list(request):
    users = UserInfo.objects.all().order_by('-id')
    return render(request, 'tpl_user_list.html', {'users': users, 'menu': '首页'})


def path(request, year, month, day):
    return render(request, "tpl_date.html")

import datetime

def filter(request):
    context = {'userName': 'Jack',
               'tags':['很酷', '很帅', '有钱'],
               'gender': 1, 'height':190.254, 'birthday': datetime.datetime.now() }
    return render(request, 'tpl_filter.html', context=context)
