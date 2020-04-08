from django.shortcuts import render
from sj_cmfz.settings import API_KEY
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.send_mess import Yun_Pian
from utils.captcha import Captcha


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
    print(mobile, name, code)
    # 校验信息是否合法
    # 验证码是否在有效期内  使用redis
    # redis.get("18500230996_2")
    if msg == "信息合法":
        return JsonResponse({'msg': 'success', 'status': 0})
    else:
        return JsonResponse({'msg': 'fail', 'status': 1})


@csrf_exempt
def get_captcha(request):
    mobile = request.POST.get("mobile")
    # 获取手机号有没有对应的验证码 查看验证码是否在120S内  如果在  提示验证码已经发送
    # value = redis.get("18500230996_1")  如果返回的值存在  代表120s之内还不能发送
    # 判断手机号是否存在  正则验证是否合法
    if mobile:
        code = Captcha().create_code()
        print(code)
        yun_pian = Yun_Pian(API_KEY)
        yun_pian.send_message(mobile, code)
        # 将手机号与对应的验证码存入redis  防止无限制发送
        # redis.set("18500230996_1", "666666", 120S)
        # 保证验证码的有效期
        # redis.set("18500230996_2", "666666", 600s)
    return JsonResponse({'msg': 'success', 'status': 0})
