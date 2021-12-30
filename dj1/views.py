"""
@author:houshuai
@software:PyCharm
@time:2021/12/24  16:47
"""
import json

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from dj1.models import User


def index(request):
    return HttpResponse('666')


def adduser(request):
    response = {'msg': '', 'status': False}
    name = request.POST.get('name', '')
    pwd = request.POST.get('pwd', '')
    print(name+"+++++++"+pwd)
    u= User.objects.create(sname=name,spwd=make_password(pwd))
    u.save()
    response['msg'] = '添加成功'
    response['status'] = True
    return HttpResponse(json.dumps(response))
def toadd(request):
    return render(request, "index.html")