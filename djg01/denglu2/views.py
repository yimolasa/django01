from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
# from .models import UserInfo
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):    
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
        user = auth.authenticate(username=username, password=password)        
        if user:            
            auth.login(request, user)  #这里做了登录    
            print('fuck')    
            # return HttpResponseRedirect(reverse('denglu:al', args=(username,)))
            return HttpResponse(username) 
    return render(request, "denglu2\login.html")
    # print('not allow')