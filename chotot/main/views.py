from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/trangchu.html'

    # def get_context_data(self,**kwargs):


def search(request):
    return render (request, 'main/timraovat.html')