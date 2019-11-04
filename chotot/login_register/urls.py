from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login_register'

urlpatterns = [
    path('profile/<int:pk>', views.ProfileView.as_view(), name = 'profile'),
    path('profile/current', views.CurrentProfileView.as_view(), name = 'current'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.LoginViewCus.as_view(template_name="login_register/dangnhap.html"),name='login'),
]