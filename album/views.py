import json

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mutagen.mp3 import MP3
from album.models import AlbumIndex, AlbumList
# Create your views here.


def get_album(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = AlbumList.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    try:
        page = Paginator(album, row_num).page(page_num)
    except:
        page = Paginator(album, row_num).page(int(page_num)-1)
    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, AlbumList):
            return {
                "author": u.author,
                "brief": u.comment,
                "broadcast": u.speaker,
                "count": u.index_num,
                "cover": u.album_image,
                "id": u.id,
                "publishDate": u.publish_time.strftime('%Y-%m-%d'),
                "score": u.rate,
                "status": u.status,
                "title": u.album_name,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


def get_chapter(request):
    album_id = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = AlbumIndex.objects.all().filter(album_id=album_id).order_by('id')
    all_page = Paginator(album, row_num)
    try:
        page = Paginator(album, row_num).page(page_num)
    except:
        page = Paginator(album, row_num).page(int(page_num)-1)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, AlbumIndex):
            return {
                "albumId": u.album_id,
                # "createDate": u.create_date,
                "duration": u.audio_time,
                "id": u.id,
                "size": u.audio_size,
                "title": u.index_name,
                "url": u.audio_url,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def add_album(request):
    title = request.POST.get('title')
    score = request.POST.get('score')
    author = request.POST.get('author')
    broadcast = request.POST.get('broadcast')
    count = request.POST.get('count')
    brief = request.POST.get('brief')
    status = request.POST.get('status')
    publish_time = request.POST.get('publishDate')
    image = request.POST.get('cover')
    oper = request.POST.get('oper')
    try:
        if oper == 'add':
            if image:
                image = image[12:]
                with transaction.atomic():
                    AlbumList.objects.create(album_name=title, author=author, speaker=broadcast, index_num=count, comment=brief, rate=score, publish_time=publish_time, status=status, album_image=image)
            else:
                with transaction.atomic():
                    AlbumList.objects.create(album_name=title, author=author, speaker=broadcast, index_num=count, comment=brief, rate=score, publish_time=publish_time, status=status)
            return HttpResponse(1)
        elif oper == 'edit':
            pk = request.POST.get('id')
            with transaction.atomic():
                album = AlbumList.objects.get(pk=pk)
                album.album_name = title
                album.author = author
                album.speaker = broadcast
                album.index_num = count
                album.comment = brief
                album.rate = score
                album.publish_time = publish_time
                album.status = status
                if image:
                    image = image[12:]
                    album.album_image = image
                album.save()
                return HttpResponse(1)
        elif oper == 'del':
            pk = request.POST.get('id')
            with transaction.atomic():
                AlbumIndex.objects.filter(album_id=pk).delete()
                AlbumList.objects.get(pk=pk).delete()
                return HttpResponse(1)
    except:
        return HttpResponse(0)


@csrf_exempt
def add_index(request):
    try:
        parent_id = request.POST.get('parent_id')
        index_name = request.POST.get('name')
        audio = request.FILES.get('audio')
        if audio:
            size = audio.size
            m = int(size) / (1024*1024)
            size = str('%.1f' % m)+ 'M'
            mp3 = MP3(audio)
            time = mp3.info.length
            minutes = int(time) // 60
            seconds = int(time) % 60
            time = str(minutes) + '分' + str(seconds)+ '秒'
        else:
            size = '0M'
            time = '0分0秒'
        with transaction.atomic():
            AlbumIndex.objects.create(index_name=index_name, audio_url=audio, album_id=parent_id, audio_size=size, audio_time=time)
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def get_index(request):
    pk = request.GET.get('id')
    index = AlbumIndex.objects.get(pk=pk)

    def mydefault(u):
        if isinstance(u, AlbumIndex):
            return {'name': u.index_name}

    return JsonResponse(index, safe=False, json_dumps_params={'default': mydefault})


@csrf_exempt
def edit_index(request):
    try:
        pk = request.POST.get('id')
        index_name = request.POST.get('name')
        audio = request.FILES.get('audio')
        with transaction.atomic():
            index = AlbumIndex.objects.get(pk=pk)
            if audio:
                size = audio.size
                m = int(size) / (1024 * 1024)
                size = str('%.1f' % m) + 'M'
                mp3 = MP3(audio)
                time = mp3.info.length
                minutes = int(time) // 60
                seconds = int(time) % 60
                time = str(minutes) + '分' + str(seconds) + '秒'
                index.audio_url = audio
                index.audio_size = size
                index.audio_time = time
            index.index_name = index_name
            index.save()
            return HttpResponse(1)
    except:
        return HttpResponse(0)


def del_index(request):
    try:
        pk = request.GET.get('id')
        with transaction.atomic():
            AlbumIndex.objects.get(pk=pk).delete()
            return HttpResponse(1)
    except:
        return HttpResponse(0)
