import json
import datetime
import os,uuid

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from redis import Redis

from article.models import Article_img, Article

#显示所有文章
def get_all_article(request):
    rows = request.GET.get('rows', 5)
    page = request.GET.get('page', 1)
    article_list = list(Article.objects.all().order_by('id'))
    print(article_list)
    paginator = Paginator(article_list, int(rows))
    try:
        rows = list(paginator.page(page).object_list)
    except:
        rows = list(paginator.page(int(page) - 1).object_list)
        page = int(page) - 1

    page_data = {
        'page': page,
        'total': paginator.num_pages,
        'records': paginator.count,
        'rows': rows
    }

    def mydefault(a):
        if isinstance(a, Article):
            return {
                'id': a.id,
                'title': a.title,
                'status': a.status,
                'content': a.content,
                'cate': a.cate,
                'author': a.author,
                'publishtime': "" if a is None else a.publish_date.strftime("%Y-%m-%d %H:%M:%S"),
            }

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)

#编辑一篇文章
@csrf_exempt
def edit_article(request):
    id = request.POST.get('id')
    cate = request.POST.get('cate')
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    status = request.POST.get('status')
    print(id,cate,title,content,author,status)
    try:
        with transaction.atomic():
            art = Article.objects.get(id=id)
            art.content = content
            art.author = author
            art.title = title
            art.cate = cate
            art.status = status
            art.save()
    except:
        return JsonResponse({'meg': 'faile'})
    return JsonResponse({'msg': 'success'})

#添加一篇文章
@csrf_exempt
def add_article(request):
    cate = request.POST.get('cate')
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    status = request.POST.get('status')
    print(cate, title, content, author, status)
    try:
        with transaction.atomic():
            Article.objects.create(title=title, cate=cate, author=author, content=content, status=status)
    except:
        return JsonResponse({'status': 'faile'})
    return JsonResponse({'status': 'success'})

#删除一篇文章
@csrf_exempt
def del_article(request):
    oper = request.POST.get('oper')
    id = request.POST.get('id')
    if oper == 'del':
        with transaction.atomic():
            Article.objects.get(id=id).delete()
    return HttpResponse()


@xframe_options_sameorigin  # 允许页面嵌套时发起访问
@csrf_exempt
def upload_img(request):
    file = request.FILES.get("imgFile")
    if file:
        ext_name = os.path.splitext(file.name)[1]
        file.name = str(uuid.uuid4()) + ext_name
        # 获取图片所在的服务的全路径
        img_url = request.scheme + "://" + request.get_host() + "/static/article_picture/" + str(file)
        result = {"error": 0, "url": img_url}
        Article_img.objects.create(article_picture=file)
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_all_img(request):
    pic_dir = request.scheme + "://" + request.get_host() + '/static/article_picture/'
    pic_list = Article_img.objects.all()
    rows = []
    for i in list(pic_list):
        # 获取图片的后缀
        path, pic_suffix = os.path.splitext(i.article_picture.url)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": i.article_picture.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": i.article_picture.name,
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
