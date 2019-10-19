from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from login_register.models import Profile
from login_register.forms import ProfileForm,UserForm
from main import views as main_views
from django.views.generic import View,TemplateView

def profile(request):
    user_list = Profile.objects.order_by('user')
    user_dict = {'users':user_list}
    return render(request,'login_register/thongtin.html',context=user_dict)

def register_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'login_register/dangky.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return main_views.search(request)
            else:
                return HttpResponse('Tài khoản chưa được active')
        else:
            return HttpResponse('Sai mật khẩu hoặc tài khoản')
    else:
        return render(request,'login_register/dangnhap.html')
@login_required
def user_logout(request):
    logout(request)
    return main_views.index(request)