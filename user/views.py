import hashlib
import json
import os
import random
import time

from django.db import transaction
from redis import Redis
from datetime import date, timedelta

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from user.models import User
red = Redis(host='192.168.133.128', port='7000')


def check_user(request):
    # salt = str(random.randint(100000, 999999))
    # sha = hashlib.sha1()
    # sha.update(('123456' + salt).encode())
    # password = sha.hexdigest()
    # couty = ["北京", "天津", "河北", "山西", "内蒙古", "吉林", "黑龙江", "辽宁", "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北",
    #          "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆", "香港", "澳门", "台湾"]
    # now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    # for i in range(0, 34):
    #     User.objects.create(user_name=i, fa_name=i, passeord=password, salt=salt, gender='男',
    #                         address=couty[i], e_mail='123', personal_brief='abc',
    #                         status=1, phone='15748412578',
    #                         register_time=now_time)
    user = User.objects.all()
    rows = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pagtor = Paginator(user, per_page=rows)
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
        if isinstance(u, User):
            return {'id': u.pk, 'username': u.user_name, 'fa_name': u.fa_name, 'gender': u.gender,
                    'address': u.address, 'email': u.e_mail, 'brief': u.personal_brief, 'pic': str(u.image),
                    'status': u.status, 'phone': u.phone,
                    'register_time': u.register_time.strftime('%Y-%m-%d %H:%M:%S')}

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


@csrf_exempt
def add_user(request):
    try:
        user_name = request.POST.get('user_name')
        fa_name = request.POST.get('fa_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        e_mail = request.POST.get('e_mail')
        brief = request.POST.get('brief')
        pic = request.FILES.get('pic')
        status = request.POST.get('status')
        phone = request.POST.get('phone')
        salt = str(random.randint(100000, 999999))
        sha = hashlib.sha1()
        sha.update((password + salt).encode())
        password = sha.hexdigest()
        now_time = time.strftime("%Y-%m-%d %H:%M:%S")
        with transaction.atomic():
            User.objects.create(user_name=user_name, fa_name=fa_name, passeord=password, salt=salt, gender=gender,
                                address=address, e_mail=e_mail, personal_brief=brief, image=pic, status=status, phone=phone,
                                register_time=now_time)
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def get_user(request):
    pk = request.GET.get('id')
    user = User.objects.get(pk=pk)

    def mydefault(u):
        if isinstance(u, User):
            return {'id': u.pk, 'username': u.user_name, 'fa_name': u.fa_name, 'gender': u.gender,
                    'address': u.address, 'email': u.e_mail, 'brief': u.personal_brief, 'pic': str(u.image),
                    'status': u.status, 'phone': u.phone,
                    'register_time': u.register_time.strftime('%Y-%m-%d %H:%M:%S')}

    return JsonResponse(user, safe=False, json_dumps_params={'default': mydefault})


def edit_user(request):
    try:
        pk = request.GET.get('id')
        status = request.GET.get('status')
        with transaction.atomic():
            user = User.objects.get(pk=pk)
            user.status = status
            user.save()
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def del_user(request):
    try:
        pk = request.GET.get('id')
        with transaction.atomic():
            user = User.objects.get(pk=pk)
            # if user.image:
            #     os.remove(r"D:\PycharmProjects\hjl_cmfz\static\\" + user.image)
            user.delete()
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def get_user_trend(request):
    if red.get('num'):
        data = eval(red.get('num'))
    else:
        now = time.strftime('%Y-%m-%d')
        day1 = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        day2 = (date.today() + timedelta(days=-6)).strftime("%Y-%m-%d")
        day3 = (date.today() + timedelta(days=-5)).strftime("%Y-%m-%d")
        day4 = (date.today() + timedelta(days=-4)).strftime("%Y-%m-%d")
        day5 = (date.today() + timedelta(days=-3)).strftime("%Y-%m-%d")
        day6 = (date.today() + timedelta(days=-2)).strftime("%Y-%m-%d")
        day7 = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
        days = [now, day7, day6, day5, day4, day3, day2, day1]
        people = []
        for i in range(7):
            count = len(list(User.objects.filter(register_time__range=[days[i + 1], days[i]])))
            people.append(count)
        data = {'x': days, 'y': people}
        red.set('num', str(data), 24*60*60)
    return JsonResponse(data)


def get_user_map(request):
    if red.get('data'):
        data = eval(red.get('data'))
        print(1)
    else:
        data = [
            {"name": '北京', "value": len(list(User.objects.filter(address="北京")))},
            {"name": '天津', "value": len(list(User.objects.filter(address="天津")))},
            {"name": '上海', "value": len(list(User.objects.filter(address="上海")))},
            {"name": '重庆', "value": len(list(User.objects.filter(address="重庆")))},
            {"name": '河北', "value": len(list(User.objects.filter(address="河北")))},
            {"name": '河南', "value": len(list(User.objects.filter(address="河南")))},
            {"name": '云南', "value": len(list(User.objects.filter(address="云南")))},
            {"name": '辽宁', "value": len(list(User.objects.filter(address="辽宁")))},
            {"name": '湖南', "value": len(list(User.objects.filter(address="湖南")))},
            {"name": '安徽', "value": len(list(User.objects.filter(address="安徽")))},
            {"name": '⼭东', "value": len(list(User.objects.filter(address="山东")))},
            {"name": '新疆', "value": len(list(User.objects.filter(address="新疆")))},
            {"name": '江苏', "value": len(list(User.objects.filter(address="江苏")))},
            {"name": '浙江', "value": len(list(User.objects.filter(address="浙江")))},
            {"name": '江⻄', "value": len(list(User.objects.filter(address="江西")))},
            {"name": '湖北', "value": len(list(User.objects.filter(address="湖北")))},
            {"name": '⼴⻄', "value": len(list(User.objects.filter(address="广西")))},
            {"name": '⽢肃', "value": len(list(User.objects.filter(address="甘肃")))},
            {"name": '⼭⻄', "value": len(list(User.objects.filter(address="山西")))},
            {"name": '陕⻄', "value": len(list(User.objects.filter(address="陕西")))},
            {"name": '吉林', "value": len(list(User.objects.filter(address="吉林")))},
            {"name": '福建', "value": len(list(User.objects.filter(address="福建")))},
            {"name": '贵州', "value": len(list(User.objects.filter(address="贵州")))},
            {"name": '⼴东', "value": len(list(User.objects.filter(address="广东")))},
            {"name": '⻘海', "value": len(list(User.objects.filter(address="青海")))},
            {"name": '⻄藏', "value": len(list(User.objects.filter(address="西藏")))},
            {"name": '四川', "value": len(list(User.objects.filter(address="四川")))},
            {"name": '宁夏', "value": len(list(User.objects.filter(address="宁夏")))},
            {"name": '海南', "value": len(list(User.objects.filter(address="海南")))},
            {"name": '台湾', "value": len(list(User.objects.filter(address="台湾")))},
            {"name": '⾹港', "value": len(list(User.objects.filter(address="香港")))},
            {"name": '澳门', "value": len(list(User.objects.filter(address="澳门")))},
        ]
        red.set('data', str(data), 24*60*60)
        print(0)
    return JsonResponse(data, safe=False)
