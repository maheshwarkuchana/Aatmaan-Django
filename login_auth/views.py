from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name = first_name)
                user.save()
                messages.info(request, "User created!")

        else:
            print("Password not matching...")
        return redirect('/')

    else:
        return render(request, 'signup.html')
