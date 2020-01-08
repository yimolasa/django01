from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.
from .models import UserInfo


def login(request):
    kwgs = {}
    # name = request.GET.get("reg")
    # if 'reg' == name:
    #     return render(request, "denglu\\reg.html")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        msg = ''
        try:
            ###############
            userInfo = UserInfo.objects.get(username=username)
            if userInfo and userInfo.password == password:
                # return render(request, "denglu\index.html", {"username": username})
                # return HttpResponseRedirect(reverse('denglu:index'))
                return HttpResponseRedirect(reverse('denglu:al'))
            else:
                msg = "用户名或密码错误"
            #################
            # user = authenticate(username=username, password=password)
            # print(user)
            # if user:
            #     return HttpResponseRedirect(reverse('denglu:al'))    
        except:
            msg = "用户名不存在"
        kwgs = {
            "msg": msg,
        }

    return render(request, "denglu\login2.html", kwgs)


def reg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        ret = UserInfo.objects.create(username=username, password=password,)
        if ret:
            # return render(request, "denglu\index.html",{"username":username})
            return HttpResponseRedirect(reverse('denglu:index'))
    return render(request, "denglu\\reg.html")


def index(request):

    # username = request.POST.get("username")
    # password = request.POST.get('password')
    # UserInfo.objects.create(username=username, password=password)
    # 查询数据
    user_list = UserInfo.objects.all()
    return render(request, 'denglu\index.html', {'user_list': user_list})


def register(request):
    return HttpResponse("register.")

@login_required(next='denglu:al')
def al(request):
    return HttpResponse("welcome")
