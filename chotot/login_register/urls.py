from django.urls import path
from . import views

app_name = 'login_register'

urlpatterns = [
    path('all/', views.profile, name = 'profile'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.user_login, name = 'login'),
]