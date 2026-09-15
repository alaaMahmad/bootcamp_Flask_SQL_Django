import random
from django.shortcuts import render, redirect

BUILDINGS = {
    'farm': (10, 20),
    'cave': (5, 10),
    'house': (2, 5),
    'casino': (-50, 50)
}

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'moves' not in request.session:
        request.session['moves'] = 0
    if 'game_over' not in request.session:
        request.session['game_over'] = False
    if 'win_status' not in request.session:
        request.session['win_status'] = None

    return render(request, 'index.html')

def process_money(request):
    if request.method == 'POST':
        building = request.POST.get('building')

        if building == 'reset':
            request.session.clear()
            return redirect('/')

        if request.session.get('game_over') or building not in BUILDINGS:
            return redirect('/')

        min_gold, max_gold = BUILDINGS[building]
        earned = random.randint(min_gold, max_gold)

        request.session['gold'] += earned
        request.session['moves'] += 1

        if earned >= 0:
            msg = f"Earned {earned} golds from the {building}!"
            color = 'green'
        else:
            msg = f"Entered a casino and lost {abs(earned)} golds"
            color = 'red'
    
        activities = request.session.get('activities', [])
        activities.insert(0, {'msg': msg, 'color': color})
        request.session['activities'] = activities

        if request.session['gold'] >= 250 and request.session['moves'] <= 15:
            request.session['game_over'] = True
            request.session['win_status'] = 'win'
        elif request.session['moves'] >= 15:
            request.session['game_over'] = True
            request.session['win_status'] = 'lose'

    return redirect('/')