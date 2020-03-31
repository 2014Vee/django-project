#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   my_views.py    
@Version :   1.0 
@Author  :   2014Vee
@Contact :   1976535998@qq.com
@License :   (C)Copyright 2014Vee From UESTC
@Modify Time :   2020/3/20 17:43
@Desciption  :   None
'''

# from django.shortcuts import render
#
# def mount_data(request):
#     if request.method == 'POST':
#         import requests
#         import json
#         import os
#         data = json.load(request.content)
#         name = data['name']
#         mount_data_path = data['location']
#         taskType = data['taskType']
#         inferNum = data['inferNum']
#         inferType = data['inferType']
#         img_path = "这里想办法获取得到"
#         # 添加mount盘
#         # add by 2014Vee mount
#         return_tmp = os.system('sudo mount -t nfs '
#                                '30.64.90.2:/pamd_core_id101154_vol1002_dev/cgj/Mask_RCNN-master/dataset/tmp '
#                                + mount_data_path)
#         # 如果执行成功os.system()会返回0
#         if return_tmp == 0:
#             "开始处理下一个字段"
#         else:
#             "提示一下mount失败"
#
#         return render(request, 'user.html', {"user": user, "username": username})
#
# def inference(name, taskType, inferNum, inferType):
#     import requests
#     import json
#     url = "余江华给我的地址"
#     data = {
#         "name": name,
#         "taskType": taskType,
#         "inferNum": inferNum,
#         "inferType": inferType,
#     }
#     request = requests.get(url, data=json.dumps(data))
#     return "返回个啥呢？"

# add by 2014Vee
from django.http import HttpResponse
from django.http import JsonResponse
def mount_data(request):
    if request.method == 'POST':
        import json
        # get web request
        get_request = json.loads(request.body.decode())
        print(get_request)
        name = get_request['name']
        mount_data_path = get_request['location']
        inference = get_request['inference']
        taskType = get_request['taskType']
        inferNum = get_request['inferNum']
        inferType = get_request['inferType']
        if inference
        res = {
            "name": name,
            "location": mount_data_path,
            "taskType": taskType,
            "inferNum": inferNum,
            "inferType": inferType
        }
        # must return sth, if np data should return None
        return JsonResponse(res)
    else:
        return HttpResponse("Request Method Is Not POST!")
# end by 2014Vee


# # add by 2014Vee
# def mount_data(request):
#     if request.method == 'POST':
#         import requests
#         import json
#         import os
#         # data = json.load(request.content)
#         # name = data['name']
#         # mount_data_path = data['location']
#         # taskType = data['taskType']
#         # inferNum = data['inferNum']
#         # inferType = data['inferType']
#         # img_path = "这里想办法获取得到"
#         # # 添加mount盘
#         # return_tmp = os.system('sudo mount -t nfs '
#         #                        '30.64.90.2:/pamd_core_id101154_vol1002_dev/cgj/Mask_RCNN-master/dataset/tmp '
#         #                        + mount_data_path)
#
#         # infer_res = inference(name, taskType, inferNum, inferType);
#         # 如果执行成功os.system()会返回0
#         # if return_tmp == 0:
#         #     "开始处理下一个字段"
#         # else:
#         #     "提示一下mount失败"
#
#         return HttpResponse("OK, test is finished!!!")
#
#
# def inference(name, taskType, inferNum, inferType):
#     import requests
#     import json
#     url = "余江华给我的地址"
#     data = {
#         "name": name,
#         "taskType": taskType,
#         "inferNum": inferNum,
#         "inferType": inferType,
#     }
#     request = requests.get(url, data=json.dumps(data))
#     return "返回个啥呢？"
