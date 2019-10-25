from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/trangchu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = 0
        context["model"] = model
        return context

# class SearchView(TemplateView):
#     template_name = 'main/timraovat.html'