from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required()
def post(request):
    return render(request, 'post/dangtin.html')

@login_required()
def profile_post(request):
    return render(request, 'post/baivietcuanguoidung.html')

@login_required()
def post_view(request):
    return render(request, 'post/baiviet.html')

# Create your views here.
