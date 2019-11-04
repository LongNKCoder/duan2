from django.shortcuts import render
from django.views.generic import View,ListView
from post import models

class IndexView(ListView):
    model = models.Category
    context_object_name = 'category'
    template_name = 'main/trangchu.html'