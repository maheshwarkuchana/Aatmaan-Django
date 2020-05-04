from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog.html', views.blog, name='blog')
]