from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from login_register.models import Profile
from login_register.forms import ProfileForm,UserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from main import views as main_views
from django.views.generic import View,TemplateView,DetailView
from . import models


class ProfileView(DetailView):
    context_object_name = 'nguoidung'
    model = models.Profile
    template_name = 'login_register/thongtin.html'

class CurrentProfileView(LoginRequiredMixin, ProfileView):
    context_object_name = 'nguoidung'
    def get_object(self):
        return self.request.user

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