from django.shortcuts import render
from django.views.generic import TemplateView

# Home 뷰
class HomeView(TemplateView):
    template_name = 'home/home.html'