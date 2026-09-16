from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        "all_dojos": models.get_all_dojos()
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    if request.method == "POST":
        models.create_dojo(request.POST)
    return redirect('/')

def create_ninja(request):
    if request.method == "POST":
        models.create_ninja(request.POST)
    return redirect('/')

def delete_dojo(request, dojo_id):
    if request.method == "POST":
        models.delete_dojo(dojo_id)
    return redirect('/')