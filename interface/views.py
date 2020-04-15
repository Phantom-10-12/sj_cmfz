from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from banner.models import Banner
from article.models import Article, Article_img
from album.models import Album, Chapter
from user.models import User


# 为前台首页，数据页，文章页提供数据
def first_page(request):
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
        # 轮播图
        banners = Banner.objects.all().order_by('id')
        header_list = []
        for banner in banners:
            dict = {
                "thumbnail": "http://127.0.0.1:8000/static/" + str(banner.picture_url),
                "desc": banner.picture_title,
                "id": str(banner.id),
            }
            header_list.append(dict)

        # 专辑,文章
        albums = Album.objects.all().order_by('id')
        body_list = []
        for album in albums:
            chapters = Chapter.objects.filter(album_id=album.id)
            dict = {
                "thumbnail": "http://127.0.0.1:8000/static/" + str(album.cover),
                "title": album.title,
                "author": album.author,
                "type": "0",
                "set_count": str(len(chapters)),
                "create_date": str(album.publish_time)
            }
            body_list.append(dict)

        articles = Article.objects.all().order_by('id')
        for article in articles:
            dict = {
                "thumbnail": "",
                "title": article.title,
                "author": article.author,
                "type": "1",
                "set_count": "",
                "create_date": str(article.create_date)
            }
            body_list.append(dict)
        data = {
            "header": header_list,
            "body": body_list,
        }
        return HttpResponse(json.dumps(data))

    elif type == "wen":
        # 代表访问的是专辑 查询专辑的信息响应回去
        # 专辑
        albums = Album.objects.all().order_by('id')
        album_list = []
        for album in albums:
            dict = {
                "thumbnail": "http://127.0.0.1:8000/static/" + str(album.cover),
                "title": album.title,
                "id": str(album.id)
            }
            album_list.append(dict)
        data = {
            "album": album_list,
        }
        return HttpResponse(json.dumps(data))

    elif type == "si":
        if sub_type == "ssyj":
            # 查询属于上师言教的文章
            article_list = []
            ssyj_list = Article.objects.filter(cate=0).order_by("id")
            for ssyj in ssyj_list:
                dict = {
                    "thumbnail": "",
                    "title": ssyj.title,
                    "author": ssyj.author,
                    "create_date": str(ssyj.create_date),
                }
                article_list.append(dict)
            data = {
                "article": article_list,
            }
            return HttpResponse(json.dumps(data))


        else:
            # 查询属于显密法要的文章
            article_list = []
            xmfy_list = Article.objects.filter(cate=1).order_by("id")
            for xmfy in xmfy_list:
                dict = {
                    "thumbnail": "",
                    "title": xmfy.title,
                    "author": xmfy.author,
                    "create_date": str(xmfy.create_date),
                }
                article_list.append(dict)
            data = {
                "article": article_list,
            }
            return HttpResponse(json.dumps(data))

    user_json = {
        "error": "无type",
    }

    return HttpResponse(json.dumps(user_json))


# 专辑的详情页接口
def album(request):
    # 获取专辑id
    id = request.GET.get("id")
    uid = request.GET.get("uid")
    print(id)
    album_ = Album.objects.filter(pk=int(id))[0]  #
    chapters = Chapter.objects.filter(album_id=id)
    print(album_)
    print(chapters)
    introduction_dict = {
        "thumbnail": "http://127.0.0.1:8000/static/" + str(album_.cover),
        "title": album_.title,
        "score": str(album_.score),
        "author": album_.author,
        "broadcast": album_.announcer,
        "set_count": str(len(chapters)),
        "brief": album_.album_info,
        "create_date": str(album_.publish_time),
    }
    chapter_list = []
    for chapter in chapters:
        size = chapter.size
        seconds = chapter.time_long
        # m, s = divmod(seconds, 60)
        dict = {
            "title": chapter.title,
            "download_url": "http://127.0.0.1:8000/static/" + str(chapter.audio),
            "size": size,
            "duration": seconds,
            # "duration": "%02dm%02ds" % (m, s),
        }
        chapter_list.append(dict)
    data = {
        "introduction": introduction_dict,
        "list": chapter_list,
    }
    return HttpResponse(json.dumps(data))


@csrf_exempt
def register(request):
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    user = User.objects.filter(username=phone)
    if user:
        data = {
            "errno": "-200",
            "error_msg": "该手机号已注册，请登录",
        }

    else:
        User.objects.create(username=phone, password=password)
        user = User.objects.get(username=phone)
        data = {
            "password": password,
            "uid": user.id,
            "phone ": user.username,
        }
    return HttpResponse(json.dumps(data))


@csrf_exempt
def modify(request):
    username = request.POST.get('uid')
    gender = request.POST.get('gender')
    photo = request.POST.get('photo')
    location = request.POST.get('location')
    description = request.POST.get('description')
    nickname = request.POST.get('nickname')
    province = request.POST.get('province')
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
        print(username)
    except:
        data = {
            "errno": "-200",
            "error_msg": "所编辑的用户不存在"
        }
        return HttpResponse(json.dumps(data))
    data = {
        "password": user.password,
        "farmington": user.nickname,
        "uid": user.id,
        "nickname": user.nickname,
        "gender": user.gender,
        "photo": "http://127.0.0.1:8000/static/" + str(user.head_pic),
        "location": user.address,
        "province": user.address,
        "email": user.email,
        "description": user.user_info,
        "phone ": user.phone,
    }
    user.gender = gender
    user.head_pic = photo
    user.user_info = description
    user.nickname = nickname
    user.address = province
    user.password = password
    user.email = email
    user.save()
    return HttpResponse(json.dumps(data))
