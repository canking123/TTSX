from hashlib import sha1
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail


# Create your views here.
def register(request):
    context = {'template': 1}
    return render(request, 'tt_user/register.html', context)


def check_user_is_repeat(request):
    username = request.GET.get('username')
    repeat_count = UserInfo.objects.filter(uname=username).count()
    context = {'count': repeat_count}
    return JsonResponse(context)


def register_handle(request):
    username = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')

    # 对密码进行sha1加密
    s1 = sha1()
    s1.update(pwd.encode())
    pwd_sha1 = s1.hexdigest()

    new_user = UserInfo()
    new_user.uname = username
    new_user.upwd = pwd_sha1
    new_user.uemail = email
    new_user.save()
    print(new_user.id)
    msg = '<a href="http://127.0.0.1:8000/user/active%s/" target="_blank">点击激活</a>' % (new_user.id)
    print(new_user.id)
    send_mail('注册激活', '', settings.EMAIL_FROM,
              [email],
              html_message=msg)
    return HttpResponse('注册成功，请前往邮箱中激活帐号')


def active(request, uid):
    user = UserInfo.objects.get(id=uid)
    user.isActive = True
    user.save()
    return HttpResponse('账户激活成功，<a href="/user/login/">点击登录</a>')


def login(request):
    context = {'template': 1}
    return render(request, 'tt_user/login.html', context)
