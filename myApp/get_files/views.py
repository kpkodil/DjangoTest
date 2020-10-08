from django.shortcuts import render
from django.http import HttpResponse
from .listdir import listdir
import json


def scan_dir(request):
    files = listdir()
    return HttpResponse(json.dumps({"data": files}), content_type='applicatication/json')

