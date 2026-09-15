from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        "all_users": models.User.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
    if request.method == "POST":
        models.add_new_user(request.POST)
        return redirect('/')