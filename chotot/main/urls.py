from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from post import views as PostView
app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('timraovat/', PostView.PostListView.as_view(), name = 'search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)