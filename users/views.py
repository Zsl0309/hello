from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# /register/
def register(request):
    """注册View视图函数"""
    return render(request,'register.html')