from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib.auth.decorators import login_required
from . import models

@login_required()
def post(request):
    return render(request, 'post/dangtin.html')

class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post
    paginate_by = 10
    teamplate_name = 'main/timraovat.html'

# class PostListViewCurrent(ListView):
    

class PostDetailView(DetailView):
    context_object_name = 'post'
    model = models.Post
    template_name = 'post/tinchitiet.html'