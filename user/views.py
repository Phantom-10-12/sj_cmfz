import json, os, uuid, time

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user.models import User
import datetime


def get_all_user(request):
    """
    获取所有注册用户的相关信息并转换成json响应的前端
    :param request:
    :return:
    """
    rows = request.GET.get('rows')
    page = request.GET.get('page')
    user_list = User.objects.all().order_by('id')
    print(user_list)
    all_page = Paginator(user_list, rows)

    # 处理最后删除当页最后一条数据
    if int(page) > all_page.num_pages:
        page = all_page.num_pages

    # 获取第一页对象
    page_obj = Paginator(user_list, rows).page(page).object_list
    page_data = {
        'page': page,
        'total': all_page.num_pages,
        'records': all_page.count,
        'rows': list(page_obj)
    }

    def myDefault(u):
        if isinstance(u, User):
            return {"id": u.id,
                    'username': u.username,
                    'nickname': u.nickname,
                    'address': u.address,
                    'status': '不禁用' if u.status == 1 else '禁用',
                    'register_time': u.register_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'head_pic': str(u.head_pic)}

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


@csrf_exempt
def add_user(request):
    username = request.POST.get("username")
    nickname = request.POST.get('nickname')
    address = request.POST.get('address')
    status = request.POST.get('status')
    gender = request.POST.get('gender')
    head_pic = request.FILES.get('head_pic')
    ext_name = os.path.splitext(head_pic.name)[1]
    head_pic.name = str(uuid.uuid4()) + ext_name
    print(status, username, nickname, address, gender, head_pic)
    try:
        result = User.objects.create(username=username,
                                     password=123456,
                                     head_pic=head_pic,
                                     nickname=nickname,
                                     gender=gender,
                                     address=address,
                                     status=int(status))
        if result:
            return HttpResponse('添加成功！')
    except BaseException as error:
        print(error)
        return HttpResponse('添加失败！')


@csrf_exempt
def edit_user(request):
    method = request.POST.get("oper")
    print(method)
    if method == 'edit':
        id = request.POST.get('id')
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        address = request.POST.get('address')
        status = request.POST.get('status')
        print(id, username, nickname, address, status)
        user = User.objects.get(pk=id)
        user.username = username
        user.nickname = nickname
        user.address = address
        user.status = status
        user.save()
        return HttpResponse('修改成功')

    elif method == 'del':
        id = request.POST.get('id')
        user = User.objects.get(pk=id)
        user.delete()
        return HttpResponse('删除成功')


def user_register_trend(request):
    from redis import Redis
    redis = Redis(host='123.57.70.140', port=6379)
    if redis.get("data"):
        data = eval(redis.get("data"))
    else:
        now = time.strftime("%Y-%m-%d")
        day1 = (datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
        day2 = (datetime.date.today() + datetime.timedelta(days=-6)).strftime("%Y-%m-%d")
        day3 = (datetime.date.today() + datetime.timedelta(days=-5)).strftime("%Y-%m-%d")
        day4 = (datetime.date.today() + datetime.timedelta(days=-4)).strftime("%Y-%m-%d")
        day5 = (datetime.date.today() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d")
        day6 = (datetime.date.today() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")
        day7 = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        x = [day1, day2, day3, day4, day5, day6, day7, now]
        y = []
        for i in range(7):
            num = len(list(User.objects.filter(register_time__gt=x[i], register_time__lt=x[i + 1])))
            y.append(num)
        x = [day1, day2, day3, day4, day5, day6, day7]
        data = {
            'x': x,
            'y': y,
        }
        # 处理要加入缓存的时间
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1
        save_time = today_end_time - int(time.time())
        redis.set("data", str(data), save_time)
    return JsonResponse(data)


def user_distribution(request):
    data = [
        {'name': '北京', 'value': 0},
        {'name': '天津', 'value': 0},
        {'name': '广东', 'value': 0},
        {'name': '上海', 'value': 0},
        {'name': '重庆', 'value': 0},
        {'name': '河北', 'value': 0},
        {'name': '河南', 'value': 0},
        {'name': '云南', 'value': 0},
        {'name': '辽宁', 'value': 0},
        {'name': '湖南', 'value': 0},
        {'name': '安徽', 'value': 0},
        {'name': '⼭东', 'value': 0},
        {'name': '新疆', 'value': 0},
        {'name': '江苏', 'value': 0},
        {'name': '浙江', 'value': 0},
        {'name': '江⻄', 'value': 0},
        {'name': '湖北', 'value': 0},
        {'name': '⼴⻄', 'value': 0},
        {'name': '⽢肃', 'value': 0},
        {'name': '⼭⻄', 'value': 0},
        {'name': '陕⻄', 'value': 0},
        {'name': '吉林', 'value': 0},
        {'name': '福建', 'value': 0},
        {'name': '贵州', 'value': 0},
        {'name': '⻘海', 'value': 0},
        {'name': '⻄藏', 'value': 0},
        {'name': '四川', 'value': 0},
        {'name': '宁夏', 'value': 0},
        {'name': '海南', 'value': 0},
        {'name': '台湾', 'value': 0},
        {'name': '⾹港', 'value': 0},
        {'name': '澳⻔', 'value': 0}
    ]
    for i in data:
        users = User.objects.filter(address=i['name'])
        i['value'] = len(users)
    return JsonResponse(data, safe=False)
