from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
from .models import UserInfo,User
# from django.urls import reverse
# from django.views import generic
# from django.utils import timezone
# from .models import Choice, Question

# Create your views here.
def index(request):
     return HttpResponse("Hello, world. You're at the polls index.")

def login(request):    
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
        user = auth.authenticate(username=username, password=password)        
    if user:            
        auth.login(request, user)  #这里做了登录        
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
    return render(request,'denglu\\register.html')
