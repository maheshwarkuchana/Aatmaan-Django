from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html" 

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

