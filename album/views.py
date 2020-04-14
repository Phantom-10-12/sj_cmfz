import json, uuid, os
from django.db import transaction
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from mutagen.mp3 import MP3
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from album.models import Album, Chapter


def get_all_album(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    rows = []
    album = Album.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)
    for i in page:
        rows.append(i)
    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, Album):
            return {
                "author": u.author,
                "brief": u.album_info,
                "announcer": u.announcer,
                "chapter_count": u.chapter_count,
                "cover": u.cover,
                "createDate": u.publish_time.strftime('%Y-%m-%d'),
                "id": u.id,
                "publishDate": u.upload_time.strftime('%Y-%m-%d'),
                "score": u.score,
                "status": u.status,
                "title": u.title,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def edit_album(request):
    method = request.POST.get("oper")
    if method == 'add':
        title = request.POST.get('title')
        score = request.POST.get('score')
        author = request.POST.get('author')
        announcer = request.POST.get("announcer")
        chapter_count = request.POST.get("chapter_count")
        album_info = request.POST.get('brief')
        status = request.POST.get('status')
        publish_time = request.POST.get('createDate')
        upload_time = request.POST.get('publishDate')
        cover = request.FILES.get('cover')
        print(cover, announcer)
        # ext_name = os.path.splitext(cover.name)[1]
        # cover.name = str(uuid.uuid4()) + ext_name
        try:
            with transaction.atomic():
                Album.objects.create(title=title, score=score, author=author, announcer=announcer,
                                     chapter_count=chapter_count, status=status, album_info=album_info, cover=cover,
                                     publish_time=publish_time, upload_time=upload_time)
        except BaseException as error:
            print(error)
            return JsonResponse({'status': 'faile'})
        return JsonResponse({'status': 'success'})
    elif method == 'del':
        id = request.POST.get('id')
        album = Album.objects.get(pk=id)
        album.delete()
        return HttpResponse('删除成功')
    elif method == 'edit':
        id = request.POST.get('id')
        title = request.POST.get('title')
        score = request.POST.get('score')
        author = request.POST.get('author')
        announcer = request.POST.get("announcer")
        chapter_count = request.POST.get("chapter_count")
        album_info = request.POST.get('brief')
        status = request.POST.get('status')
        publish_time = request.POST.get('createDate')
        upload_time = request.POST.get('publishDate')
        cover = request.FILES.get('cover')
        print(cover)
        album = Album.objects.get(pk=id)
        album.title = title
        album.score = score
        album.author = author
        album.announcer = announcer
        album.chapter_count = chapter_count
        album.album_info = album_info
        album.status = status
        album.publish_time = publish_time
        album.upload_time = upload_time
        album.cover = cover
        album.save()
        return HttpResponse('修改成功')
    else:
        return HttpResponse()




@csrf_exempt
def add_chapter(request):
    album_id = request.POST.get("album_id")
    title = request.POST.get("title")
    audio = request.FILES.get("audio")
    status = request.POST.get("status")
    print(album_id, status, audio)
    size = round(audio.size / 1024 / 1024, 2)  # 音频大小
    size = str(size) + "MB"
    audio_mp3 = MP3(audio)  # 音频时长
    time_long = round(audio_mp3.info.length / 60, 2)
    time_long = str(time_long) + "分"
    print(album_id, title, audio, status, size, time_long)
    try:
        with transaction.atomic():
            Chapter.objects.create(album_id=album_id, title=title, url=audio, status=status, size=size,
                                   time_long=time_long, audio=audio)
    except BaseException as error:
        print(error)
        return JsonResponse({'status': 'faile'})
    return JsonResponse({'status': 'success'})


@csrf_exempt
def edit_chapter(request):
    method = request.POST.get("oper")
    if method == 'del':
        id = request.POST.get('id')
        chapter = Chapter.objects.get(pk=id)
        chapter.delete()
        return HttpResponse('删除成功')
    elif method == 'edit':
        id = request.POST.get('id')
        status = request.POST.get('status')
        chapter = Chapter.objects.get(pk=id)
        chapter.status = status
        chapter.save()
        return HttpResponse('修改成功')
    else:
        return HttpResponse()


def get_chapter(request):
    album_Id = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    rows = []
    album = Chapter.objects.all().filter(album_id=album_Id).order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)
    for i in page:
        rows.append(i)
    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, Chapter):
            return {
                "albumId": u.album_id,
                "createDate": u.create_date,
                "duration": u.time_long,
                "id": u.id,
                "size": u.size,
                "title": u.title,
                "url": u.url,
                "audio": u.audio,
                "status": u.status,
            }

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)
