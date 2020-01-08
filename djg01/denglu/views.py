from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
from .models import UserInfo
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from django.views import generic
# from django.utils import timezone
# from .models import Choice, Question

# Create your views here.
def index(request):
     return HttpResponse("Hello, world. index.")

def login(request):    
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
        user = auth.authenticate(username=username, password=password)        
        if user:            
            auth.login(request, user)  #这里做了登录    
            print('fuck')    
            return HttpResponseRedirect(reverse('denglu:al', args=(username,)))
    return render(request, "denglu\login.html")

def register(request):    
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
        #username, email=None, password=None, **extra_fields        
        user = User.objects.create_user(username=username,password=password)        
        user.save()       
        if user:            
            auth.login(request, user)
            return HttpResponseRedirect(reverse('denglu:al', args=(username,)))
    return render(request, "denglu\\register.html")

@login_required(login_url="denglu:login" ) # , redirect_field_name="xxxx",
def al(request,username):
    print(username)
    return HttpResponse(username)    