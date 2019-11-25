from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . import models,form
from PIL import Image

@login_required()
def post(request):
    return render(request, 'post/dangtin.html')

class IndexView(ListView):
    model = models.Category
    context_object_name = 'category'
    template_name = 'main/trangchu.html'

class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post
    paginate_by = 10
    template_name = 'post/timraovat.html'
    def get_queryset(self):
        filter_title = self.request.GET.get('title') or ''
        filter_brand = self.request.GET.get('brand') or ''
        filter_time = self.request.GET.get('time') or 'update_date'
        filter_type = self.request.GET.get('type') or ''
        filter_category = self.request.GET.get('category') or ''
        filter_price = self.request.GET.get('price') or 'price'
        new_context = models.Post.objects.filter(
            title__contains=filter_title,category__name__contains=filter_category,
            brand__name__contains=filter_brand,type_post__contains=filter_type
        ).order_by(filter_price,filter_time)
        return new_context
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['category'] = models.Category.objects.all
        context['brand'] = models.Brand.objects.all
        return context

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
            for pic in files:
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
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form_report'] = form.ReportForm()
        return context
    def post(self, request, *args, **kwargs):
        post = models.Post.objects.get(pk=self.kwargs['pk'])
        content = request.POST['content']
        type_report = request.POST['type_report']
        pic = request.FILES['pic']
        report = models.ReportPost(post=post,content=content,type_report=type_report,pic=pic)
        report.save()
        return redirect('/post/'+str(self.kwargs['pk']))