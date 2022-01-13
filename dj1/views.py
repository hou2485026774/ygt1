"""
@author:houshuai
@software:PyCharm
@time:2021/12/24  16:47
"""
import json

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from dj1.models import User, Data1


def index(request):
    return render(request, "login.html")
def home(request):
    return render(request,'table.html')
@xframe_options_exempt
def toadd(request):
    return render(request, "index.html")
def getdata(request):
    mes = Data1.objects.all()
    result = {"message": 'success', "code": '0', "data": [],"count":0}
    type = []
    for data  in mes:
        dic = {}
        dic['id'] = data.id
        dic['name'] = data.name
        dic['sex'] = data.sex
        dic['city'] = data.citt
        type.append(dic)
    result['data'] = type
    result['count'] = len(type)
    return JsonResponse(result, safe=False)
@xframe_options_exempt
def edit(request):
    id = request.GET.get('id')
    result = Data1.objects.filter(id=id)
    for i in result:
        print(i.id,i.name,i.sex,i.citt)
    return render(request,'edit.html',{'result':result})
@xframe_options_exempt
def adddata(request):
    if request.method == 'POST':
        response = {'msg': '', 'status': False}
        name = request.POST.get('name', '')
        city = request.POST.get('city', '')
        sex = request.POST.get('sex', '')
        print(name+"+++++++"+city+''+city)
        u= Data1.objects.create(name=name,citt=city,sex=sex)
        u.save()
        response['msg'] = '添加成功'
        response['status'] = True
        return HttpResponse(json.dumps(response))


def doedit(request):
    if request.method == 'POST':
        response = {'msg': '', 'status': False}
        id = request.POST.get('id','')
        name = request.POST.get('name', '')
        city = request.POST.get('city', '')
        sex = request.POST.get('sex', '')
        print(name+"+++++++"+city)
        u= Data1.objects.filter(id=id)
        u.update(name=name,citt=city,sex=sex)
        response['msg'] = '更新成功'
        response['status'] = True
        return HttpResponse(json.dumps(response))