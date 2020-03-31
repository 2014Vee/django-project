#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py    
@Version :   1.0 
@Author  :   2014Vee
@Contact :   1976535998@qq.com
@License :   (C)Copyright 2014Vee From UESTC
@Modify Time :   2020/3/24 11:22
@Desciption  :   None
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def test(request):

    if request.method == 'POST':
        import requests
        import json
        # 解析前端传来的json请求
        get_request = json.loads(request.body.decode())
        print(get_request)
        name = get_request['name']
        mount_data_path = get_request['location']
        taskType = get_request['taskType']
        inferNum = get_request['inferNum']
        inferType = get_request['inferType']
        res = {
            "name": name,
            "location": mount_data_path,
            "taskType": taskType,
            "inferNum": inferNum,
            "inferType": inferType
        }
        # 记住下面这句话必须得返回东西，如果没有那就返回None
        return JsonResponse(res)
    else:
        return HttpResponse("请求方式不是POST!")


