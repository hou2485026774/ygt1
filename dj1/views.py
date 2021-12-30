"""
@author:houshuai
@software:PyCharm
@time:2021/12/24  16:47
"""
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render



def index(request):
    return HttpResponse('666')


# def adduser(request):
#     response = {'msg': '', 'status': False}
#     if request.method=='POST':
#         name = request.POST.get('name', '')
#         pwd = request.POST.get('pwd', '')
#         print(name+"+++++++"+pwd)
#         u= User.objects.create(name=name,pwd=make_password(pwd))
#         u.save()
#         response['msg'] = '添加成功'
#         response['status'] = True
#         return JsonResponse(response)
#     elif request.method=='GET':
#         return render(request, "index.html")


def add(request):
    return None