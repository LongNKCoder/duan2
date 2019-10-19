from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('dangtin/', views.post, name = 'dangtin'),
    path('profile/', views.profile_post, name = 'profile_post'),
    path('', views.post_view, name = 'post'),
]