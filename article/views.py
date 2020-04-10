import json
import os
import time

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

from article.models import ContentImage, ArticleList

# Create your views here.


def get_article(request):
    article = ArticleList.objects.all()
    rows = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pagtor = Paginator(article, per_page=rows)
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
        if isinstance(u, ArticleList):
            return {'id': u.pk, 'title': u.header, 'category': u.category, 'content': u.comment, 'publish_time': u.publish_time.strftime('%Y-%m-%d %H:%M:%S')}

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


@xframe_options_sameorigin  # 允许页面嵌套时发起访问
@csrf_exempt
def upload_pic(request):
    file = request.FILES.get("imgFile")

    if file:
        # 获取图片所在的服务的全路径
        img_url = request.scheme + "://" + request.get_host() + "/static/article_pic/" + str(file)
        result = {"error": 0, "url": img_url}
        with transaction.atomic():
            ContentImage.objects.create(pic=file)
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_all_img(request):
    # 找到图片所在的目录  方便进行回显
    pic_dir = request.scheme + "://" + request.get_host() + '/static/'
    pic_list = ContentImage.objects.all()

    rows = []

    for i in list(pic_list):
        # 获取图片的后缀
        path, pic_suffix = os.path.splitext(i.pic.url)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": i.pic.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": i.pic.name,
            "datetime": "2018-06-06 00:36:39"
        })

    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_dir,
        "total_count": len(pic_list),
        "file_list": rows

    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def add_article(request):
    try:
        title = request.GET.get('title')
        category = request.GET.get('category')
        content = request.GET.get('content')
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        with transaction.atomic():
            ArticleList.objects.create(header=title, category=category, comment=content, publish_time=now)
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def edit_article(request):
    try:
        pk = request.GET.get('article_id')
        title = request.GET.get('title2')
        category = request.GET.get('category2')
        content = request.GET.get('content2')
        with transaction.atomic():
            article = ArticleList.objects.get(pk=pk)
            article.header = title
            article.category = category
            article.comment = content
            article.save()
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def del_article(request):
    try:
        pk = request.GET.get('id')
        with transaction.atomic():
            ArticleList.objects.get(pk=pk).delete()
            return HttpResponse(1)
    except:
        return HttpResponse(0)
