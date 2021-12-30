"""
@author:houshuai
@software:PyCharm
@time:2021/12/30  16:30
"""
from django.urls import path, include

from app01 import views

urlpatterns = [
    path('toadd',views.toadd),
    path('add',views.add)
]
