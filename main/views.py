from django.shortcuts import render
from sj_cmfz.settings import API_KEY
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.send_mess import Yun_Pian
from utils.captcha import Captcha

import re
from redis import Redis

redis = Redis(host='123.57.70.140', port=6379)


# Create your views here.


def index(request):
    return render(request, "main.html")


def login(request):
    return render(request, "login.html")


@csrf_exempt
def login_logic(request):
    mobile = request.GET.get('mobile')
    name = request.GET.get("name")
    code = request.GET.get('code')
    phone_result = re.match(r"^1[35678]\d{9}$", mobile)
    code_result = re.match(r"\d{6}$", code)
    # 校验信息是否合法
    # 验证码是否在有效期内  使用redis
    # redis.get("18500230996_2")
    if phone_result and code_result:
        try:
            saved_code = redis.get(f'{mobile}_2')
            if saved_code.decode() == code:
                return JsonResponse({'status': 1, 'msg': '登陆成功！'})
        except BaseException as error:
            print(error)
            return JsonResponse({'status': 0, 'msg': f'{error}请先发送验证码！'})
        return JsonResponse({'status': 0, 'msg': '登陆失败！'})
    else:
        return JsonResponse({'status': 0, 'msg': '有字段输入不合法！请检查！'})


@csrf_exempt
def get_captcha(request):
    mobile = request.POST.get('mobile')
    # 获取手机号有没有对应的验证码 查看验证码是否在120S内  如果在  提示验证码已经发送
    # value = redis.get("18500230996_1")  如果返回的值存在  代表120s之内还不能发送
    # 判断手机号是否存在  正则验证是否合法
    # 正则判断输入手机号是否合法
    result = re.match(r"^1[35678]\d{9}$", mobile)
    if result:
        # 将手机号与对应的验证码存入redis  防止无限制发送
        # redis.set("18500230996_1", "666666", 120S)
        # 保证验证码的有效期
        # redis.set("18500230996_2", "666666", 600s)
        saved_code = redis.get(f'{mobile}_1')
        if saved_code:
            return JsonResponse({'status': 0, 'msg': '已发送验证码，请注意查收！'})
        code = Captcha().create_code()
        print(f'验证码：{code}')
        yun_pian = Yun_Pian(API_KEY)
        yun_pian.send_message(mobile, code)

        # 将手机号与对应的验证码存入redis  防止无限制发送
        redis.set(f"{mobile}_1", code, 120)
        # 保证验证码的有效期
        redis.set(f"{mobile}_2", code, 600)

        return JsonResponse({'status': 1, 'msg': '发送成功！'})
    else:
        return JsonResponse({'status': 0, 'msg': '请输入合法的手机号！'})
