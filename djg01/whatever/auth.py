from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User

@csrf_exempt
def loginauth(request):
    user_loggedin='Guest'
    errors_list=[]
    if request.method == 'POST':
        print 'pp: ',request.POST.get('name'),request.POST.get('password')
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        print 'authuser',user
        if user is not None:
            auth_login(request,user)
            uu=request.user
            u=User.objects.get(username=uu)return HttpResponseRedirect("../check_dict")
        
    context={'errors_list':errors_list,'user_loggedin':user_loggedin}
    return render(request,'aptest/loginauth.html',context)




    ###################################
python-ldap
    ldap认证代码 auth.py
初始化连接，bind认证账号密码。如果bind成功，就返回True，若bind报错，就返回False。

import ldap
def auth_user(user, passwd):
    conn = ldap.initialize("ldap://IP:PORT")
    try:
        conn.simple_bind_s(user, passwd)
        return 1
    except:
        return 0
登陆的view代码
拿到form中用户输入的账号、密码。调用User对象的login方法，验证成功，就跳转登陆，否则，就提示错误并返回登陆页面。

def login(request):
    name = request.POST.get('username')
    password = request.POST.get('userpassword')
    user = User.login(name, password)
    if user:
        ...
        return redirect('user:users')
    else:
        context = {}
        context['name'] = name
        context['error'] = '用户名或密码错误'
        return render(request, 'user/login.html', context)
User对象的Login方法代码
login方法提供了登陆验证功能。调用auth_user函数，传入user，password参数，注意用户名前需要添加本地域名Domain:\。

    @classmethod
    def login(cls, name, password):
        username = 'Domain\\' + name
        ret = auth_user(username, password)
        # password correct
        if ret:
            try:
                user = User.objects.get(name=name)
                return user
            except ObjectDoesNotExist as e:
                user = User()
                user.name = name
                user.save()
                return user
        # password error
        else:
            return None
怎么样，这就实现了在django中通过ldap验证用户登陆的功能，是不是比在settings里配置ldap来导入用户信息要方便的多？

作者：brownchen
链接：https://www.jianshu.com/p/db62586b438f
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


###################

from django.contrib.auth import authenticate ###################

class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('main')
    template_name = 'module_name/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password) ##################


################################

https://www.cnblogs.com/fuckily/p/6255685.html



urls.py，

复制代码
from app0104 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^loginauth/', views.loginauth),
    url(r'^index/', views.index),
]
复制代码
index.html,

复制代码
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>fuck,{{ usergo }}</h1>
</body>
</html>
复制代码
loginauth.html,

复制代码
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form class="formone" action="/loginauth/" method="post">
        <input type="text" name="name" />
        <input type="password" name="password" />
        <input type="submit" value="ss" />
    </form>

{{ context.errors_list }}
{{ context.user_loggedin }}



</body>
</html>
复制代码
views.py,

复制代码
from django.shortcuts import render,HttpResponseRedirect

# Create your views here.



from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

name = ''


def loginauth(request):

    user_loggedin = 'Guest'
    errors_list = []
    if request.method == 'POST':
        print('pp: ', request.POST.get('name'), request.POST.get('password'))
        global name
        name = request.POST.get('name')
        password = request.POST.get('password')
        usergo = authenticate(username=name, password=password)

        print('authuser', usergo)
        if usergo is not None:
            auth_login(request, usergo)
            uu = request.user
            loginusername = usergo
            u = User.objects.get(username=uu)
            return HttpResponseRedirect("/index/")

    context = {'errors_list': errors_list, 'user_loggedin': user_loggedin}
    return render(request, 'loginauth.html', context)


def index(request):
    print('last:',name)
    return render(request,'index.html',{'usergo':name})
复制代码
settings.py,

复制代码
import os

import ldap
#LDAP configurationimport ldap
from django_auth_ldap.config import LDAPSearch
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# base_dn = 'dc=example,dc=com'
# AUTH_LDAP_SERVER_URI = 'ldap://192.168.187.55:389'
# AUTH_LDAP_BIND_DN = 'cn=admin,dc=example,dc=com'
# AUTH_LDAP_BIND_PASSWORD = "123456"
#
# # 用户的DN是uid=caojun,ou=People,dc=ldap,dc=ssotest,dc=net，所以用uid
# AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=People,dc=example,dc=com', ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

basedn = "OU=fds,DC=ddd,DC=com"
AUTH_LDAP_SERVER_URI = 'ldap://192.112.250.140:31338'
AUTH_LDAP_BIND_DN = 'CN=Admin.BJSHOP,OU=dfd_Admin,OU=AdminAccounts,OU=Applications,DC=sf,DC=com'
AUTH_LDAP_BIND_PASSWORD = "dddw33rewq"

# 用户的DN是uid=caojun,ou=People,dc=ldap,dc=ssotest,dc=net，所以用uid
AUTH_LDAP_USER_SEARCH = LDAPSearch('OU=ddd,DC=dd,DC=com', ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
     "first_name": "givenName",
     "last_name": "sn",
     "email": "mail"
}