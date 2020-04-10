import json
import os
import time

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from banner.models import AutoImage

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def check_banner(request):
    data = AutoImage.objects.all()
    rows = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pagtor = Paginator(data, per_page=rows)
    try:
        pager = pagtor.page(page).object_list
    except:
        pager = pagtor.page(int(page) - 1).object_list
    page_data = {
        "page": page,
        "total": pagtor.num_pages,
        "records": pagtor.count,
        "rows": list(pager)
    }

    def mydefault(u):
        if isinstance(u, AutoImage):
            return {'id': u.pk, 'desc': u.image_decoration, 'date': u.upload_time.strftime('%Y-%m-%d %H:%M:%S'), 'status': u.status,
                    'pic': str(u.image)}

    data = json.dumps(page_data, default=mydefault)
    print(data)
    return HttpResponse(data)


@csrf_exempt
def add_banner(request):
    try:
        title = request.POST.get('title')
        status = request.POST.get('status')
        pic = request.FILES.get('pic')
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        with transaction.atomic():
            AutoImage.objects.create(image=pic, image_decoration=title, status=status, upload_time=now_time)
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def get_one_nanner(request):
    pk = request.GET.get('id')
    data = AutoImage.objects.get(pk=pk)

    def mydefault(u):
        if isinstance(u, AutoImage):
            return {'id': u.pk, 'desc': u.image_decoration, 'date': u.upload_time.strftime('%Y-%m-%d %H:%M:%S'), 'status': u.status,
                    'pic': str(u.image)}

    # data = json.dumps(data, default=mydefault)
    return JsonResponse(data, safe=False, json_dumps_params={'default': mydefault})


def del_banner(request):
    try:
        pk = request.GET.get('id')
        with transaction.atomic():
            image = AutoImage.objects.get(pk=pk)
            if image.image:
                os.remove(r"D:\PycharmProjects\hjl_cmfz\static\\"+image.image.url)
            image.delete()
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def edit_banner(request):
    try:
        pk = request.GET.get('id')
        desc = request.GET.get('desc')
        status = request.GET.get('status')
        with transaction.atomic():
            data = AutoImage.objects.get(pk=pk)
            data.image_decoration = desc
            data.status = status
            data.save()
            return HttpResponse(1)
    except:
        return HttpResponse(0)

