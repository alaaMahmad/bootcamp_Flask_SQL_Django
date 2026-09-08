import random
from django.shortcuts import render, redirect

LEADERBOARD = []

def index(request):
    if 'target' not in request.session:
        request.session['target'] = random.randint(1, 100)
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    if 'game_over' not in request.session:
        request.session['game_over'] = False

    return render(request, 'index.html', {'leaderboard': LEADERBOARD})

def guess(request):
    if request.method == 'POST':
        if request.session.get('game_over'):
            return redirect('/')

        guess_val = int(request.POST.get('guess', 0))
        request.session['attempts'] = request.session.get('attempts', 0) + 1

        target = request.session['target']
        attempts = request.session['attempts']

        if guess_val == target:
            request.session['result'] = 'correct'
            request.session['game_over'] = True
        elif attempts >= 5:
            request.session['result'] = 'lose'
            request.session['game_over'] = True
        elif guess_val < target:
            request.session['result'] = 'low'
        else:
            request.session['result'] = 'high'

    return redirect('/')

def submit_score(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Anonymous')
        LEADERBOARD.append({
            'name': name,
            'attempts': request.session.get('attempts', 0)
        })
        return redirect('/leaderboard')
    return redirect('/')

def show_leaderboard(request):
    return render(request, 'leaderboard.html', {'leaderboard': LEADERBOARD})

def reset(request):
    request.session.clear()
    return redirect('/')