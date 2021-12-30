"""
@author:houshuai
@software:PyCharm
@time:2021/12/24  16:47
"""
from django.http import HttpResponse


def index(request):
    return HttpResponse('666')


