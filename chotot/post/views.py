from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . import models,form

@login_required()
def post(request):
    return render(request, 'post/dangtin.html')

class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post
    paginate_by = 10
    template_name = 'post/timraovat.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    form_class = form.PostForm
    model = models.Post
    template_name = 'post/post.html'
    def form_valid(self, form):
        files = self.request.FILES.getlist('pic')
        if form.is_valid() and len(files)>=3 and len(files)<5:
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            for f in files:
                pic = f
                photo = models.Image(post=self.object, pic=pic)
                photo.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        ctx = super(CreatePostView, self).get_context_data(**kwargs)
        ctx['form_image'] = form.ImageForm
        return ctx
    def get_success_url(self):
        return '/timraovat'

class UpdatePostView(UpdateView):
    form_class = form.PostFormUpdate
    model = models.Post
    template_name = 'post/post.html'
    def get_success_url(self):
        return '/timraovat'

class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'post/post.html'

class PostDetailView(DetailView):
    context_object_name = 'post'
    model = models.Post
    template_name = 'post/tinchitiet.html'