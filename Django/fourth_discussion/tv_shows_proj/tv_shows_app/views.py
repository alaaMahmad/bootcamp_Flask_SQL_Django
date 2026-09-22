from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

def root(request):
    return redirect('/shows')

def shows_index(request):
    context = {
        "shows": models.get_all_shows()
    }
    return render(request, 'shows.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    if request.method == "POST":
        # Run validations
        errors = models.Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        
        # Create show if valid
        new_show_obj = models.create_show(request.POST)
        return redirect(f'/shows/{new_show_obj.id}')
    return redirect('/shows/new')

def show_detail(request, show_id):
    context = {
        "show": models.get_show_by_id(show_id)
    }
    return render(request, 'show_detail.html', context)

def edit_show(request, show_id):
    context = {
        "show": models.get_show_by_id(show_id)
    }
    return render(request, 'edit_show.html', context)

def update_show(request, show_id):
    if request.method == "POST":
        # Run validations with current show_id for uniqueness check
        errors = models.Show.objects.basic_validator(request.POST, show_id=show_id)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
        
        # Update show if valid
        models.update_show(show_id, request.POST)
        return redirect(f'/shows/{show_id}')
    return redirect(f'/shows/{show_id}/edit')

def delete_show(request, show_id):
    if request.method == "POST":
        models.delete_show(show_id)
    return redirect('/shows')