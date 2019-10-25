from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('dangtin/', views.post, name = 'dangtin'),
    path('<pk>', views.PostDetailView.as_view(), name = 'baitinchitiet'),
]