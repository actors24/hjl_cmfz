import hashlib
import json
import random

from django.db import transaction
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from album.models import AlbumList, AlbumIndex
from article.models import ArticleList
from banner.models import AutoImage
from user.models import User


# Create your views here.


def first_page(request):
    """
    为前台系统的首页 专辑页  文章页提供数据支持
    :param request:
    :return:
    """

    user_id = request.GET.get("uid")
    type = request.GET.get("type")
    sub_type = request.GET.get("sub_type")

    if not user_id:
        data = {
            'status': 401,
            'msg': "用户未登陆"
        }
        return HttpResponse(json.dumps(data))

    # 代表访问的事首页
    if type == "all":
        # 查询首页所需的数据并按规定的格式响应回去
        # 轮播图  专辑  文章
        image = AutoImage.objects.filter(status=1)
        headers = []
        for i in image:
            headers.append({"id": i.pk, "desc": i.image_decoration, "image_url": str(i.image)})
        data = json.dumps({"headers": headers})
        return HttpResponse(data)
    elif type == "wen":
        # 代表范文的是专辑 查询专辑的信息响应回去
        album = AlbumList.objects.all()
        albums = []
        for i in album:
            albums.append(
                {"id": i.pk, "name": i.album_name, "author": i.author, "broadcast": i.speaker, "count": i.index_num,
                 "score": i.rate, "image": str(i.album_image)})
        data = json.dumps({"albums": albums})
        return HttpResponse(data)
    elif type == "si":
        if sub_type == "ssyj":
            # 查询属于上师言教的文章
            article = ArticleList.objects.filter(category=1)
            articles = []
            for i in article:
                articles.append({"id": i.pk, "title": i.header, "comment": str(i.comment),
                                 "publish_time": i.publish_time.strftime("%Y-%m-%d")})
            data = json.dumps({"articles": articles})
            return HttpResponse(data)
        else:
            # 查询属于显密法要的文章
            article = ArticleList.objects.filter(category=2)
            articles = []
            for i in article:
                articles.append({"id": i.pk, "title": i.header, "comment": str(i.comment),
                                 "publish_time": i.publish_time.strftime("%Y-%m-%d")})
            data = json.dumps({"articles": articles})
            return HttpResponse(data)


def get_album_content(request):
    user_id = request.GET.get("uid")
    album_id = request.GET.get('id')
    if not user_id:
        data = {
            'status': 401,
            'msg': "用户未登陆"
        }
        return HttpResponse(json.dumps(data))

    if album_id:
        detail = AlbumIndex.objects.filter(album_id=album_id)
        details = []
        for i in detail:
            details.append({"id": i.pk, "name": i.index_name, "audio_url": str(i.audio_url), "audio_size": i.audio_size,
                            "duration": i.audio_time})
        data = json.dumps({"details": details})
        return HttpResponse(data)


@csrf_exempt
def register(request):
    user_name = request.POST.get('phone')
    password = request.POST.get('password')
    salt = str(random.randint(100000, 999999))
    sha = hashlib.sha1()
    sha.update((password + salt).encode())
    password = sha.hexdigest()
    print(user_name, password)
    try:
        if User.objects.filter(phone=user_name):
            data = json.dumps({"error": "-200", "error_msg": "该手机号已存在"})
            return HttpResponse(data)
        with transaction.atomic():
            User.objects.create(phone=user_name, passeord=password)
        user = User.objects.filter(phone=user_name, passeord=password).last()
        data = json.dumps({"uid": user.pk, "phone": user.phone, "password": user.passeord})
        return HttpResponse(data)
    except:
        return HttpResponse({"data": []})


@csrf_exempt
def modify_user(request):
    user_id = request.POST.get('uid')
    user_name = request.POST.get('user_name')
    fa_name = request.POST.get('fa_name')
    password = request.POST.get('password')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    email = request.POST.get('email')
    brief = request.POST.get('brief')
    phone = request.POST.get('phone')
    try:
        user = User.objects.get(pk=user_id)
        if user:
            with transaction.atomic():
                if user_name:
                    user.user_name = user_name
                if fa_name:
                    user.fa_name = fa_name
                if password:
                    salt = str(random.randint(100000, 999999))
                    sha = hashlib.sha1()
                    sha.update((password + salt).encode())
                    password = sha.hexdigest()
                    user.passeord = password
                if gender:
                    user.gender = gender
                if address:
                    user.address = address
                if email:
                    user.e_mail = email
                if brief:
                    user.personal_brief = brief
                if phone:
                    user.phone = phone
                user.save()
            new_user = User.objects.get(pk=user_id)
            data = json.dumps({"uid": new_user.pk, "user_name": new_user.user_name, "fa_name": new_user.fa_name,
                               "password": new_user.passeord, "gender": new_user.gender,
                               "address": new_user.address, "email": new_user.e_mail, "brief": new_user.personal_brief,
                               "phone": new_user.phone})
            return HttpResponse(data)
        else:
            return HttpResponse(json.dumps({"error": "-200", "error_msg": "该用户不存在"}))
    except:
        return HttpResponse(json.dumps({"error": "-200", "error_msg": "该用户不存在"}))
