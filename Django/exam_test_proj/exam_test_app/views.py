from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from . import models

# --- AUTHENTICATION VIEWS ---

def landing_page(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        errors = models.User.objects.register_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        user = models.add_user(request.POST, pw_hash)
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        return redirect('/dashboard')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user = models.get_user_by_username(request.POST['username'])
        if user and bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            return redirect('/dashboard')
        
        messages.error(request, "Invalid account or password.")
        return redirect('/')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

# --- DASHBOARD & PARTICIPANT VIEWS ---

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'logged_user': models.get_user_by_id(request.session['user_id']),
        'all_participants': models.get_all_participants()
    }
    return render(request, 'dashboard.html', context)

def create_participant(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    if request.method == 'POST':
        errors = models.Participant.objects.participant_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/create')
            
        models.add_participant(request.POST, request.session['user_id'])
        return redirect('/dashboard')
        
    context = {'logged_user': models.get_user_by_id(request.session['user_id'])}
    return render(request, 'create_participant.html', context)

def edit_participant(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    if request.method == 'POST':
        errors = models.Participant.objects.participant_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/edit/{id}')
            
        models.update_participant(id, request.POST)
        return redirect('/dashboard')

    context = {
        'logged_user': models.get_user_by_id(request.session['user_id']),
        'participant': models.get_participant_by_id(id)
    }
    return render(request, 'edit_participant.html', context)

def view_participant(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    context = {
        'logged_user': models.get_user_by_id(request.session['user_id']),
        'participant': models.get_participant_by_id(id)
    }
    return render(request, 'view_participant.html', context)

def delete_participant(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    models.delete_participant(id, request.session['user_id'])
    return redirect('/dashboard')

# --- STRETCH GOAL VIEW ---

def current_report(request):
    if 'user_id' not in request.session:
        return redirect('/')
        
    context = {
        'logged_user': models.get_user_by_id(request.session['user_id']),
        'active_participants': models.get_active_participants()
    }
    return render(request, 'report.html', context)