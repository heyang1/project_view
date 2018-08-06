from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'csrf.html')

def home(request):
    return render(request,'csrf_home.html')

def home_ajax(request):
    return render(request,'csrf_home_ajax.html')

@csrf_exempt
def form(request):
    print(request.POST)
    return HttpResponse('接收参数')