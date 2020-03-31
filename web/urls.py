#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py.py    
@Version :   1.0 
@Author  :   2014Vee
@Contact :   1976535998@qq.com
@License :   (C)Copyright 2014Vee From UESTC
@Modify Time :   2020/3/12 9:03
@Desciption  :   None
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.user, name="user"),
    # path('test/')

]
