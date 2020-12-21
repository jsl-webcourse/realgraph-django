from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import random
import psutil

# クエリパラメータではなくパスパラメータの方がいいかも
def __get_param(type):
    cpu_dict = {}
    mem_dict = {}
    if type == "cpu":
        cpu_dict['cpu'] = psutil.cpu_percent(interval=1)
        return cpu_dict

    mem_dict['memory'] = psutil.virtual_memory().percent
    if type == "memory":
        return mem_dict

    return cpu_dict.update(mem_dict)

def index(request):

    type = request.GET.get(key="type", default=None)

    json_dict = __get_param(type)
    print(json_dict)
    return JsonResponse(json_dict)
