from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request,'polls/index.html',{})


# 直接アクセスのみ
# from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self,request):
        client_addr = request.META.get('REMOTE_ADDR')

        return render(request,'polls/index.html',{'ip':client_addr,'title':'direct_access'})


# django-ipwareを使用したipアドレスの取得方法
# from django.http import HttpResponse
from django.views import View
from ipware import get_client_ip

class IPWare(View):
    def get(self,request):
        client_addr, _ = get_client_ip(request)
        return render(request,'polls/index.html',{'ip':client_addr,'title':'django-ipware'})